# 2026-06-09 V3 recovery checkpoint

## 当前停点（2026-10-01）

正式报告已通过apr29_close非作者日级验收，普通待办为0；旧“112项均已有覆盖”不得作为当前验收。旧112项全部为日期隔离，不是当前普通审阅队列；已恢复的11处实际Books机制及2处中心争议保留有效证据，但不计本日采用。当前唯一确定候选n-days的来源、实际正文、非作者写后及最终日级复核均已通过。来源/日期外部保留项仍不支持全部Coverage/Evidence通过或无遗漏断言。

日期依据另行重开：旧owner receipt把DataCite DOI `created`误作公开批次。其头部15/84是旧归属迁移分类，实际99个items中90个正常schedule与注册日相合、9个不合，不能把84称为延迟公告。正确官方月目录 `https://arxiv.org/list/cs.CL/2026-06?skip=0&show=2000` 可读，但只有月份和条目、没有逐日公告headers；短路径 `/2606` 是404，不是零命中。官方advanced search已实际读取，Announcement date仅支持年月粒度。有限目标查询未取得当日公告。

精确API `https://api.datacite.org/dois/10.48550/arxiv.2606.07881` 的v1 Submitted为2026-06-05T22:33:57Z，Updated为2026-06-09T00:14:24Z，Available只有2026-06，Created为2026-06-09T03:16:21Z。Updated不是公开或解除embargo时间，Created更不是；非作者sep22_resume_v3已按DataCite dateType定义独立确认。正常schedule是归属线索，不提供排除hold的实际公开上界，不能据此补造[08:00,08:14]或[08:00,09:00]。正式表内旧时段尚未获得本轮落窗验收，不继续用它授权新Books写入。

必要外部材料请求：2026-06-08/09的arXiv官方逐日New/Cross/Replacement公告或含精确first-public事件的官方记录，须能逐个识别原表家族与版本；可接受原始HTML、RSS/公告邮件导出、官方时间语义明确的metadata。仅题摘页的Submitted、月份Available、DOI注册时刻或最新PDF不补足日期。材料到达后仅恢复112工作家族的日期、重复关系与依赖此归属的处置，不重扫1,235 raw或重读未变全文。日期不明项须先移出确定本窗候选并保留有效必要证据；本文件不把尚未审完的技术内容写成已经完成。

> **2026-09-11 final update：** 本文件保存恢复过程中的中间队列，不再是当前状态依据。两轮非作者审计最终冻结 112 Candidate / 1,123 Close；112 项 Evidence 与 Books Decision 已逐项完成，结果均为 `已有覆盖`，new Integrate = 0。2606.09774 撤回采用链已清理。权威结论见当日 README、`V3_SCREENING_LEDGER.md` 与 `JUNE_09_SECOND_FULL_TABLE_AUDIT.md`；下方旧队列仅用于解释审计演进，不表示仍有待执行工作。

## Historical denominator checkpoint（非权威）

可读基线为 1,235 raw / 99 prior / 1,136 closure proposals。896 项共用 incremental closure 理由被反例击穿后已逐题重审，其余 240 项也完成 title-first、边界项完整摘要复核。权威分母冻结为 Candidate 125 / Close 1,110：old prior 保留 77、关闭 22；old closure 恢复 48、维持关闭 1,088。Training-Inference Kernel Contracts（2606.07581）、Agent Skill System（2606.07586）、routing plateau（2606.07587）与 action-boundary failures（2606.07595）均恢复。逐项依据与 12+12 FP/FN 抽查见 V3_SCREENING_LEDGER.md。当前 blocker 转为 48 个新恢复 Candidate 的评分/Evidence/Books Decision，以及 surviving Integrate 的 Books trace-to-body。

## Historical Books body queue（已被终审覆盖）

已有正文 anchor，且 survives 当前分母：

- SF-2026-ARXIV-2606-07881 → books/part-04-training-system/38-pipeline-parallel.md（约 328 行）。
- SF-2026-ARXIV-2606-09692 → books/part-06-ai-infrastructure/69-trace.md（约 230 行）。

旧 Integrate SF-2026-ARXIV-2606-09774 撤回：论文只讨论用轻量 coding-agent adapter 配置科学模拟器，属于当前延后的 AI-for-Science 分支；应删除 books/part-07-agent/81-workflow.md 中相应 semantic-body-binding 与 daily-books-trace，而不是继续修订日期。

其余三十六项只找到 daily-books-trace，且均 survives 当前分母，需补写正文：

- books/part-07-agent/77-memory.md: SF-2026-ARXIV-2606-07684
- books/part-07-agent/82-multi-agent.md: SF-2026-ARXIV-2606-07790, SF-2026-ARXIV-2606-07805
- books/part-06-ai-infrastructure/66-evaluation-system.md: SF-2026-ARXIV-2606-07783, SF-2026-ARXIV-2606-07822, SF-2026-ARXIV-2606-07834, SF-2026-ARXIV-2606-07874, SF-2026-ARXIV-2606-08200, SF-2026-ARXIV-2606-08960, SF-2026-ARXIV-2606-09809
- books/part-06-ai-infrastructure/72-security.md: SF-2026-ARXIV-2606-07808, SF-2026-ARXIV-2606-07833, SF-2026-ARXIV-2606-07867, SF-2026-ARXIV-2606-07943, SF-2026-ARXIV-2606-08403, SF-2026-ARXIV-2606-08539, SF-2026-ARXIV-2606-09005, SF-2026-ARXIV-2606-09084
- books/part-06-ai-infrastructure/67-monitoring.md: SF-2026-ARXIV-2606-07889
- books/part-05-inference-system/45-why-kv-cache-speeds-up.md: SF-2026-ARXIV-2606-07878
- books/part-05-inference-system/56-inference-scheduling.md: SF-2026-ARXIV-2606-07923, SF-2026-ARXIV-2606-09613
- books/part-07-agent/81-workflow.md: SF-2026-ARXIV-2606-08049, SF-2026-ARXIV-2606-08919
- books/part-07-agent/84-agent-platform.md: SF-2026-ARXIV-2606-08106
- books/part-05-inference-system/44-decode.md: SF-2026-ARXIV-2606-08411
- books/part-04-training-system/36-distributed-training.md: SF-2026-ARXIV-2606-08476
- books/part-05-inference-system/55-pd-disaggregation.md: SF-2026-ARXIV-2606-08635
- books/part-07-agent/80-reflection.md: SF-2026-ARXIV-2606-08671
- books/part-05-inference-system/54-gpu-memory.md: SF-2026-ARXIV-2606-08761
- books/part-07-agent/76-rag.md: SF-2026-ARXIV-2606-08950
- books/part-05-inference-system/43-prefill.md: SF-2026-ARXIV-2606-09441
- books/part-05-inference-system/53-kserve-llm.md: SF-2026-ARXIV-2606-09643
- books/part-05-inference-system/49-tensorrt-llm.md: SF-2026-ARXIV-2606-09682, SF-2026-ARXIV-2606-09686
- books/part-04-training-system/31-rlhf.md: SF-2026-ARXIV-2606-09711

## Historical trace date queue（已被终审覆盖）

前二十五项 trace 日期错误，应改为 2026-06-09：

- 当前 2026-06-06（十三项）：07684, 07783, 07790, 07805, 07808, 07822, 07833, 07834, 07867, 07874, 07878, 07881, 07889。
- 当前 2026-06-07（五项）：07923, 07943, 08049, 08106, 08200。
- 当前 2026-06-08（七项）：08403, 08411, 08476, 08539, 08635, 08671, 08761。

上述简写均指 SF-2026-ARXIV-2606-*；从 08919 到 09809 的十四项日期已正确。

## 2026-10-01 当前日期隔离与有限恢复结果

旧112行112唯一身份统一为DateHold；下方原报告仅为保留证据的过程快照，其日期、评分、深入完成、已有覆盖/整合与普通待办声明均未获得本轮日级采用，不是当前候选表。原始1,235身份不是本轮全文队列。旧11处真实正文、2处中央争议及有效必要审阅仍保存，但日期隔离不支持当前日正面采用；不因日期缺口删除其他有效正文，也不把未读项谎称已核。收到官方逐日公告后仅恢复具体家族归属及其必要采用链。

具名版本：2606.07632v1、2606.07684v1、2606.07703v1、2606.07710v1、2606.07713v1、2606.07726v1、2606.07846v1、2606.07878v1、2606.07881v1、2606.07923v1、2606.08094v1、2606.08197v1、2606.08382v1、2606.08411v1、2606.08476v1、2606.08635v1、2606.08761v1、2606.08891v1、2606.08950v1、2606.09061v1、2606.09441v1、2606.09613v1、2606.09643v1、2606.09682v1、2606.09686v1、2606.07631v1、2606.07904v1、2606.08049v1、2606.08106v1、2606.08348v1、2606.08367v1、2606.08539v1、2606.08590v1、2606.08671v1、2606.08755v1、2606.08790v1、2606.08867v1、2606.08919v1、2606.09692v1、2606.07783v1、2606.07790v1、2606.07805v1、2606.07808v1、2606.07822v1、2606.07833v1、2606.07834v1、2606.07845v1、2606.07867v1、2606.07874v1、2606.07889v1、2606.07936v1、2606.07943v1、2606.07968v1、2606.07992v1、2606.08200v1、2606.08340v1、2606.08381v1、2606.08403v1、2606.08417v1、2606.08433v1、2606.08529v1、2606.08531v1、2606.08661v1、2606.08679v1、2606.08831v1、2606.08840v1、2606.08893v1、2606.08960v1、2606.09005v1、2606.09084v1、2606.09711v1、2606.09809v1、2606.08615v1、2606.08892v1、2606.07571v1、2606.07577v1、2606.07581v1、2606.07586v1、2606.07587v1、2606.07665v1、2606.08090v1、2606.09079v1、2606.09080v1、2606.09138v1、2606.09200v1、2606.09508v1、2606.09514v1、2606.09551v1、2606.07711v1、2606.08151v1、2606.08275v1、2606.09122v1、2606.09316v1、2606.09421v1、2606.09447v1、2606.09483v1、2606.09549v1、2606.09751v1、2606.07595v1、2606.07623v1、2606.07682v1、2606.08044v1、2606.09046v1、2606.09071v1、2606.09376v1、2606.09426v1、2606.09461v1、2606.09748v1、2606.09764v1、2606.07996v1、2606.09401v1、2606.09411v1。

两处必要纠正获sep22_resume_v3非作者核：09751v1 §7.1 Listing4/§6.8/§8的entry原子持久后publish与追加corrective，实际长期owner为AGENT-PLATFORM Ch84 journal→fold→committed projection、snapshot offset及append-before-resolve；Ch81 saved/active不是持久耦合证据。07623v1 §9/Table2确有9系统23确定性certificate probes，exact与fraction-correct fields分开，作者亦说明small probe不证明theorem；这不是没有实验，也不证明校准概率或通用emergence。仅报告的有限certificate边界仍保留，当前日期未准，不计本日正式处置。

其他四项有限源核尚不获得本日采用：07881v1 PACI的pending queue与stage相关延迟/版本步数，不是任意梯度范数保证；08761v1 APEX4混合granularity的scaled INT32 partial→FP32与intra-SM重叠归INFER-TENSORRT-LLM而非GPU memory，A100/小batch反侧必须保留；09686v1标题是84-Format、六Tier1编码/解码oracle，不是83或完整算术算子一致性；07631v1 Trait-space冻结contrast/层与heldout traits只支持作者模型/校准人口的诊断，不是行为安全或API端完整检测。必要审阅可复用，未核完整采用边界不冒充Evidence完成。

本窗新增机构漏项N-days：官方Research hydration精确原字段publishedOn=2026-06-08T13:00:00.000Z、slug=n-days，转为21:00+08，位于固定窗。Research实际316,674 bytes，173 publication字段仅按目标窗及相邻事件提取；另agents-in-biology=13:20Z因AI for Science暂缓关闭。N-days实际读Setup/Results/Figure1–5/Conclusion；正文重要命题是patch公开至真实fleet激活的exposure，而不是把PoC crash当native effect或best-of-three时间当典型生产时延。已落实PLATFORM-SECURITY Ch72生命周期威胁后两段，score3+2+3=8；非作者apr29_close的源→实际owner及写后邻接复核均已通过。OpenAI三当窗核心说明为战略/政策/证券公告，无新系统机制，前分母关闭；Economic Exchange在06/08 00Z早于窗，Notion/Nextdoor在06/09 10/12Z晚于窗，均未扩大本窗。

### 原报告保留快照（旧时段和处置均非当前验收）

当前正式六部分已替换旧日期/采用表。n-days必要来源→实际Ch72 owner与两段窄写、写后及邻接已由非作者apr29_close实际通过；普通待办仅当前正式报告的日级复核。旧112身份全部DateHold，原完整README的878行逐段取回并保留于下方围栏，没有删失旧证据，也不把旧评分/采用升级为本轮验收。0.11=06/05 10:26:45Z、0.12=06/09 03:56:11Z与kimi-cli 1.47=06/05 10:35:01Z、1.48=06/22 12:50:45Z均为元数据停止边界；窗内无相应release，不读窗外patch。MiniMax06/09卡片实际为MaxProof，非单独M3发布，原页JSON-LD datePublished=06/09 13:43Z晚于窗，已排除日期缺口，不沿用相交展示日。OpenAI原始三URL为built-to-benefit-everyone-our-plan、openai-submits-confidential-s-1与industrial-policy-for-the-intelligence-age；准确RSS身份与原文核一致。

````markdown
# Daily Research — 2026-06-09

**规范：** V3
**窗口：** 2026-06-08T09:00:00+08:00 ～ 2026-06-09T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-09-14T22:00:00+08:00

## 1. 结论

本窗不能继承旧完成结论。1,235 个去重题摘身份经作者侧重审和两轮非作者 full-table audit，最终权威分母为 Candidate 112 / Close 1,123。第一轮复核纠正 owner identity、关闭 12 个 false positive 并恢复 2 个 false negative；第二轮又将 2606.07909、2606.08300、2606.08702 判为局部组合或薄封装，降回 pre-denominator closure。逐项结论见 [JUNE_09_SECOND_FULL_TABLE_AUDIT.md](../_sources/JUNE_09_SECOND_FULL_TABLE_AUDIT.md)，作者侧 `125 / 1,110` 与第一轮 `115 / 1,120` 只保留为审计历史。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [厂商源再认证](../_sources/daily-20260601/CURRENT_CONTRACT_DAILY_SOURCE_RECERT_20260914.md#来源结论)：经济研究项目不改变当前 AI System 设计，已关闭 | 已检查 | 无 |
| SRC-ANTHROPIC | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-META-AI | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-QWEN | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MOONSHOT | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 同上；“全部”列表本窗无条目 | 已检查 | 无 |
| SRC-ZAI | 同上；Research 列表本窗无条目 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 同上；技术博客本窗无条目 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-MINIMAX | 同上；本窗无保留事件 | 已检查 | 无 |
| SRC-ARXIV | [canonical-raw-identity-inventory-v2.1.json.gz](../_sources/daily-20260609/canonical-raw-identity-inventory-v2.1.json.gz)、[canonical-semantic-screening-checkpoint-v2.1.json.gz](../_sources/daily-20260609/canonical-semantic-screening-checkpoint-v2.1.json.gz)、[V3_SCREENING_LEDGER.md](../_sources/daily-20260609/V3_SCREENING_LEDGER.md) 与独立 [second full-table audit](../_sources/JUNE_09_SECOND_FULL_TABLE_AUDIT.md)；1,235 identities，最终分母 112 Candidate / 1,123 Close | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment](https://arxiv.org/abs/2606.07632v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-COST` | 深入完成 | 已有覆盖：`PLATFORM-COST`（[books/part-06-ai-infrastructure/70-cost.md](../../../../books/part-06-ai-infrastructure/70-cost.md)) |
| [Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching](https://arxiv.org/abs/2606.07684v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models](https://arxiv.org/abs/2606.07703v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-PREFILL` | 深入完成 | 已有覆盖：`INFER-PREFILL`（[books/part-05-inference-system/43-prefill.md](../../../../books/part-05-inference-system/43-prefill.md)) |
| [WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing](https://arxiv.org/abs/2606.07710v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-SPECULATIVE-DECODING` | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`（[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)) |
| [Attention at the Theoretical Minimum: A Mathematics of Arrays Framework for Memory-Optimal Transformer Kernels](https://arxiv.org/abs/2606.07713v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm that Provably Exploits Model Similarity](https://arxiv.org/abs/2606.07726v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension Method](https://arxiv.org/abs/2606.07846v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`AGENT-WORKFLOW` | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [Still: Amortized KV Cache Compaction in a Single Forward Pass](https://arxiv.org/abs/2606.07878v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency](https://arxiv.org/abs/2606.07881v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`TRAIN-PIPELINE-PARALLEL` | 深入完成 | 已有覆盖：`TRAIN-PIPELINE-PARALLEL`（[books/part-04-training-system/38-pipeline-parallel.md](../../../../books/part-04-training-system/38-pipeline-parallel.md)) |
| [Larch: Learned Query Optimization for Semantic Predicates](https://arxiv.org/abs/2606.07923v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models](https://arxiv.org/abs/2606.08094v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`INFER-REQUEST-LIFECYCLE` | 深入完成 | 已有覆盖：`INFER-REQUEST-LIFECYCLE`（[books/part-05-inference-system/42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)) |
| [AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments](https://arxiv.org/abs/2606.08197v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`TRAIN-DISTRIBUTED-TRAINING` | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://arxiv.org/abs/2606.08382v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`INFER-KV-CACHE` | 深入完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding](https://arxiv.org/abs/2606.08411v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-DECODE` | 深入完成 | 已有覆盖：`INFER-DECODE`（[books/part-05-inference-system/44-decode.md](../../../../books/part-05-inference-system/44-decode.md)) |
| [FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training](https://arxiv.org/abs/2606.08476v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`TRAIN-DISTRIBUTED-TRAINING` | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2606.08635v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-PD-DISAGGREGATION` | 深入完成 | 已有覆盖：`INFER-PD-DISAGGREGATION`（[books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)) |
| [APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing](https://arxiv.org/abs/2606.08761v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-GPU-MEMORY` | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY`（[books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md)) |
| [PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference](https://arxiv.org/abs/2606.08891v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [When More Cores Hurts: The Vector Database Scaling Paradox in HPC](https://arxiv.org/abs/2606.08950v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-RAG` | 深入完成 | 已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)) |
| [Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving](https://arxiv.org/abs/2606.09061v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance](https://arxiv.org/abs/2606.09441v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-PREFILL` | 深入完成 | 已有覆盖：`INFER-PREFILL`（[books/part-05-inference-system/43-prefill.md](../../../../books/part-05-inference-system/43-prefill.md)) |
| [AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving](https://arxiv.org/abs/2606.09613v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-SCHEDULING` | 深入完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [FMplex: Model Virtualization for Serving Extensible Foundation Models](https://arxiv.org/abs/2606.09643v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-KSERVE-TOPOLOGY` | 深入完成 | 已有覆盖：`INFER-KSERVE-TOPOLOGY`（[books/part-05-inference-system/53-kserve-llm.md](../../../../books/part-05-inference-system/53-kserve-llm.md)) |
| [AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis](https://arxiv.org/abs/2606.09682v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [An 83-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats](https://arxiv.org/abs/2606.09686v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`INFER-TENSORRT-LLM` | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning](https://arxiv.org/abs/2606.07631v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+2=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents](https://arxiv.org/abs/2606.07904v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-TOOL-CALLING` | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows](https://arxiv.org/abs/2606.08049v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-WORKFLOW` | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses](https://arxiv.org/abs/2606.08348v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](https://arxiv.org/abs/2606.08367v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions](https://arxiv.org/abs/2606.08539v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents](https://arxiv.org/abs/2606.08590v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History](https://arxiv.org/abs/2606.08671v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-REFLECTION` | 深入完成 | 已有覆盖：`AGENT-REFLECTION`（[books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md)) |
| [Co-Evolving Skill Generation and Policy Optimization](https://arxiv.org/abs/2606.08755v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`AGENT-REFLECTION` | 深入完成 | 已有覆盖：`AGENT-REFLECTION`（[books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md)) |
| [RAILS: Verification-Native Clearing For Agentic Commerce](https://arxiv.org/abs/2606.08790v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+2=8；exact-v1 与当前 claim 一致，owner=`AGENT-TOOL-CALLING` | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)) |
| [Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework](https://arxiv.org/abs/2606.08867v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-PLATFORM` | 深入完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human](https://arxiv.org/abs/2606.08919v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`AGENT-WORKFLOW` | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)) |
| [Observability for Delegated Execution in Agentic AI Systems](https://arxiv.org/abs/2606.09692v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-TRACE` | 深入完成 | 已有覆盖：`PLATFORM-TRACE`（[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md)) |
| [Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval](https://arxiv.org/abs/2606.07783v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games](https://arxiv.org/abs/2606.07790v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`AGENT-MULTI-AGENT` | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems](https://arxiv.org/abs/2606.07805v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`AGENT-MULTI-AGENT` | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models](https://arxiv.org/abs/2606.07808v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust](https://arxiv.org/abs/2606.07822v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks](https://arxiv.org/abs/2606.07833v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Cherry-pick Override: Unsafe Directional Commitment in LLM Judges under Mixed Evidence](https://arxiv.org/abs/2606.07834v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [GRPO Does Not Close the Multi-Agent Coordination Gap](https://arxiv.org/abs/2606.07845v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-MULTI-AGENT` | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [The Cold-Start Safety Gap in LLM Agents](https://arxiv.org/abs/2606.07867v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators](https://arxiv.org/abs/2606.07874v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories](https://arxiv.org/abs/2606.07889v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation](https://arxiv.org/abs/2606.07936v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents](https://arxiv.org/abs/2606.07943v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](https://arxiv.org/abs/2606.07968v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-MONITORING` | 深入完成 | 已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)) |
| [VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation](https://arxiv.org/abs/2606.07992v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`AGENT-MCP` | 深入完成 | 已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md)) |
| [Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents](https://arxiv.org/abs/2606.08200v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](https://arxiv.org/abs/2606.08340v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`AGENT-MULTI-AGENT` | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)) |
| [Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard](https://arxiv.org/abs/2606.08381v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection](https://arxiv.org/abs/2606.08403v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics](https://arxiv.org/abs/2606.08417v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing)](https://arxiv.org/abs/2606.08433v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Scaffold Effects on GAIA: A Controlled Comparison](https://arxiv.org/abs/2606.08529v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [ForesightSafety-SAGE:A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents](https://arxiv.org/abs/2606.08531v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+2=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems](https://arxiv.org/abs/2606.08661v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation](https://arxiv.org/abs/2606.08679v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models](https://arxiv.org/abs/2606.08831v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+2+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs](https://arxiv.org/abs/2606.08840v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Cheap Reward Hacking Detection](https://arxiv.org/abs/2606.08893v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+3=7；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries](https://arxiv.org/abs/2606.09005v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps](https://arxiv.org/abs/2606.09084v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`TRAIN-RLHF` | 深入完成 | 已有覆盖：`TRAIN-RLHF`（[books/part-04-training-system/31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md)) |
| [Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting](https://arxiv.org/abs/2606.09809v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 3+3+3=9；exact-v1 与当前 claim 一致，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Harnessing Streaming Video in the Wild](https://arxiv.org/abs/2606.08615v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`MULTIMODAL-REPRESENTATION` | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`（[books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)) |
| [Diffuse AI Control on Fuzzy Tasks](https://arxiv.org/abs/2606.08892v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+3+3=8；exact-v1 与当前 claim 一致，owner=`PLATFORM-SECURITY` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)) |
| [Enabling KV Caching of Shared Prefix for Diffusion Language Models](https://arxiv.org/abs/2606.07571v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-KV-CACHE` | 标准完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs](https://arxiv.org/abs/2606.07577v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-KV-CACHE` | 深入完成 | 整合：`INFER-KV-CACHE`（[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)）；实际正文及独立写后通过 |
| [Training-Inference Kernel Contracts: Bounding Divergence in Post-Training and Deployment](https://arxiv.org/abs/2606.07581v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；per-token kernel ratio合同的clip公式与policy equivalence主张冲突，owner=`INFER-TENSORRT-LLM` | 争议 | 暂缓：中心冲突隔离，不进入Books，精确重开条件见§5 |
| [From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs](https://arxiv.org/abs/2606.07586v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 标准完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [The Routing Plateau: Understanding and Breaking the Accuracy Limits of LLM Routers](https://arxiv.org/abs/2606.07587v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-SCHEDULING` | 标准完成 | 已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)) |
| [AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference](https://arxiv.org/abs/2606.07665v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-TENSORRT-LLM` | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)) |
| [Fast LLM-Based Semantic Filtering: From a Unified Framework to an Adaptive Two-Phase Method](https://arxiv.org/abs/2606.08090v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-SCHEDULING` | 标准完成 | 仅报告：proxy/oracle取舍为局部证据，CP混合界不作为已证明SLA保证 |
| [FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/abs/2606.09079v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-KV-CACHE` | 标准完成 | 已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)) |
| [Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy](https://arxiv.org/abs/2606.09080v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)) |
| [Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.09138v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`TRAIN-GRPO` | 标准完成 | 已有覆盖：`TRAIN-GRPO`（[books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)) |
| [Resource-aware Computation-Communication Overlap for multi-GPU ML Workloads](https://arxiv.org/abs/2606.09200v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`TRAIN-DISTRIBUTED-TRAINING` | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)) |
| [From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs](https://arxiv.org/abs/2606.09508v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-KV-CACHE` | 争议 | 暂缓：中心冲突隔离，不进入Books，精确重开条件见§5 |
| [BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference](https://arxiv.org/abs/2606.09514v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`INFER-TENSORRT-LLM` | 深入完成 | 整合：`INFER-TENSORRT-LLM`（[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)）；实际正文及独立写后通过 |
| [FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing](https://arxiv.org/abs/2606.09551v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-SECURITY` | 深入完成 | 整合：`PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；实际正文及独立写后通过 |
| [Rosetta Memory: Adaptive Memory for Cross-LLM Agents](https://arxiv.org/abs/2606.07711v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 深入完成 | 整合：`AGENT-MEMORY`（[Ch77](../../../../books/part-07-agent/77-memory.md)）；实际正文及独立写后通过 |
| [Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents](https://arxiv.org/abs/2606.08151v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures](https://arxiv.org/abs/2606.08275v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-TRACE` | 深入完成 | 整合：`PLATFORM-TRACE`（[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)）；实际正文及独立写后通过 |
| [Autonomous Incident Resolution at Hyperscale: An Agentic AI Architecture for Network Operations](https://arxiv.org/abs/2606.09122v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents](https://arxiv.org/abs/2606.09316v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [What Should a Skill Remember? Quality--Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents](https://arxiv.org/abs/2606.09421v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-PLATFORM` | 标准完成 | 已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)) |
| [AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning](https://arxiv.org/abs/2606.09447v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`TRAIN-GRPO` | 深入完成 | 整合：`TRAIN-GRPO`（[Ch33](../../../../books/part-04-training-system/33-grpo.md)）；实际正文及独立写后通过 |
| [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.09483v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-MEMORY` | 标准完成 | 已有覆盖：`AGENT-MEMORY`（[books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)）；在线 writer/离线 sweeper、consolidation 与读路径 |
| [SecureClaw: Clawing Back Control of LLM Agents](https://arxiv.org/abs/2606.09549v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 深入完成 | 整合：`PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；实际正文及独立写后通过 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [Collaborative Human-Agent Protocol (CHAP)](https://arxiv.org/abs/2606.09751v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`AGENT-WORKFLOW` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents](https://arxiv.org/abs/2606.07595v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-SECURITY` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [Finite Certificates for In-Context Determinacy and a Threshold Theory of Emergence in Language Models](https://arxiv.org/abs/2606.07623v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?](https://arxiv.org/abs/2606.07682v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；完整题摘与 exact-v1 正文给出长期合同增量，owner=`PLATFORM-EVALUATION-SYSTEM` | 待审阅 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [When Behavioral Safety Evaluation Fails: A Representation-Level Perspective](https://arxiv.org/abs/2606.08044v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；拒答行为与representation probe可解耦；版本化sensor不拥有真值，owner=`PLATFORM-SECURITY` | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；实际论点及独立复核通过
| [Decoy-Calibrated Failure Audits for Language Models](https://arxiv.org/abs/2606.09046v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；假descriptor经验底线→冻结幸存集合→holdout；非FDR/因果，owner=`PLATFORM-EVALUATION-SYSTEM` | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；实际论点及独立复核通过
| [REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces](https://arxiv.org/abs/2606.09071v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；exact-v1 证明 prefix-preserving replay、diagnosis-specific faithfulness gate 与归因边界，owner=`PLATFORM-TRACE` | 深入完成 | 整合：`PLATFORM-TRACE`（[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)）；实际正文及独立写后通过 |
| [Precision Is Not Faithfulness: Coverage-Aware Evaluation of Grounded Generation with a Complete Oracle](https://arxiv.org/abs/2606.09376v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；atomic precision/目标事实coverage与派生oracle的有限完备性，owner=`PLATFORM-EVALUATION-SYSTEM` | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)）；实际论点及独立复核通过
| [WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces](https://arxiv.org/abs/2606.09426v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 标准完成 | 仅报告：受限机制/评价案例，必要证据及非作者处置通过，具体边界见§4 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](https://arxiv.org/abs/2606.09461v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 标准完成 | 仅报告：受限机制/评价案例，必要证据及非作者处置通过，具体边界见§4 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback](https://arxiv.org/abs/2606.09748v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 标准完成 | 仅报告：受限机制/评价案例，必要证据及非作者处置通过，具体边界见§4 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [iOSWorld: A Benchmark for Personally Intelligent Phone Agents](https://arxiv.org/abs/2606.09764v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 标准完成 | 仅报告：受限机制/评价案例，必要证据及非作者处置通过，具体边界见§4 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [MC-PDD: Masked Corpus-Level Pretraining Data Detection for Black-Box Large Language Models](https://arxiv.org/abs/2606.07996v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 标准完成 | 仅报告：受限机制/评价案例，必要证据及非作者处置通过，具体边界见§4 | 暂缓：普通证据恢复与Books重判待执行，不是外部终态，见§5 |
| [Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models](https://arxiv.org/abs/2606.09401v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；adaptation DP邻接不追溯fixed pretraining；MIA与accountant分账，owner=`PLATFORM-SECURITY` | 深入完成 | 整合：`PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；实际论点及独立复核通过
| [Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs](https://arxiv.org/abs/2606.09411v1) | 2026-06-09T08:00:00+08:00 ～ 2026-06-09T09:00:00+08:00 | 2+2+2=6；受控recontext检验nuisance捷径；proxy KL非完整检测保证，owner=`PLATFORM-SECURITY` | 深入完成 | 整合：`PLATFORM-SECURITY`（[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)）；实际论点及独立复核通过

候选分母112及身份纠正记录保持不变：上表74个既有家族和38个恢复家族。REFLECT已发现并补写具体正文差异，待非作者写后核；其余旧已有覆盖判断不能替代本輪必要证据。恢复包中33项只列章节名而缺少具体机制、评价与反证的呈现正在定点修复，尚不宣称Evidence 112/112或本日完成。2606.09483的官方export精确版本PDF恢复仍有效，不推倒已核验材料。

## 4. 证据与知识整合

下列74项复用归档中的精确版本审阅，逐项保留机制摘录与唯一review定位；旧owner不作为当前归属。评价和关键反证仍以完整原记录为准，当前采用只按本日报Books判断，不由旧完成标签授权。

### [Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment](https://arxiv.org/abs/2606.07632v1)

精确版本 `2606.07632v1`；归档机制摘录（不替代全文证据）：Model life-cycle assessment expands efficiency accounting from one training run or inference sample to data, experimentation, deployment, refresh, infrastructure and retirement under an explicit functional unit. The governed state is an inventory keyed by functional unit, stage boundary, model/service revision, hardware lifetime…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-ML-LIFECYCLE-ASSESSMENT`（标题“Position: Evaluation of ML Resource Utilization Requires Model Life Cycle Assessment”）。当前 Books 决定：已有覆盖：`PLATFORM-COST`（[books/part-06-ai-infrastructure/70-cost.md](../../../../books/part-06-ai-infrastructure/70-cost.md))；现有论点与采用边界以当前对照为准。

### [Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching](https://arxiv.org/abs/2606.07684v1)

精确版本 `2606.07684v1`；归档机制摘录（不替代全文证据）：We propose Semantic Cache Distillation (SCD), a loss-constrained framework that replaces raw KV transmission with compact semantic codes. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MEMORY`，对应 `books/part-07-agent/77-memory.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit aut…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07684`（标题“2606.07684 — Semantic Cache Distillation: Efficient State Transfer via Reuse and Selective Patching”）。当前 Books 决定：已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有论点与采用边界以当前对照为准。

### [How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models](https://arxiv.org/abs/2606.07703v1)

精确版本 `2606.07703v1`；归档机制摘录（不替代全文证据）：We introduce an attention-mass top-k oracle for existing GQA checkpoints: for each layer and query position, it computes dense attention, selects head-averaged token support, and recomputes attention only on that support. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-PREFILL`，对应 `books/part-05-inference-system/43-prefill.md`。新增的预…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07703`（标题“2606.07703 — How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models”）。当前 Books 决定：已有覆盖：`INFER-PREFILL`（[books/part-05-inference-system/43-prefill.md](../../../../books/part-05-inference-system/43-prefill.md))；现有论点与采用边界以当前对照为准。

### [WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing](https://arxiv.org/abs/2606.07710v1)

精确版本 `2606.07710v1`；归档机制摘录（不替代全文证据）：To address this volatility, we introduce WhiFlash, the first cross-paradigm SD method that unifies autoregressive and diffusion-based parallel drafting under a single token-level controller. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-SPECULATIVE-DECODING`，对应 `books/part-05-inference-system/48-speculative-decoding.md`。新增的预测、派生状…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07710`（标题“2606.07710 — WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing”）。当前 Books 决定：已有覆盖：`INFER-SPECULATIVE-DECODING`（[books/part-05-inference-system/48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md))；现有论点与采用边界以当前对照为准。

### [Attention at the Theoretical Minimum: A Mathematics of Arrays Framework for Memory-Optimal Transformer Kernels](https://arxiv.org/abs/2606.07713v1)

精确版本 `2606.07713v1`；归档机制摘录（不替代全文证据）：We present a Mathematics of Arrays (MoA) reformulation of scaled dot-product attention and its numerically stable softmax, deriving a Denotational Normal Form (DNF) that eliminates all intermediate arrays -- including the implicit transposed-key buffer and every softmax temporary -- by algebraic construction rather than empirica…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07713`（标题“2606.07713 — Attention at the Theoretical Minimum: A Mathematics of Arrays Framework for Memory-Optimal Transformer Kernels”）。当前 Books 决定：已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md))；现有论点与采用边界以当前对照为准。

### [Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm that Provably Exploits Model Similarity](https://arxiv.org/abs/2606.07726v1)

精确版本 `2606.07726v1`；归档机制摘录（不替代全文证据）：We propose Synchronized Successive Rejects (SySRs), augmenting the classical Successive Rejects algorithm with paired comparisons. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owne…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07726`（标题“2606.07726 — Cutting LLM Evaluation Costs with SySRs: A Bandit Algorithm that Provably Exploits Model Similarity”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension Method](https://arxiv.org/abs/2606.07846v1)

精确版本 `2606.07846v1`；归档机制摘录（不替代全文证据）：Speculative execution can reclaim that idle time by launching a downstream operation with a predicted upstream input, but here each speculation costs real money (per-token billing) and its success probability is hard to estimate and drifts over time. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-WORKFLOW`，对应 `books/part-07-agent/…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07846`（标题“2606.07846 — Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension Method”）。当前 Books 决定：已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md))；现有论点与采用边界以当前对照为准。

### [Still: Amortized KV Cache Compaction in a Single Forward Pass](https://arxiv.org/abs/2606.07878v1)

精确版本 `2606.07878v1`；归档机制摘录（不替代全文证据）：Here we introduce Still, a small per-layer Perceiver trained once against a frozen base model that produces compact keys and values in a single forward pass. 本次 exact-v1 全文复核把 canonical owner 固定为 `INFER-KV-CACHE`，对应 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recove…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07878`（标题“2606.07878 — Still: Amortized KV Cache Compaction in a Single Forward Pass”）。当前 Books 决定：已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有论点与采用边界以当前对照为准。

### [Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency](https://arxiv.org/abs/2606.07881v1)

精确版本 `2606.07881v1`；归档机制摘录（不替代全文证据）：We introduce PACI (Pipeline Asynchronous training with Controlled Inconsistency), a bubble-free asynchronous pipeline method that bounds forward/backward version drift without weight stashing, prediction, additional parameter copies, or global synchronization. 本次 exact-v1 全文复核把 canonical owner 固定为 `TRAIN-PIPELINE-PARALLEL`，对应 `b…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07881`（标题“2606.07881 — Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency”）。当前 Books 决定：已有覆盖：`TRAIN-PIPELINE-PARALLEL`（[books/part-04-training-system/38-pipeline-parallel.md](../../../../books/part-04-training-system/38-pipeline-parallel.md))；现有论点与采用边界以当前对照为准。

### [Larch: Learned Query Optimization for Semantic Predicates](https://arxiv.org/abs/2606.07923v1)

精确版本 `2606.07923v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-07923:start -->
Larch: Learned Query Optimization for Semantic Predicates 处理的问题是：Online selectivity learning plus exact per-row ordering makes semantic-predicate token cost query-planner state rather than an opaque LLM charge.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点是 `§3 Larch; §§3.1–3.4 sta…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07923`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md))；现有论点与采用边界以当前对照为准。

### [vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models](https://arxiv.org/abs/2606.08094v1)

精确版本 `2606.08094v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08094:start -->
vla.cpp: A Unified Inference Runtime for Vision-Language-Action Models 处理的问题是：A single C++ runtime owns cached vision-language prefix state, cross-attending action-expert solver steps, portable model bundles, and one request protocol across VLA families.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08094`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`INFER-REQUEST-LIFECYCLE`（[books/part-05-inference-system/42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md))；现有论点与采用边界以当前对照为准。

### [AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments](https://arxiv.org/abs/2606.08197v1)

精确版本 `2606.08197v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08197:start -->
AlignFed: Alignment-Aware Asynchronous Federated Fine-Tuning for Large Language Models in Heterogeneous Edge Environments 处理的问题是：Version grouping, calibration-set semantic alignment, and freshness/participation weighting make staleness and fairness explicit asynchronous federated agg…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08197`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md))；现有论点与采用边界以当前对照为准。

### [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://arxiv.org/abs/2606.08382v1)

精确版本 `2606.08382v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08382:start -->
STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control 处理的问题是：Differentiable head/block thresholds, sensitivity-specific factorization, and rank-aware mixed precision turn KV rank into adaptive runtime compression state backed by kernels.。旧路径把这一变化隐藏在静态…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08382`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`INFER-KV-CACHE`（[books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md))；现有论点与采用边界以当前对照为准。

### [AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding](https://arxiv.org/abs/2606.08411v1)

精确版本 `2606.08411v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AsyncLane 用 lane tree 把 DLM 的 prefix refinement 与 frontier advancement 解耦，并以 shared-prefix batching、lookahead reuse 与 cache refresh 管理异步依赖。 exact-v1 摘要将具体问题界定为：Block-wise semi-autoregressive decoding is the standard inference paradigm for diffusion large language models (DLMs), but …（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08411`（标题“2606.08411 — AsyncLane: Decoupling Refinement from Advancement in Diffusion Language Model Decoding”）。当前 Books 决定：已有覆盖：`INFER-DECODE`（[books/part-05-inference-system/44-decode.md](../../../../books/part-05-inference-system/44-decode.md))；现有论点与采用边界以当前对照为准。

### [FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training](https://arxiv.org/abs/2606.08476v1)

精确版本 `2606.08476v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：FlashCP 将 context-parallel 的负载均衡、attention kernel 与 KV 通信共同建模，避免静态 sequence sharding 把三类瓶颈分开优化。 exact-v1 摘要将具体问题界定为：Context parallelism (CP) is essential for training large-scale, long-context language models, as it partitions sequences to reduce memory overhead. However, existing C…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08476`（标题“2606.08476 — FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training”）。当前 Books 决定：已有覆盖：`TRAIN-DISTRIBUTED-TRAINING`（[books/part-04-training-system/36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md))；现有论点与采用边界以当前对照为准。

### [SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving](https://arxiv.org/abs/2606.08635v1)

精确版本 `2606.08635v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：SpectrumKV 将 PD 之间的 KV 传输从 token keep/drop 二元决策改为 per-token mixed precision，使网络字节、量化误差与重算成为同一控制面。 exact-v1 摘要将具体问题界定为：Prefill-decode (PD) disaggregation decouples prompt processing from token generation, but it also turns the key-value (KV) cache into a network payload. Existing PD-…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08635`（标题“2606.08635 — SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving”）。当前 Books 决定：已有覆盖：`INFER-PD-DISAGGREGATION`（[books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md))；现有论点与采用边界以当前对照为准。

### [APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing](https://arxiv.org/abs/2606.08761v1)

精确版本 `2606.08761v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：APEX4 把 W4A4 的瓶颈定位到同一 SM 内 Tensor Core 与 CUDA Core 的 compute imbalance，并用 kernel mapping 避免 mixed-precision fallback。 exact-v1 摘要将具体问题界定为：W4A4 quantization promises full utilization of INT4 Tensor Cores, yet group dequantization overhead on CUDA Cores has driven existing systems to …（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08761`（标题“2606.08761 — APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing”）。当前 Books 决定：已有覆盖：`INFER-GPU-MEMORY`（[books/part-05-inference-system/54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md))；现有论点与采用边界以当前对照为准。

### [PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference](https://arxiv.org/abs/2606.08891v1)

精确版本 `2606.08891v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：PALUTE 用 processing-in-memory lookup table 同时吸收 quantized GEMM 的 dequantization 与 nonlinear operator 成本，改变 edge inference 的 data-movement owner。 exact-v1 摘要将具体问题界定为：Large language models are increasingly deployed on edge devices with tight power and area budgets. While mixed-precisi…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08891`（标题“2606.08891 — PALUTE: Processing-In-Memory Acceleration via Lookup Table for Edge LLM Inference”）。当前 Books 决定：已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md))；现有论点与采用边界以当前对照为准。

### [When More Cores Hurts: The Vector Database Scaling Paradox in HPC](https://arxiv.org/abs/2606.08950v1)

精确版本 `2606.08950v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：向量数据库的 insertion、indexing、query 与 mixed read/write 生命周期必须同 storage hierarchy、broadcast-gather 与 partitioning 一起评估；增加 core/node 可因协调瓶颈反向降低吞吐。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08950`（标题“2606.08950 — When More Cores Hurts: The Vector Database Scaling Paradox in HPC”）。当前 Books 决定：已有覆盖：`AGENT-RAG`（[books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md))；现有论点与采用边界以当前对照为准。

### [Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving](https://arxiv.org/abs/2606.09061v1)

精确版本 `2606.09061v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：chunked-prefill scheduler 需联合持有 request age、remaining prefill work、predicted latency 与 active-prefill cap，而不只用 arrival order 或 static token budget。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09061`（标题“2606.09061 — Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill LLM Serving”）。当前 Books 决定：已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md))；现有论点与采用边界以当前对照为准。

### [SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance](https://arxiv.org/abs/2606.09441v1)

精确版本 `2606.09441v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：RAG 重复文档的 prefill 可保存 selective index 而非整份 KV：offline 编码局部 attention，online 只重算 query-sensitive cross attention，以 storage traffic 换 TTFT。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09441`（标题“2606.09441 — SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance”）。当前 Books 决定：已有覆盖：`INFER-PREFILL`（[books/part-05-inference-system/43-prefill.md](../../../../books/part-05-inference-system/43-prefill.md))；现有论点与采用边界以当前对照为准。

### [AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving](https://arxiv.org/abs/2606.09613v1)

精确版本 `2606.09613v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：agent serving simulator 的执行单位必须从独立 request 提升为 program，显式模拟 turn dependency、tool gap、session affinity 与跨 HBM/host/CXL 的 KV residency。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09613`（标题“2606.09613 — AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving”）。当前 Books 决定：已有覆盖：`INFER-SCHEDULING`（[books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md))；现有论点与采用边界以当前对照为准。

### [FMplex: Model Virtualization for Serving Extensible Foundation Models](https://arxiv.org/abs/2606.09643v1)

精确版本 `2606.09643v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：extensible foundation model serving 需要把 base weights 与 extension state 虚拟化：共享公共层、按请求装载/组合扩展，并由 placement/cache 控制其生命周期。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09643`（标题“2606.09643 — FMplex: Model Virtualization for Serving Extensible Foundation Models”）。当前 Books 决定：已有覆盖：`INFER-KSERVE-TOPOLOGY`（[books/part-05-inference-system/53-kserve-llm.md](../../../../books/part-05-inference-system/53-kserve-llm.md))；现有论点与采用边界以当前对照为准。

### [AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis](https://arxiv.org/abs/2606.09682v1)

精确版本 `2606.09682v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：agent 生成 megakernel 必须经过 typed IR、静态 shape/layout/resource checks、编译与数值验证门，失败后才允许 self-retarget；自然语言计划不直接获得 kernel authority。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09682`（标题“2606.09682 — AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakernel Synthesis”）。当前 Books 决定：已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md))；现有论点与采用边界以当前对照为准。

### [An 83-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats](https://arxiv.org/abs/2606.09686v1)

精确版本 `2606.09686v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：低精度 format contract 需要 vendor-neutral、bit-exact 的 encode/decode、rounding、overflow、NaN/Inf/subnormal 与 microscaling conformance vectors；格式名相同不代表语义相同。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09686`（标题“2606.09686 — An 84-Format Numeric Catalog with Bit-Exact Conformance Vectors: A Vendor-Neutral Reference for FP8, BF16, MXFP4, and Microscaling Formats”）。当前 Books 决定：已有覆盖：`INFER-TENSORRT-LLM`（[books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md))；现有论点与采用边界以当前对照为准。

### [Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning](https://arxiv.org/abs/2606.07631v1)

精确版本 `2606.07631v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-TRAIT-MISALIGNMENT-MONITOR:start -->只靠周期性行为评估能发现 emergent misalignment，但检测间隔长且成本高。该方法把七个 alignment trait 编成 activation direction，跨 checkpoint 追踪低维 drift，并用该 profile 训练轻量 monitor。 四个 7–9B 模型和 14B stress test 支持研究 regime 内的 AUROC/误报漏报；内部 drift 只是 sensor，跨模型、起始 misalignment 与更长训练需要重校准。它需要白盒 activation 访问，不能取代行为验收或 eff…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-TRAIT-MISALIGNMENT-MONITOR`（标题“Trait-space Monitoring for Emergent Misalignment During Supervised Finetuning”）。当前 Books 决定：已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md))；现有论点与采用边界以当前对照为准。

### [Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents](https://arxiv.org/abs/2606.07904v1)

精确版本 `2606.07904v1`；归档机制摘录（不替代全文证据）：We introduce Contract2Tool, a framework for inferring tool contracts from metadata, schemas, documentation, and execution traces. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-TOOL-CALLING`，对应 `books/part-07-agent/78-tool-calling.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，不接管其 commit…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07904`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md))；现有论点与采用边界以当前对照为准。

### [SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows](https://arxiv.org/abs/2606.08049v1)

精确版本 `2606.08049v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08049:start -->
SKILL.nb: Selective Formalization and Gated Execution for Durable Agent Workflows 处理的问题是：Versioned notebooks make each reusable step auditable state and let validation gates choose code execution or local natural-language fallback when environments drift.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08049`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md))；现有论点与采用边界以当前对照为准。

### [PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents](https://arxiv.org/abs/2606.08106v1)

精确版本 `2606.08106v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08106:start -->
PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents 处理的问题是：Anytime-valid paired tests move self-evolution authority from noisy score improvement to a false-commit-controlled acceptor that remains valid under optional stopping.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08106`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md))；现有论点与采用边界以当前对照为准。

### [Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses](https://arxiv.org/abs/2606.08348v1)

精确版本 `2606.08348v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08348:start -->
Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses 处理的问题是：Verified trajectories and posterior beliefs turn skills into evidence-bearing lifecycle objects with auditable update and guardrail actions across harnesses.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08348`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md))；现有论点与采用边界以当前对照为准。

### [Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy](https://arxiv.org/abs/2606.08367v1)

精确版本 `2606.08367v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08367:start -->
Emergence World: A Platform for Evaluating Long-Horizon Multi-Agent Autonomy 处理的问题是：Continuously running heterogeneous agent populations, persistent memories, consequential governance, and live exogenous data expose drift and cross-influence absent from exam-style evaluation.。旧路径把这一变…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08367`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions](https://arxiv.org/abs/2606.08539v1)

精确版本 `2606.08539v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。 exact-v1 摘要将具体问题界定为：AI agents increasingly take consequential actions -- shell commands, cloud operations, and arbitrary tool-calls -- so a trust layer must decide, per …（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08539`（标题“2606.08539 — AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents](https://arxiv.org/abs/2606.08590v1)

精确版本 `2606.08590v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Kubernetes RCA 将 typed evidence graph、read-only tool collection、bounded traversal 与独立 verdict validation 分开，避免 prompt leakage 冒充诊断增益。 exact-v1 摘要将具体问题界定为：Kubernetes incidents are diagnosed reliably only when a root-cause system's reported gains come from incident evidence rather tha…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08590`（标题“2606.08590 — Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents”）。当前 Books 决定：已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md))；现有论点与采用边界以当前对照为准。

### [SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History](https://arxiv.org/abs/2606.08671v1)

精确版本 `2606.08671v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：SkillHone 为 skill revision 保留 decision history、evaluation 与 rejected alternatives，使后续 agent 能解释、回退和继续演化持久技能。 exact-v1 摘要将具体问题界定为：Agent skills extend language-model agents with task-specific procedures, scripts, and references, but the tasks and environments they target continually c…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08671`（标题“2606.08671 — SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History”）。当前 Books 决定：已有覆盖：`AGENT-REFLECTION`（[books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md))；现有论点与采用边界以当前对照为准。

### [Co-Evolving Skill Generation and Policy Optimization](https://arxiv.org/abs/2606.08755v1)

精确版本 `2606.08755v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：skill generation 与 policy optimization 必须共同验证新 skill 的 usefulness，避免 skill bank 只积累未经行为结果校验的文本程序。 exact-v1 摘要将具体问题界定为：Skill-augmented reinforcement learning improves language agents by storing reusable procedural knowledge acquired from past experience. Existing methods typically us…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08755`（标题“2606.08755 — Co-Evolving Skill Generation and Policy Optimization”）。当前 Books 决定：已有覆盖：`AGENT-REFLECTION`（[books/part-07-agent/80-reflection.md](../../../../books/part-07-agent/80-reflection.md))；现有论点与采用边界以当前对照为准。

### [RAILS: Verification-Native Clearing For Agentic Commerce](https://arxiv.org/abs/2606.08790v1)

精确版本 `2606.08790v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：RAILS 把 delegated obligation、verification、liability 与 settlement action 组合成 agent commerce 的 clearing contract，而不把支付成功等同于任务履约。 exact-v1 摘要将具体问题界定为：Autonomous agents negotiate, purchase, deploy code, and move funds, but no neutral mechanism determines whether they met their delegated…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08790`（标题“2606.08790 — RAILS: Verification-Native Clearing For Agentic Commerce”）。当前 Books 决定：已有覆盖：`AGENT-TOOL-CALLING`（[books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md))；现有论点与采用边界以当前对照为准。

### [Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework](https://arxiv.org/abs/2606.08867v1)

精确版本 `2606.08867v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：100M-user support agent 把离线 evaluation、context engineering、training 与 online measurement 组成闭环，单一模型分数不代表生产 readiness。 exact-v1 摘要将具体问题界定为：The rapid rise in LLM capabilities has made AI agents increasingly viable across a broad range of tasks. Among the most promising applications is …（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08867`（标题“2606.08867 — Building Customer Support AI Agents at 100M-User Scale: An Evaluation-Driven Framework”）。当前 Books 决定：已有覆盖：`AGENT-PLATFORM`（[books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md))；现有论点与采用边界以当前对照为准。

### [Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human](https://arxiv.org/abs/2606.08919v1)

精确版本 `2606.08919v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：人工审批不是无限 oracle；guard 的 escalation policy 必须把 reviewer 分歧、疲劳与 flooding 下的有限 attention 当作可耗尽资源。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08919`（标题“2606.08919 — Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human”）。当前 Books 决定：已有覆盖：`AGENT-WORKFLOW`（[books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md))；现有论点与采用边界以当前对照为准。

### [Observability for Delegated Execution in Agentic AI Systems](https://arxiv.org/abs/2606.09692v1)

精确版本 `2606.09692v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：agent telemetry 必须把 authority graph 与 causal execution graph 分离，并在调用时绑定 durable delegation_id、re-delegation lineage、normalized action/resource semantics。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09692`（标题“2606.09692 — Observability for Delegated Execution in Agentic AI Systems”）。当前 Books 决定：已有覆盖：`PLATFORM-TRACE`（[books/part-06-ai-infrastructure/69-trace.md](../../../../books/part-06-ai-infrastructure/69-trace.md))；现有论点与采用边界以当前对照为准。

### [Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval](https://arxiv.org/abs/2606.07783v1)

精确版本 `2606.07783v1`；归档机制摘录（不替代全文证据）：In this work, we propose an evaluation protocol to systematically test how the RAG system handles conflicts between parametric knowledge and evidence retrieved from context with varying amounts of misleading information. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-eva…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07783`（标题“2606.07783 — Evaluating RAG Reliability under Clean, Misleading, and Mixed Retrieval”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games](https://arxiv.org/abs/2606.07790v1)

精确版本 `2606.07790v1`；归档机制摘录（不替代全文证据）：Building on prior work showing that cheap-talk channels enable cooperation in LLM coordination games, we investigate two vulnerability classes in a 4-player Stag Hunt across six model families and 720 trials. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MULTI-AGENT`，对应 `books/part-07-agent/82-multi-agent.md`。新增的预测、派生状态、验证或调度控制会带…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07790`（标题“2606.07790 — Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games”）。当前 Books 决定：已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md))；现有论点与采用边界以当前对照为准。

### [Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems](https://arxiv.org/abs/2606.07805v1)

精确版本 `2606.07805v1`；归档机制摘录（不替代全文证据）：Most current evaluation frameworks neglect procedural compliance, leading to ''Machiavellian'' behaviors where agents strategically violate safety rules to maximize rewards - a direct manifestation of Goodhart's Law. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MULTI-AGENT`，对应 `books/part-07-agent/82-multi-agent.md`。新增的预测、派生状态、验…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07805`（标题“2606.07805 — Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems”）。当前 Books 决定：已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md))；现有论点与采用边界以当前对照为准。

### [Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models](https://arxiv.org/abs/2606.07808v1)

精确版本 `2606.07808v1`；归档机制摘录（不替代全文证据）：We introduce a white-box diagnostic framework that localizes instruction hierarchy failures into instruction identification, conflict resolution, and response realization, making failures more interpretable. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-SECURITY`，对应 `books/part-06-ai-infrastructure/72-security.md`。新增的预测、派生状态、验…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07808`（标题“2606.07808 — Where Instruction Hierarchy Breaks: Diagnosing and Repairing Failures in Reasoning Language Models”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust](https://arxiv.org/abs/2606.07822v1)

精确版本 `2606.07822v1`；归档机制摘录（不替代全文证据）：Calibration is a good proxy for trust: well-calibrated confidence estimates help inform the risk versus reward tradeoff when trusting a specific model output. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failu…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07822`（标题“2606.07822 — The ACUTE Protocol: Operationalizing Language Model Activations for Better Calibration, Utility, and Trust”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks](https://arxiv.org/abs/2606.07833v1)

精确版本 `2606.07833v1`；归档机制摘录（不替代全文证据）：We propose applying process mining, a discipline for discovering and analyzing process models from event logs, to red teaming traces. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-SECURITY`，对应 `books/part-06-ai-infrastructure/72-security.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 contract，…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07833`（标题“2606.07833 — Beyond Pass/Fail: Using Process Mining to Understand How LLMs Resist (and Fail) Red Team Attacks”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Cherry-pick Override: Unsafe Directional Commitment in LLM Judges under Mixed Evidence](https://arxiv.org/abs/2606.07834v1)

精确版本 `2606.07834v1`；归档机制摘录（不替代全文证据）：Under mixed evidence (claims with both supporting and refuting sources) this is unsafe: when the schema exposes CONFLICTING as the authorized non-directional verdict, returning SUPPORTS/REFUTES is an unauthorized directional commitment, a failure we name Cherry-pick Override (CCO). 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07834`（标题“2606.07834 — Cherry-pick Override: Unsafe Directional Commitment in LLM Judges under Mixed Evidence”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [GRPO Does Not Close the Multi-Agent Coordination Gap](https://arxiv.org/abs/2606.07845v1)

精确版本 `2606.07845v1`；归档机制摘录（不替代全文证据）：Across 630 episodes spanning seven models and three philosopher counts, four frontier closed-source systems reach mean reward 0.45 to 0.87 and Mistral-Small 24B reaches 0.83 to 0.99, while Qwen3-14B reaches 0.13 to 0.35. 本次 exact-v1 全文复核把 canonical owner 固定为 `AGENT-MULTI-AGENT`，对应 `books/part-07-agent/82-multi-agent.md`。新增的预测、派生…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07845`（标题“2606.07845 — GRPO Does Not Close the Multi-Agent Coordination Gap”）。当前 Books 决定：已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md))；现有论点与采用边界以当前对照为准。

### [The Cold-Start Safety Gap in LLM Agents](https://arxiv.org/abs/2606.07867v1)

精确版本 `2606.07867v1`；归档机制摘录（不替代全文证据）：To study this systematically, we introduce Safety Over Depth for Agents (SODA), a benchmark that controls how many regular agentic tasks the agent completes before encountering a safety threat, supporting up to 20 preceding tasks. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-SECURITY`，对应 `books/part-06-ai-infrastructure/72-se…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07867`（标题“2606.07867 — The Cold-Start Safety Gap in LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators](https://arxiv.org/abs/2606.07874v1)

精确版本 `2606.07874v1`；归档机制摘录（不替代全文证据）：Despite their importance, LLM-judges themselves are rarely evaluated beyond human agreement in simple, static benchmarks. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-EVALUATION-SYSTEM`，对应 `books/part-06-ai-infrastructure/66-evaluation-system.md`。新增的预测、派生状态、验证或调度控制会带来 metadata、校准、维护与 failure-recovery 成本；相邻章节只消费该 owner 产出的 con…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07874`（标题“2606.07874 — Safety is Contextual, LLM-Judges Are Not: Navigating the Rigid Priors of Evaluators”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories](https://arxiv.org/abs/2606.07889v1)

精确版本 `2606.07889v1`；归档机制摘录（不替代全文证据）：We call this pattern strained coherence: a safety-relevant failure mode in which an agent has information that should change its behavior, states that information, and still acts against it. 本次 exact-v1 全文复核把 canonical owner 固定为 `PLATFORM-MONITORING`，对应 `books/part-06-ai-infrastructure/67-monitoring.md`。新增的预测、派生状态、验证或调度控制会带来 met…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07889`（标题“2606.07889 — Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories”）。当前 Books 决定：已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md))；现有论点与采用边界以当前对照为准。

### [Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation](https://arxiv.org/abs/2606.07936v1)

精确版本 `2606.07936v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-07936:start -->
Illusions of the Gold Standard: A Large-scale Analysis of Human Evaluation Protocols for Long-form Text Generation 处理的问题是：Twenty reproducibility fields separate what human judges measured, who judged, and how judgments may be interpreted; this changes the evaluation receipt contract.…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07936`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents](https://arxiv.org/abs/2606.07943v1)

精确版本 `2606.07943v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-07943:start -->
Poise: Position-Aware One-Instruction Skill Injection for Silent Execution on LLM Agents 处理的问题是：Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth an…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07943`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks](https://arxiv.org/abs/2606.07968v1)

精确版本 `2606.07968v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-07968:start -->
RecurGuard: Runtime Monitoring for Reasoning-Token Consumption Attacks 处理的问题是：A generation-time monitor combines recurrence, volume growth, and task progress over consecutive chunks and owns early termination of reasoning-token consumption attacks.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；ex…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07968`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-MONITORING`（[books/part-06-ai-infrastructure/67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md))；现有论点与采用边界以当前对照为准。

### [VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation](https://arxiv.org/abs/2606.07992v1)

精确版本 `2606.07992v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-07992:start -->
VATS: Exploiting Implicit Authority in Error-Path Injection via Systematic Mutation 处理的问题是：Tool errors are an authority-bearing ingress path; mutation across error structure and language changes MCP trust from tool output validation to error-loop admission and containment.。旧路径把这一变化隐藏…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-07992`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`AGENT-MCP`（[books/part-07-agent/83-mcp.md](../../../../books/part-07-agent/83-mcp.md))；现有论点与采用边界以当前对照为准。

### [Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents](https://arxiv.org/abs/2606.08200v1)

精确版本 `2606.08200v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08200:start -->
Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents 处理的问题是：An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention.。旧路径把这一变化隐藏…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08200`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Benchmarking Open-Ended Multi-Agent Coordination in Language Agents](https://arxiv.org/abs/2606.08340v1)

精确版本 `2606.08340v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08340:start -->
Benchmarking Open-Ended Multi-Agent Coordination in Language Agents 处理的问题是：A long-horizon world separates individual task reward from coordination reward while controlling communication, role specialization, and coordination difficulty.。旧路径把这一变化隐藏在静态规则、一次性分数、全局预算或事后处置中；exact-v1 的机制锚点…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08340`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`AGENT-MULTI-AGENT`（[books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md))；现有论点与采用边界以当前对照为准。

### [Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard](https://arxiv.org/abs/2606.08381v1)

精确版本 `2606.08381v1`；归档机制摘录（不替代全文证据）：<!-- claim:SF-2026-ARXIV-2606-08381:start -->
Auditing Proprietary Alignment in Large Language Models: A Comparative Framework Without a Ground-Truth Standard 处理的问题是：Reference-set-relative semantic divergence provides a black-box audit contract for provider-specific alignment when absolute ground truth is unavailable.。旧路径把这一变化隐藏…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08381`（标题“2606.07904 — Contract2Tool: Learning Preconditions and Effects for Reliable Tool-Augmented LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection](https://arxiv.org/abs/2606.08403v1)

精确版本 `2606.08403v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。 exact-v1 摘要将具体问题界定为：Text-centered prompt-injection defenses assume that the malicious signal is visible in one of the inspected text views. We study a reproducible LLM01-style indirect prompt/c…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08403`（标题“2606.08403 — Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics](https://arxiv.org/abs/2606.08417v1)

精确版本 `2606.08417v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：零参数劣质 sampler 可在非退化 entropy 下优化 gen-PPL，说明单一 scorer predictability 不能充当生成质量，评测必须转向分布差异。 exact-v1 摘要将具体问题界定为：Diffusion and continuous flow-based language models have emerged as the leading non-autoregressive alternatives to language modeling. Progress in both paradigms is overwhelmin…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08417`（标题“2606.08417 — Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing)](https://arxiv.org/abs/2606.08433v1)

精确版本 `2606.08433v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：AI code sandbox 不能用单一总分排序；host attack surface、leakage、stackability、CVE、patch cadence 与 fuzzing posture 必须按 threat model 分轴负责。 exact-v1 摘要将具体问题界定为：This paper reads six engine-level measurements together -- 1.1 host attack surface, 1.2 information leakage, 1.3 defense-in-depth stackab…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08433`（标题“2606.08433 — AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing)”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Scaffold Effects on GAIA: A Controlled Comparison](https://arxiv.org/abs/2606.08529v1)

精确版本 `2606.08529v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：GAIA 控制实验显示 scaffold 本身可显著移动同一模型的得分，因此 capability owner 必须分离 model、scaffold 与 attempt budget。 exact-v1 摘要将具体问题界定为：Published agent capability scores conflate what a model can do with what its scaffold lets it do, and the magnitude of this elicitation gap is not well characterized und…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08529`（标题“2606.08529 — Scaffold Effects on GAIA: A Controlled Comparison”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [ForesightSafety-SAGE:A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents](https://arxiv.org/abs/2606.08531v1)

精确版本 `2606.08531v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：ForesightSafety-SAGE 把 agent 风险从静态 prompt/终局判断扩展为 scenario generation、authority context 与执行轨迹上的多维检查。 exact-v1 摘要将具体问题界定为：Large language models (LLMs) are increasingly evolving from simple text-based interaction systems into LLM agents that can maintain memory, use tools, access exte…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08531`（标题“2606.08531 — VESTA: A Fully Automated Scenario Generation and Safety Evaluation Framework for LLM Agents”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems](https://arxiv.org/abs/2606.08661v1)

精确版本 `2606.08661v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Data Agent 把数据库执行、外部数据资源与 agent reasoning 三个攻击面串联，安全 owner 必须覆盖 query authority、tool side effects 与 evidence provenance。 exact-v1 摘要将具体问题界定为：Data agents integrate LLM-driven reasoning with relational data access, executable analytical tools, and multi-step workflow orchestration, ma…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08661`（标题“2606.08661 — Data Agents Under Attack: Vulnerabilities in LLM-Driven Analytical Systems”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation](https://arxiv.org/abs/2606.08679v1)

精确版本 `2606.08679v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：leaderboard 必须传播 task-level 不确定性并输出 rank intervals，而不是把多任务均值压成确定名次。 exact-v1 摘要将具体问题界定为：Pretrained models are often evaluated on multi-task leaderboards to measure their applicability in diverse contexts. However, current methods for aggregating performance across tasks into leaderb…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08679`（标题“2606.08679 — Rank Intervals for Leaderboards: A Hierarchical Framework for Model Evaluation”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models](https://arxiv.org/abs/2606.08831v1)

精确版本 `2606.08831v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：multi-step reasoning 的 factuality error 具有 ancestor-conditioned DAG 结构，conformal control 不能把 node-wise error 简单累加。 exact-v1 摘要将具体问题界定为：Large language models (LLMs) increasingly perform multi-step reasoning, where intermediate claims form implicit directed acyclic graphs whose node c…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08831`（标题“2606.08831 — Inference-Time Conformal Reasoning with Valid Factuality Control for Large Language Models”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs](https://arxiv.org/abs/2606.08840v1)

精确版本 `2606.08840v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：code model 的 pass rate 必须按语言、题型与 execution failure mode 分层，aggregate pass rate 会掩盖可部署性边界。 exact-v1 摘要将具体问题界定为：Code generation models are typically compared using compact execution benchmarks and aggregate pass rates, but such summaries obscure how performance varies across programmi…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08840`（标题“2606.08840 — Beyond Pass Rate: A Multilingual, Execution-Grounded Evaluation of Open Code LLMs”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Cheap Reward Hacking Detection](https://arxiv.org/abs/2606.08893v1)

精确版本 `2606.08893v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：cheap reward-hacking detector 用 trajectory embedding 与 metadata/reward distance 近似替代昂贵 LLM judge，但其清洗 split 与阈值不能外推为通用证明。 exact-v1 摘要将具体问题界定为：A small transformer encoder is trained to map Terminal-Wrench trajectories onto a unit sphere where embedding distance approximates the $L_1$…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08893`（标题“2606.08893 — Cheap Reward Hacking Detection”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops](https://arxiv.org/abs/2606.08960v1)

精确版本 `2606.08960v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：benchmark verifier 应通过 hacker→fixer→solver 的闭环迭代：攻击发现 exploit、修补拒绝 exploit、solver 防止补丁把合法解一并拒绝。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08960`（标题“2606.08960 — Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries](https://arxiv.org/abs/2606.09005v1)

精确版本 `2606.09005v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：RAG prompt assembly 必须把 document-authored metadata/provenance 视为 data 而非 policy，避免不可信文档在同一自然语言 channel 中冒充 control signal。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09005`（标题“2606.09005 — Document-Authored Control-Signal Impersonation: A Low-Cost Indirect Prompt Attack on RAG Safety Boundaries”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps](https://arxiv.org/abs/2606.09084v1)

精确版本 `2606.09084v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：tool agent 的安全状态跨越多轮 artifact write/read；防御必须记录 artifact lineage 并在组合读取时执行 provenance-aware policy，不能只审核当前 turn。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09084`（标题“2606.09084 — Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。

### [Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization](https://arxiv.org/abs/2606.09711v1)

精确版本 `2606.09711v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：reward-hacking 监测需观察显性 exploit 之前形成的 proxy-reward internalization：正确性判断、proxy acceptance 预测与 proxy-gold gap 推理三种状态。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09711`（标题“2606.09711 — Proxy Reward Internalization and Mechanistic Exploitation: A Learned Precursor to Reward Hacking and Its Generalization”）。当前 Books 决定：已有覆盖：`TRAIN-RLHF`（[books/part-04-training-system/31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md))；现有论点与采用边界以当前对照为准。

### [Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting](https://arxiv.org/abs/2606.09809v1)

精确版本 `2606.09809v1`；归档机制摘录（不替代全文证据）：旧路径在输入、workload 与 trust boundary 稳定时仍然合理；该 exact-v1 的约束变化是：Evaluation result 需要把 benchmark metadata、run data 与 model metadata 组合成可追踪 record，并按读者呈现 reproducibility、completeness、provenance/risk 与 score comparability。

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-09809`（标题“2606.09809 — Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting”）。当前 Books 决定：已有覆盖：`PLATFORM-EVALUATION-SYSTEM`（[books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md))；现有论点与采用边界以当前对照为准。

### [Harnessing Streaming Video in the Wild](https://arxiv.org/abs/2606.08615v1)

精确版本 `2606.08615v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：unbounded streaming video 同时要求 proactive interaction、long-horizon memory 与 real-time processing，形成跨 chunk state retention 与 bounded-latency 的联合合同。 exact-v1 摘要将具体问题界定为：Vision-Language Models (VLMs) are increasingly required to process unbounded video streams in applications such as v…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08615`（标题“2606.08615 — Harnessing Streaming Video in the Wild”）。当前 Books 决定：已有覆盖：`MULTIMODAL-REPRESENTATION`（[books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md))；现有论点与采用边界以当前对照为准。

### [Diffuse AI Control on Fuzzy Tasks](https://arxiv.org/abs/2606.08892v1)

精确版本 `2606.08892v1`；归档机制摘录（不替代全文证据）：旧路径在较稳定的输入、workload 或单一控制面下仍然合理；该 v1 所处理的约束变化是：Diffuse AI Control 针对长时段、fuzzy-task sabotage 把控制证据分散到多次任务与审计预算，而非依赖单次可验证 outcome。 exact-v1 摘要将具体问题界定为：AI models deployed in critical domains, such as AI safety research, may subtly sabotage our efforts due to misalignment. Diffuse AI Control is a subfield of AI safety concerned with…（完整机制与条件见原审阅）

完整方法、评价与反证见[该家族原审阅](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md)，唯一定位 `review:SF-2026-ARXIV-2606-08892`（标题“2606.08892 — Diffuse AI Control on Fuzzy Tasks”）。当前 Books 决定：已有覆盖：`PLATFORM-SECURITY`（[books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md))；现有论点与采用边界以当前对照为准。











归档保留旧 exact-v1，只在 identity/claim 不变时复用。独立 audit 将旧 39 项 disposition 重判为 38 项 `已有覆盖`、2606.09774 撤回；new Integrate = 0，正文缺口 = 0。root 已删除 2606.09774 的 Books body/trace adoption chain。READY、QUEUE、POST_WRITE、source-specific Review note 与章末 trace 都只能作为路由/审计材料，不能授权 candidate 或 Books body。以下 38 项为 closure-recovered Candidate 的同标题、同 URL Evidence；74 个 prior 的完整审阅由 [V2_1_EVIDENCE_ARCHIVE.md](../_sources/daily-20260609/V2_1_EVIDENCE_ARCHIVE.md) 提供。

### [Enabling KV Caching of Shared Prefix for Diffusion Language Models](https://arxiv.org/abs/2606.07571v1)

`arXiv:2606.07571v1`；正文定位：§4 Observations、§5 BiCache、§6 Experiments、§9 Limitations。机制是在浅层复用 exact-prefix KV，并按共享前缀比例选择安全深度；深层按间隔刷新。作者实验为 LLaDA、B200 180GB、batch=1、generation length=256、steps=128，报告相对无缓存 36.3%～82.8% 加速；不证明其他 diffusion architecture、accelerator 或生产 SLO。Books：`已有覆盖`，`INFER-KV-CACHE` 已明确 causal decoder immutable-prefix 与 bidirectional dependency 的差异、refresh frontier 及旧路径共存边界。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs](https://arxiv.org/abs/2606.07577v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07577v1) §3.1–3.3：chunk后按Attention importance与hidden-state cosine redundancy提议淘汰；audio/visual独立cache，逐层/模态预算在小视频集校准。不是未来Query的无损保证；SFT另用hidden-state carrier与截断反向，不等于原淘汰器本身的收益。
- **Evaluation：** §4.3、§5/Table2–3：SALMONN 4B/8B、Qwen2.5-Omni 7B，1FPS/360p，默认每层8K budget，H800。比例变化呈现音频/视觉的任务取舍；Qwen Contextual 34.2低于HERMES 34.5。SFT仅SALMONN，32×H800/36h，不能与training-free成本混同；precision、batch/concurrency、SLO未披露。
- **Limitations：** §7明确hidden-state驻留开销、长音视频benchmark不足与linear-attention需要重设计。校准不覆盖未来问题、并发和硬件迁移；未复现实验。
- **Books：** `整合`：Ch45旧Prefill/Decode query校准没有独立modality budget。6分保留，因确认知识缺口深入必要范围；`INFER-KV-CACHE`已在该段之后写入两段机制/代价/反例。sep21_resume_v3准入、必要证据与实际写后独立通过；不代表整日日级验收已通过。

### [Training-Inference Kernel Contracts: Bounding Divergence in Post-Training and Deployment](https://arxiv.org/abs/2606.07581v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07581v1) §4–6给kernel-indexed policy、分slice合同与per-token梯度偏差界；§6.1要求support overlap、有界advantage与score norm，不控制trajectory乘积或完整训练收敛。
- **Evaluation / Counterevidence：** §8只是待执行protocol，Appendix C明确未随论文发布的实现草图，无生产实测。§6.3 Eq17在c=0时clip(w,1,1)=1，退回Eq15的有偏估计器，不能如正文声称强制policy equivalence；large c的文字解释也与不截断可恢复Eq14的方向不一致。
- **Limitations：** §11含测量、proxy Goodhart、观测不完整与recovery自身风险；概念合同不证明实现或正式保证。上述中央公式/解释冲突不能用已有章节覆盖标签抹去。
- **Books：** 保留原6分，纠错触发深入必要范围；`争议/暂缓`，不写入Books、不作为正面保证。重开需作者纠正Eq17及clip/bias解释并明确per-token与trajectory范围。root与sep21_resume_v3实际独立核准冲突；未复现实验。

### [From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs](https://arxiv.org/abs/2606.07586v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07586v1) §IV将人工协作的NPU部署记录分为CPU参考、逐kernel、单block、全model、prefill/decode优化与集成等阶段；各阶段数值门后保留human checkpoint，最终独立context evaluator重跑数值与profile。Skill提出编译/优化，验收不由自身成功trace授予。
- **Evaluation：** §V为Ryzen AI9 HX370/XDNA2、MLIR-AIR、2048序列、Claude Code/Opus4.7，8新模型加Llama3.2-1B参考；roofline归一化利用率不等实际绝对时延。部分耗时为估计，未有去除Skill/独立review的受控因果消融；权重/KV为BF16的bytes模型亦不证明任意kernel数值等价，在线并发/SLO未披露。
- **Limitations / Books：** §VI将MoE/MLA/其他spatial devices列未来，少量human debug仍存在，独立evaluator不能被外推为防止一切reward hacking。`已有覆盖`：Ch84“Skill Compiler必须绑定Target Profile”及“reproduction boundary”正文已分别规定target-specific候选、独立held-out admission与fresh executor重执行，正好承载本次采用的边界；不为八阶段实施案例另建机制owner。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [The Routing Plateau: Understanding and Breaking the Accuracy Limits of LLM Routers](https://arxiv.org/abs/2606.07587v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07587v1) §4–6区分query-only预测与生成后correctness oracle：不同router可频繁交换选择却赢输抵消；data/encoder scale及task fine-tuning改进instance-level预测，不能仅靠router类别决定上限。
- **Evaluation：** 21方法/5 benchmark，§5按hard-query与paired wins/losses拆分，而非只看aggregate；§6.2–6.3中30K→300K、base→large与FT分别消融，但仍残留oracle gap。该oracle需要事后标签，不是deployable免费route；五类离线工作负载结果无生产并发、SLO或跨model-pool保证。
- **Limitations / Books：** §6.4与Appendix B保留query-only困难和后续partial generation成本。`已有覆盖`：Ch56“Cascade与Pregen Router的成本坐标不同”“效用预测与委派率预算需要分别校准”实际正文已经区分事前不确定性、逐例expert增量预测与标签authority；不把模型平均更强当当前请求必有收益。这里只用受限反证验证这项已有判断，不声称原章含本论文全部实验。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference](https://arxiv.org/abs/2606.07665v1)

`arXiv:2606.07665v1`；正文定位：§2–§3 Method、§4 Evaluation、§7 Limitations。LLM 只给 metadata、ranking 与参数建议，compiler/runtime 负责 bounded candidate、模板生成、静态检查、验证、benchmark 与 fallback；LLM 不直接准入可执行 CUDA。作者在 A800 SXM4 80GB、FP16、四个 1B～4B 模型和披露长度上报告 full hybrid 相对 vLLM 约 1.06～1.07×；消融没有独立隔离 LLM guidance。Books：`已有覆盖`，`INFER-TENSORRT-LLM` 已承载“Agent proposal 不拥有 executable admission”及 fallback。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [Fast LLM-Based Semantic Filtering: From a Unified Framework to an Adaptive Two-Phase Method](https://arxiv.org/abs/2606.08090v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08090v1) §3–6将cluster voting的已标注样本复用于proxy训练；mixed clusters触发第二阶段，另取score-stratified校准，再对全语料重打分；训练、校准、oracle fallback与proxy成本共同结算。设计不是“cluster全同票即真值”。
- **Evaluation / Boundary：** §8三10K-document语料及各20 query，以固定oracle label为truth；oracle相对accuracy不等外部正确性。§5.2的经验率与Clopper–Pearson上界加权仍小于完整上界，不能据此宣称同置信水平保证；§5.5的独立Bernoulli/同分布条件也不消除训练使用校准集带来的依赖。实验95%query达目标不是全query硬SLA。
- **Books：** `仅报告`：成熟token interaction、两阶段复用与校准启发式的组合提供受限成本案例，但未支持更强概率保证。Ch56现有流式semantic predicate段已有label authority、质量—委派成本与失配升级原则，不把此blend写成新的形式保证；原6分标准审阅保留，不因为本轮不采用而删候选或降分。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/abs/2606.09079v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09079v1) §2训练query-side低秩indexer，对冻结compressed keys作Sigmoid阈值lookahead；离线未来window目标、跨layer筛选与每64 decode step更新，把冷CPU chunks按预测迁回HBM。HCA及recent/decode窗口仍保留，不是常数总cache。
- **Evaluation / Counterevidence：** §3.1–3.3固定所述DS-V4骨干/保留路径；context-independent请求的绝对保留仍随长度增长，MRCR严重退步，golden-chunk oracle也不消除密集全局依赖。短训长测的失败不能由pointwise打分形式排除，文中“恰好2倍”只属于该测例，不是一般理论边界。
- **Books：** `已有覆盖`：Ch45“隐式lookahead”正文已绑定future-importance target、selector identity、kept indices与未知query回退，CPU可恢复tier已有独立owner。此案例验证这些具体适用边界，不把局部headline或固定layer sweet spot写成普遍部署recipe；未复现，benchmark性能不推production SLO。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy](https://arxiv.org/abs/2606.09080v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09080v1) §3–5/B按GEMM M/N/K及static/dynamic拆pruning，通过真实operator replacement和统一profiling解释删FLOPs与可执行工作不同；额外projection、selector、GEMM分解与非GEMM成本可抵消理论收益。
- **Evaluation：** Llama3.1-8B/RTX Pro6000(sm120)，CUDA graph、尺寸16对齐，零样本最大4096评测；不同family训练预算非同一条件：dynamic M需更多steps、static K不能vanilla LoRA merge。throughput的shape模拟/单step计时不能与真实production请求队列等同，precision及线上concurrency/SLO未披露不补造。
- **Limitations / Books：** Limitations排除MoE、Hopper/数据中心Blackwell并说明高层DSL与hand CUDA差异。`已有覆盖`：Ch66的runtime/configuration-conditional evidence与Ch49硬件/FLOPs及单kernel≠完整Serving正文已承载实际采用命题；不同family的质量—成本frontier是局部证据，不采用普遍最优pruning排名。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.09138v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09138v1) §3.1–3.3、4.1–4.5：Gateway 接黑盒 model calls/白盒 callbacks，Data Pool 持久保存 tokens、reward、trajectory relation、policy/source metadata；ready batch 由 trainer pull，prefix-tree 合并共享前缀但各步 reward/训练语义仍独立。
- **Evaluation / Boundary：** §4 是 dashboard demo，不是质量、吞吐或 RL 收敛对照；未披露可支持性能数字的模型/硬件/precision/长度/并发/SLO。可见数据不证明 reward 正确、完整轨迹兼容或任意算法无偏。
- **Books：** `已有覆盖`，`TRAIN-GRPO` 的“Agent RL …不同终态”和“从 Opaque Harness Call 到可训练 Trajectory Tree”实际承载 token lineage、版本/环境/reward completeness、共享prefix与独立训练消费。采用数据接口分责，不采用未验证的效率承诺；标准审阅完成，独立复核待完成。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [Resource-aware Computation-Communication Overlap for multi-GPU ML Workloads](https://arxiv.org/abs/2606.09200v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09200v1) §3.1–3.3：用每block shared-memory占用塑造 GEMM residency，双stream/event维持依赖，给 collective 较高priority以减少尾部；priority不是抢占保证。
- **Evaluation / Counterevidence：** §4.1–4.3：4×A40/A100/H100与8×MI250X，896MB collective；GEMM 8192×8192×8192或8192×57344×8192，64×64×{32,64}tiles。高block数MI250X可更慢，communication priority的收益可被compute residency损失抵消。作者kernel/collective实验不是完整model训练质量或线上SLO；precision未披露不补造。
- **Books：** `已有覆盖`，`TRAIN-DISTRIBUTED-TRAINING` 的“Overlap不是免费隐藏：Communication与Compute共享资源预算”实际解释共同争用、critical path、资源分配及profile/fallback。采用条件性overlap，不采用跨GPU通用提升；标准完成，独立复核待完成。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs](https://arxiv.org/abs/2606.09508v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09508v1) §3–4：分块observation attention的entropy区分head行为，动态head按entropy变化分配读取预算，rigidhead固定额度；生成Nd个tokens后再用output-query选择decode留存，区别于prefill末尾query proxy。entropy是选择sensor，不是未来无损证书。
- **Evaluation / Counterevidence：** §5：Llama3.1-8B/Qwen2.5-7B，单H10080GB、192GBCPU/8cores；LongBench/InfiniteBench，延迟改写needle为summary并生成100tokens。作者prefill2048/decode1024与StreamingLLM4096+4sink不等统一预算，precision/线上concurrency/SLO未披露。§4.4保留小系数N²项，“近线性”不能改写成渐近O(N)。短context profiling成本限制收益。
- **Books：** 保留6分，中心争议触发深入：`争议/暂缓`。exact HTML Algorithm3 L14/PDF p5 L12 的 `max(min(Bi,B0),3B0)` 在正 B0 下恒为3B0；§3.1 entropy 集中/均匀定义与 dense/near-deterministic 分类说明不一致。sep22_resume_v3 独立确认。不用于正面证据、Books或性能保证；重开需作者修正算法与分类并给出实现/实验对应。

### [BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference](https://arxiv.org/abs/2606.09514v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09514v1) §4.1–4.4：first-layer KV作为prefix sensor，scorer+offline prior选top-k中间层，首尾层始终执行；无指定budget时GRPO predictor提议depth，decode可逐token改变路径。
- **Evaluation / Counterevidence：** §5.2.1/D.4/D.5/C.2/Limitations：Llama3-8B/Qwen2.5-7B、V10032GB/A10080GB配置，Alpaca/SAMSum输出128tokens；轻剪枝routing/gather-scatter可抵消节省，decode固定路径可更快，GSM8K大幅质量损失。全部weights仍驻留，batch异路径导致skipped-layer cache miss，论文以zero-fill表达未执行状态，不是exact完整cache。precision、input长度/batch/concurrency/SLO未完整披露。
- **Books：** `整合`：`INFER-TENSORRT-LLM` Ch49 early-exit 后已写逐 token layer-path、缺失 KV/zero-fill、routing 代价与固定路径回退。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过。

### [FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing](https://arxiv.org/abs/2606.09551v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09551v1) §3.1、4.2、Theorem4.6/4.7：spec-compatible scalar gate把masked comparison和interval coefficient payload编成至多两次noninteractive backend interface evaluation；仍有Horner/Beaver乘法、fixed postprocessing和域转换，vector reduction另由MPC处理，不是整模型仅两次通信。
- **Evaluation / Security Boundary：** §6.1–6.4/B.4：两server各RTX PRO6000 Blackwell/EPYC9654/CUDA13；BERT/GPT、32–512token；LAN/WAN延迟为投影非真实WAN测量。gate-level semi-honest、至多腐化一方/non-collusion，显式shape leakage与fresh uniform masks依赖primitive/subprotocol安全。compiled program可复用但每inference的keys/masks/triples一次性；padding消除mask-dependent shape增加离线/在线成本。未复现、未证明malicious安全或任意Transformer统一收益。
- **Books：** `整合`：`PLATFORM-SECURITY` Ch72 隐私推理分支实际加入 compiled shape 与每执行 fresh preprocessing 分责、非共谋威胁面及 padding 代价。6分知识缺口深入；sep22_resume_v3 源→owner与实际正文/邻接写后通过。

### [Rosetta Memory: Adaptive Memory for Cross-LLM Agents](https://arxiv.org/abs/2606.07711v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07711v1) §3.1–3.2 Eq1–3/4.1–4.2：writer按source model profile将本步observation/action形成memory entry，reader按target profile和当前observation从bank构造使用context；二者不能互换。Flan-T5-small soft-prefix双模块，reward-filtered expert iteration保留topα，并以minimum gain偏置抽样跨模型组合。sep22非作者定点核验纠正了初稿中read/write角色写反的问题，尚未写入Books。
- **Evaluation / Boundary：** §5.2–5.6/Implementation Details，六种API profile、Hotpot/2Wiki/MuSiQue，normalized containment及GPT-5.4-mini judge并非exact match或独立真值。held-out API transfer限所测混合；reader移除在部分任务仍竞争，η过强会降益，硬件、precision、并发/SLO未披露。
- **Books：** `整合`：`AGENT-MEMORY` Ch77 late construction 后实际加入 source writer 与 target reader、迁移训练成本/局部反例/固定模型回退。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过；初稿角色纠正在写书之前完成。

### [Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents](https://arxiv.org/abs/2606.08151v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08151v1) §3.1–3.6：用反事实启发的action/outcome/necessity/negative-transfer效用选结构化cards；selection前压缩可改变选中ID，selection后只压缩同组证据。图/provenance/schema审核不证明因果识别或语义忠实。
- **Evaluation / Boundary：** §4–5/7，SWE-bench Verified仅file-level 50例；Codex-5.5仅5例。合成Repo设置中generic summary可强于cards；postselection节省tokens不等task增益。stale/harmful证据仍会被选，MLP/QLoRA拟合agreement不等真实任务质量，API硬件/precision/SLO未披露。
- **Books：** 仅报告：保留局部selection/compression反证，不把counterfactual-inspired打分写成因果或通用Memory增益。Ch76既有retrieval relevance与answer utility分责继续成立；原6分标准审阅，不因不改书删候选，非作者复核待完成。

### [Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures](https://arxiv.org/abs/2606.08275v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08275v1) §2–3/5–7：固定prefix与mock tool环境，对action/observation/context/policy做干预，K次随机continuation比较outcome分布，并以same-policy resample作null；总效应不是直接效应，承诺点与Shapley估计受预算和方差约束。
- **Evaluation / Boundary：** §5在planted SCM ground-truth上验证归因，API temperature=0也不能保证重放相同；本地seed与action-match仅受控域。common random numbers列未来，judge outcome有噪声，真实不可逆tool/外部effect不在mock replay保证内。
- **Books：** `整合`：`PLATFORM-TRACE` Ch69 prefix-preserving replay 后实际加入 same-policy null、随机 continuation/CI、总效应非直接效应及不可逆操作边界。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过。

### [Autonomous Incident Resolution at Hyperscale: An Agentic AI Architecture for Network Operations](https://arxiv.org/abs/2606.09122v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09122v1) §III/IV：Intake→Planning→带锁/授权Execution→health/bake-in Verification与rollback；typed skills限blast radius，at-least-once ack消息不等exactly-once effect。
- **Evaluation / Boundary：** §VI/VIII，>90%、hours→minutes及zero critical等无可核sample窗口、分母、matched comparator或不确定性；model、hardware、precision、并发/SLO未披露。范围仍是有限network incidents，formal verification与跨域扩展为未来。
- **Books：** 仅报告：architecture提供运维实现背景，未支持新的可靠性保证；不把其headline写为生产事实。Ch84已有action authority、bounded capability、rollback原则，不能仅凭主题将整篇宣布已覆盖。原6分标准审阅，非作者复核待完成。

### [Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents](https://arxiv.org/abs/2606.09316v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09316v1) §3–4：taxonomy prior引导资源抽取，生成skill contract并与registry reconciliation，versioned SkillBank投影层级检索；程序性skill与declarative RAG共同消费，源文档不因此获得执行authority。
- **Evaluation / Boundary：** §4.1/§5命令行任务success对照分别检验无task-time retrieval和skill+RAG；不证明所有资源可安全执行或跨harness泛化。未披露的硬件/precision/并发/SLO不补造；只采用结构化资产分责，不采用通用效能倍率。
- **Books：** 已有覆盖：Ch84“Resource和trajectory…不能共享无类型summarizer”实际含typed tuple、provenance/schema/dedup/permission/smoke-test、temporary pool、held-out admission与publish/rollback。该处承载采用命题而非论文全实验；标准完成，非作者复核待完成。

### [What Should a Skill Remember? Quality--Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents](https://arxiv.org/abs/2606.09421v1)

`arXiv:2606.09421v1`；正文定位：§3 Method、§4 Evaluation、Limitations。系统先 profile task/skill，再从 source-native、workflow、API/code、rule/formula preservation strategy 中选择 anchor，并审计缺失 anchor；选择目标是受约束的 quality–cost utility，而不是最短 rewrite。SkillsBench 86 个可运行 skill、固定 task/environment/verifier，并覆盖多种 agent stack；held-out 与 cross-model 结果只证明该受控语料中的 token/cost 下降，不覆盖动态资源、更新 skill、生产 latency/pricing 或人工审阅。Books：`已有覆盖`，`AGENT-PLATFORM` 已要求 paired no-skill/skill evaluation、correctness/trajectory/cost 分账与生命周期 compaction。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning](https://arxiv.org/abs/2606.09447v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09447v1) §3.2/4/5.1–5.2：SoM+DOM观测；隔离account/sandbox，META记录资源create/verify/destroy依赖，ResourceCoder按需provision。环境缺资源应区别于policy失败；group/batch两级normalization、σ=0跳过改变训练语义。
- **Evaluation / Boundary：** §6/7.4，400单动作×3runs；278任务/12产品含76标准202hard，相同环境3runs pass@1与any-pass@3分开；two-judge/human对齐不保证ORM无false positives。32B仍gray test，旧frontier线上数据与projected成本不等32B生产实测。DOM维护/provision成本与环境真实性限制收益。
- **Books：** `整合`：`TRAIN-GRPO` Ch33 service 环境后实际加入 create/verify/destroy 资源前置条件、provision失败与policy失败分账及成本/旧固定环境回退。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过。训练 admission/cleanup 记录是工程推断，不冒称作者已实现收据系统。

### [Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.09483v1)

`arXiv:2606.09483v1`；arXiv official export PDF §2 Method、§2.1 Cognitive Capability Hierarchy、§2.2 Synchronous Daytime Writer、§2.3 Asynchronous Nighttime Sweeper 与 §2.4 Read Path and Latency。Evaluation：§3 Experiments（Setup/Main Results/Ablation/Analysis）。Limitations：独立 Limitations；只覆盖披露的 vector store、benchmarks 与双进程 memory implementation。Books：`已有覆盖`，owner=`AGENT-MEMORY`；现有 episodic/semantic consolidation、在线写入/离线归并、visibility/commit 与读路径已覆盖。完整记录见 [V3_EVIDENCE_RECOVERED.md](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [SecureClaw: Clawing Back Control of LLM Agents](https://arxiv.org/abs/2606.09549v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09549v1) §3.1–3.3：untrusted runtime只能planning；gateway把plaintext存trusted handle store，以caller/session/TTL/object/sink绑定opaque handle。bounded schema summary是显式declassification。executor独占effect sink，重算canonical request digest并核freshness/replay/confirmation后commit。
- **Evaluation / Boundary：** §4.1/6，ASB/AgentDojo/AgentLeak同harness；AgentLeak仍16/496 leakage、AgentDojo4/629 ASR，不能声称zero所有风险。可信gateway/policy/executor、完整sink mediation和字段分类为前提；合法动作语义错误/summary泄漏/utility损失未消除，未复现实验。
- **Books：** `整合`：`PLATFORM-SECURITY` Ch72 在既有 handle/授权论证内补齐读侧 plaintext 驻留于 trusted store、caller/session/TTL/object/sink 绑定，以及 bounded summary 的显式 declassification；executor 的 effect 授权保持独立。必要知识缺口已深入核验，sep22_resume_v3 源→owner及实际两段/邻接写后通过；不采用跨部署安全保证，不代表整日日级通过。

### [Collaborative Human-Agent Protocol (CHAP)](https://arxiv.org/abs/2606.09751v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09751v1) §4–8：workspace/participant/task/audit接口，accepted envelope原子推进authoritative task projection与event；human override记录base/diff/reviewer identity，rollback追加corrective evidence而非删史。
- **Evaluation / Boundary：** normative protocol/reference v0.2不是实测性能或法律合规证明；optional Ed25519/SCITT只绑定身份/日志，不证明override正确。shadow/trial/production policy不同，append-only原始敏感数据仍需治理，concurrency/SLO未披露。
- **Books：** 已有覆盖：Ch81“对象已保存→状态已激活”实际规定predecessor authority、revalidation和Commit/Reject/Quarantine/Defer，event persistence/approval与compensation也有独立职责；Ch84 human consent仍不是truth。采用该已有合同，不宣称原书含每个API；标准完成，非作者待完成。

### [VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents](https://arxiv.org/abs/2606.07595v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07595v1) §2/4–5：将image中标为non-propagatable的字符串是否进入tool argument，区别于chat response泄露和真实downstream harm。按no tool/safe tool/response-only/tool-only/both拆trace分母。
- **Evaluation / Boundary：** §4/8每model/scenario通常50，parse-error格用非error45/47/49/42/46不可混同；simulated单步tool未执行effect、无multi-turn recovery。PII prompt多靠抑制tool use降传播，不能由低ASR推utility保持或全链安全。
- **Books：** 已有覆盖：Ch72实际typed tool/action boundary、最小数据暴露与effect授权段已要求同时审查参数和输出，benchmark补充受限验证而不授新安全保证。6分安全约束必要范围深入，非作者待完成。

### [Finite Certificates for In-Context Determinacy and a Threshold Theory of Emergence in Language Models](https://arxiv.org/abs/2606.07623v1)

- **Identity / Theory：** [exact-v1](https://arxiv.org/html/2606.07623v1) §2–6外置many-sorted first-order semantic presentation，prompt约束/preference与decoder kernel分开；compactness下有限certificate、finite deterministic task family pair separator、finite-field rank见§4–5，不是Transformer内部实现或任意LLM的可计算证书。
- **Evidence Boundary：** §6的latent-confidence与不连续metric threshold是数学构造；不提供参数模型可识别的语义measure、可操作oracle或真实model calibration实验。有限certificate存在性不等有效求解/小样本可学；不能据此声称解决hallucination或必然涌现。
- **Books：** 仅报告：保留逻辑/解码/指标的区分及严格假设，不将外置语义模型当已验证模型机制。原6分标准理论审阅，非作者必要定理与边界复核待完成。

### [SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?](https://arxiv.org/abs/2606.07682v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07682v1) §3.1–3.3/4.1–4.4：Harbor容器最终状态与hidden verifier计分，visible development feedback分离；reference oracle/no-op/exploit search构成task admission。CLI产品与固定Terminus scaffold不同，不是只比较模型权重。
- **Evaluation / Counterevidence：** §5，20tasks×13configs×5=1300rollouts，2–10h、CPU/内存/GPU按task，pass@1及binomial SE；human expert时长是估计。failure分析仅10task subset，141infra+79证据不足被隔离，526分类不等全部1300独立判断。post-hoc judge嫌疑不是作弊因果证明，cached/API costs与context/provider配置不同。
- **Books：** 已有覆盖：Ch66 actual harness/model/environment identity与agent process/effect评价、Ch84 held-out independent executor已承载采用判断。受限长任务验证不证明开放任务成功率，也不把新suite当新owner；标准完成，非作者待完成。

### [When Behavioral Safety Evaluation Fails: A Representation-Level Perspective](https://arxiv.org/abs/2606.08044v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08044v1) §2–4 / dissociated construction / KL note / §7：在保持回答拒答的 SFT+KL 约束下，另用 harmful-prompt indicator 和分离 optimizer 改变隐状态 probe 的可分性；标签不是逐回答的真实危害。行为不变与表示分数改变可被人为解耦。
- **Evaluation / Boundary：** Gemma2-2B、Llama3.2-3B、Qwen2.5-3B 和固定 HarmBench/probe；受控白盒构造不证明黑盒生产攻击，probe 层、prompt 前缀、训练分布改变可改变结论。未验证任意 detector，未复现。
- **Books：** 已有覆盖：`PLATFORM-SECURITY` Ch72 refusal 与潜在知识/行为可提取性的区分，以及 probe/version/geometry 不能拥有真值的具体正文；不是 Ch66 全主题覆盖。sep22_resume_v3 必要源→实际正文独立通过，整日日Gate另验收。

### [Decoy-Calibrated Failure Audits for Language Models](https://arxiv.org/abs/2606.09046v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09046v1) §2.1–2.3：冻结错误标签与 descriptor library，置换每个描述子的布尔成员保持 prevalence，用同一 lift/support 规则比较真实与假 descriptor；经验 FDP 阈值后固定 survivor，再要求 holdout 支持、同方向和最小绝对 lift。
- **Evaluation / Boundary：** §3–5：Claude Haiku4.5，controlled multi-table 与 MuSiQue/LongBench v2；后两者不确认任何 finding。单 descriptor 置换不保持联合相关，估计 FDP 不是 finite-sample FDR；不能把零 finding 当错误不存在或相关当因果。硬件、precision、服务 concurrency/SLO 未披露/非此比较目标。
- **Books：** 整合：`PLATFORM-EVALUATION-SYSTEM` Ch66 已实际补齐 prevalence-matched fake competitor 的经验底线与冻结 survivor 后 holdout 复验，不能将其当 formal FDR 或因果证据。保留6分，确认缺口后深入必要范围；sep22_resume_v3 必要源→owner及实际两段/邻接写后独立通过。

### [REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces](https://arxiv.org/abs/2606.09071v1)

- **Identity / Method：** `arXiv:2606.09071v1`；§3。诊断 candidate 后执行 prefix-preserving targeted replay；diagnosis-specific faithfulness gate 阻止无关恢复，失败时 verified rollback，并以 contrastive explanation 更新诊断。
- **Evaluation：** §4；WTQ 137/119、GAIA 117/83、BBM 150/150、SWE 31/30，gpt-5.2 auditor/agent、temperature=0；主实验使用 oracle expected answer 与 exact-match localization。
- **Limitations：** Appendix R；结构化环境、oracle 依赖、不可逆副作用与缺失环境会阻止 replay；只处理 single earliest decisive error。Outcome flip 支持 intervention 的充分性，不证明归因唯一或最小。
- **Books：** `整合`，owner=`PLATFORM-TRACE`；实际正文写入 prefix preservation、diagnosis-specific faithfulness gate 与 sufficiency/non-uniqueness 边界；`AGENT-REFLECTION` 只保留短 handoff。sep21_resume_v3必要来源、实际写后与邻接独立通过。

完整定位与边界见[恢复证据](../_sources/daily-20260609/V3_EVIDENCE_RECOVERED.md)。

### [Precision Is Not Faithfulness: Coverage-Aware Evaluation of Grounded Generation with a Complete Oracle](https://arxiv.org/abs/2606.09376v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09376v1) §3–6 / §8 / §11：FastF1 结构化提取生成 race facts oracle；将输出 claim 分成 supported/contradicted/unverifiable，同时核对目标事实覆盖，verifier-guided edit 补漏。所谓 complete 仅限派生 schema/fact types，非所有实体、因果或自然语言含义。
- **Evaluation / Boundary：** 7253 构造样本与207 test/season holdout；完整性提示可使 recall 从.60降到.47，部分模型反向变化。抽 claim 漏检、过拆分与 oracle 派生错误都是 evaluator error；提高 precision 可能只是删 claim。非开放世界 gold、未复现。
- **Books：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` Ch66 atomic claim precision/recall、grounding/coverage、reference snapshot 和 evaluator 分账的具体正文。只采用该 contract，不采用开放事实完备/通用生成增益；sep22_resume_v3 必要源→实际正文独立通过。

### [WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces](https://arxiv.org/abs/2606.09426v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09426v1) Task Admission / P1–P3 / Main Results / Failure Analysis：114任务按通道不可替代、交错及跨 app admission；冻结 Linux VM/任务材料，judge 新进程重新取实际 artifact、评估 clause 与过程维度，防只看 final claim。
- **Evaluation / Boundary：** GUI-only/CLI-only 低分受 task construction 必须混合通道影响，不证明通用界面优劣；harness/model/thinking budget 和 best setting 不全可比。final-only 重打分差额不是识别出的真实 cheating 因果率，judge 并非独立 human gold，timeout/context overflow须分账。
- **Books：** 仅报告：保留受限任务 admission 与 artifact re-fetch 的实现案例；不把一个 benchmark 的混合通道需要升为普遍架构条件，也不以 Ch66 同主题冒充具体机制已覆盖。

### [H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions](https://arxiv.org/abs/2606.09461v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09461v1) §3–5 / annotation：human directors+LLM scripts 构造有 speaker/time/modality 归属的多会话内容，人工问答检验 current facts、更新冲突与跨人引用。memory retrieval 与归属/更新可分。
- **Evaluation / Boundary：** dyadic/multiparty 会话密度、长度不相同，不能归因 participant 数；caption+text 与 multimodal 输入信息不同。human200 子集 judge κ=.84 不覆盖全体；100 selected failures 的 misalignment/speaker 比例非总体频率。memory build 与 query inference 延迟不横比；模型为所测 Qwen2.5VL3B/7B/GPT4.1nano。
- **Books：** 仅报告：受限 benchmark 暴露归属/更新误差，但尚未支持新的 memory 改进机制或通用因果结论。保留6分标准审阅，不因不改书删除候选。

### [Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback](https://arxiv.org/abs/2606.09748v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09748v1) §3 / §4.1–4.4 / §5：LC-ODR 每轮重新 plan/search/report，RGI 从固定 rubric 给 process feedback；将新 criterion incorporation 与已满足 criterion regression 分开，不能只看总分增长。
- **Evaluation / Boundary：** 50 DRACO任务/10域、三轮、三配置，反馈 GPT4.1、评判 GPT5.2/Tavily 检索设置。不同 criterion 分母不能直接横比净率；Turn3 非单调，rubric/反馈/评分共用 gold 与 API budget 限制独立性。案例不证明长期自改善。
- **Books：** 仅报告：保留反馈收益与旧 criterion 回退并存的受限证据；不将既有迭代流程新命名作为机制，也不把自动反馈的本地增益写成跨任务可靠性。

### [iOSWorld: A Benchmark for Personally Intelligent Phone Agents](https://arxiv.org/abs/2606.09764v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09764v1) §3 / Evaluation / §4.2：26 cloned native apps、固定 persistent user state，133 tasks 分 single/multi-app/memory；运行50step后按实际交互结果 judge。Vision+XML 有额外访问面，非同信息纯视觉对照。
- **Evaluation / Boundary：** API computer-use 系统与 Qwen35B/vLLM 设置不同，closed/open 与 harness 混杂；128human subset κ=.77不提供全部gold。分任务成功率不相乘为综合概率，step budget failures 不等规划不能；cloned simulator 不证明真实手机权限/生产隐私。
- **Books：** 仅报告：任务/环境实现与失败诊断有上下文价值，但不产生新的长期 Agent 执行机制或跨模型能力排序。

### [MC-PDD: Masked Corpus-Level Pretraining Data Detection for Black-Box Large Language Models](https://arxiv.org/abs/2606.07996v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07996v1) §IV–VI / limitations：按实体/TF-IDF 挑 corpus-specific words，遮盖后黑盒候选补全，用语料级 hit 差异与 reference/non-specific baseline 比较；无需 logits，不是逐记录 membership oracle。
- **Evaluation / Boundary：** SteamMIA 有标记参考语料，Llama3.1 instruct 与10次重复；API release date proxy、BBC 年份不能确认旧语料必然 member。OLMo arXiv 某些设置区间/差异不显著；topic/time/word uniqueness、shadow/reference 差异可解释效果，需 instruction 能力。
- **Books：** 仅报告：保留概率性 corpus 检测在身份核验中的限制，不把统计线索写为法律归属或已知 pretraining provenance；原6分不改，未核验代码/未复现。

### [Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models](https://arxiv.org/abs/2606.09401v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09401v1) §2–4 / §5 / §7：固定 pretrained checkpoint，仅对 adaptation 集执行 DP；分别测 full/LoRA/prefix/head、IID/overlap/OOD、不同 shadow/attacker knowledge。被保护邻接单位是 adaptation 数据，不是固定 pretraining 历史。
- **Evaluation / Boundary：** Pythia/GPT-Neo/OLMo 70M–1.4B 的公开参数/概率攻击，utility 与攻击接口、shadow 匹配一起改变实测 MIA。相同 ε不保证相同经验 attack rate；高攻击分不等 DP 数学失效。当前图表未完整核数字，不采用数值排名、closed API 外推或 unlearning 保证。
- **Books：** 整合：`PLATFORM-SECURITY`；adaptation DP邻接不追溯fixed pretraining；MIA与accountant分账。源→owner及实际两段/邻接写后已由 sep22_resume_v3 独立通过，整日日级Gate另验收。

### [Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs](https://arxiv.org/abs/2606.09411v1)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09411v1) §3–5 / Appendix F：将32bit secret 映射到固定 output embedding 的 token buckets，受限 teacher 生成 SFT 数据，输出 embedding 冻结；定期重拟合的 detached ridge probe 可被 evasion 训练绕开，同时以 bucket NLL/KL 保留 payload。recontextualization 冻结模板/改变话题以压低无关变化。
- **Evaluation / Boundary：** 五类开放8B/14B模型与短固定secret/白盒训练，不覆盖任意 detector/未知生产攻击。nuisance slack 是有假设的理论/代理，不是实测完整熵；Appendix F 明确代理 KL 不约束任意完整表示探测器。信息可恢复不等实践中有稳定通用检测器。
- **Books：** 整合：`PLATFORM-SECURITY`；受控recontext检验nuisance捷径；proxy KL非完整检测保证。源→owner及实际两段/邻接写后已由 sep22_resume_v3 独立通过，整日日级Gate另验收。

## 5. 缺口与下一步

普通可执行工作：恢复包中仍仅有章节定位的候选须补齐必要机制、评价、反证与真实owner对照，再完成非作者复核；这些项在§3标为待审阅，不是外部材料缺失或安全终态。74项归档复用也需完成当前呈现/映射复核，未变有效证据不重新全文审读。

已实际整合并经非作者写后通过的11项为 REFLECT、OmniMem、BUDDY、FuseFSS、Rosetta Memory、Causal Agent Replay、AliyunConsoleAgent、Decoy-Calibrated Audits、Adaptation Privacy、Steganographic Detection及SecureClaw。对应 owner 正文保留具体新机制、代价与反证，不把来源标记当正文。其余有限已有覆盖/仅报告判断及74项归档呈现复核仍普通待办，本日不宣称Evidence 112/112或整日闭环。

本窗已核中央争议：Training-Inference Kernel Contracts（2606.07581v1）§6.3 Eq17在c=0回到有偏式，而非强制policy equivalence；§8仅实验protocol。Entropy-Guided Adaptive Inference（2606.09508v1）Algorithm3的 `max(min(Bi,B0),3B0)` 在正B0下恒为3B0，entropy分类文字与对应密集/集中解释亦冲突。两项不用于正面证据、Books或保证，重开分别需要作者纠正clip/bias/per-token与trajectory范围，以及算法/分类与实现实验对应；不请求无关附件。它们的隔离不替代本日普通工作。

## 6. 复核

复核者：JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md；JUNE_09_SECOND_FULL_TABLE_AUDIT.md；INDEPENDENT_EXACT_V1_RECOVERY_20260914.md
结论：进行中；旧整体通过结论重开，逐项有效结果复用

两轮非作者full-table audit的1,235 = 112候选 + 1,123关闭及身份/准入证据仍保留。旧恢复包把章节标题当作Source Review、把主题相似当作已有覆盖，因此当前只恢复相关证据与Books判断，不推倒已核验来源和候选身份。sep21_resume_v3独立核REFLECT/OmniMem真实写后及KernelContracts中央冲突；sep22_resume_v3独立核其余九项实际Books及具体已有覆盖/中央争议小批。11实际写后通过不等于112全部通过；其余有限复核及整日日Gate仍未完成，格式校验不代替语义验收。

````
