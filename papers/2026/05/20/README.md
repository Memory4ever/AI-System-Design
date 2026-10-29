# Daily Research — 2026-05-20

**规范：** V3

**窗口：** 2026-05-19T09:00:00+08:00 ～ 2026-05-20T09:00:00+08:00

**补充窗口：** 2026-05-19 ～ 2026-05-19

**冻结候选日期：** [原报告](../_sources/daily-20260520/baseline-before-supplement-20261019.md)

**窗口说明：** 用户授权现有Daily只补遗漏；原小时窗、70条候选的整行/日期/评分与连续原§4保留，不按自然日搬移旧材料。本轮仅新增检查前一完整北京时间自然日。

**状态：** 完成

**Books：** 纳入本次

**检查时间：** 2026-10-20T21:41:20+08:00

本轮分批补查，检查时间不作为公开日期筛选条件。

用户明确恢复后的本日补查已通过独立R64整日验收；21项新增实际整合均通过非writer POST，有限来源已处理到下述明确边界。完成包含被明确隔离的历史coverage、日期与中心争议保留项，不授这些缺失证据通过或无遗漏。恢复及实际分层结果见[作者SUP](../_sources/daily-20260520/SUP_SOURCES_20261019.md)与[独立R64](../_sources/daily-20260520/SUP_REVIEW_20261019.md#r64--当前六部分实际day复核)。

2026-09-15旧审阅保留其70候选与36 Applied/34 No Change的历史范围，不替代本轮补查验收。当前新增30个确定May19事件家族：21项实际整合、4项具体已有覆盖、3项仅报告、2项中心争议隔离。三条原legacy只在§4恢复原事实/判断，不列补窗新候选；后到PopPy18697/Mosaic18710/RRFP18750已是[May19旧日报](../19/README.md)正式候选，R57直接复用，不迁日/重评或重复计数。过程依据集中于[唯一补查记录](../_sources/daily-20260520/SUP_SOURCES_20261019.md)，独立复核见[reader记录](../_sources/daily-20260520/SUP_REVIEW_20261019.md)。

## 1. 结论

本轮确定30个May19事件家族：21项实际Books整合经非writer POST通过、4项具体已有覆盖、3项仅报告，17232/16651两项中心争议隔离而未获正面Evidence/Books。主表为原70＋新增30＝100行；表外16399/16430两项公开日期争议不在此数。新增主线是表示/生成接口、拓扑与训练状态复用、条件reward/内部监测证据边界，以及重传层次改变后的窗口回收不变量；没有把高分、低检出或局部加速升级为生产保证。原70整行/旧小时窗与连续§4保持，另3项原legacy仅§4保May20/3+2+3=8，不重复列新候选。PopPy/Mosaic/RRFP直接去重。Qwen/MiMo当前入口与具名结果有效，但历史完整索引不可回放；这两coverage保留与两日期争议均不支撑“无遗漏”。有限联合日期核验只用exact-v1/适用历史公告发号规则及sameDOI arxiv.content/findable/registered上下界，不以created单证，也不证明全球首次或实验复现。下列575/577、70、Complete和旧Gate数字仅描述原小时窗口历史。

旧 V2.1 的 DataCite `created` 账本与 `Complete` 结论不再拥有当前状态。当前 owner 使用落在严格窗口内的 arXiv 官方 announcement batch：covered-category inventory 为 575。base receipt 的逐项状态先把 `closure`、`pre_denominator_closed` 与 `pre_denominator_closure` 三种旧拼法归一为 closure，再应用作者 14 个 FN override；fresh 非作者挑战又把 2605.18810、2605.18999、2605.19260、2605.19619 四项从二次 closure 恢复为候选，形成 `575 = 70 retained + 505 pre-denominator closure + 0 withdrawn`。13 个机构来源另有 Google AI 两个日期为 05-19 的原始事件，但二者均为 ROADMAP 明确排除的 AI for Science 应用，无论日内时刻位于截点哪侧都在候选分母前关闭。因此全日守恒为 `577 = 70 retained + 507 pre-denominator closure + 0 withdrawn`。

70 项候选均完成 exact-v1 深入审阅；其中 55 项仅在 identity/version/claim 不变时复用旧审阅，15 项由当前 V3 challenge 重新读取 exact-v1 的方法、评测、反证/限制与 artifact locator。不能复用旧 owner-day 算术或旧 Complete 状态。评分分布为 `8 score7 + 51 score8 + 11 score9`，即 `70 deep + 0 standard`；blocked=0，materials request=0。

Books 最终对账为 `70 = 27 prior Applied + 9 root Applied + 34 No Change + 0 Structural Candidate`。36 个正文 binding 均已存在，marker 唯一成对且位于目标章节首个 `## Review notes` 前；34 个 No Change 均有当前正文命题锚点。fresh 非作者逐段核验 9 个 root binding 的旧路径、约束变化、state/control owner、evidence boundary、trade-off、failure 与 fallback，其中 2605.19260 由 Ch23 已有 token-budget、position identity、temporal redundancy 与 full-token fallback 命题承载，不重复写入。Coverage、Evidence、Books 三个 Gate 全部通过。

## 2. 来源覆盖

下表只授May19补窗实际切片；旧“无候选”不授自然日覆盖。查询、分页、停止点与具体限制见[作者SUP](../_sources/daily-20260520/SUP_SOURCES_20261019.md)及[独立复核R62](../_sources/daily-20260520/SUP_REVIEW_20261019.md#r62--有限历史来源与两具名跨日归属的保留边界)。已完成有限可用入口恢复，不因参数错误冒称网络阻塞；Qwen/MiMo不可回放历史与arXiv两项跨日区间分别隔离，未授对应完整Coverage或零命中。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方Research/news与May19 provenance原事件；R30必要Source/R51具体已有覆盖，Jul31/Oct5后续更新不回填 | 已检查 | 仅已记录入口/事件切片，不授全站历史召回 |
| SRC-ANTHROPIC | 官方目录及May19 SLEIGHT Blog；R55定点比较exact-v1正文与v2/Blog，采用协议及正文相同，复用旧家族 | 已检查 | v1题摘24/40、23%与正文20/40、32%不一致；不解释为实验提升，不采用数字历史保证 |
| SRC-GOOGLE-AI | Research May4附近切片及I/O具名3.5、ManagedAgents、Omni、TPU；R25/46/51/52。Science范围前关闭，TPU Apr22旧事件，Jan安全链接有限消费 | 已检查 | 产品demo不授未披露机制；不把旧事件、Jan安全家族或后续版本重复计入 |
| SRC-META-AI | 官方具名GIM、EgoBaby、RL-RCHAT；R52核后者May1旧原页；EgoBaby19130实际May20归May21，不迁入本补窗 | 已检查 | 仅上述已恢复具名切片，不授全目录历史召回 |
| SRC-QWEN | 旧域迁站、新blog静态shell与精确May19主域fallback；恢复LiveTranslate完整官方core/日期，R60标准Only；Qwen3.7主源May20不迁日 | 受阻 | 当前具名检查已完；被删除/未索引的历史完整索引不可回放，不支持整体零命中或无遗漏，具名官方May19索引/文章到达再开 |
| SRC-DEEPSEEK | 官方updates实际相邻Jul31→Apr24，原件SUP_DEEPSEEK_UPDATES；本切片无May19新系统事件 | 已检查 | 有界相邻目录，不声称全部历史内容 |
| SRC-MOONSHOT | 新Kimi官方Blog实际相邻Jul16→Apr20，SUP_KIMI_NEW；官方GitHub不以pushed_at充首次公开 | 已检查 | 有界目录切片，不声称全站无遗漏 |
| SRC-TENCENT-HUNYUAN | 官方公开列表11项中文切片，Apr30→May21；补窗内未见同类新事件 | 已检查 | 不扩成英文目录或全历史覆盖 |
| SRC-ZAI | 官方Research实际May20→Apr29相邻切片；ZCube May20留原真实归属，不迁入May19 | 已检查 | 仅所记录目录范围 |
| SRC-BYTEDANCE-SEED | R42实际首18/offset18分页重叠1617/1615与May15 Charon1655，May26→May15切片有效；Lance具名Blog/论文R56 Source/date、R59实际整合通过 | 已检查 | publication切片不代替全Blog历史；只复用具名Lance，不重扫246条或授全站召回 |
| SRC-BAIDU-ERNIE | 官方技术博客首May9，下一页至Apr30停止；未见May19新系统事件 | 已检查 | 所记录页面切片，不外推全站 |
| SRC-XIAOMI-MIMO | 官方8论文；servedJS的17个/blog路由补首页More缺项，ASR/Pro iframe原页及具名frontmatter定点日期已恢复，R62未见新增May19 | 受阻 | 当前8paper/17路由有限核验已完，但不可回放被删除/未索引历史；不授整个历史零命中，具名May19官方原件到达再开 |
| SRC-MINIMAX | 官方当前12篇完整相邻Mar18→May26/27目录切片；补窗内未见新系统事件 | 已检查 | 仅本次实际目录范围 |
| SRC-ARXIV | 六主题220/同义279均仅第一页发现；CL skip900/show100标题有界补检。575非队列；具名四系统三旧项R57去重、EPIC R63实际整合。16399/16430另经合法月表/all分页及具名日门恢复 | 受阻 | 两项v1最早界到registered仍跨日，月表不带首次公告日、参数错误不证明外部故障；无精确日批次前不列确定候选/不记零命中，不授全学科召回 |

完整机构来源边界见 [`non-arxiv-source-coverage-v3.json`](../_sources/daily-20260520/non-arxiv-source-coverage-v3.json)，官方批次投影与可复用取得方法见 [`official-owner-batch-evidence-v3.json`](../_sources/daily-20260520/official-owner-batch-evidence-v3.json)，逐 identity 筛选投影见 [`screening-outcomes-v3.json`](../_sources/daily-20260520/screening-outcomes-v3.json)。`已检查` 只证明注册入口的有界检查，不声称整个互联网绝无遗漏。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2605.18755 Operational Memory Architecture for Kubernetes](https://arxiv.org/html/2605.18755v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-LOGGING；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-LOGGING [章节](../../../../books/part-06-ai-infrastructure/68-logging.md) |
| [2605.18762 ALDEN](https://arxiv.org/html/2605.18762v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+2+2=7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.18792 Trust or Abstain? A Self-Aware RAG Approach](https://arxiv.org/html/2605.18792v1) | 2026-05-20T08:00:00+08:00 | 由 FN closure 恢复；AGENT-RAG；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [2605.18796 UCCI](https://arxiv.org/html/2605.18796v1) | 2026-05-20T08:00:00+08:00 | 由 FN closure 恢复；INFER-SCHEDULING；3+3+3=9 | 深入完成 | 已有覆盖：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [2605.18810 D-PACE](https://arxiv.org/html/2605.18810v1) | 2026-05-20T08:00:00+08:00 | fresh 非作者 FN challenge 恢复；INFER-SPECULATIVE-DECODING；3+2+3=8 | 深入完成 | 整合：root 已写回并通过 fresh 语义复核；INFER-SPECULATIVE-DECODING [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [2605.18812 PASC](https://arxiv.org/html/2605.18812v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.18813 Composition of Memory Experts for Diffusion World Models](https://arxiv.org/html/2605.18813v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；MULTIMODAL-WORLD-MODELS；3+3+3=9 | 深入完成 | 整合：root 已写回并通过 fresh 非作者复核；MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.18814 Trajectory-Based Data Attribution](https://arxiv.org/html/2605.18814v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-DATA；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.18815 DynaTrain](https://arxiv.org/html/2605.18815v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-DISTRIBUTED-TRAINING；3+3+3=9 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2605.18822 Hybrid-LoRA](https://arxiv.org/html/2605.18822v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；TRAIN-SFT；3+2+3=8 | 深入完成 | 已有覆盖：TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [2605.18824 Fine-Grained Benchmark Generation](https://arxiv.org/html/2605.18824v1) | 2026-05-20T08:00:00+08:00 | 由 FN closure 恢复；PLATFORM-EVALUATION-SYSTEM；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.18825 Semantic-Aware Prefix-Cache Eviction](https://arxiv.org/html/2605.18825v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-KV-CACHE；3+2+3=8 | 深入完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.18841 Adaptive Runtime Safety Control](https://arxiv.org/html/2605.18841v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；PLATFORM-SECURITY；3+3+2=8 | 深入完成 | 整合：root 已写回并通过 fresh 非作者复核；PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.18853 INAR-VL](https://arxiv.org/html/2605.18853v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-SCHEDULING；3+2+3=8 | 深入完成 | 已有覆盖：INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [2605.18854 Memory Condensation for Coding Agents](https://arxiv.org/html/2605.18854v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-MEMORY；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [2605.18857 The 99% Success Paradox](https://arxiv.org/html/2605.18857v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；AGENT-TOOL-CALLING；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.18882 To Call or Not to Call](https://arxiv.org/html/2605.18882v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；AGENT-TOOL-CALLING；3+2+3=8 | 深入完成 | 整合：root 已写回并通过 fresh 非作者复核；AGENT-TOOL-CALLING [章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [2605.18891 Reasoning-Trace Memorization Audit](https://arxiv.org/html/2605.18891v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-DATA；3+3+3=9 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.18918 ESLD](https://arxiv.org/html/2605.18918v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.18930 OEP Memory Poisoning](https://arxiv.org/html/2605.18930v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-MEMORY；3+3+3=9 | 深入完成 | 已有覆盖：AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [2605.18999 Distance-Aware Muon](https://arxiv.org/html/2605.18999v1) | 2026-05-20T08:00:00+08:00 | fresh 非作者 FN challenge 恢复；TRAIN-PRETRAINING；3+2+3=8 | 深入完成 | 整合：root 已写回并通过 fresh 语义复核；TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.19008 Learn-by-Wire Training Control](https://arxiv.org/html/2605.19008v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-PRETRAINING；3+3+2=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.19049 KVBuffer](https://arxiv.org/html/2605.19049v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-KV-CACHE；3+3+3=9 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.19095 ScheduleFree+](https://arxiv.org/html/2605.19095v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；TRAIN-PRETRAINING；3+3+2=8 | 深入完成 | 整合：root 已写回并通过 fresh 非作者复核；TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.19099 DecisionBench](https://arxiv.org/html/2605.19099v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-MULTI-AGENT；3+2+2=7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.19101 Heterogeneity-Aware Dataset Scheduling](https://arxiv.org/html/2605.19101v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-DATA；3+3+2=8 | 深入完成 | 已有覆盖：TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.19127 POLAR-Bench](https://arxiv.org/html/2605.19127v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19140 Learning to Hand Off](https://arxiv.org/html/2605.19140v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-WORKFLOW；3+3+2=8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [2605.19151 Progressive Autonomy](https://arxiv.org/html/2605.19151v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19169 Geo-Distributed Training Fiber Latency](https://arxiv.org/html/2605.19169v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-DISTRIBUTED-TRAINING；3+2+2=7 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [章节](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2605.19193 Sequential Consensus](https://arxiv.org/html/2605.19193v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-MULTI-AGENT；3+2+3=8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT [章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [2605.19196 Time to REFLECT](https://arxiv.org/html/2605.19196v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；3+3+3=9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.19218 Rotation-Aligned KV Pruning](https://arxiv.org/html/2605.19218v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-KV-CACHE；3+2+2=7 | 深入完成 | 已有覆盖：INFER-KV-CACHE [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [2605.19220 Position: Uncertainty Quantification in LLMs is Just Unsupervised Clustering](https://arxiv.org/html/2605.19220v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；PLATFORM-EVALUATION-SYSTEM；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.19240 CASPIAN](https://arxiv.org/html/2605.19240v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19242 PhyWorld](https://arxiv.org/html/2605.19242v1) | 2026-05-20T08:00:00+08:00 | exact-v1；MULTIMODAL-WORLD-MODELS；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.19250 Causal Evidence for Attention Head Imbalance in Modality Conflict Hallucination](https://arxiv.org/html/2605.19250v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；MULTIMODAL-REPRESENTATION；3+2+3=8 | 深入完成 | 整合：root 已写回并通过 fresh 非作者复核；MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.19260 AQuaUI](https://arxiv.org/html/2605.19260v1) | 2026-05-20T08:00:00+08:00 | fresh 非作者 FN challenge 恢复；MULTIMODAL-REPRESENTATION；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.19282 Rethinking Muon Beyond Pretraining](https://arxiv.org/html/2605.19282v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-PRETRAINING；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.19314 ContextFlow](https://arxiv.org/html/2605.19314v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-WORKFLOW；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；AGENT-WORKFLOW [章节](../../../../books/part-07-agent/81-workflow.md) |
| [2605.19317 Inference-Time Scaling in Diffusion Models through Iterative Partial Refinement](https://arxiv.org/html/2605.19317v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；MULTIMODAL-GENERATIVE-PARADIGMS；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS [章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [2605.19319 SWEET](https://arxiv.org/html/2605.19319v1) | 2026-05-20T08:00:00+08:00 | exact-v1；MULTIMODAL-WORLD-MODELS；3+3+2=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；MULTIMODAL-WORLD-MODELS [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [2605.19321 Pre-Model Safeguard with Draft Models](https://arxiv.org/html/2605.19321v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；2+2+3=7 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19322 DynaTok](https://arxiv.org/html/2605.19322v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；MULTIMODAL-REPRESENTATION；3+2+3=8 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2605.19328 RoboJailBench](https://arxiv.org/html/2605.19328v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.19335 Scheduling ANNS with I/O Stalls](https://arxiv.org/html/2605.19335v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-RAG；3+3+2=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [2605.19341 HalluWorld](https://arxiv.org/html/2605.19341v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.19373 CRDT Model Merging](https://arxiv.org/html/2605.19373v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-MODEL-REGISTRY；3+3+3=9 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-MODEL-REGISTRY [章节](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [2605.19407 A Bitter Lesson for Data Filtering](https://arxiv.org/html/2605.19407v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-DATA；3+3+3=9 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-DATA [章节](../../../../books/part-04-training-system/27-data.md) |
| [2605.19447 Selective Hindsight Distillation](https://arxiv.org/html/2605.19447v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-RLHF；3+3+2=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.19461 Distribution Matching for Diverse Reasoning](https://arxiv.org/html/2605.19461v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-RLHF；3+3+3=9 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.19478 Functional Fusion Backdoor](https://arxiv.org/html/2605.19478v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+3+2=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19481 C2CServe](https://arxiv.org/html/2605.19481v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-PD-DISAGGREGATION；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；INFER-PD-DISAGGREGATION [章节](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [2605.19577 GoLongRL](https://arxiv.org/html/2605.19577v1) | 2026-05-20T08:00:00+08:00 | FN challenge 恢复；TRAIN-GRPO；3+3+2=8 | 深入完成 | 整合：root 已写回并通过 fresh 非作者复核；TRAIN-GRPO [章节](../../../../books/part-04-training-system/33-grpo.md) |
| [2605.19604 Formal Skill](https://arxiv.org/html/2605.19604v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-PLATFORM；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；AGENT-PLATFORM [章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [2605.19619 MiMuon](https://arxiv.org/html/2605.19619v1) | 2026-05-20T08:00:00+08:00 | fresh 非作者 FN challenge 恢复；TRAIN-PRETRAINING；3+2+3=8 | 深入完成 | 整合：root 已写回并通过 fresh 语义复核；TRAIN-PRETRAINING [章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [2605.19722 Autonomous Security-Agent Evaluation](https://arxiv.org/html/2605.19722v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19755 Operationalising AIBOMs](https://arxiv.org/html/2605.19755v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+3+2=8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.19769 OpenComputer](https://arxiv.org/html/2605.19769v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；3+2+3=8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.19779 Distribution-Free UQ for Agent Evaluation](https://arxiv.org/html/2605.19779v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.19932 PEEK Context Map](https://arxiv.org/html/2605.19932v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-CONTEXT；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；AGENT-CONTEXT [章节](../../../../books/part-07-agent/75-context.md) |
| [2605.19945 GEM Expert Mapping](https://arxiv.org/html/2605.19945v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-SCHEDULING；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；INFER-SCHEDULING [章节](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [2605.19952 Beyond Atomic Facts in Agent Memory](https://arxiv.org/html/2605.19952v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-MEMORY；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；AGENT-MEMORY [章节](../../../../books/part-07-agent/77-memory.md) |
| [2605.19999 Contamination-Resistant Benchmarks](https://arxiv.org/html/2605.19999v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-EVALUATION-SYSTEM；2+2+3=7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2605.20005 Loss-Adaptive Fine-Tuning](https://arxiv.org/html/2605.20005v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-SFT；3+3+3=9 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-SFT [章节](../../../../books/part-04-training-system/29-sft.md) |
| [2605.20022 FlexDraft](https://arxiv.org/html/2605.20022v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-SPECULATIVE-DECODING；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；INFER-SPECULATIVE-DECODING [章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [2605.20051 Vulnerability Variant Hunting](https://arxiv.org/html/2605.20051v1) | 2026-05-20T08:00:00+08:00 | exact-v1；PLATFORM-SECURITY；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；PLATFORM-SECURITY [章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2605.20061 Consistency-Guided Credit Assignment](https://arxiv.org/html/2605.20061v1) | 2026-05-20T08:00:00+08:00 | exact-v1；TRAIN-RLHF；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；TRAIN-RLHF [章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [2605.20084 BalanceRAG](https://arxiv.org/html/2605.20084v1) | 2026-05-20T08:00:00+08:00 | exact-v1；AGENT-RAG；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；AGENT-RAG [章节](../../../../books/part-07-agent/76-rag.md) |
| [2605.20179 TIDE](https://arxiv.org/html/2605.20179v1) | 2026-05-20T08:00:00+08:00 | exact-v1；INFER-TENSORRT-LLM；3+2+3=8 | 深入完成 | 整合：正文已存在并通过 fresh 非作者复核；INFER-TENSORRT-LLM [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [2605.17938 Training data attribution in diffusion models via mirrored unlearning and noise-consistent skew](https://arxiv.org/html/2605.17938v1) | 2026-05-19 | 受限镜像unlearning与共享噪声配对归因；2+2+3=7 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；reader R11实际POST通过 |
| [2605.17759 FrequencyBooster](https://arxiv.org/html/2605.17759v1) | 2026-05-19 | 同patch宽global decoder分责低/高频；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R11实际POST通过 |
| [2605.18597 Latent Action Reparameterization for Efficient Agent Inference](https://arxiv.org/html/2605.18597v1) | 2026-05-19 | 轨迹词表压缩与entropy surrogate的语义边界；2+2+2=6 | 深入完成 | 整合：MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md)；R11实际POST通过 |
| [2605.18530 Continuous Diffusion Scales Competitively with Discrete Diffusion for Language](https://arxiv.org/html/2605.18530v1) | 2026-05-19 | 排除架构/精度混杂的likelihood扩容比较；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R11实际POST通过 |
| [2605.17232 Vocabulary-size-independent Convergence of Discrete Diffusion Models](https://arxiv.org/html/2605.17232v1) | 2026-05-19 | singular-prior下adjoint/IPM误差及假设边界；2+1+3=6 | 争议 | 暂缓：masked额外相对score条件与IPM常数和中心普适主张冲突，不进入Books |
| [2605.18736 Spectral Progressive Diffusion for Efficient Image and Video Generation](https://arxiv.org/html/2605.18736v1) | 2026-05-19 | 谱padding加state/timestep重标的渐进空间网格；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R14实际POST通过 |
| [2605.16551 PQR: A Framework to Generate Diverse and Realistic User Queries that Elicit QA Agent Failures](https://arxiv.org/html/2605.16551v1) | 2026-05-19 | 现实意图约束的query/prompt双层failure搜索；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；R21实际POST通过 |
| [2605.18599 Resolving Representation Ambiguity in Feedforward Novel View Synthesis Transformer via Semantic-Spatial Decoupling](https://arxiv.org/html/2605.18599v1) | 2026-05-19 | 共享QK路由但分开semantic/spatial value更新；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；R29实际POST通过 |
| [2605.16918 HighSync: High-Quality Lip Synchronization via Latent Diffusion Models](https://arxiv.org/html/2605.16918v1) | 2026-05-19 | crop/temporal/mask序列化的条件shortcut反证；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R29实际POST通过 |
| [2605.16861 Prefix-Adaptive Block Diffusion for Efficient Document Recognition](https://arxiv.org/html/2605.16861v1) | 2026-05-19 | candidate range与commit解耦、CSL前沿和clean KV物化；2+2+3=7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；R21实际POST通过 |
| [2605.16871 SADP: Subgoal-Aware Diffusion Policy for Explainable Robots Learned from Foundation Model Generated Demonstrations](https://arxiv.org/html/2605.16871v1) | 2026-05-19 | subgoal同时监督action与ongoing head、可解释性边界；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；R29实际POST通过 |
| [2605.17535 AgentModernize: Preserving Business Logic in Legacy Modernization with Multi-Agent LLMs and Behavioral Specification Graphs](https://arxiv.org/html/2605.17535v1) | 2026-05-19 | inspectable IR与独立behavior/feedback回退分责；2+2+3=7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) problem compilation/heldout/可信revision；R22，保v2直接反证 |
| [2605.17393 Heterogeneous Information-Bottleneck Coordination Graphs for Multi-Agent Reinforcement Learning](https://arxiv.org/html/2605.17393v1) | 2026-05-19 | group-aware neural graph prior与feature瓶颈联合约束；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；R33实际POST通过，不采中心普适理论保证 |
| [2605.17361 MasFACT: Continual Multi-Agent Topology Learning via Geometry-Aware Posterior Transfer](https://arxiv.org/html/2605.17361v1) | 2026-05-19 | FGW对齐历史topology prior及受限posterior保留；2+2+3=7 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；R33实际POST通过 |
| [2605.17482 Residual Semantic Decomposition of Word Embeddings](https://arxiv.org/html/2605.17482v1) | 2026-05-19 | GloVe关系重建诊断的assignment entropy非sense语义；1+1+2=4 | 已关闭 | 仅报告：6人工pair/有限seed的局部诊断，不改变长期sense发现机制 |
| [2605.16651 Right Predictions, Misleading Explanations: On the Vulnerability of Vision-Language Model Explanations](https://arxiv.org/html/2605.16651v1) | 2026-05-19 | 稳定prediction仍有heatmap drift的攻击主张与内部反证；2+1+3=6 | 争议 | 暂缓：Eq5/Alg1及Table3直接冲突，R26隔离，不进入Books |
| [2605.17314 Weak-to-Strong Elicitation via Mismatched Wrong Drafts](https://arxiv.org/html/2605.17314v1) | 2026-05-19 | 外部错draft只改prompt条件、rollout与gradient仍on-policy；2+2+3=7 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；R41实际POST通过 |
| [2605.17342 Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment](https://arxiv.org/html/2605.17342v1) | 2026-05-19 | scalar与antisymmetric分支共同拟合及动态权重消费；2+1+3=6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；R48实际POST通过 |
| [2605.17359 Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains](https://arxiv.org/html/2605.17359v1) | 2026-05-19 | 离线query-conditioned prior初始化原topology refiner；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；R47实际POST通过 |
| [2605.18226 Context Memorization for Efficient Long Context Generation](https://arxiv.org/html/2605.18226v1) | 2026-05-19 | query索引的attention-state字典及exact merge/聚类近似分界；2+2+3=7 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；R41实际POST通过 |
| [2605.18253 Machine Unlearning for Masked Diffusion Language Models](https://arxiv.org/html/2605.18253v1) | 2026-05-19 | same-state prompt-masked frozen anchor的conditional KL目标；2+2+3=7 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)；R47实际POST通过 |
| [2605.17978 AutoVecCoder: Teaching LLMs to Generate Explicitly Vectorized Code](https://arxiv.org/html/2605.17978v1) | 2026-05-19 | 正确资格内有界相对latency reward的局部组合控制；2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)；R39具体NC、R46日期通过 |
| [2605.17187 PluRule: A Benchmark for Moderating Pluralistic Communities on Social Media](https://arxiv.org/html/2605.17187v1) | 2026-05-19 | paired submission/context下local-rule评价的弱标签边界；1+1+2=4 | 已关闭 | 仅报告：局部弱反证不改变独立policy/事实验收机制；R34/R46 |
| [2605.18549 Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/html/2605.18549v1) | 2026-05-19 | 多层MIL/cummax轨迹与独立readout校准；2+2+3=7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；R54实际POST通过 |
| [2605.18646 Language-Switching Triggers Take a Latent Detour Through Language Models](https://arxiv.org/html/2605.18646v1) | 2026-05-19 | probe阴性、语义轴稳定性、corruption干预与utility分责；2+2+3=7 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；R54实际POST通过 |
| [Advancing content provenance](https://openai.com/index/advancing-content-provenance/) | 2026-05-19 | C2PA metadata/SynthID互补与negative verifier语义；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；R51具体NC |
| [Introducing Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/) | 2026-05-19 | remote environment续接及file-defined agent配置接口；2+2+2=6 | 深入完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；R51具体NC |
| [2605.18678 Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://arxiv.org/html/2605.18678v1) | 2026-05-19 | semantic/clean/noisy三token group的temporal-position offset接口；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)单段R59实际POST通过 |
| [2605.18683 EPIC: Abstraction and Polymorphism of In-Network Collectives on Ethernet](https://arxiv.org/html/2605.18683v1) | 2026-05-19 | 重传责任变化后的PSN窗口/回收不变量；2+2+3=7 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)单段R63实际POST通过 |
| [Qwen3.5-LiveTranslate: From Sound to Sight, From Word to Right](https://qwen.ai/blog?id=qwen3.5-livetranslate) | 2026-05-19 | chunk输入与ReadableUnit tags控制合成粒度；2+1+2=5 | 标准完成 | 仅报告：官方极简接口未披tag规则/监督与完整预算/时延评价条件，不足新增长期机制；R60 |

## 4. 证据与知识整合

70 个候选逐项 exact-v1 清单、canonical/legacy marker alias、评分与 Stable Node 见 [`evidence-review-v3.json`](../_sources/daily-20260520/evidence-review-v3.json)。55 项可读的 Method、Evaluation、Counterevidence/Limitations、Artifact 与 adopted claim 保留在下方 legacy evidence appendix 的 Source Reviews 中；复用只因 identity、版本与命题未变，不沿用旧完成结论。15 个 FN 恢复项的当前可读审阅在本节，完整结构化 locator 同步写入 V3 artifact。

当前 Books 对读见 [`books-comparison-v3.json`](../_sources/daily-20260520/books-comparison-v3.json)：27 个 prior Applied 与 9 个 root Applied 均已通过 target file、正文 heading、marker、首个 Review-notes line、相邻衔接和语义完整性检查；34 个 No Change 逐项给出当前正文命题。root 写回队列、exact-v1 locator 与 fresh post-write 结果见 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260520/root-books-writeback-queue-v3.json)。

### [2605.18755 Operational Memory Architecture for Kubernetes](https://arxiv.org/html/2605.18755v1)
对应 exact-v1 deep review 由 `review:SF-2026-ARXIV-2605-18755` 与 `evidence-review-v3.json` 共同定位；只复用版本和命题不变的证据正文。

### [2605.18762 ALDEN](https://arxiv.org/html/2605.18762v1)
对应 exact-v1 deep review 由 `review:SF-2026-ARXIV-2605-18762` 与 V3 artifact 共同定位。

### [2605.18792 Trust or Abstain? A Self-Aware RAG Approach](https://arxiv.org/html/2605.18792v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位；adopted claim 只覆盖 belief estimator 到 trust/retrieve/abstain decision 的控制边界。

### [2605.18796 UCCI](https://arxiv.org/html/2605.18796v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位；adopted claim 只覆盖 calibrated error probability 与 constrained cost threshold。

### [2605.18810 D-PACE](https://arxiv.org/html/2605.18810v1)
问题与机制：固定 head/block-position weight 在 bottleneck 稳定时简单且可重放；parallel block drafter 的早位变准后，限制 accepted prefix 的位置会迁移。exact-v1 §3.1–3.3 用 expected accepted-length surrogate 的 prefix-survival 与 continuation contribution 动态分配 CE credit，并以 asymmetric smoothing 避免后位权重消失；target verifier 仍独占 accept/commit，architecture 与 inference procedure 不变。§4、§5.1–5.6 只支持所列 DFlash、Qwen/Llama targets、六个 benchmark、T=0/1 与 H200/L40S 配置；2.3% training overhead、speedup 与 emitted-length 不能外推到 tree drafter 或 production SLO。surrogate 相关性下降、低置信度不稳、target/temperature 漂移或成本超界时，回退 fixed decayed CE、普通 Forward-KL/CE 或重新标定。

### [2605.18812 PASC](https://arxiv.org/html/2605.18812v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18813 Composition of Memory Experts for Diffusion World Models](https://arxiv.org/html/2605.18813v1)
问题与机制：单一 Transformer memory 保留局部细节却承担二次注意力成本，recurrent/SSM 则会压缩丢失历史；exact-v1 §3.2–3.3 把 short-term、weight-adapted episodic long-term 与 spatial long-term memory 拆给不同 diffusion experts，再以 contrastive product-of-experts 在 sampling 时组合。§4 与 Appendix D 在多个 simulated/real-world dataset 上评估 temporal consistency、recall 与 navigation。限制与回退：§3.2 trade-off 与 §G 表明 contrast 会压低有效 secondary modes，test-time LoRA 还产生 revision/遗忘与成本；专家不一致、freshness 不可证或预算不足时回退有界 history bank 或单一 world-model path。Artifact 为论文 project page，event-time commit 未披露。长期命题不把权重 memory 当作事实存储。

### [2605.18814 Trajectory-Based Data Attribution](https://arxiv.org/html/2605.18814v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18815 DynaTrain](https://arxiv.org/html/2605.18815v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18822 Hybrid-LoRA](https://arxiv.org/html/2605.18822v1)
问题与机制：full fine-tuning 自由度高但状态/显存成本大，纯 LoRA 限制 trainable subspace；exact-v1 §3.1–3.4 用固定参数预算和 gradient/parameter-based Hybrid-Score 把少数 LoRA 不适配模块交给 FFT，其余交给 LoRA。§4 的模型、reasoning tasks 与 matched baselines 支持作者报告结果；§5 明确仅到 7B，且 two-stage probing 仍增加分配成本。长期命题已由 TRAIN-SFT 的 parameter-mask/trainable-subspace artifact 覆盖；budget、base revision 或 probe 失真时回退纯 LoRA、单轴选择或 full SFT。

### [2605.18824 Fine-Grained Benchmark Generation](https://arxiv.org/html/2605.18824v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位；benchmark 结论绑定 reference、solution graph 与 validation artifact。

### [2605.18825 Semantic-Aware Prefix-Cache Eviction](https://arxiv.org/html/2605.18825v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18841 Adaptive Runtime Safety Control](https://arxiv.org/html/2605.18841v1)
问题与机制：CMDP cumulative budget 不能阻止单次危险动作，fixed shield 又会在 nonstationarity 下过严或过松；exact-v1 §3–§4.1 从 remaining budget、horizon 与 context 投影 per-state admissibility threshold，policy 只提议 action，shield 执行或切换 fallback。§6 在 highway-env 四环境评估；§5.1/§7 限制 theoretical guarantee 与 safety-cost proxy，不证明真实驾驶安全。sensor/predictor 漂移时回退保守 fixed threshold、预定义 safe controller 或人工接管；reproducibility package 有声明但 event-time commit 未披露。

### [2605.18853 INAR-VL](https://arxiv.org/html/2605.18853v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18854 Memory Condensation for Coding Agents](https://arxiv.org/html/2605.18854v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18857 The 99% Success Paradox](https://arxiv.org/html/2605.18857v1)
问题与机制：top-K coverage 接近 100% 仍可能只等于随机选择；exact-v1 §4 以 hypergeometric baseline 计算 BoR，§5–§7 检查 retrieval 与 tool-selection collapse。该 measure 只校正 selectivity，不证明候选正确、工具安全或 downstream answer 正确；小 catalog、success rule 或 relevant-count 分布变化需重新校准。当前 AGENT-TOOL-CALLING 已明确拥有“exposure reward 扣随机候选集优势”，因此 No Change。

### [2605.18882 To Call or Not to Call](https://arxiv.org/html/2605.18882v1)
问题与机制：合法调用率无法区分是否存在 intrinsic over-calling；exact-v1 §3–§5 把 SAE feature margin 与 activation-independent call offset 分开，并用 AMCS 做 causal steering。§5.2 在六模型上验证，§6 限定 When2Call、SAE basis 与局部线性近似，不解释训练来源或长程 agent。calling-effort 只能是 proposal sensor，执行仍由外部 policy；漂移或必要调用受损时回退显式 necessity rule、ask-user/abstain 和 effect-time authorization。代码仓库有声明，event-time commit 未披露。

### [2605.18891 Reasoning-Trace Memorization Audit](https://arxiv.org/html/2605.18891v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18918 ESLD](https://arxiv.org/html/2605.18918v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18930 OEP Memory Poisoning](https://arxiv.org/html/2605.18930v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.18999 Distance-Aware Muon](https://arxiv.org/html/2605.18999v1)
问题与机制：normalized optimizer 的 direction 与 step scale 是独立控制；固定 scale 在几何和轨迹半径稳定时仍是合理基线。exact-v1 §3–§5 分别用 explored trajectory、local descent certificate 与 recentered majorized scalar search 决定 step radius，要求 optimizer owner 把 certificate、momentum、参数块和 checkpoint transition 一起版本化。§2 assumption map 将 DA/SC/DF-Muon 分别约束于 bounded trajectory、star-convex/bounded sublevel set 与 majorized search；§6 只覆盖 GPT-124M/WikiText-103、ViT-Tiny/CIFAR-100 及附录小型配置，不证明大规模分布式 wall-clock 优势。certificate 失真、轨迹爆炸、假设不成立或搜索成本过高时，回退 tuned fixed-scale Muon、clipped trust radius 或 AdamW。

### [2605.19008 Learn-by-Wire Training Control](https://arxiv.org/html/2605.19008v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19049 KVBuffer](https://arxiv.org/html/2605.19049v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19095 ScheduleFree+](https://arxiv.org/html/2605.19095v1)
问题与机制：传统 WSD/cosine 需要预知 horizon；exact-v1 §2–§8 把 schedule-free interpolation/averaging 与 large-batch gradient-norm drift、weight decay、adaptive step 共同处理，§12 解释 model averaging/merging。§9–§11 的比较只支持披露模型、token-per-parameter 与配置，31% headline 不可外推。它以 averaged-iterate state 和更复杂 weighting 换 anytime training；短 run、scale 超界或终点明确时回退 tuned WSD/cosine 与显式 tail averaging。Artifact commit 未披露。

### [2605.19099 DecisionBench](https://arxiv.org/html/2605.19099v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19101 Heterogeneity-Aware Dataset Scheduling](https://arxiv.org/html/2605.19101v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19127 POLAR-Bench](https://arxiv.org/html/2605.19127v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19140 Learning to Hand Off](https://arxiv.org/html/2605.19140v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19151 Progressive Autonomy](https://arxiv.org/html/2605.19151v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19169 Geo-Distributed Training Fiber Latency](https://arxiv.org/html/2605.19169v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19193 Sequential Consensus](https://arxiv.org/html/2605.19193v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19196 Time to REFLECT](https://arxiv.org/html/2605.19196v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19218 Rotation-Aligned KV Pruning](https://arxiv.org/html/2605.19218v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19220 Position: Uncertainty Quantification in LLMs is Just Unsupervised Clustering](https://arxiv.org/html/2605.19220v1)
问题与机制：exact-v1 §2–§4 论证 semantic entropy、graph 与 verbal-belief UQ 主要测 generation consistency，而非外部 correctness；稳定但错误的答案会形成 confident hallucination。§5 提议 tail-risk、sensitivity curve、conformal/native uncertainty 与 objective truth grounding，但这是一篇 position paper，不提供 production confidence authority。当前 PLATFORM-EVALUATION-SYSTEM 已明确 internal probe 是 model-specific sensor、外部 evidence/verifier 才拥有 truth，故 No Change；标签或 calibration drift 时回退 external verification、abstain 或人工复核。

### [2605.19240 CASPIAN](https://arxiv.org/html/2605.19240v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19242 PhyWorld](https://arxiv.org/html/2605.19242v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19250 Causal Evidence for Attention Head Imbalance in Modality Conflict Hallucination](https://arxiv.org/html/2605.19250v1)
问题与机制：只看输出 hallucination rate 不能定位 text-over-vision 的 causal owner；exact-v1 §3 用 path patching 区分分布式 driving heads 与少量 resisting heads，§4 让 conflict probe 触发 conditional suppression。§4.2 与 Appendix 0.A 支持五个开源 MLLM、MMMC 与 SCI-SemanticConflict；§5 明确 labeled probe、prefill/object-conflict 与 visual-as-truth 限制。head identity 漂移、视觉不可信或干预伤害 task state 时回退原始 multimodal path、外部 evidence check 或 abstain。Artifact 未披露。

### [2605.19260 AQuaUI](https://arxiv.org/html/2605.19260v1)
问题与机制：GUI screenshot 的信息密度高度不均；exact-v1 §3.2 用 adaptive quadtree 对 homogeneous region 合并 visual token、保留代表 token 的位置身份，§3.3 用前一 screenshot 的 quadtree 区分 static/shifted/replaced region。§4–§5 的 grounding/navigation 结果只支持作者列出的 GUI models、benchmarks 与 serving path；Qwen2 路径上 reduction overhead 会抵消 latency，2B models 也几乎无收益，不能把 13.22%/29.52% headline 外推。当前 Ch23 已拥有分层 token-budget、position identity、temporal redundancy、selector drift 与 full-token fallback 的更一般命题，因此 Books No Change；变化检测或布局假设失效、overhead 超界、证据完整性优先时回退独立截图或完整 tokens。

### [2605.19282 Rethinking Muon Beyond Pretraining](https://arxiv.org/html/2605.19282v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19314 ContextFlow](https://arxiv.org/html/2605.19314v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19317 Inference-Time Scaling in Diffusion Models through Iterative Partial Refinement](https://arxiv.org/html/2605.19317v1)
问题与机制：one-pass sequential diffusion 会让早期区域决定不可修正；exact-v1 §3 反复 re-noise 子区域并以其余区域为 context 再生，无外部 verifier。§4 只在 Sudoku/shape/pixel constraint tasks 评估；§6 披露约 13× compute、resampling-ratio 敏感与随机 region selection。当前 MULTIMODAL-GENERATIVE-PARADIGMS 已拥有 mutable correction、runtime commit 与重开 provisional region 的命题，故 No Change；延迟超限或 context 被过多丢弃时回退 one-pass/更小 refinement budget。

### [2605.19319 SWEET](https://arxiv.org/html/2605.19319v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19321 Pre-Model Safeguard with Draft Models](https://arxiv.org/html/2605.19321v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19322 DynaTok](https://arxiv.org/html/2605.19322v1)
问题与机制：attention-only compression 忽略 positional bias 与长期 temporal redundancy；exact-v1 §3.2–3.3 用 EMA memory 先分 temporal budget，再以 spatial memory 分配区域 token。§4 覆盖两类 Video-LLM 与四个 VideoQA benchmark；未证明 streaming scene-cut、任意 encoder 或生产 latency。当前 MULTIMODAL-REPRESENTATION 已拥有固定总预算→时空/模态分层分配、selector drift 与 full-token fallback，故 No Change；memory/position identity 失效时回退固定帧/固定预算或完整 tokens。

### [2605.19328 RoboJailBench](https://arxiv.org/html/2605.19328v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19335 Scheduling ANNS with I/O Stalls](https://arxiv.org/html/2605.19335v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19341 HalluWorld](https://arxiv.org/html/2605.19341v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19373 CRDT Model Merging](https://arxiv.org/html/2605.19373v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19407 A Bitter Lesson for Data Filtering](https://arxiv.org/html/2605.19407v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19447 Selective Hindsight Distillation](https://arxiv.org/html/2605.19447v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19461 Distribution Matching for Diverse Reasoning](https://arxiv.org/html/2605.19461v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19478 Functional Fusion Backdoor](https://arxiv.org/html/2605.19478v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19481 C2CServe](https://arxiv.org/html/2605.19481v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19577 GoLongRL](https://arxiv.org/html/2605.19577v1)
问题与机制：heterogeneous long-context tasks 的 EM/F1/NDCG/ROUGE-L reward scale 不可直接混合；exact-v1 §3 冻结九类 capability/data construction，§4 以 task-level RMS 替代跨任务不可比的 per-prompt scale，再用 smoothed pass rate 调节难度权重。§5 只覆盖 23K、Qwen3 4B/30B 与作者 benchmark，§6/Appendix C–D 不证明 taxonomy 完备或 reward 是现实 outcome truth。task 样本不足、metric 不可比或历史难度漂移时回退 task-specific GRPO、单任务 batch 或不跨任务聚合；代码/数据仓库有声明，event-time commit 未披露。

### [2605.19604 Formal Skill](https://arxiv.org/html/2605.19604v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19619 MiMuon](https://arxiv.org/html/2605.19619v1)
问题与机制：持续 orthogonalization 在 singular-value gap 稳定时是清晰 Muon 路径；gap 接近阈值时 paper 的 stability/generalization bound 会恶化。exact-v1 §3 的 MiMuon 以 gap test 选择 orthogonalized direction 或 momentum-SGD direction，optimizer owner 因而必须保存 threshold、branch decision、momentum 和 checkpoint identity。§4–§5 的结论受论文 smoothness/stability 条件约束，§6 仅覆盖 Qwen3-0.6B/WikiText-103 与 YOLO26m；不证明大规模、分布式或生产吞吐优势。Introduction contribution 句把 Muon/MiMuon bound 方向写反，与 abstract、Table 1、定理和 §7 冲突，本审阅只采用后者一致的受限命题。gap estimate 噪声、threshold 抖动、假设不可验证或 matrix path 无收益时，回退版本化 pure Muon、SGDM 或 AdamW。

### [2605.19722 Autonomous Security-Agent Evaluation](https://arxiv.org/html/2605.19722v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19755 Operationalising AIBOMs](https://arxiv.org/html/2605.19755v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19769 OpenComputer](https://arxiv.org/html/2605.19769v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19779 Distribution-Free UQ for Agent Evaluation](https://arxiv.org/html/2605.19779v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19932 PEEK Context Map](https://arxiv.org/html/2605.19932v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19945 GEM Expert Mapping](https://arxiv.org/html/2605.19945v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19952 Beyond Atomic Facts in Agent Memory](https://arxiv.org/html/2605.19952v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.19999 Contamination-Resistant Benchmarks](https://arxiv.org/html/2605.19999v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.20005 Loss-Adaptive Fine-Tuning](https://arxiv.org/html/2605.20005v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.20022 FlexDraft](https://arxiv.org/html/2605.20022v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.20051 Vulnerability Variant Hunting](https://arxiv.org/html/2605.20051v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.20061 Consistency-Guided Credit Assignment](https://arxiv.org/html/2605.20061v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.20084 BalanceRAG](https://arxiv.org/html/2605.20084v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### [2605.20179 TIDE](https://arxiv.org/html/2605.20179v1)
对应 exact-v1 deep review 由 canonical/legacy marker alias 与 V3 artifact 共同定位。

### 本轮新增证据（原连续§4块之后追加）

原连续证据块逐字保留。以下为本轮新增及必要纠正证据；三条legacy恢复只说明原日事实/判断，不重复计入补窗新候选。必要原件、反证、owner差额和逐字PRE见[唯一补查记录](../_sources/daily-20260520/SUP_SOURCES_20261019.md)，实际分层复核见[独立reader](../_sources/daily-20260520/SUP_REVIEW_20261019.md)。

### [2605.16551 PQR: A Framework to Generate Diverse and Realistic User Queries that Elicit QA Agent Failures](https://arxiv.org/html/2605.16551v1)

精确v1 §§2–5/T1–2/B2–3/C1–2/D1/D4：query策略/变体与prompt反思双层搜索，现实意图约束、objective利用/探索/补测分责。单shopping assistant/100产品与近似query数量匹配不等全token预算；GEPA自动realism3.81>PQR3.66，人评排序不同；B2专家协商并非主文majority统一口径。词汇/embedding多样性不证failure类别覆盖，自适应judge有search-overfit，时间推估非实测墙钟。Ch66单段R21实际POST通过。

### [2605.16651 Right Predictions, Misleading Explanations: On the Vulnerability of Vision-Language Model Explanations](https://arxiv.org/html/2605.16651v1)

精确v1 §§3–4/A–C：Eq5负entropy最小化趋均匀，Alg1正梯度与所述最小化冲突；T3 pred-only IoU最低、xai-only MaxΔP反低于full，直接不支持四loss必要/移除pred近十倍。Alg1稀疏clamp与C epsilon/Adam、主7×7与多种patch grid不一致。保prediction stability≠heatmap stability线索，不采用中心定向隐蔽操纵、任意/无需梯度/faithfulness保证，中心争议R26隔离，不入Books。

### [2605.16861 Prefix-Adaptive Block Diffusion for Efficient Document Recognition](https://arxiv.org/html/2605.16861v1)

精确v1 §§3–5/T1–4：CSL监督包含第一低confidence前沿、PPC连续prefix且必要时forced-one；候选range非commit unit，未决suffix丢弃重置，下轮clean KV物化同时新预测。confidence非正确/AR分布认证，RTX4090 batch1/non-diagram TPS非整页或并发SLO；重训/公开基线数据不全等，causal非全格最优，宽窗口可退步。完整视觉/文本前向、被丢预测与clean重算都计费。Ch24两段R21实际POST通过。

### [2605.16871 SADP: Subgoal-Aware Diffusion Policy for Explainable Robots Learned from Foundation Model Generated Demonstrations](https://arxiv.org/html/2605.16871v1)

精确v1 III–V/TI–III：成功执行示范分段，末帧0完成、其余1进行，task/subgoal同时进入diffusion action和focal head，ongoing p<.2才切换。task级baseline与分段训练人口不同，sim oracle masks、实机外部affordance有额外依赖；sim每200epoch测试取top3非final holdout，TARAD部分task更好，oracle进度差额不证解释忠实/HRI或安全。Ch26单段R29实际POST通过。

### [2605.16918 HighSync: High-Quality Lip Synchronization via Latent Diffusion Models](https://arxiv.org/html/2605.16918v1)

精确v1 III-A–F/IV-A–F/TI–V：随张嘴变化的crop resize可让upperface泄漏原唇形，temporal通路与有损mask另有条件shortcut；silence/错音频诊断、固定全video crop及通路mask不同于已证彻底消漏。T5未独立量化PNG，静止闭嘴也可高silence分；train共享随机reference与infer逐帧原reference信息不等，全video与周围audio窗口不由cache授在线因果streaming。Ch24两段R29实际POST通过。

### [2605.17232 Vocabulary-size-independent Convergence of Discrete Diffusion Models](https://arxiv.org/html/2605.17232v1)

精确v1 §§3–5/Theorem5.1/Eq15/Table2发现中心冲突：masked定理还需support上估计score处于[s/2,3s/2]，并非摘要所称仅rate integrability；IPM常数含embedding diameter，未给随词表一致界，sequence d、β、loss及cubic correction仍在。实际forward为独立token的masked/uniform Kronecker，连续CTMC误差不含tau-leap离散化或实测。争议隔离，不把窄adjoint线索当中心命题证成，不作正面Evidence或Books。

### [2605.17361 MasFACT: Continual Multi-Agent Topology Learning via Geometry-Aware Posterior Transfer](https://arxiv.org/html/2605.17361v1)

精确v1 §§2–4与PDF B/D1/D3/D5–8/Alg1、主T4–5/Fig3必要恢复：历史bank角色属性+关系用FGW匹配，transport prior支持残差拓扑适配与旧任务只读。Gibbs分析与Gumbel实现不同，support-conditioned scaffold不能自动满足独立prior条件，不采用PAC/普遍无忘却。CodeAA61.14<replay62.09、AF多项正、复杂度proxy与图改动式不同；局部ablation非全任务保证。R28窄Source有效，Ch82实际正文/两侧/本人注经R33非writer POST通过。

### [2605.17393 Heterogeneous Information-Bottleneck Coordination Graphs for Multi-Agent Reinforcement Learning](https://arxiv.org/html/2605.17393v1)

精确v1 §§3–5/Prop4.2/4.4/T2/4与collapse消融：每层group-prior图KL+末层feature瓶颈可作神经协作策略的窄替代。最优匹配prior族不劣≠固定prior/return无害；Q还读obs/history，低TD不证明消息本身relevance；water-filling KKT非实际最优解。reversed prior/部分MAgent反退、跨posterior KL、混合tail/peak口径与±0.5σ非CI保留，主复杂度仍n²而非已证稀疏网络执行。Ch82实际两段/两侧/本人注经R33非writer POST通过，不采中心普适理论保证。

### [2605.17482 Residual Semantic Decomposition of Word Embeddings](https://arxiv.org/html/2605.17482v1)

精确v1 GloVe100重建+cos-affinity/K2 residual，仅6手工pair与declared-pool随机12诊断；assignment entropy不能直接当词义歧义，残差不是自动sense输出。随机entropy gap均值负、bank十seed有40%collapse，source-fit/union-fit应分，固定seed42不认证稳定。1+1+2=4关闭判断，局部诊断仅报告，不借后到GPT2/context版本推高v1贡献。

### [2605.17535 AgentModernize: Preserving Business Logic in Legacy Modernization with Multi-Agent LLMs and Behavioral Specification Graphs](https://arxiv.org/html/2605.17535v1)

精确v1 II–VII与后到v2受影响IV–VII/TIII–IX分开：v2纠正测试/API协议，v1‘baseline全0/feedback唯一非零’不再正面采用。每method见自身generated code的测试不是共同测集，noFB均值23.8/23.9>FB23.0且有回归；BSG同抽取链非独立oracle，无BSG移除或同调用预算控制，8synthetic/3trial不证generation唯一瓶颈。只采inspectable IR、独立behavior与回退分责；Ch81 problem-compilation/heldout/可信revision已具体承载，R22 NC通过。v2不是May19新家族。

### [2605.17759 FrequencyBooster](https://arxiv.org/html/2605.17759v1)

精确v1 §§3–4及局部消融：同patch宽global decoder分工高频、DiT偏低频，x-pred/v-loss与iREPA/LPIPS共同训练，noVAE不等无预训练表征。1.1B与约0.68B、epochs/NFE不同，200epoch ablation只支持3.99→3.55→3.50局部差额；latent方法有更好FID，不能称overall SOTA或已证总成本下降。具体长期decoder差额因而深入审阅并整合Ch24，R11实际POST通过，不因原5分只写标准完成。

### [2605.17938 Training data attribution in diffusion models via mirrored unlearning and noise-consistent skew](https://arxiv.org/html/2605.17938v1)

精确v1 §§2.1–2.4/4–5：镜像retention−λgenerated的受限unlearning配合同100噪声的normalized skew，null clamp与停止阈值限制轨迹，不是因果归因或认证删除。分母为两模型损失各自绝对值之和加epsilon。低分辨率DiT/EDM、最多40%聚合删除与6初始化/120图重训限制外推，COCO不显著且CLIP并非落后于本法；hub/ensemble反侧保留。TRAIN-DATA Ch27两段实际整合，R11非writer POST通过。

### [2605.18530 Continuous Diffusion Scales Competitively with Discrete Diffusion for Language](https://arxiv.org/html/2605.18530v1)

精确v1 §§2–5：learned Gaussian embedding配modern DiT与NELBO，用non-embedding FLOPs控制架构/精度混杂；self-conditioning额外8.3%以减steps抵消，仍约20倍AR，非完整墙钟等费。22.1是NELBO bound非精确likelihood，LM1B仍输MDLM，高步数self-conditioning熵下降而MAUVE退步。Prop2需Bayes-optimal/不collapse且有conditional total-correlation残差，不能称任意训练器严格线性CE。Ch24两段R11实际POST通过。

### [2605.18597 Latent Action Reparameterization for Efficient Agent Inference](https://arxiv.org/html/2605.18597v1)

精确v1 §§3–5及A2–4/A10–11/A14：词/短语统计与经验next-token entropy指导增词，最长匹配、初始化与teacher-KL/LoRA适配共同压缩token horizon。低entropy不推出所有history的transition equivalence或无风险，新增词普通forward不授外部协议可执行保证；TT非完整E2E，部分peak memory上升，A14是静态system prompt替换而非多步真实动作闭环。MODEL-TOKENIZER Ch11具体迁移边界两段已整合，R11实际POST通过。

### [2605.18599 Resolving Representation Ambiguity in Feedforward Novel View Synthesis Transformer via Semantic-Spatial Decoupling](https://arxiv.org/html/2605.18599v1)

精确v1 §§3–4/A/G：每patch总D不变，两支D/2，共享完整QK路由而V/output/LN/FFN分责；目标语义零起点，可选teacher、DA3 pointmap与affine调制增加依赖。等预算重实现中混合baseline加监督/调制反退，独立QK或joint LN也较差，只支持局部接口，不证明统计独立或真实几何。warmup后的model-forward非预处理/训练/请求全费，动态与长轨迹未验。Ch23两段R29实际POST通过。

### [2605.18736 Spectral Progressive Diffusion for Efficient Image and Video Generation](https://arxiv.org/html/2605.18736v1)

精确v1 §§3–6：DCT保低频、补高频噪声后state rescale/timestep重索引，δ-optimal只在Bayes-optimal/Gaussian单频/单调谱假设下界定局部velocity误差，非全轨迹最优。TF依赖未见分辨率泛化，FT另rank32/2000iter；基线引用RALU且步数也减少，GenEval/ZImage/WAN有直接质量反退，只改spatial。未采用7.09倍等速度数字，D/E计时全费未核不冒称原文未披。Ch24两段R14实际POST通过。

### [2605.19775 Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles](https://arxiv.org/html/2605.19775v1)

本段及下两段仅恢复原legacy事实，均保2026-05-20/原3+2+3=8；不是May19补窗新候选，不在当前候选表重复列。有效必要Source/具体Books校正由[May21报告](../21/README.md)及其root R4/R6/R8/R12直接复用，不更改原70行或原日分。

原legacy保留的May20/8分候选，仅此处恢复引用，非补May19新候选。复用May21定点发现后的root必要Source/具体owner R4/R6：单H200节点下DP/TP及memory压力、未来KV增长与状态传输取舍，只为已有Ch56 SLO-aware admission、future-state reservation、chain capacity与DP↔TP切换增加受限实证，不形成32B等长期阈值；不把static TP与完整权重驻留的其它路线混同。具体NC有效，不重复全文审阅。

### [2605.19893 SpecSA: Bridging Speculative Decoding and Sparse Attention for Efficient LLM Inference](https://arxiv.org/html/2605.19893v1)

原legacy May20/8分保持。v1题名为SpecSA，SSV只是后版导航；采用§3–7对union KV加载/query ownership mask的strict重排，区分共享代表query/跨层复用索引的近似，不能把机制写成跳过可能无分歧的待验token。Ch48原两段仅纠正此归因与sparse-target/dense-target边界，May21作者窄写后root R8实际非writer POST通过。3.49倍相对AR NSA与6.86倍局部kernel不可互换，H100/所列NSA-adapted负载和四1B质量任务不授通用target-law或生产SLO。

### [2605.19269 CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs](https://arxiv.org/html/2605.19269v1)

原legacy May20/8分保持。复用精确v1 §§3–5/C.2必要Source，Ch49仅两既有段窄纠正，root R12实际POST通过：tile-local epilogue与辅助reduction分开，kernel不计而block计的费用不可混同，实数缩放重排不承诺BF16逐bit。单H100/common Transformer非Attention/非embedding的kernel/block实验并非完整模型训练或serving E2E，LLM author带示例/日志/人工监督不等无人干预。此恢复不新增整合数。三项具体依据见[跨日定点去重及归因修正](../_sources/daily-20260521/SUP_SOURCES_20261019.md#a3--首个必要source与具体owner提案19775)，只复用这三身份的有效层，不继承另一日研究池。

### [2605.17314 Weak-to-Strong Elicitation via Mismatched Wrong Drafts](https://arxiv.org/html/2605.17314v1)

精确v1 §§3–6/T1–4/D3–4及B：弱且更math-trained drafter每题32份中取错稿、固定derangement给其它题，learner仍执行on-policy DrGRPO；外部经验改变prompt条件，不是off-policy gradient或teacher imitation。2×2和no-draft只支持单Mathstral7B/QwenMath1.5B及所测math人口，MATH500挑ckpt2000并非独立选择、AIME少题/两seed、AIME24高k反输no-draft；selected creation/inverse正确rollout里的96.7%判错不外推全体rigor。drafter、过滤、完整RL/采样及多层审计全计费，有限pass@k零命中不是原模型support严格零。TRAIN-GRPO Ch33原组内reward链后单段已实际写入，R41非writer POST通过。

### [2605.17342 Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment](https://arxiv.org/html/2605.17342v1)

精确v1 §§3–7/T1–2/C3/C7：shared backbone共同学习clipped scalar差与unitnorm antisymmetric bilinear分支，prompt gating控制尺度，self-play先偏scalar再回原混合。unitnorm不等zero-mean，实测均值偏离；理论realizable/exact oracle与bounded条件不自动成立，schedule趋learned proxy不证明真实oracle误差消退或Nash。部分去gating/clipping/unitnorm设置反升；4A80080G/BF16/2048及三alignment迭代是作者协议，单human500对/同GPT-family排序不证明多rater一致或排尽偏差。TRAIN-RLHF Ch31在GBPM后保留旧标量/pairwise合理边界新增单段，R48实际POST通过；不采用唯一正交偏好因素或安全保证。

### [2605.17359 Learning Transferable Topology Priors for Multi-Agent LLM Collaboration Across Domains](https://arxiv.org/html/2605.17359v1)

精确v1 III-B–E/Alg1/IV-C–K/T V/VII/VIII/XI：offline query/referencegraph训练conditional VAE，frozen BERT/GCN编码与query Gaussian prior产生角色/边初始化，再交原backbone refine；GRL在训练期，不是每个测试query更新模型。廉价/静态/随机监督可低于scratch，weak与full实际差4.20pp而非1.25；linear-contraction与domain bound仅条件动机。AgentDropout/ARG teacher计费口径不一，120M/322只token摊销，非含GPU/全reference搜索的生产回本。AGENT-MULTI-AGENT Ch82 MasFACT后单段区分现场bank与参数化prior，R47实际POST通过。

### [2605.18226 Context Memorization for Efficient Long Context Generation](https://arxiv.org/html/2605.18226v1)

精确v1 §§2.2–5/A/C/B直接反侧：固定query、原KV分块的(a,Z)能按Z权重精确merge；校准queries聚类/平均Z/最近centroid是不同query间的近似，GQA共KV不令query-head输出同，分块编码也可改高层上下文。Llama3.1-8B的32K ICL/NBA20K及Qwen必要反侧中容量/质量非单调，validation选表示；top16 hierarchy并非任意规模exact检索。trace前向、最长约1.5h构造、索引与失效重建均付费；attention-only RTX4500Ada batch1和主文/附录生成长度不一，不采用1.36/1.8倍E2E。INFER-KV-CACHE Ch45普通exact-cache链后新增两段，绑定prefix/model/layer/head/position/校准身份及fullprefix回退；R41实际POST通过。

### [2605.18253 Machine Unlearning for Masked Diffusion Language Models](https://arxiv.org/html/2605.18253v1)

精确v1 §§3–7/Alg1/B1–4：保同一partially revealed response state，以冻结初始模型的全mask-prompt分布为conditional forwardKL anchor，概率取幂再归一；TOFU另retain SFT，RWKU没有。anchor/已揭response仍可携带目标知识，局部state匹配非MI归零或不可恢复删除。TOFU只20虚构作者/retain末20、RWKU首10实体；128MC answerprob与256mask pseudoPPL非joint likelihood。低τ乱码/空输出、高τ流畅假替换，Dream worldfacts和RA mean尾部反退不由median抹去。四H200训练、anchor前向、MC/τ选择及独立提取和utility回归全计费。TRAIN-DATA Ch27反事实optimizer链后两段，R47实际POST通过，不将忘记分数签为隐私资格。

### [2605.17978 AutoVecCoder: Teaching LLMs to Generate Explicitly Vectorized Code](https://arxiv.org/html/2605.17978v1)

精确v1 §§3–5/T2–3/A：correctness gate内正baseline加tanh有界相对CPU latency改善；Qwen3-8B/SSE-AVX SimdBench/Xeon8374C及全部-O3、64专用核、20秒test门、150秒profile三次均值仅作者协议。fastp含所有cases，P50/P75只correct人口；NSR对照同时改变gate/floor/shape/relative定义，不能识别每一项长期必要性。allcorrect组常数中心化可抵消，reward有界不界policy ratio；tests不认证语义等价，teacher早于benchmark不排其它污染。R34标准完成/R46日期通过；Ch33正确资格内效率分账、组常数与reward形状链已承载这些选择，R39具体已有覆盖，不制造新diff。

### [2605.17187 PluRule: A Benchmark for Moderating Pluralistic Communities on Social Media](https://arxiv.org/html/2605.17187v1)

精确v1 §§3–7/T2：same-submission violating/compliant pair和context层提供局部评价边界，不是同评论跨rule的causal swap。13,371pairs/1,989社区/9语言，未见moderator行动作compliant为弱标签；100English人工核只看moderatorcomment→rule匹配，不认证目标评论真实合规。历史2005–2023行为对2025Nov规则有时漂，stage2回答抽取/英语与筛选限制、User57.7与images57.6不混算；低分不证明普遍不理解社区规范。R34关闭判断/R46日期通过；1+1+2=4仅报告，不改变Books已有policy与独立事实验收。

### [2605.18549 Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/html/2605.18549v1)

精确v1 §2–3.3/Limitations/A1–3/G：多层非线性probe沿prefix逐坐标cummax，合并logit形成轨迹再提统计/趋势等特征。latent单调非probability单调，template继承标签和actual response标签不同；evaluation split内三折拟合并选RF只诊断separability，不是固定readout的OOD部署成绩。4–14B两family/安全与math，WildGuard标签噪声、全轨迹与early信号差、约3000 A10040GB GPUh/probe50–80M及hidden读取费保留；未授FPR、真实意图或生产monitor。PLATFORM-SECURITY Ch72白盒节新增轨迹/校准分责单段，R54实际POST通过。

### [2605.18646 Language-Switching Triggers Take a Latent Detour Through Language Models](https://arxiv.org/html/2605.18646v1)

精确v1 §3–5/7/A/D/E/F：Gaperon8B语言切换触发、100prompts×5seed及30 paired corruption，只支持这组model/intervention人口。自然语言probe未读到触发状态不证明信息不存在，natural axis在16–29层本身不稳，不能授正交；Gaussian与neutral早层恢复大变，neutral约95%mitigation非完全，移除末位置可能伤正常语言且缺定量utility。clean/corrupt/patch、读出和独立回归付费；不采唯一三段电路、任意后门不可检出或安全修复。PLATFORM-SECURITY Ch72原observer/标签分责后单段，R54实际POST通过。

### [Advancing content provenance](https://openai.com/index/advancing-content-provenance/)

May19官方核心采用C2PA metadata与SynthID互补及OpenAI来源verifier的negative语义，不把Jul31 audio/API和Oct5 EUtext更新回填。metadata可能剥离，watermark没有检测到必须保Unknown，不推非AI/其他厂商；签名不认证内容真伪、版权或权限。未披TPR/FPR、攻击/变换协议和完整时延，不采普适robustness。R30必要Source/R51实际owner：Ch72 layered provenance的signature/origin/sensor及阴性Unknown已具体承载，2+2+2=6深入后已有覆盖，无新Books写入。

### [Introducing Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/)

May19官方核心及代码明确interaction创建/接收remote environment并在后续调用续接files/state，AGENTS.md/SKILL.md配置后register agent；不由versionable files推registry自动immutable/pinning，也未披TTL/durability/exact isolation/权限继承或生产SLO。R25必要Source/R51实际owner：Ch84的source/digest/admission/run identity、instance生命周期、harness绑定environment/definition及internal resume≠external对账已具体承载，2+2+2=6深入后已有覆盖，不增机制段。

### [2605.18678 Lance: Unified Multimodal Modeling by Multi-Task Synergy](https://arxiv.org/html/2605.18678v1)

精确v1 §3.2–4/T2–4/6/T9–10/7必要域，R56日期与2+2+2=6窄Source、R58具体owner/逐字PRE通过。MaPE仅给semantic/cleanVAE/noisyVAE三group的时间轴加常数offset，同组相对坐标保留而跨组被改写，不证明语义对齐或真实同步。abstract scratch与正文Qwen初始化口径冲突、T9跨任务比率非单调、T10局部无seed/完整matchedcompute均保留；双expert、冻结codec、数据制备、多阶段训练与采样全计费，不采全任务synergy或实时净省费。Ch23唯一一段已保存，R59真实新增/两侧/本人注nonwriter POST通过并释放。

### [2605.18683 EPIC: Abstraction and Polymorphism of In-Network Collectives on Ethernet](https://arxiv.org/html/2605.18683v1)

R57完整题摘/May19有限日期通过，2+2+3=7；必要§2–7/H1–4及Ch36实际owner/逐字PRE R61通过。窄增量为端到端重传改为逐跳ACK后，聚合完成不再足以授权所有rank的旧window回收，pipe按合法PSN范围/最慢输出ACK推进。H2只Tree3-2/四clients×3packets/最多一次loss，不授任意规模活性；Tofino真机仅II、host拷贝、emulation/packet/flow/RTL各自分证，不拼成生产性能。ModeII PSN同步、确定顺序的额外buffer、整树资源全取或全退亦保留。Ch36真实一段/两侧/本人注经R63非writer POST通过并释放。

### [Qwen3.5-LiveTranslate: From Sound to Sight, From Word to Right](https://qwen.ai/blog?id=qwen3.5-livetranslate)

官方2026/05/19完整core/architecture/streaming评价与API说明由primary域检索恢复，静态目录shell不证明无事件。实际新增为chunk-wise输入与ReadableUnit tags控制合成粒度；Thinker输出译文、Talker另消费译文/sourceaudio。2+1+2=5标准Only经R60独核通过；tag生成/监督、lookahead、完整预算硬件、样本与tail统计未披，均值不是SLO，榜单/视听demo不证明端到端因果或身份授权。只保公开版本接口事实，不强写长期Books，也未运行客户端或服务。

## 5. 缺口与下一步

无未处理的可执行研究或Books待办。全部21项新整合已完成真实POST，有限来源按R62收口，R64整日复核通过。以下均为本窗终态保留项：缺失或争议部分不作正面证据、不进入Books、不支持无遗漏断言，也不授相应Coverage通过；各项仅按所列条件定点重开：

- [16399 Stable and Near-Reversible Diffusion ODE Solvers for Image Editing](https://arxiv.org/abs/2605.16399v1)与[16430 A Theory of Training Profit-Optimal LLMs](https://arxiv.org/abs/2605.16430v1)：exact-v1最早公告界分别May13/May15，sameDOI arxiv.content/findable registered为May19 03:40:27/03:41:13Z，整个可能区间跨日。官方有效May月表/all分页只证当前月身份，Updated不是首公开，无效daily参数不算网络故障；有限具名公告恢复未得到日批次。二者不列确定当窗候选、不评分/写Books、不记零命中。可接受exact-v1官方日批次或已公开正文的官方早记录，足以收窄区间时只重开日期层与其依赖，不扩全月/附件。
- Qwen/MiMo历史coverage：旧Qwen迁站/新blog shell及MiMo当前17路由不能回放被删除/未索引历史。已恢复的LiveTranslate完整core/日期与8paper/17route有界检查各自有效，但不证明原日完整索引。仅在具名May19官方完整索引或正文原件到达时重开对应项，不把现有单篇推倒或重新泛扫。

17232中心争议保留：masked定理另要求support上score相对夹界；泛IPM常数含embedding diameter而无词表一致界，重开需受影响定理明确假设/常数或可核更正。16651中心争议保留：Eq5/Alg1方向与Table3直接冲突，重开需精确更正或能解释目标/实现及反侧的必要原件。二者准入/日期有效，故在30家族内保原分/争议处置；中心命题不作正面Evidence、Books或全覆盖依据，不以降分或删反证改成通过。

晚发现的PopPy18697/Mosaic18710/RRFP18750已有May19旧正式候选/原8、9、9分及有效处置，R57直接复用；EgoBaby19130与Qwen3.7主源May20线索留真实May21归属，不迁入本补窗。17936贡献前排除不评分；Anthropic v1题摘/正文差异不解释成新实验提升。以下四条仅为原小时窗历史处置，不授本轮完成：

- 无待修复项。fresh 非作者挑战恢复了 4 个 false negative；其 exact-v1 Evidence、score、Books comparison 已同步。
- root 已按 serialized queue 写回 2605.18810、2605.18999、2605.19619；连同先前 6 项，9/9 root binding 均通过 post-write 语义复核。
- 2605.19260 为 No Change；Ch23 已完整承载空间/时间 token budget、position identity、压缩 state、failure 与 full-token fallback。
- Materials Request=0；未 stage、commit 或 push。

## 6. 复核

本轮复核者：独立reader `/root/supp_may20_reader`（此前有效记录由`/root/may20_supp_reader`产生）。结论：通过，R64实际整日DAY已验，R65完成态保存后FINAL通过。实际检查14源有限主题/分页停止点、100行当前候选与全部§4/六节，复用未变化的有效旧绑定。新增30=21I/4NC/3Only/2中心争议；21I真实POST为原R11/R14/R21/R29/R33/R41与R47/R48/R54/R59/R63。安全/纠错/直接反证逐项核；普通排除复用R3的17107/17542/16406分层样本，另实际核17936及机构Omni/TPU/RL-RCHAT，不把样本说成575全量验收。R55只核修订差额，R57三旧系统直接去重，R62历史coverage/两日期保留不授对应正面Coverage。DAY实际发现并修正过时16项措辞与17938分母多余“差”；原Books精确式有效未重审。原70整行唯一/顺序、原小时窗及17442字符连续旧§4均保持，100行及115本地文件链接、V3与限定diff-check通过；机械检查不替代上述语义核验。依据[独立R64](../_sources/daily-20260520/SUP_REVIEW_20261019.md#r64--当前六部分实际day复核)。以下通过声明仅对应2026-09-15历史范围。

复核者：fresh-context non-author final reviewer `/root/may12_fresh_postwrite`

结论：通过

Fresh non-author final Gate：PASS。官方 announcement owner/cutoff、`575 = 70 + 505`、两项机构 closure、70 份 exact-v1 Evidence、`8 score7 + 51 score8 + 11 score9`、`70 = 36 Applied + 34 No Change` 已对账。36 个 Applied 的 marker 唯一/成对/位于首个 `## Review notes` 前；9 个 root binding 顺读相邻段落后语义通过。整体状态：Complete；Coverage=Closed、Evidence=Passed、Books=Passed、unresolved findings=0。

Fresh 审阅记录见 [`FRESH_NON_AUTHOR_FINAL_REVIEW_20260915.md`](../_sources/daily-20260520/FRESH_NON_AUTHOR_FINAL_REVIEW_20260915.md)。

完整作者检查点见 [`AUTHOR_V3_RECERTIFICATION_20260915.md`](../_sources/daily-20260520/AUTHOR_V3_RECERTIFICATION_20260915.md)。

### Legacy V2.1 evidence appendix — Executive Summary

本次独立重放枚举并逐项闭合 727 个注册 arXiv identity，冻结 75 个 Source Family；pre-denominator closure=652，withdrawn pre-denominator=0。32 个旧候选被迁回正确 owner day，3 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

### Legacy V2.1 — Coverage

<!-- legacy-validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-20 |
| Window End | 2026-05-20 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260520-CREATED-8ba5495e97ea385a |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Historical V2.1 record only; current V3 final status is Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Historical V2.1 record only; current V3 Books Gate is Passed |

### Source Coverage Receipt

<!-- legacy-validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-19T09:00:00+08:00 | 2026-05-20T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 727 | SF-2026-ARXIV-2605-18755;SF-2026-ARXIV-2605-18762;SF-2026-ARXIV-2605-18792;SF-2026-ARXIV-2605-18796;SF-2026-ARXIV-2605-18803;SF-2026-ARXIV-2605-18859;SF-2026-ARXIV-2605-18891;SF-2026-ARXIV-2605-18899;SF-2026-ARXIV-2605-18918;SF-2026-ARXIV-2605-18930;SF-2026-ARXIV-2605-18991;SF-2026-ARXIV-2605-19008;SF-2026-ARXIV-2605-19049;SF-2026-ARXIV-2605-19099;SF-2026-ARXIV-2605-19101;SF-2026-ARXIV-2605-19127;SF-2026-ARXIV-2605-19140;SF-2026-ARXIV-2605-19151;SF-2026-ARXIV-2605-19169;SF-2026-ARXIV-2605-19192;SF-2026-ARXIV-2605-19193;SF-2026-ARXIV-2605-19196;SF-2026-ARXIV-2605-19218;SF-2026-ARXIV-2605-19228;SF-2026-ARXIV-2605-19240;SF-2026-ARXIV-2605-19242;SF-2026-ARXIV-2605-19262;SF-2026-ARXIV-2605-19269;SF-2026-ARXIV-2605-19276;SF-2026-ARXIV-2605-19282;SF-2026-ARXIV-2605-19314;SF-2026-ARXIV-2605-19319;SF-2026-ARXIV-2605-19321;SF-2026-ARXIV-2605-19328;SF-2026-ARXIV-2605-19335;SF-2026-ARXIV-2605-19341;SF-2026-ARXIV-2605-19373;SF-2026-ARXIV-2605-19407;SF-2026-ARXIV-2605-19444;SF-2026-ARXIV-2605-19447;SF-2026-ARXIV-2605-19461;SF-2026-ARXIV-2605-19478;SF-2026-ARXIV-2605-19481;SF-2026-ARXIV-2605-19537;SF-2026-ARXIV-2605-19576;SF-2026-ARXIV-2605-19593;SF-2026-ARXIV-2605-19604;SF-2026-ARXIV-2605-19722;SF-2026-ARXIV-2605-19755;SF-2026-ARXIV-2605-19769;SF-2026-ARXIV-2605-19775;SF-2026-ARXIV-2605-19779;SF-2026-ARXIV-2605-19811;SF-2026-ARXIV-2605-19847;SF-2026-ARXIV-2605-19893;SF-2026-ARXIV-2605-19932;SF-2026-ARXIV-2605-19945;SF-2026-ARXIV-2605-19952;SF-2026-ARXIV-2605-19999;SF-2026-ARXIV-2605-20005;SF-2026-ARXIV-2605-20022;SF-2026-ARXIV-2605-20023;SF-2026-ARXIV-2605-20051;SF-2026-ARXIV-2605-20061;SF-2026-ARXIV-2605-20084;SF-2026-ARXIV-2605-20179;SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING;SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV;SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA;SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES;SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE;SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL;SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-;SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A;SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | created-day pages=closed; OAI category sets=closed; direct same-day OAI=575 | 2026-05-20T09:00:00+08:00 | coverage:SRC-ARXIV:20260520 | — |

<!-- coverage:SRC-ARXIV:20260520:start -->全量 raw inventory=727；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260520:end -->

### Coverage Limitations

- arXiv 月度 listing 只证明月份收录；逐日 owner 使用 initial DOI `created` 日历日 proxy，并以 exact-v1 history 与官方发布节奏约束。
- DOI ingestion timestamp 不是精确的 09:00 publication instant；本日报不把 `updated` 或 current OAI datestamp 当作 first-public。

### Materials Request Ledger

<!-- legacy-validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
None — 没有 exact-version primary-material blocker。

### Legacy V2.1 — Candidate Ledger

<!-- legacy-validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | arXiv:2605.18755v1 | paper-v1:2605.18755 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18755 | self | — | new_in_window | PLATFORM-LOGGING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18755 | yes |
| SF-2026-ARXIV-2605-18762 | arXiv:2605.18762v1 | paper-v1:2605.18762 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18762 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18762 | yes |
| SF-2026-ARXIV-2605-18792 | arXiv:2605.18792v1 | paper-v1:2605.18792 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18792 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18792 | no |
| SF-2026-ARXIV-2605-18796 | arXiv:2605.18796v1 | paper-v1:2605.18796 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18796 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18796 | no |
| SF-2026-ARXIV-2605-18803 | arXiv:2605.18803v1 | paper-v1:2605.18803 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18803 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18803 | no |
| SF-2026-ARXIV-2605-18859 | arXiv:2605.18859v1 | paper-v1:2605.18859 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18859 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-18859 | no |
| SF-2026-ARXIV-2605-18891 | arXiv:2605.18891v1 | paper-v1:2605.18891 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18891 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-18891 | no |
| SF-2026-ARXIV-2605-18899 | arXiv:2605.18899v1 | paper-v1:2605.18899 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18899 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18899 | no |
| SF-2026-ARXIV-2605-18918 | arXiv:2605.18918v1 | paper-v1:2605.18918 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18918 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18918 | no |
| SF-2026-ARXIV-2605-18930 | arXiv:2605.18930v1 | paper-v1:2605.18930 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18930 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18930 | no |
| SF-2026-ARXIV-2605-18991 | arXiv:2605.18991v1 | paper-v1:2605.18991 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18991 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18991 | no |
| SF-2026-ARXIV-2605-19008 | arXiv:2605.19008v1 | paper-v1:2605.19008 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19008 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19008 | no |
| SF-2026-ARXIV-2605-19049 | arXiv:2605.19049v1 | paper-v1:2605.19049 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19049 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-19049 | no |
| SF-2026-ARXIV-2605-19099 | arXiv:2605.19099v1 | paper-v1:2605.19099 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19099 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19099 | no |
| SF-2026-ARXIV-2605-19101 | arXiv:2605.19101v1 | paper-v1:2605.19101 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19101 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19101 | no |
| SF-2026-ARXIV-2605-19127 | arXiv:2605.19127v1 | paper-v1:2605.19127 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19127 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19127 | no |
| SF-2026-ARXIV-2605-19140 | arXiv:2605.19140v1 | paper-v1:2605.19140 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19140 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19140 | no |
| SF-2026-ARXIV-2605-19151 | arXiv:2605.19151v1 | paper-v1:2605.19151 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19151 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19151 | no |
| SF-2026-ARXIV-2605-19169 | arXiv:2605.19169v1 | paper-v1:2605.19169 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19169 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19169 | no |
| SF-2026-ARXIV-2605-19192 | arXiv:2605.19192v1 | paper-v1:2605.19192 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19192 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19192 | no |
| SF-2026-ARXIV-2605-19193 | arXiv:2605.19193v1 | paper-v1:2605.19193 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19193 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19193 | no |
| SF-2026-ARXIV-2605-19196 | arXiv:2605.19196v1 | paper-v1:2605.19196 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19196 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19196 | no |
| SF-2026-ARXIV-2605-19218 | arXiv:2605.19218v1 | paper-v1:2605.19218 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19218 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19218 | no |
| SF-2026-ARXIV-2605-19228 | arXiv:2605.19228v1 | paper-v1:2605.19228 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19228 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19228 | no |
| SF-2026-ARXIV-2605-19240 | arXiv:2605.19240v1 | paper-v1:2605.19240 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19240 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19240 | no |
| SF-2026-ARXIV-2605-19242 | arXiv:2605.19242v1 | paper-v1:2605.19242 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19242 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19242 | no |
| SF-2026-ARXIV-2605-19262 | arXiv:2605.19262v1 | paper-v1:2605.19262 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19262 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19262 | no |
| SF-2026-ARXIV-2605-19269 | arXiv:2605.19269v1 | paper-v1:2605.19269 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19269 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-19269 | no |
| SF-2026-ARXIV-2605-19276 | arXiv:2605.19276v1 | paper-v1:2605.19276 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19276 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19276 | no |
| SF-2026-ARXIV-2605-19282 | arXiv:2605.19282v1 | paper-v1:2605.19282 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19282 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19282 | no |
| SF-2026-ARXIV-2605-19314 | arXiv:2605.19314v1 | paper-v1:2605.19314 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19314 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-19314 | no |
| SF-2026-ARXIV-2605-19319 | arXiv:2605.19319v1 | paper-v1:2605.19319 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19319 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-19319 | no |
| SF-2026-ARXIV-2605-19321 | arXiv:2605.19321v1 | paper-v1:2605.19321 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19321 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19321 | no |
| SF-2026-ARXIV-2605-19328 | arXiv:2605.19328v1 | paper-v1:2605.19328 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19328 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19328 | no |
| SF-2026-ARXIV-2605-19335 | arXiv:2605.19335v1 | paper-v1:2605.19335 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19335 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-19335 | no |
| SF-2026-ARXIV-2605-19341 | arXiv:2605.19341v1 | paper-v1:2605.19341 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19341 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19341 | no |
| SF-2026-ARXIV-2605-19373 | arXiv:2605.19373v1 | paper-v1:2605.19373 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19373 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Integrate | books-review:SF-2026-ARXIV-2605-19373 | no |
| SF-2026-ARXIV-2605-19407 | arXiv:2605.19407v1 | paper-v1:2605.19407 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19407 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-19407 | no |
| SF-2026-ARXIV-2605-19444 | arXiv:2605.19444v1 | paper-v1:2605.19444 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19444 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19444 | no |
| SF-2026-ARXIV-2605-19447 | arXiv:2605.19447v1 | paper-v1:2605.19447 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19447 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19447 | no |
| SF-2026-ARXIV-2605-19461 | arXiv:2605.19461v1 | paper-v1:2605.19461 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19461 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19461 | no |
| SF-2026-ARXIV-2605-19478 | arXiv:2605.19478v1 | paper-v1:2605.19478 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19478 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19478 | no |
| SF-2026-ARXIV-2605-19481 | arXiv:2605.19481v1 | paper-v1:2605.19481 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19481 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2605-19481 | no |
| SF-2026-ARXIV-2605-19537 | arXiv:2605.19537v1 | paper-v1:2605.19537 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19537 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-19537 | no |
| SF-2026-ARXIV-2605-19576 | arXiv:2605.19576v1 | paper-v1:2605.19576 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19576 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-19576 | no |
| SF-2026-ARXIV-2605-19593 | arXiv:2605.19593v1 | paper-v1:2605.19593 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19593 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-19593 | no |
| SF-2026-ARXIV-2605-19604 | arXiv:2605.19604v1 | paper-v1:2605.19604 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19604 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-19604 | no |
| SF-2026-ARXIV-2605-19722 | arXiv:2605.19722v1 | paper-v1:2605.19722 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19722 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19722 | no |
| SF-2026-ARXIV-2605-19755 | arXiv:2605.19755v1 | paper-v1:2605.19755 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19755 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19755 | yes |
| SF-2026-ARXIV-2605-19769 | arXiv:2605.19769v1 | paper-v1:2605.19769 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19769 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19769 | no |
| SF-2026-ARXIV-2605-19775 | arXiv:2605.19775v1 | paper-v1:2605.19775 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19775 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19775 | no |
| SF-2026-ARXIV-2605-19779 | arXiv:2605.19779v1 | paper-v1:2605.19779 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19779 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-19779 | no |
| SF-2026-ARXIV-2605-19811 | arXiv:2605.19811v1 | paper-v1:2605.19811 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19811 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19811 | no |
| SF-2026-ARXIV-2605-19847 | arXiv:2605.19847v1 | paper-v1:2605.19847 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19847 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19847 | no |
| SF-2026-ARXIV-2605-19893 | arXiv:2605.19893v1 | paper-v1:2605.19893 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19893 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-19893 | no |
| SF-2026-ARXIV-2605-19932 | arXiv:2605.19932v1 | paper-v1:2605.19932 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19932 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-19932 | no |
| SF-2026-ARXIV-2605-19945 | arXiv:2605.19945v1 | paper-v1:2605.19945 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19945 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-19945 | no |
| SF-2026-ARXIV-2605-19952 | arXiv:2605.19952v1 | paper-v1:2605.19952 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19952 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-19952 | no |
| SF-2026-ARXIV-2605-19999 | arXiv:2605.19999v1 | paper-v1:2605.19999 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19999 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19999 | no |
| SF-2026-ARXIV-2605-20005 | arXiv:2605.20005v1 | paper-v1:2605.20005 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20005 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-20005 | no |
| SF-2026-ARXIV-2605-20022 | arXiv:2605.20022v1 | paper-v1:2605.20022 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20022 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-20022 | no |
| SF-2026-ARXIV-2605-20023 | arXiv:2605.20023v1 | paper-v1:2605.20023 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20023 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20023 | no |
| SF-2026-ARXIV-2605-20051 | arXiv:2605.20051v1 | paper-v1:2605.20051 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20051 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-20051 | no |
| SF-2026-ARXIV-2605-20061 | arXiv:2605.20061v1 | paper-v1:2605.20061 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20061 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20061 | no |
| SF-2026-ARXIV-2605-20084 | arXiv:2605.20084v1 | paper-v1:2605.20084 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20084 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-20084 | no |
| SF-2026-ARXIV-2605-20179 | arXiv:2605.20179v1 | paper-v1:2605.20179 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20179 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-20179 | no |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | arXiv:2605.18815v1 | paper-v1:2605.18815 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | no |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | arXiv:2605.18854v1 | paper-v1:2605.18854 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | no |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | arXiv:2605.18824v1 | paper-v1:2605.18824 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | no |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | arXiv:2605.18814v1 | paper-v1:2605.18814 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | no |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | arXiv:2605.18853v1 | paper-v1:2605.18853 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | no |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | arXiv:2605.18825v1 | paper-v1:2605.18825 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | no |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | arXiv:2605.18812v1 | paper-v1:2605.18812 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | no |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | arXiv:2605.18852v1 | paper-v1:2605.18852 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | no |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | arXiv:2605.18856v1 | paper-v1:2605.18856 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | no |

### Legacy V2.1 — Review Completion Receipt

<!-- legacy-validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | RP-10421f11c0c05fee | deep | arXiv:2605.18755v1 | SRC-ARXIV@arXiv:2605.18755v1 | https://arxiv.org/html/2605.18755v1#S2 | https://arxiv.org/html/2605.18755v1#S4 | https://arxiv.org/html/2605.18755v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-18755 | complete |
| SF-2026-ARXIV-2605-18762 | RP-d07f2bb444275d67 | deep | arXiv:2605.18762v1 | SRC-ARXIV@arXiv:2605.18762v1 | https://arxiv.org/html/2605.18762v1#S2 | https://arxiv.org/html/2605.18762v1#S4 | https://arxiv.org/html/2605.18762v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-18762 | complete |
| SF-2026-ARXIV-2605-18792 | RP-7c4961ebc928422c | deep | arXiv:2605.18792v1 | SRC-ARXIV@arXiv:2605.18792v1 | arXiv:2605.18792v1 §2 knowledge-conflict benchmark; §3 self-prior, conditional belief estimation and abstention — parametric and contextual knowledge beliefs govern retrieval and abstention | arXiv:2605.18792v1 §4 Experiments, selective answering and ablations | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18792v1 No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-18792 | complete |
| SF-2026-ARXIV-2605-18796 | RP-ecb151b4d0133aa8 | deep | arXiv:2605.18796v1 | SRC-ARXIV@arXiv:2605.18796v1 | arXiv:2605.18796v1 §3 formulation; §4 calibrated uncertainty and threshold policy; §5 theory — calibrated correctness and cost jointly select a model cascade | arXiv:2605.18796v1 §6 Experiments and diagnostics | arXiv:2605.18796v1 §7 Discussion and Limitations | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-18796 | complete |
| SF-2026-ARXIV-2605-18803 | RP-fb6876e49931644e | deep | arXiv:2605.18803v1 | SRC-ARXIV@arXiv:2605.18803v1 | arXiv:2605.18803v1 §3 PROWL: asymmetric min-max objective, chunked diffusion forcing and adversarial curriculum — adversarial curriculum and prioritized failures change world-model training state | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Evaluation fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Evaluation, prioritized-failure and ablation sections | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Limitations discussion; world-model backbone, environments and regret proxy bound generality | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-18803 | complete |
| SF-2026-ARXIV-2605-18859 | RP-35caa4f2dad6931c | deep | arXiv:2605.18859v1 | SRC-ARXIV@arXiv:2605.18859v1 | https://arxiv.org/html/2605.18859v1 §3 TwinRouterBench Overview; §4 Dataset — mechanism boundary: LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls. | https://arxiv.org/html/2605.18859v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.18859v1 §7 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.18859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-18859 | complete |
| SF-2026-ARXIV-2605-18891 | RP-95ea8bc96626981c | deep | arXiv:2605.18891v1 | SRC-ARXIV@arXiv:2605.18891v1 | arXiv:2605.18891v1 — §3 Setup and the Bypass Metric (frozen exact-v1 official HTML receipt) | arXiv:2605.18891v1 — §4 Results (frozen exact-v1 official HTML receipt) | arXiv:2605.18891v1 — §5 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-g.txt#sha256=804cad573138683e86544b653813a5ca64961d7fe4c52ed742315b9a7f54ce63; exact-v1 URL=https://arxiv.org/html/2605.18891v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-18891 | complete |
| SF-2026-ARXIV-2605-18899 | RP-de7028b2b7ed378a | deep | arXiv:2605.18899v1 | SRC-ARXIV@arXiv:2605.18899v1 | arXiv:2605.18899v1 — §3 Anchored Bandit Policy Optimization (official exact-v1 HTML) | arXiv:2605.18899v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.18899v1 — Appendix E.4 Scope limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.18899v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-18899 | complete |
| SF-2026-ARXIV-2605-18918 | RP-92e4f3c42456da80 | deep | arXiv:2605.18918v1 | SRC-ARXIV@arXiv:2605.18918v1 | arXiv:2605.18918v1 HTML — §3 ESLD latent sensor architecture and external enforcement path | arXiv:2605.18918v1 HTML — §4 Experiments against prompt injection | arXiv:2605.18918v1 HTML — §5 Limitations; learned detector is not an authority | arXiv:2605.18918v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18918 | complete |
| SF-2026-ARXIV-2605-18930 | RP-0044fd324e10c1d9 | deep | arXiv:2605.18930v1 | SRC-ARXIV@arXiv:2605.18930v1 | arXiv:2605.18930v1 HTML — §3 threat model; §4.1–4.2 poisoning | arXiv:2605.18930v1 HTML — §5 mechanistic analysis; §6 evaluation | arXiv:2605.18930v1 HTML — §7 limitations | arXiv:2605.18930v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18930 | complete |
| SF-2026-ARXIV-2605-18991 | RP-4923f6156c159e4f | deep | arXiv:2605.18991v1 | SRC-ARXIV@arXiv:2605.18991v1 | arXiv:2605.18991v1 HTML — §2 system-level invariants, model-as-untrusted-component and attack analysis | arXiv:2605.18991v1 HTML — §3 open systems-security problems; no empirical mechanism evaluation | arXiv:2605.18991v1 HTML — §4 objections and position-paper boundary | arXiv:2605.18991v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18991 | complete |
| SF-2026-ARXIV-2605-19008 | RP-e156c3001ce0a6ba | deep | arXiv:2605.19008v1 | SRC-ARXIV@arXiv:2605.19008v1 | arXiv:2605.19008v1 HTML — §3 LBW-Guard bounded training-control layer, actions and safety envelope | arXiv:2605.19008v1 HTML — §4–§5 setup, stress runs and controller outcomes | arXiv:2605.19008v1 HTML — §6 Limitations; simulator/recipe and stability boundary | arXiv:2605.19008v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19008 | complete |
| SF-2026-ARXIV-2605-19049 | RP-153638f65b985ca9 | deep | arXiv:2605.19049v1 | SRC-ARXIV@arXiv:2605.19049v1 | arXiv:2605.19049v1 HTML — §3.1–§3.4 KVBuffer IO-aware state placement and update pipeline | arXiv:2605.19049v1 HTML — §4 Evaluation on linear-attention serving | arXiv:2605.19049v1 HTML — §6 Discussion/limitations; linear-attention state only | arXiv:2605.19049v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19049 | complete |
| SF-2026-ARXIV-2605-19099 | RP-ebae37d76cd708ea | deep | arXiv:2605.19099v1 | SRC-ARXIV@arXiv:2605.19099v1 | arXiv:2605.19099v1 HTML — §3 DecisionBench delegation substrate, interface and metrics | arXiv:2605.19099v1 HTML — §4 Experiments across peer pools and tasks | arXiv:2605.19099v1 HTML — §5 Limitations; benchmark delegation is not production authority | arXiv:2605.19099v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19099 | complete |
| SF-2026-ARXIV-2605-19101 | RP-8c36c0c8793720bd | deep | arXiv:2605.19101v1 | SRC-ARXIV@arXiv:2605.19101v1 | arXiv:2605.19101v1 HTML — §3–§4 GST heterogeneity state, scheduler and optimization rule | arXiv:2605.19101v1 HTML — §5 Experiments on Audio LLM training | arXiv:2605.19101v1 HTML — §6 Limitations; audio datasets and selected recipes | arXiv:2605.19101v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19101 | complete |
| SF-2026-ARXIV-2605-19127 | RP-037480cb13b63529 | deep | arXiv:2605.19127v1 | SRC-ARXIV@arXiv:2605.19127v1 | arXiv:2605.19127v1 HTML — §3.1–3.6 policy/attack/evaluation contract | arXiv:2605.19127v1 HTML — §4–§5 diagnostic surface | arXiv:2605.19127v1 HTML — §6 Limitations | arXiv:2605.19127v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19127 | complete |
| SF-2026-ARXIV-2605-19140 | RP-8a5d21f5abe58713 | deep | arXiv:2605.19140v1 | SRC-ARXIV@arXiv:2605.19140v1 | arXiv:2605.19140v1 HTML — §3–§4 local-observation handoff interface and convergent learning rule | arXiv:2605.19140v1 HTML — §5 theoretical/empirical evaluation | arXiv:2605.19140v1 HTML — §6 Limitations; assumptions do not prove open-system delivery or authority | arXiv:2605.19140v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19140 | complete |
| SF-2026-ARXIV-2605-19151 | RP-5aed86fc7416098f | deep | arXiv:2605.19151v1 | SRC-ARXIV@arXiv:2605.19151v1 | arXiv:2605.19151v1 HTML — §2–§3 approval/deny observations, GP preference posterior and autonomy threshold | arXiv:2605.19151v1 HTML — §3–§4 theoretical and simulated evaluation | arXiv:2605.19151v1 HTML — §4 Limitations; preference stationarity and calibration boundary | arXiv:2605.19151v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19151 | complete |
| SF-2026-ARXIV-2605-19169 | RP-40eb64e1b509dd01 | deep | arXiv:2605.19169v1 | SRC-ARXIV@arXiv:2605.19169v1 | arXiv:2605.19169v1 HTML — §2 Methods; latency/serialization model and ASTRA-sim overlap model | arXiv:2605.19169v1 HTML — §3 Results; GPT-3 13B/175B, A100/H100, 256–8192 GPU simulation | arXiv:2605.19169v1 HTML — §4 Conclusions; lumped two-DC, uncongested-network and simulation-only boundary | arXiv:2605.19169v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19169 | complete |
| SF-2026-ARXIV-2605-19192 | RP-674c2cb06c4707c0 | deep | arXiv:2605.19192v1 | SRC-ARXIV@arXiv:2605.19192v1 | arXiv:2605.19192v1 HTML — §3–§4 evidence certificate and action-admission architecture | arXiv:2605.19192v1 HTML — §5 Evaluation under multimodal hallucination-to-action attacks | arXiv:2605.19192v1 HTML — §6 Limitations; certificate coverage and evaluator trust | arXiv:2605.19192v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19192 | complete |
| SF-2026-ARXIV-2605-19193 | RP-0ac837392fe4f247 | deep | arXiv:2605.19193v1 | SRC-ARXIV@arXiv:2605.19193v1 | arXiv:2605.19193v1 HTML — §III–V sequential stopping and calibration | arXiv:2605.19193v1 HTML — §VI simulation; §VII real-LLM study | arXiv:2605.19193v1 HTML — §V-E i.i.d. violations; §VIII discussion | arXiv:2605.19193v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19193 | complete |
| SF-2026-ARXIV-2605-19196 | RP-a0a24df6793a2acd | deep | arXiv:2605.19196v1 | SRC-ARXIV@arXiv:2605.19196v1 | arXiv:2605.19196v1 HTML — §2.1–2.2 controlled-intervention benchmark | arXiv:2605.19196v1 HTML — §3.1–3.5 judge meta-evaluation | arXiv:2605.19196v1 HTML — §4 related work; §5 conclusion | arXiv:2605.19196v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19196 | complete |
| SF-2026-ARXIV-2605-19218 | RP-71652ae2e632c2a7 | deep | arXiv:2605.19218v1 | SRC-ARXIV@arXiv:2605.19218v1 | arXiv:2605.19218v1 HTML — §3.1–§3.3 RotateK query-weighted PCA, structured channel pruning and Triton kernel | arXiv:2605.19218v1 HTML — §4 Experiments; matched KV budgets, prefill/decode latency and memory | arXiv:2605.19218v1 HTML — Appendix G Limitations | arXiv:2605.19218v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19218 | complete |
| SF-2026-ARXIV-2605-19228 | RP-822c0c4354bc34dc | deep | arXiv:2605.19228v1 | SRC-ARXIV@arXiv:2605.19228v1 | arXiv:2605.19228v1 HTML — §3 problem; §4.1–4.3 step confidence | arXiv:2605.19228v1 HTML — §5 experiments | arXiv:2605.19228v1 HTML — §6 limitations | arXiv:2605.19228v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19228 | complete |
| SF-2026-ARXIV-2605-19240 | RP-4de7916633823656 | deep | arXiv:2605.19240v1 | SRC-ARXIV@arXiv:2605.19240v1 | arXiv:2605.19240v1 HTML — §4.1–4.4 causal cross-channel monitoring | arXiv:2605.19240v1 HTML — §5 detection and attribution evaluation | arXiv:2605.19240v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19240v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19240 | complete |
| SF-2026-ARXIV-2605-19242 | RP-bc66eb851cc20588 | deep | arXiv:2605.19242v1 | SRC-ARXIV@arXiv:2605.19242v1 | arXiv:2605.19242v1 HTML — §3 physics-faithful data and objective | arXiv:2605.19242v1 HTML — §4 controlled video/world-model evaluation | arXiv:2605.19242v1 HTML — §5 Conclusion and inherited generator biases | https://arxiv.org/html/2605.19242v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19242 | complete |
| SF-2026-ARXIV-2605-19262 | RP-5a772c65a8c3c199 | deep | arXiv:2605.19262v1 | SRC-ARXIV@arXiv:2605.19262v1 | arXiv:2605.19262v1 HTML — §4 masked-diffusion backdoor construction | arXiv:2605.19262v1 HTML — §5 attack and defense experiments | arXiv:2605.19262v1 HTML — Appendix A Limitations | https://arxiv.org/html/2605.19262v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19262 | complete |
| SF-2026-ARXIV-2605-19269 | RP-c96f6605cb2f6e46 | deep | arXiv:2605.19269v1 | SRC-ARXIV@arXiv:2605.19269v1 | arXiv:2605.19269v1 HTML — §3 GEMM-epilogue program representation | arXiv:2605.19269v1 HTML — §4 kernel and end-to-end evaluation | arXiv:2605.19269v1 HTML — §5 limitations and portability boundary | https://arxiv.org/html/2605.19269v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19269 | complete |
| SF-2026-ARXIV-2605-19276 | RP-bbd40a725e79e647 | deep | arXiv:2605.19276v1 | SRC-ARXIV@arXiv:2605.19276v1 | arXiv:2605.19276v1 HTML — §3.1–3.5 evaluation-platform architecture | arXiv:2605.19276v1 HTML — §4 benchmark execution and comparison | arXiv:2605.19276v1 HTML — §5 Future Works | https://arxiv.org/html/2605.19276v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19276 | complete |
| SF-2026-ARXIV-2605-19282 | RP-2a2084963c482440 | deep | arXiv:2605.19282v1 | SRC-ARXIV@arXiv:2605.19282v1 | arXiv:2605.19282v1 HTML — §3 spectral failure analysis; §4 high-pass remedy | arXiv:2605.19282v1 HTML — §5 VLA/RLVR optimization experiments | arXiv:2605.19282v1 HTML — Appendix M Limitations | https://arxiv.org/html/2605.19282v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19282 | complete |
| SF-2026-ARXIV-2605-19314 | RP-2cbc2c4c9f3e9bf9 | deep | arXiv:2605.19314v1 | SRC-ARXIV@arXiv:2605.19314v1 | arXiv:2605.19314v1 HTML — §3 hierarchical task-state alignment | arXiv:2605.19314v1 HTML — §4.1–4.4 long-horizon embodied evaluation | arXiv:2605.19314v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19314v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19314 | complete |
| SF-2026-ARXIV-2605-19319 | RP-5e77ad5261b0bf4f | deep | arXiv:2605.19319v1 | SRC-ARXIV@arXiv:2605.19319v1 | arXiv:2605.19319v1 HTML — §3 sparse keyframe world-model planner and goal-conditioned action predictor | arXiv:2605.19319v1 HTML — §4 real-robot and simulation experiments | arXiv:2605.19319v1 HTML — §5 Limitations: short horizon, annotations and edited-image domain gap | https://arxiv.org/html/2605.19319v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19319 | complete |
| SF-2026-ARXIV-2605-19321 | RP-d33cdabd99e9957c | deep | arXiv:2605.19321v1 | SRC-ARXIV@arXiv:2605.19321v1 | arXiv:2605.19321v1 HTML — §3 draft-model pre-guard design | arXiv:2605.19321v1 HTML — §6 jailbreak and latency evaluation | arXiv:2605.19321v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19321v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19321 | complete |
| SF-2026-ARXIV-2605-19328 | RP-a5c0a05c1cd5ca31 | deep | arXiv:2605.19328v1 | SRC-ARXIV@arXiv:2605.19328v1 | arXiv:2605.19328v1 HTML — §3 embodied-agent threat and benchmark protocol | arXiv:2605.19328v1 HTML — §4 attacks and defenses | arXiv:2605.19328v1 HTML — §5 Limitations | https://arxiv.org/html/2605.19328v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19328 | complete |
| SF-2026-ARXIV-2605-19335 | RP-4d11184eb7d065fd | deep | arXiv:2605.19335v1 | SRC-ARXIV@arXiv:2605.19335v1 | arXiv:2605.19335v1 HTML — §4 LIOS update decomposition, overrun-bounded budgeting and feedback control | arXiv:2605.19335v1 HTML — §6 search/update evaluation on FreshDiskANN and OdinANN | arXiv:2605.19335v1 HTML — §8 Conclusion; disk ANNS and measured hardware scope | https://arxiv.org/html/2605.19335v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19335 | complete |
| SF-2026-ARXIV-2605-19341 | RP-38bfb8462e1788ff | deep | arXiv:2605.19341v1 | SRC-ARXIV@arXiv:2605.19341v1 | arXiv:2605.19341v1 HTML — §3.1–3.3 controlled reference-world benchmark | arXiv:2605.19341v1 HTML — §4 cross-context hallucination experiments | arXiv:2605.19341v1 HTML — §5 Discussion; controlled-world boundary | https://arxiv.org/html/2605.19341v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19341 | complete |
| SF-2026-ARXIV-2605-19373 | RP-100563ab07b862d8 | deep | arXiv:2605.19373v1 | SRC-ARXIV@arXiv:2605.19373v1 | section 4 The Solution: Two-Layer Architecture (§4 The Solution: Two-Layer Architecture) | section 3.1 Formal Analysis of CRDT Property Violations (§3.1 Formal Analysis of CRDT Property Violations) | section 7 Discussion (§7 Discussion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.19373v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-19373 | complete |
| SF-2026-ARXIV-2605-19407 | RP-231b13021875ae63 | deep | arXiv:2605.19407v1 | SRC-ARXIV@arXiv:2605.19407v1 | arXiv:2605.19407v1 HTML — §3–§6 compute/data/filter scaling design | arXiv:2605.19407v1 HTML — §6–§7 scaling experiments | arXiv:2605.19407v1 HTML — §8 Discussion and scope boundary | https://arxiv.org/html/2605.19407v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19407 | complete |
| SF-2026-ARXIV-2605-19444 | RP-e2adfa9f6bdc8469 | deep | arXiv:2605.19444v1 | SRC-ARXIV@arXiv:2605.19444v1 | arXiv:2605.19444v1 HTML — §2 extinction-window dynamics; §3 TTRL-Guard | arXiv:2605.19444v1 HTML — §4 model/benchmark experiments and per-problem migration | arXiv:2605.19444v1 HTML — §6 Breadth of evaluation; signal quality at the extremes | https://arxiv.org/html/2605.19444v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19444 | complete |
| SF-2026-ARXIV-2605-19447 | RP-79adcf64a80e6d6d | deep | arXiv:2605.19447v1 | SRC-ARXIV@arXiv:2605.19447v1 | arXiv:2605.19447v1 HTML — §3 selective hindsight placement and environment-guided advantage reweighting | arXiv:2605.19447v1 HTML — §4 ALFWorld/WebShop experiments and ablations | arXiv:2605.19447v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.19447v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19447 | complete |
| SF-2026-ARXIV-2605-19461 | RP-487abf8826107f40 | deep | arXiv:2605.19461v1 | SRC-ARXIV@arXiv:2605.19461v1 | arXiv:2605.19461v1 HTML — §3 forward/group distribution-matching policy optimization | arXiv:2605.19461v1 HTML — §4–§5 reasoning experiments and ablations | arXiv:2605.19461v1 HTML — Appendix B Limitations; group-local coverage does not prove global target matching | https://arxiv.org/html/2605.19461v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19461 | complete |
| SF-2026-ARXIV-2605-19478 | RP-364a9e53a3f33227 | deep | arXiv:2605.19478v1 | SRC-ARXIV@arXiv:2605.19478v1 | arXiv:2605.19478v1 HTML — §4 threat model; §5–§6 dynamic-prompt functional fusion | arXiv:2605.19478v1 HTML — §7 attack, pruning and transfer evaluation | arXiv:2605.19478v1 HTML — §8 Conclusion; ViT/VPT threat-model boundary | https://arxiv.org/html/2605.19478v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19478 | complete |
| SF-2026-ARXIV-2605-19481 | RP-c5cf1a54d2cf261f | deep | arXiv:2605.19481v1 | SRC-ARXIV@arXiv:2605.19481v1 | arXiv:2605.19481v1 HTML — §III–V C2C weight/state movement design | arXiv:2605.19481v1 HTML — §VI MIG/serverless serving evaluation | arXiv:2605.19481v1 HTML — §VII Conclusion and hardware boundary | https://arxiv.org/html/2605.19481v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19481 | complete |
| SF-2026-ARXIV-2605-19537 | RP-7c3307e883eee92e | deep | arXiv:2605.19537v1 | SRC-ARXIV@arXiv:2605.19537v1 | arXiv:2605.19537v1 HTML — §3 backend-reproducibility protocol | arXiv:2605.19537v1 HTML — §4 backend/model benchmark deltas | arXiv:2605.19537v1 HTML — §5 Discussion and reproducibility boundary | https://arxiv.org/html/2605.19537v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19537 | complete |
| SF-2026-ARXIV-2605-19576 | RP-a9ccb737bed9e193 | deep | arXiv:2605.19576v1 | SRC-ARXIV@arXiv:2605.19576v1 | arXiv:2605.19576v1 HTML — §3–§5 lifecycle-managed skill library | arXiv:2605.19576v1 HTML — §6 library-drift evaluation | arXiv:2605.19576v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19576v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19576 | complete |
| SF-2026-ARXIV-2605-19593 | RP-0f47708fa3dff185 | deep | arXiv:2605.19593v1 | SRC-ARXIV@arXiv:2605.19593v1 | arXiv:2605.19593v1 HTML — §3 multi-model offload/preemption methodology | arXiv:2605.19593v1 HTML — §4–§5 heterogeneous-serving measurements | arXiv:2605.19593v1 HTML — §6 Conclusion; interconnect and hardware constraints | https://arxiv.org/html/2605.19593v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19593 | complete |
| SF-2026-ARXIV-2605-19604 | RP-fccbad05e0667a78 | deep | arXiv:2605.19604v1 | SRC-ARXIV@arXiv:2605.19604v1 | arXiv:2605.19604v1 HTML — §3 programmable runtime skill contract | arXiv:2605.19604v1 HTML — §4 execution and accuracy evaluation | arXiv:2605.19604v1 HTML — §5 Conclusion; language/runtime boundary | https://arxiv.org/html/2605.19604v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19604 | complete |
| SF-2026-ARXIV-2605-19722 | RP-5fd2a3cffdd101d8 | deep | arXiv:2605.19722v1 | SRC-ARXIV@arXiv:2605.19722v1 | arXiv:2605.19722v1 HTML — §3 trace-based autonomous security-agent protocol | arXiv:2605.19722v1 HTML — §4–§5 sandbox/tool-use evaluation | arXiv:2605.19722v1 HTML — §6 Limitations | https://arxiv.org/html/2605.19722v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19722 | complete |
| SF-2026-ARXIV-2605-19755 | RP-6c6c2fd691379eb4 | deep | arXiv:2605.19755v1 | SRC-ARXIV@arXiv:2605.19755v1 | https://arxiv.org/html/2605.19755v1#S2 | https://arxiv.org/html/2605.19755v1#S4 | https://arxiv.org/html/2605.19755v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-19755 | complete |
| SF-2026-ARXIV-2605-19769 | RP-abeedde730e8f1d5 | deep | arXiv:2605.19769v1 | SRC-ARXIV@arXiv:2605.19769v1 | arXiv:2605.19769v1 HTML — §2–§3 verifier-grounded software worlds | arXiv:2605.19769v1 HTML — §4.1 computer-use agent evaluation | arXiv:2605.19769v1 HTML — § unnumbered exact heading ‘Limitations and Future Work’ | https://arxiv.org/html/2605.19769v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19769 | complete |
| SF-2026-ARXIV-2605-19775 | RP-cb624bce171b6667 | deep | arXiv:2605.19775v1 | SRC-ARXIV@arXiv:2605.19775v1 | arXiv:2605.19775v1 HTML — §2–§3 inference-scaling model | arXiv:2605.19775v1 HTML — §4–§5 reasoning-workload measurements | arXiv:2605.19775v1 HTML — §6 Conclusions and disclosed scope | https://arxiv.org/html/2605.19775v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19775 | complete |
| SF-2026-ARXIV-2605-19779 | RP-9170e3bce78cea00 | deep | arXiv:2605.19779v1 | SRC-ARXIV@arXiv:2605.19779v1 | arXiv:2605.19779v1 HTML — §2–§3 conformal continuous-agent UQ | arXiv:2605.19779v1 HTML — §4 longitudinal agent studies | arXiv:2605.19779v1 HTML — §5 Limitations: bounded shift and dependence | https://arxiv.org/html/2605.19779v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19779 | complete |
| SF-2026-ARXIV-2605-19811 | RP-73b18d970281f078 | deep | arXiv:2605.19811v1 | SRC-ARXIV@arXiv:2605.19811v1 | arXiv:2605.19811v1 HTML — §3 optimizer geometry; §4 LionMuon alternating spectral/sign descent | arXiv:2605.19811v1 HTML — §5 language-model training experiments and ablations | arXiv:2605.19811v1 HTML — §6 Limitations and optimizer/workload boundary | https://arxiv.org/html/2605.19811v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19811 | complete |
| SF-2026-ARXIV-2605-19847 | RP-1aad2db51346f336 | deep | arXiv:2605.19847v1 | SRC-ARXIV@arXiv:2605.19847v1 | arXiv:2605.19847v1 HTML — §2–§3 collusion threat model and tenant accounting | arXiv:2605.19847v1 HTML — §4 privacy audit; §5 protocol | arXiv:2605.19847v1 HTML — §7.1 Limitations: retrieval only, not generation | https://arxiv.org/html/2605.19847v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19847 | complete |
| SF-2026-ARXIV-2605-19893 | RP-443e8b0329a419a2 | deep | arXiv:2605.19893v1 | SRC-ARXIV@arXiv:2605.19893v1 | arXiv:2605.19893v1 HTML — §3–§4 sparse speculative verification | arXiv:2605.19893v1 HTML — §5 long-context evaluation | arXiv:2605.19893v1 HTML — §6 Conclusion and sparse-attention boundary | https://arxiv.org/html/2605.19893v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19893 | complete |
| SF-2026-ARXIV-2605-19932 | RP-26b2069b16f34d38 | deep | arXiv:2605.19932v1 | SRC-ARXIV@arXiv:2605.19932v1 | arXiv:2605.19932v1 HTML — §3 orientation-cache representation | arXiv:2605.19932v1 HTML — §4 recurring-context agent evaluation | arXiv:2605.19932v1 HTML — §5 Limitations | https://arxiv.org/html/2605.19932v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19932 | complete |
| SF-2026-ARXIV-2605-19945 | RP-3896ccf40dc4ab6d | deep | arXiv:2605.19945v1 | SRC-ARXIV@arXiv:2605.19945v1 | arXiv:2605.19945v1 HTML — §3–§4 variability-aware expert placement | arXiv:2605.19945v1 HTML — §5 heterogeneous-GPU evaluation | arXiv:2605.19945v1 HTML — §6 Limitations | https://arxiv.org/html/2605.19945v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19945 | complete |
| SF-2026-ARXIV-2605-19952 | RP-a53c47202f099e7a | deep | arXiv:2605.19952v1 | SRC-ARXIV@arXiv:2605.19952v1 | arXiv:2605.19952v1 HTML — §3 trace/chunk memory representation | arXiv:2605.19952v1 HTML — §4 lifelong-memory evaluation | arXiv:2605.19952v1 HTML — Appendix C.1 Limitations | https://arxiv.org/html/2605.19952v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19952 | complete |
| SF-2026-ARXIV-2605-19999 | RP-f5326dc8eaa49252 | deep | arXiv:2605.19999v1 | SRC-ARXIV@arXiv:2605.19999v1 | arXiv:2605.19999v1 HTML — §3–§4 contamination-resistant benchmark construction | arXiv:2605.19999v1 HTML — §5 benchmark analysis | arXiv:2605.19999v1 HTML — § unnumbered exact heading ‘Limitations’: contamination detection and task scope | https://arxiv.org/html/2605.19999v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19999 | complete |
| SF-2026-ARXIV-2605-20005 | RP-11cbff9a3b48da86 | deep | arXiv:2605.20005v1 | SRC-ARXIV@arXiv:2605.20005v1 | arXiv:2605.20005v1 HTML — §3 per-step forgetting bound and loss-adaptive learning rate | arXiv:2605.20005v1 HTML — §4–§5 task/forgetting, factuality and calibration experiments | arXiv:2605.20005v1 HTML — §6 Conclusion, Limitations, and Future Work | https://arxiv.org/html/2605.20005v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20005 | complete |
| SF-2026-ARXIV-2605-20022 | RP-8ea859d9af48ceee | deep | arXiv:2605.20022v1 | SRC-ARXIV@arXiv:2605.20022v1 | arXiv:2605.20022v1 HTML — §3–§4 asynchronous flexible drafting | arXiv:2605.20022v1 HTML — §5 end-to-end evaluation | arXiv:2605.20022v1 HTML — §6 Conclusion: bonus-token and accepted-length uncertainty | https://arxiv.org/html/2605.20022v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20022 | complete |
| SF-2026-ARXIV-2605-20023 | RP-bf3892f84b15bf42 | deep | arXiv:2605.20023v1 | SRC-ARXIV@arXiv:2605.20023v1 | arXiv:2605.20023v1 HTML — §3 procedural-skill intervention and tool-grounded agent protocol | arXiv:2605.20023v1 HTML — §4 offensive-cybersecurity experiments | arXiv:2605.20023v1 HTML — §5 Limitations; negative result is workload/model specific | https://arxiv.org/html/2605.20023v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20023 | complete |
| SF-2026-ARXIV-2605-20051 | RP-6480603c921c3a94 | deep | arXiv:2605.20051v1 | SRC-ARXIV@arXiv:2605.20051v1 | arXiv:2605.20051v1 HTML — §3–§4 reference-driven variant detection | arXiv:2605.20051v1 HTML — §5 AI-infra repository measurement | arXiv:2605.20051v1 HTML — §6 Discussion and false-positive boundary | https://arxiv.org/html/2605.20051v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20051 | complete |
| SF-2026-ARXIV-2605-20061 | RP-0d3da93c05663e30 | deep | arXiv:2605.20061v1 | SRC-ARXIV@arXiv:2605.20061v1 | arXiv:2605.20061v1 HTML — §3 belief-consistency credit assignment | arXiv:2605.20061v1 HTML — §4 long-horizon agent evaluation | arXiv:2605.20061v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.20061v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20061 | complete |
| SF-2026-ARXIV-2605-20084 | RP-d18ad7b1d473540d | deep | arXiv:2605.20084v1 | SRC-ARXIV@arXiv:2605.20084v1 | arXiv:2605.20084v1 HTML — §3–§4 joint escalation/abstention calibration | arXiv:2605.20084v1 HTML — §5 cascaded-RAG evaluation | arXiv:2605.20084v1 HTML — § unnumbered exact heading ‘Limitations’: distribution shift and calibration | https://arxiv.org/html/2605.20084v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20084 | complete |
| SF-2026-ARXIV-2605-20179 | RP-ac18ffca87654a07 | deep | arXiv:2605.20179v1 | SRC-ARXIV@arXiv:2605.20179v1 | arXiv:2605.20179v1 HTML — §3 I/O-aware MoE expert-offload design | arXiv:2605.20179v1 HTML — §4 LLaDA2.0 experiments | arXiv:2605.20179v1 HTML — §5 Conclusion: block-only activation and limited hardware | https://arxiv.org/html/2605.20179v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20179 | complete |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | RP-9554d51c20273802 | deep | arXiv:2605.18815v1 | SRC-ARXIV@arXiv:2605.18815v1 | arXiv:2605.18815v1 HTML — §3 DynaTrain elastic parallelism transition controller | arXiv:2605.18815v1 — §4 distributed-training evaluation | arXiv:2605.18815v1 — §5 limitations: topology, transition cost and failure scope | arXiv:2605.18815v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | complete |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | RP-04fc7c27ca53f7fa | deep | arXiv:2605.18854v1 | SRC-ARXIV@arXiv:2605.18854v1 | arXiv:2605.18854v1 HTML — §2 Memory Condensation Strategies | arXiv:2605.18854v1 HTML — §3 Experimental Setup and §4 Results — 480 DiscoveryBench evaluations | arXiv:2605.18854v1 HTML — §5 Discussion / Conclusion — GPT-4o, six-domain and task-length boundary | arXiv:2605.18854v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | complete |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | RP-a0cc23ba143ecd7e | deep | arXiv:2605.18824v1 | SRC-ARXIV@arXiv:2605.18824v1 | arXiv:2605.18824v1 HTML — §3 multi-agent benchmark generation and solution-graph ground-truth pipeline | arXiv:2605.18824v1 — §4 expert review and twelve-model evaluation | arXiv:2605.18824v1 — §6 Conclusion — limitations include multiple-choice scope, frontier-model generator/verifier dependence and nonzero residual error | arXiv:2605.18824v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | complete |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | RP-cbf851c4d19fe35e | deep | arXiv:2605.18814v1 | SRC-ARXIV@arXiv:2605.18814v1 | arXiv:2605.18814v1 HTML — §3 trajectory-data attribution estimator | arXiv:2605.18814v1 — §4 attribution experiments | arXiv:2605.18814v1 — §5 limitations: causal identifiability and data coverage | arXiv:2605.18814v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | complete |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | RP-be39b4b74377b92f | deep | arXiv:2605.18853v1 | SRC-ARXIV@arXiv:2605.18853v1 | arXiv:2605.18853v1 HTML — §Method / System Design — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的机制、状态 owner 与控制/数据流 | arXiv:2605.18853v1 HTML — §Experiments / Evaluation — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的作者披露 workload、baseline 与 ablation | arXiv:2605.18853v1 HTML — §Limitations / Discussion — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的适用范围、未证明项与 failure boundary | arXiv:2605.18853v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | complete |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | RP-87243552d8690f7f | deep | arXiv:2605.18825v1 | SRC-ARXIV@arXiv:2605.18825v1 | arXiv:2605.18825v1 HTML — §3 semantic prefix-cache eviction policy | arXiv:2605.18825v1 — §4 serving evaluation | arXiv:2605.18825v1 — §5 limitations: semantic estimator, workload and cache budget | arXiv:2605.18825v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | complete |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | RP-1adc08455070fb87 | deep | arXiv:2605.18812v1 | SRC-ARXIV@arXiv:2605.18812v1 | arXiv:2605.18812v1 HTML — §3 PASC pipeline-conformal evidence contract | arXiv:2605.18812v1 — §4 calibration/evaluation experiments | arXiv:2605.18812v1 — §5 limitations: exchangeability and pipeline shift | arXiv:2605.18812v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | complete |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | RP-e5c082087faf9b76 | deep | arXiv:2605.18852v1 | SRC-ARXIV@arXiv:2605.18852v1 | arXiv:2605.18852v1 HTML — §Method / System Design — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的机制、状态 owner 与控制/数据流 | arXiv:2605.18852v1 HTML — §Experiments / Evaluation — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的作者披露 workload、baseline 与 ablation | arXiv:2605.18852v1 HTML — §Limitations / Discussion — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的适用范围、未证明项与 failure boundary | arXiv:2605.18852v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | complete |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | RP-b75ae65aa7c08ba3 | deep | arXiv:2605.18856v1 | SRC-ARXIV@arXiv:2605.18856v1 | arXiv:2605.18856v1 HTML — §Method / System Design — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的机制、状态 owner 与控制/数据流 | arXiv:2605.18856v1 HTML — §Experiments / Evaluation — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的作者披露 workload、baseline 与 ablation | arXiv:2605.18856v1 HTML — §Limitations / Discussion — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的适用范围、未证明项与 failure boundary | arXiv:2605.18856v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-18755:start -->
#### Operational Memory Architecture for Kubernetes:Preserving Causal Context Across the Evidence Horizon

<!-- claim:SF-2026-ARXIV-2605-18755:start -->
- **Problem:** Kubernetes clusters generate rich operational events during pod lifecycle transitions, yet the platform's native event retention model discards the most diagnostically valuable context.
- **Old path / changed constraint:** Kubernetes 原生 Pod 状态和 Event 在 kubelet 重启轮转后只保留当前快照；当 LastTerminationState 被新一次终止覆盖、对象又被删除时，故障因果链跨过 evidence horizon 后无法由 kubectl 恢复。Metrics、logs 与 traces 各自保留观测，但不自动保存同一对象的时点快照与因果边。
- **Mechanism / ownership:** We propose OMA, a four-layer framework positioning operational memory as an architectural primitive alongside metrics, logs, and traces in the Kubernetes observability stack (Section IV).
- **Evaluation contract:** Experiments on Minikube and AKS include a 30-run latency analysis and stress tests with up to 20 crash-looping pods.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 当前 collector 仅 namespace-scoped；生产化需要 cluster-wide RBAC 或多 namespace 实例，且 ConfigMap watch 涉及敏感配置，论文默认只保存 metadata 与 content hash。SQLite 只适合单集群，跨集群需要分布式存储与查询联邦。30 次统计实验来自 Apple M-series 上的 Minikube，AKS 仅单次；NodeMemoryPressure→OOMKill 边未被观察到，因此不能外推到不同 runtime、硬件、kubelet 配置或大规模生产集群。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.18755v1](https://arxiv.org/abs/2605.18755v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.18755v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-18755:end -->
<!-- review:SF-2026-ARXIV-2605-18755:end -->

<!-- review:SF-2026-ARXIV-2605-18762:start -->
#### ALDEN: Boosting Private Data Extraction from Retrieval-Augmented Generation Systems via Active Learning and Distribution Estimation

<!-- claim:SF-2026-ARXIV-2605-18762:start -->
- **Problem:** Retrieval-Augmented Generation (RAG) is widely used to augment large language models with external knowledge retrieval to improve reliability and generalization.
- **Old path / changed constraint:** However, recent studies have shown that RAG systems remain vulnerable to data extraction attacks, where adversaries can extract private data by embedding malicious commands into user queries.
- **Mechanism / ownership:** Here, we propose ALDEN, a novel attack that effectively and efficiently extracts private data from RAGs.
- **Evaluation contract:** By combining them together, we demonstrate that ALDEN substantially outperforms state-of-the-art methods through comprehensive evaluations.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** To address these limitations, Retrieval-Augmented Generation (RAG) has emerged as a practical solution to improve LLM reliability by incorporating externally retrieved knowledge into the input context Shi et al.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.18762v1](https://arxiv.org/abs/2605.18762v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.18762v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-18762:end -->
<!-- review:SF-2026-ARXIV-2605-18762:end -->

<!-- review:SF-2026-ARXIV-2605-18792:start -->
#### Trust or Abstain? A Self-Aware RAG Approach

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`AGENT-RAG`。
Method / identity：arXiv:2605.18792v1 §2 knowledge-conflict benchmark; §3 self-prior, conditional belief estimation and abstention — parametric and contextual knowledge beliefs govern retrieval and abstention。
Evaluation：arXiv:2605.18792v1 §4 Experiments, selective answering and ablations。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18792v1 No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-18792:start -->The exact-v1 body supports the mechanism under §4 Experiments, selective answering and ablations. Counterevidence/scope was checked at No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims. It does not prove that “Trust or Abstain? A Self-Aware RAG Approach” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-18792:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-18792:end -->

<!-- review:SF-2026-ARXIV-2605-18796:start -->
#### UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`INFER-SCHEDULING`。
Method / identity：arXiv:2605.18796v1 §3 formulation; §4 calibrated uncertainty and threshold policy; §5 theory — calibrated correctness and cost jointly select a model cascade。
Evaluation：arXiv:2605.18796v1 §6 Experiments and diagnostics。
Counterevidence / limitations：arXiv:2605.18796v1 §7 Discussion and Limitations。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-18796:start -->The exact-v1 body supports the mechanism under §6 Experiments and diagnostics. Counterevidence/scope was checked at §7 Discussion and Limitations. It does not prove that “UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-18796:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-18796:end -->

<!-- review:SF-2026-ARXIV-2605-18803:start -->
#### PROWL: Prioritized Regret-Driven Optimization for World Model Learning

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`MULTIMODAL-WORLD-MODELS`。
Method / identity：arXiv:2605.18803v1 §3 PROWL: asymmetric min-max objective, chunked diffusion forcing and adversarial curriculum — adversarial curriculum and prioritized failures change world-model training state。
Evaluation：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Evaluation fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Evaluation, prioritized-failure and ablation sections。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Limitations discussion; world-model backbone, environments and regret proxy bound generality。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-18803:start -->The exact-v1 body supports the mechanism under Evaluation, prioritized-failure and ablation sections. Counterevidence/scope was checked at Limitations discussion; world-model backbone, environments and regret proxy bound generality. It does not prove that “PROWL: Prioritized Regret-Driven Optimization for World Model Learning” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-18803:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-18803:end -->

<!-- review:SF-2026-ARXIV-2605-18859:start -->
#### TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing

问题与演进：Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.18859v1 §3 TwinRouterBench Overview; §4 Dataset — mechanism boundary: LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls.`。

Evaluation：`https://arxiv.org/html/2605.18859v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.18859v1 §7 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.18859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-18859:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-18859:end -->
<!-- review:SF-2026-ARXIV-2605-18859:end -->

<!-- review:SF-2026-ARXIV-2605-18891:start -->
#### Auditing Reasoning-Trace Memorization Claims after Unlearning with Head-Conditioned Canaries

问题与 changed constraint：reasoning-trace bypass gap 可能由 prefill/parser/format 造成，不能直接证明 weights 仍记忆；unlearning evaluation 必须冻结 parser、prompt head、seed 与 intervention identity。

机制与 ownership：Evaluations of unlearning on reasoning models sometimes show a bypass pattern. owner=`TRAIN-DATA`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.18891v1 — §3 Setup and the Bypass Metric (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.18891v1 — §4 Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.18891v1 — §5 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-18891:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-18891:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-18891:end -->

<!-- review:SF-2026-ARXIV-2605-18899:start -->
#### Don't Let Bandit Feedback Pull Continual LLM-Recommender Updates Off Target

问题与 changed constraint：continual policy updates bind logged-action propensity and ambiguous no-response feedback to the serving-policy revision

机制与 ownership：We propose an Anchored Bandit Policy Optimization (ABPO) framework for continual LLM-Rec updates that combines group-relative policy optimization (GRPO) with explicit treatment of exposure bias and feedback ambiguity. owner=`TRAIN-GRPO`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.18899v1 — §3 Anchored Bandit Policy Optimization (official exact-v1 HTML)`；Evaluation=`arXiv:2605.18899v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.18899v1 — Appendix E.4 Scope limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-18899:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-18899:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-18899:end -->

<!-- review:SF-2026-ARXIV-2605-18918:start -->
#### ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense

**问题与机制。** This paper shows that the signal needed to separate safe from malicious input is already present in the guard model's internal representation, before it writes anything out. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 ESLD latent sensor architecture and external enforcement path`；Evaluation=`§4 Experiments against prompt injection`；Limitations/Counterevidence=`§5 Limitations; learned detector is not an authority`。

<!-- claim:SF-2026-ARXIV-2605-18918:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18918:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18918:end -->

<!-- review:SF-2026-ARXIV-2605-18930:start -->
#### OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences

**问题与机制。** Memory-augmented large language model (LLM) agents use iterative reflection and self-evolution to solve complex tasks, but these mechanisms introduce security risks. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 threat model; §4.1–4.2 poisoning`；Evaluation=`§5 mechanistic analysis; §6 evaluation`；Limitations/Counterevidence=`§7 limitations`。

<!-- claim:SF-2026-ARXIV-2605-18930:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18930:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18930:end -->

<!-- review:SF-2026-ARXIV-2605-18991:start -->
#### Agent Security is a Systems Problem

**问题与机制。** We also identify the research challenges that stand in the way of implementing these principles in agents. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 system-level invariants, model-as-untrusted-component and attack analysis`；Evaluation=`§3 open systems-security problems; no empirical mechanism evaluation`；Limitations/Counterevidence=`§4 objections and position-paper boundary`。

<!-- claim:SF-2026-ARXIV-2605-18991:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18991:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18991:end -->

<!-- review:SF-2026-ARXIV-2605-19008:start -->
#### Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under Stress for Stability and Efficiency

**问题与机制。** Modern language-model training is increasingly exposed to instability, degraded runs, and wasted compute, especially under aggressive learning-rate, scale, and runtime-stress conditions. 该 family 改变或挑战 `TRAIN-PRETRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 LBW-Guard bounded training-control layer, actions and safety envelope`；Evaluation=`§4–§5 setup, stress runs and controller outcomes`；Limitations/Counterevidence=`§6 Limitations; simulator/recipe and stability boundary`。

<!-- claim:SF-2026-ARXIV-2605-19008:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19008:end -->

**Books Comparison。** 当前 pretraining 章有 optimizer/clip/rollback，尚缺 optimizer 之上的 bounded autonomous control envelope、action budget 与 human override；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19008:end -->

<!-- review:SF-2026-ARXIV-2605-19049:start -->
#### KVBuffer: IO-aware Serving for Linear Attention

**问题与机制。** In this paper, we propose KVBuffer, an IO-aware serving mechanism for linear attention. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–§3.4 KVBuffer IO-aware state placement and update pipeline`；Evaluation=`§4 Evaluation on linear-attention serving`；Limitations/Counterevidence=`§6 Discussion/limitations; linear-attention state only`。

<!-- claim:SF-2026-ARXIV-2605-19049:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19049:end -->

**Books Comparison。** 当前 KV 章以 Transformer KV 为主，没有明确 linear-attention recurrent state 的 IO-aware buffering/placement owner；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19049:end -->

<!-- review:SF-2026-ARXIV-2605-19099:start -->
#### DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows

**问题与机制。** We introduce DecisionBench, a benchmark substrate for emergent delegation in long-horizon agentic workflows. 该 family 改变或挑战 `AGENT-MULTI-AGENT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 DecisionBench delegation substrate, interface and metrics`；Evaluation=`§4 Experiments across peer pools and tasks`；Limitations/Counterevidence=`§5 Limitations; benchmark delegation is not production authority`。

<!-- claim:SF-2026-ARXIV-2605-19099:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19099:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19099:end -->

<!-- review:SF-2026-ARXIV-2605-19101:start -->
#### Heterogeneity-Aware Dataset Scheduling for Efficient Audio Large Language Model Training

**问题与机制。** In this work, we analyze multi-dataset AudioQA training from a convergence perspective and propose Grouped Sequential Training (GST). 该 family 改变或挑战 `TRAIN-DATA` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 GST heterogeneity state, scheduler and optimization rule`；Evaluation=`§5 Experiments on Audio LLM training`；Limitations/Counterevidence=`§6 Limitations; audio datasets and selected recipes`。

<!-- claim:SF-2026-ARXIV-2605-19101:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19101:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19101:end -->

<!-- review:SF-2026-ARXIV-2605-19127:start -->
#### POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents

**问题与机制。** We introduce POLAR-Bench (Policy-aware adversarial Benchmark), in which a trusted model with a privacy policy and a task converses with a third-party model that adversarially probes for both task-relevant and protected attributes. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.6 policy/attack/evaluation contract`；Evaluation=`§4–§5 diagnostic surface`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19127:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19127:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19127:end -->

<!-- review:SF-2026-ARXIV-2605-19140:start -->
#### Learning to Hand Off: Provably Convergent Workflow Learning under Interface Constraints

**问题与机制。** We study workflow learning in a setting where specialized agents hand off control through a shared artifact, each agent observes only a local function of that artifact and its own private state, and no centralized learner accesses joint trajectories -- the operating regime of multi-agent LLM pipelines that span organizational, vendor, or trust boundaries. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 local-observation handoff interface and convergent learning rule`；Evaluation=`§5 theoretical/empirical evaluation`；Limitations/Counterevidence=`§6 Limitations; assumptions do not prove open-system delivery or authority`。

<!-- claim:SF-2026-ARXIV-2605-19140:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19140:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19140:end -->

<!-- review:SF-2026-ARXIV-2605-19151:start -->
#### Progressive Autonomy as Preference Learning: A Formalization of Trust Calibration for Agentic Tool Use

**问题与机制。** We formalize trust calibration for agentic tool use (deciding when an automated agent's proposed action may execute autonomously versus require human approval) as a preference-learning problem. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2–§3 approval/deny observations, GP preference posterior and autonomy threshold`；Evaluation=`§3–§4 theoretical and simulated evaluation`；Limitations/Counterevidence=`§4 Limitations; preference stationarity and calibration boundary`。

<!-- claim:SF-2026-ARXIV-2605-19151:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19151:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19151:end -->

<!-- review:SF-2026-ARXIV-2605-19169:start -->
#### Modeling the Impact of Fiber Latency on Compute-Communication Overlap in Geo-Distributed Multi-Datacenter AI Training

**问题与机制。** We use discrete-event simulation to quantify the impact of fiber latency on the efficacy of geo-distributed AI model training with data parallelism. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 Methods; latency/serialization model and ASTRA-sim overlap model`；Evaluation=`§3 Results; GPT-3 13B/175B, A100/H100, 256–8192 GPU simulation`；Limitations/Counterevidence=`§4 Conclusions; lumped two-DC, uncongested-network and simulation-only boundary`。

<!-- claim:SF-2026-ARXIV-2605-19169:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19169:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19169:end -->

<!-- review:SF-2026-ARXIV-2605-19192:start -->
#### Hallucination as Exploit: Evidence-Carrying Multimodal Agents

**问题与机制。** We formalize this failure mode as hallucination-to-action conversion: an unsupported claim supplies the precondition for a privileged action. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 evidence certificate and action-admission architecture`；Evaluation=`§5 Evaluation under multimodal hallucination-to-action attacks`；Limitations/Counterevidence=`§6 Limitations; certificate coverage and evaluator trust`。

<!-- claim:SF-2026-ARXIV-2605-19192:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19192:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19192:end -->

<!-- review:SF-2026-ARXIV-2605-19193:start -->
#### Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection

**问题与机制。** We evaluate two tracks: (i) a Monte-Carlo study under calibrated Beta models characterising working curves, error rates, capping behaviour, and sensitivity; and (ii) a real-LLM evaluation on 200 attempted MMLU and 200 attempted GSM8K items with three heterogeneous agents (gpt-5, claude-opus-4-6, gemini-2.5-pro) and a claude-opus-4-6 judge, using disjoint 40-item calibration subsets. 该 family 改变或挑战 `AGENT-MULTI-AGENT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§III–V sequential stopping and calibration`；Evaluation=`§VI simulation; §VII real-LLM study`；Limitations/Counterevidence=`§V-E i.i.d. violations; §VIII discussion`。

<!-- claim:SF-2026-ARXIV-2605-19193:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19193:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19193:end -->

<!-- review:SF-2026-ARXIV-2605-19196:start -->
#### Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents?

**问题与机制。** To address these gaps, we introduce REFLECT (REliable Fine-grained LLM judge Evaluation via Controlled inTervention), a meta-evaluation benchmark targeting fine-grained failure detection in agentic environments. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2.1–2.2 controlled-intervention benchmark`；Evaluation=`§3.1–3.5 judge meta-evaluation`；Limitations/Counterevidence=`§4 related work; §5 conclusion`。

<!-- claim:SF-2026-ARXIV-2605-19196:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19196:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19196:end -->

<!-- review:SF-2026-ARXIV-2605-19218:start -->
#### Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference

**问题与机制。** Experiments on two representative VLM backbones show that RotateK consistently outperforms prior Key channel pruning in both accuracy and decoding latency, while joint token-channel pruning improves over token-only baselines at matched KV cache budgets. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–§3.3 RotateK query-weighted PCA, structured channel pruning and Triton kernel`；Evaluation=`§4 Experiments; matched KV budgets, prefill/decode latency and memory`；Limitations/Counterevidence=`Appendix G Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19218:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19218:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19218:end -->

<!-- review:SF-2026-ARXIV-2605-19228:start -->
#### Diagnosing Multi-step Reasoning Failures in Black-box LLMs via Stepwise Confidence Attribution

**问题与机制。** In this paper, we introduce Stepwise Confidence Attribution (SCA), a framework for closed-source LLMs that assigns step-level confidence based only on generated reasoning traces. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 problem; §4.1–4.3 step confidence`；Evaluation=`§5 experiments`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-19228:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19228:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19228:end -->

<!-- review:SF-2026-ARXIV-2605-19240:start -->
#### CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring

**问题与机制。** Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4.1–4.4 causal cross-channel monitoring`；Evaluation=`§5 detection and attribution evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19240:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19240:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19240:end -->

<!-- review:SF-2026-ARXIV-2605-19242:start -->
#### PhyWorld: Physics-Faithful World Model for Video Generation

**问题与机制。** We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 physics-faithful data and objective`；Evaluation=`§4 controlled video/world-model evaluation`；Limitations/Counterevidence=`§5 Conclusion and inherited generator biases`。

<!-- claim:SF-2026-ARXIV-2605-19242:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19242:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19242:end -->

<!-- review:SF-2026-ARXIV-2605-19262:start -->
#### Backdooring Masked Diffusion Language Models

**问题与机制。** In this work, we present the first systematic study of training-time backdoor attacks on MDLMs. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 masked-diffusion backdoor construction`；Evaluation=`§5 attack and defense experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19262:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19262:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19262:end -->

<!-- review:SF-2026-ARXIV-2605-19269:start -->
#### CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

**问题与机制。** We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 GEMM-epilogue program representation`；Evaluation=`§4 kernel and end-to-end evaluation`；Limitations/Counterevidence=`§5 limitations and portability boundary`。

<!-- claim:SF-2026-ARXIV-2605-19269:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19269:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19269:end -->

<!-- review:SF-2026-ARXIV-2605-19276:start -->
#### OpenCompass: A Universal Evaluation Platform for Large Language Models

**问题与机制。** Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3.1–3.5 evaluation-platform architecture`；Evaluation=`§4 benchmark execution and comparison`；Limitations/Counterevidence=`§5 Future Works`。

<!-- claim:SF-2026-ARXIV-2605-19276:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19276:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19276:end -->

<!-- review:SF-2026-ARXIV-2605-19282:start -->
#### Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR

**问题与机制。** While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 spectral failure analysis; §4 high-pass remedy`；Evaluation=`§5 VLA/RLVR optimization experiments`；Limitations/Counterevidence=`Appendix M Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19282:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19282:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19282:end -->

<!-- review:SF-2026-ARXIV-2605-19314:start -->
#### ContextFlow: Hierarchical Task-State Alignment for Long-Horizon Embodied Agents

**问题与机制。** We study task-state misalignment, a task-level consistency failure in which the planner's active stage, runtime evidence, remembered context, and delegated executor no longer justify the same next-step decision. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 hierarchical task-state alignment`；Evaluation=`§4.1–4.4 long-horizon embodied evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19314:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19314:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19314:end -->

<!-- review:SF-2026-ARXIV-2605-19319:start -->
#### SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution

**问题与机制。** In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 sparse keyframe world-model planner and goal-conditioned action predictor`；Evaluation=`§4 real-robot and simulation experiments`；Limitations/Counterevidence=`§5 Limitations: short horizon, annotations and edited-image domain gap`。

<!-- claim:SF-2026-ARXIV-2605-19319:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19319:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19319:end -->

<!-- review:SF-2026-ARXIV-2605-19321:start -->
#### Exploring and Developing a Pre-Model Safeguard with Draft Models

**问题与机制。** In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 draft-model pre-guard design`；Evaluation=`§6 jailbreak and latency evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19321:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19321:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19321:end -->

<!-- review:SF-2026-ARXIV-2605-19328:start -->
#### RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents

**问题与机制。** We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 embodied-agent threat and benchmark protocol`；Evaluation=`§4 attacks and defenses`；Limitations/Counterevidence=`§5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19328:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19328:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19328:end -->

<!-- review:SF-2026-ARXIV-2605-19335:start -->
#### Leveraging I/O Stalls for Efficient Scheduling in ANNS

**问题与机制。** We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§4 LIOS update decomposition, overrun-bounded budgeting and feedback control`；Evaluation=`§6 search/update evaluation on FreshDiskANN and OdinANN`；Limitations/Counterevidence=`§8 Conclusion; disk ANNS and measured hardware scope`。

<!-- claim:SF-2026-ARXIV-2605-19335:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19335:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19335:end -->

<!-- review:SF-2026-ARXIV-2605-19341:start -->
#### HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models

**问题与机制。** To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3.1–3.3 controlled reference-world benchmark`；Evaluation=`§4 cross-context hallucination experiments`；Limitations/Counterevidence=`§5 Discussion; controlled-world boundary`。

<!-- claim:SF-2026-ARXIV-2605-19341:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19341:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19341:end -->

<!-- review:SF-2026-ARXIV-2605-19373:start -->
#### Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies

问题与机制：Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies 提出的具体变化是：To resolve this, we present a two-layer architecture -- CRDTMergeState -- that wraps any merge strategy in a CRDT-compliant (Conflict-Free Replicated Data Type) layer. 摘要中的长期系统挑战为：distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations。它可能改变 `PLATFORM-MODEL-REGISTRY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We prove that this separation guarantees Strong Eventual Consistency: all replicas receiving the same contributions compute identical merged models, regardless of message ordering.”暂不作为最终证据。

Evaluation contract：The reference implementation is available as crdt-merge v0.9.4.

Evidence locators：Method=`section 4 The Solution: Two-Layer Architecture (§4 The Solution: Two-Layer Architecture)`；Evaluation=`section 3.1 Formal Analysis of CRDT Property Violations (§3.1 Formal Analysis of CRDT Property Violations)`；Counterevidence=`section 7 Discussion (§7 Discussion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-19373:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-19373:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19373:end -->

<!-- review:SF-2026-ARXIV-2605-19407:start -->
#### A Bitter Lesson for Data Filtering

**问题与机制。** We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§3–§6 compute/data/filter scaling design`；Evaluation=`§6–§7 scaling experiments`；Limitations/Counterevidence=`§8 Discussion and scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-19407:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19407:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19407:end -->

<!-- review:SF-2026-ARXIV-2605-19444:start -->
#### Detecting and Mitigating the Correct-Answer Extinction Window in Test-Time Reinforcement Learning with Majority Voting

**问题与机制。** We argue these gains are systematically misinterpreted: most reflect sharpening of already-solvable problems rather than genuine learning, while problems corrupted from correct to incorrect outnumber truly learned ones, and this damage is irreversible once majority vote locks onto a wrong answer. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§2 extinction-window dynamics; §3 TTRL-Guard`；Evaluation=`§4 model/benchmark experiments and per-problem migration`；Limitations/Counterevidence=`§6 Breadth of evaluation; signal quality at the extremes`。

<!-- claim:SF-2026-ARXIV-2605-19444:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19444:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19444:end -->

<!-- review:SF-2026-ARXIV-2605-19447:start -->
#### What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents

**问题与机制。** We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 selective hindsight placement and environment-guided advantage reweighting`；Evaluation=`§4 ALFWorld/WebShop experiments and ablations`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19447:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19447:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19447:end -->

<!-- review:SF-2026-ARXIV-2605-19461:start -->
#### Beyond Mode Collapse: Distribution Matching for Diverse Reasoning

**问题与机制。** We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 forward/group distribution-matching policy optimization`；Evaluation=`§4–§5 reasoning experiments and ablations`；Limitations/Counterevidence=`Appendix B Limitations; group-local coverage does not prove global target matching`。

<!-- claim:SF-2026-ARXIV-2605-19461:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19461:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19461:end -->

<!-- review:SF-2026-ARXIV-2605-19478:start -->
#### Exposing Functional Fusion: A New Class of Strategic Backdoor in Dynamic Prompt Architectures

**问题与机制。** While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 threat model; §5–§6 dynamic-prompt functional fusion`；Evaluation=`§7 attack, pruning and transfer evaluation`；Limitations/Counterevidence=`§8 Conclusion; ViT/VPT threat-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-19478:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19478:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19478:end -->

<!-- review:SF-2026-ARXIV-2605-19481:start -->
#### C2CServe: Leveraging NVLink-C2C for Elastic Serverless LLM Serving on MIG

**问题与机制。** Leveraging this capability, we present C2CServe, a request-granularity serverless LLM serving system that allows MIG instances to switch models across requests without reloading weights into HBM. 系统 owner=`INFER-PD-DISAGGREGATION`。

**Exact-v1。** Method=`§III–V C2C weight/state movement design`；Evaluation=`§VI MIG/serverless serving evaluation`；Limitations/Counterevidence=`§VII Conclusion and hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-19481:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19481:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19481:end -->

<!-- review:SF-2026-ARXIV-2605-19537:start -->
#### The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility

**问题与机制。** While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 backend-reproducibility protocol`；Evaluation=`§4 backend/model benchmark deltas`；Limitations/Counterevidence=`§5 Discussion and reproducibility boundary`。

<!-- claim:SF-2026-ARXIV-2605-19537:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19537:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19537:end -->

<!-- review:SF-2026-ARXIV-2605-19576:start -->
#### Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries

**问题与机制。** Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3–§5 lifecycle-managed skill library`；Evaluation=`§6 library-drift evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19576:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19576:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19576:end -->

<!-- review:SF-2026-ARXIV-2605-19593:start -->
#### Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption

**问题与机制。** In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 multi-model offload/preemption methodology`；Evaluation=`§4–§5 heterogeneous-serving measurements`；Limitations/Counterevidence=`§6 Conclusion; interconnect and hardware constraints`。

<!-- claim:SF-2026-ARXIV-2605-19593:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19593:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19593:end -->

<!-- review:SF-2026-ARXIV-2605-19604:start -->
#### Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents

**问题与机制。** We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 programmable runtime skill contract`；Evaluation=`§4 execution and accuracy evaluation`；Limitations/Counterevidence=`§5 Conclusion; language/runtime boundary`。

<!-- claim:SF-2026-ARXIV-2605-19604:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19604:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19604:end -->

<!-- review:SF-2026-ARXIV-2605-19722:start -->
#### Measuring Safety Alignment Effects in Autonomous Security Agents

**问题与机制。** We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 trace-based autonomous security-agent protocol`；Evaluation=`§4–§5 sandbox/tool-use evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19722:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19722:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19722:end -->

<!-- review:SF-2026-ARXIV-2605-19755:start -->
#### Operationalising Artificial Intelligence Bills of Materials (AIBOMs) for Verifiable AI Provenance and Lifecycle Assurance

<!-- claim:SF-2026-ARXIV-2605-19755:start -->
- **Problem:** Artificial Intelligence (AI) systems are increasingly dependent on complex, multi-layered software supply chains that introduce challenges for reproducibility, transparency, and security assurance.
- **Old path / changed constraint:** 传统 SBOM 以静态组件名和版本为主，无法完整绑定模型、数据引用、运行时依赖、配置与生成过程；在 AI artifact 持续演化和环境漂移时，仅凭名称清单不足以重放、归责或判断漏洞匹配。
- **Mechanism / ownership:** 方案扩展 CycloneDX，记录 AI provenance、model lineage、disclosure metadata，并用组件 hash、签名、容器运行态和 agent 生成的环境记录绑定 artifact；自动化流水线负责环境发现、漏洞富化、schema 校验和 reproducibility audit，材料不全时保留 partial-attestation 状态。
- **Evaluation contract:** 作者在受控 containerised analytic workflows 中报告 98.7% reproducibility fidelity、96.2% vulnerability-match precision 和 63% manual-oversight reduction。这些是作者在论文 workload 下的结果；尚无跨组织、长期生产采用或不同 vulnerability database 的独立验证。
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 完整性依赖 runtime discovery、包名归一化、base-image 可见性和漏洞数据库覆盖；hash 改善身份绑定，却不能证明语义等价或实际可利用性。非确定性执行仍可能阻止 bit-identical replay，持续采集、签名和富化也增加存储与治理成本；无法解析的瞬态依赖必须保持 unverifiable，而非伪造完整性。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.19755v1](https://arxiv.org/abs/2605.19755v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.19755v1.pdf`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-19755:end -->
<!-- review:SF-2026-ARXIV-2605-19755:end -->

<!-- review:SF-2026-ARXIV-2605-19769:start -->
#### OpenComputer: Verifiable Software Worlds for Computer-Use Agents

**问题与机制。** We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 verifier-grounded software worlds`；Evaluation=`§4.1 computer-use agent evaluation`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations and Future Work’`。

<!-- claim:SF-2026-ARXIV-2605-19769:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19769:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19769:end -->

<!-- review:SF-2026-ARXIV-2605-19775:start -->
#### Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles

**问题与机制。** By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§2–§3 inference-scaling model`；Evaluation=`§4–§5 reasoning-workload measurements`；Limitations/Counterevidence=`§6 Conclusions and disclosed scope`。

<!-- claim:SF-2026-ARXIV-2605-19775:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19775:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19775:end -->

<!-- review:SF-2026-ARXIV-2605-19779:start -->
#### Distribution-Free Uncertainty Quantification for Continuous AI Agent Evaluation

**问题与机制。** We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 conformal continuous-agent UQ`；Evaluation=`§4 longitudinal agent studies`；Limitations/Counterevidence=`§5 Limitations: bounded shift and dependence`。

<!-- claim:SF-2026-ARXIV-2605-19779:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19779:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19779:end -->

<!-- review:SF-2026-ARXIV-2605-19811:start -->
#### LionMuon: Alternating Spectral and Sign Descent for Efficient Training

**问题与机制。** In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 optimizer geometry; §4 LionMuon alternating spectral/sign descent`；Evaluation=`§5 language-model training experiments and ablations`；Limitations/Counterevidence=`§6 Limitations and optimizer/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-19811:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19811:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19811:end -->

<!-- review:SF-2026-ARXIV-2605-19847:start -->
#### Auditing Privacy in Multi-Tenant RAG under Account Collusion

**问题与机制。** We show that this framing understates leakage under same-index account collusion. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§2–§3 collusion threat model and tenant accounting`；Evaluation=`§4 privacy audit; §5 protocol`；Limitations/Counterevidence=`§7.1 Limitations: retrieval only, not generation`。

<!-- claim:SF-2026-ARXIV-2605-19847:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19847:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19847:end -->

<!-- review:SF-2026-ARXIV-2605-19893:start -->
#### SSV: Sparse Speculative Verification for Efficient LLM Inference

**问题与机制。** We present SSV, a sparse speculative-verification framework that turns dynamic sparse attention into a verification-oriented workload. 系统 owner=`INFER-SPECULATIVE-DECODING`。

**Exact-v1。** Method=`§3–§4 sparse speculative verification`；Evaluation=`§5 long-context evaluation`；Limitations/Counterevidence=`§6 Conclusion and sparse-attention boundary`。

<!-- claim:SF-2026-ARXIV-2605-19893:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19893:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19893:end -->

<!-- review:SF-2026-ARXIV-2605-19932:start -->
#### PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents

**问题与机制。** We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context. 系统 owner=`AGENT-CONTEXT`。

**Exact-v1。** Method=`§3 orientation-cache representation`；Evaluation=`§4 recurring-context agent evaluation`；Limitations/Counterevidence=`§5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19932:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19932:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19932:end -->

<!-- review:SF-2026-ARXIV-2605-19945:start -->
#### GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems

**问题与机制。** We propose GEM, GPU-variability-aware Expert Mapping, a framework for GPU variability-aware expert to GPU mapping for MoE models. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3–§4 variability-aware expert placement`；Evaluation=`§5 heterogeneous-GPU evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19945:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19945:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19945:end -->

<!-- review:SF-2026-ARXIV-2605-19952:start -->
#### Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory

**问题与机制。** To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§3 trace/chunk memory representation`；Evaluation=`§4 lifelong-memory evaluation`；Limitations/Counterevidence=`Appendix C.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19952:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19952:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19952:end -->

<!-- review:SF-2026-ARXIV-2605-19999:start -->
#### LLM Benchmark Datasets Should Be Contamination-Resistant

**问题与机制。** Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3–§4 contamination-resistant benchmark construction`；Evaluation=`§5 benchmark analysis`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: contamination detection and task scope`。

<!-- claim:SF-2026-ARXIV-2605-19999:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19999:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19999:end -->

<!-- review:SF-2026-ARXIV-2605-20005:start -->
#### Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates

**问题与机制。** We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 per-step forgetting bound and loss-adaptive learning rate`；Evaluation=`§4–§5 task/forgetting, factuality and calibration experiments`；Limitations/Counterevidence=`§6 Conclusion, Limitations, and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20005:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20005:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20005:end -->

<!-- review:SF-2026-ARXIV-2605-20022:start -->
#### FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration

**问题与机制。** Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel. 系统 owner=`INFER-SPECULATIVE-DECODING`。

**Exact-v1。** Method=`§3–§4 asynchronous flexible drafting`；Evaluation=`§5 end-to-end evaluation`；Limitations/Counterevidence=`§6 Conclusion: bonus-token and accepted-length uncertainty`。

<!-- claim:SF-2026-ARXIV-2605-20022:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20022:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20022:end -->

<!-- review:SF-2026-ARXIV-2605-20023:start -->
#### When Skills Don't Help: A Negative Result on Procedural Knowledge for Tool-Grounded Agents in Offensive Cybersecurity

**问题与机制。** Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 procedural-skill intervention and tool-grounded agent protocol`；Evaluation=`§4 offensive-cybersecurity experiments`；Limitations/Counterevidence=`§5 Limitations; negative result is workload/model specific`。

<!-- claim:SF-2026-ARXIV-2605-20023:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20023:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20023:end -->

<!-- review:SF-2026-ARXIV-2605-20051:start -->
#### Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection

**问题与机制。** Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3–§4 reference-driven variant detection`；Evaluation=`§5 AI-infra repository measurement`；Limitations/Counterevidence=`§6 Discussion and false-positive boundary`。

<!-- claim:SF-2026-ARXIV-2605-20051:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20051:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20051:end -->

<!-- review:SF-2026-ARXIV-2605-20061:start -->
#### Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents

**问题与机制。** To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 belief-consistency credit assignment`；Evaluation=`§4 long-horizon agent evaluation`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20061:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20061:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20061:end -->

<!-- review:SF-2026-ARXIV-2605-20084:start -->
#### BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation

**问题与机制。** In this work, we develop BalanceRAG to certify threshold pairs at a target risk level. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§3–§4 joint escalation/abstention calibration`；Evaluation=`§5 cascaded-RAG evaluation`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: distribution shift and calibration`。

<!-- claim:SF-2026-ARXIV-2605-20084:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20084:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20084:end -->

<!-- review:SF-2026-ARXIV-2605-20179:start -->
#### TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload

**问题与机制。** In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 I/O-aware MoE expert-offload design`；Evaluation=`§4 LLaDA2.0 experiments`；Limitations/Counterevidence=`§5 Conclusion: block-only activation and limited hardware`。

<!-- claim:SF-2026-ARXIV-2605-20179:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20179:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20179:end -->

<!-- review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->
#### DynaTrain: Fast Online Parallelism Switching for Elastic LLM Training

问题与机制：We present DynaTrain, a distributed training system for sub-second, online reconfiguration across arbitrary multi-dimensional parallelism.。机制 owner=`TRAIN-DISTRIBUTED-TRAINING`。
全文定位：`arXiv:2605.18815v1 HTML — §3 DynaTrain elastic parallelism transition controller`；evaluation=`arXiv:2605.18815v1 — §4 distributed-training evaluation`；limitations/counterevidence=`arXiv:2605.18815v1 — §5 limitations: topology, transition cost and failure scope`。
<!-- claim:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->

<!-- review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->
#### Evaluating Memory Condensation Strategies for Coding Agents in Data-Driven Scientific Discovery

问题与机制：Coding agents accumulate extensive context during long-running tasks, yet fixed context windows force practitioners to choose between truncation and task failure.。机制 owner=`AGENT-MEMORY`。
全文定位：`arXiv:2605.18854v1 HTML — §2 Memory Condensation Strategies`；evaluation=`§3 Experimental Setup and §4 Results — 480 DiscoveryBench evaluations`；limitations/counterevidence=`§5 Discussion / Conclusion — GPT-4o, six-domain and task-length boundary`。
<!-- claim:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->

<!-- review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->
#### Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models

问题与机制：We introduce a framework for automated benchmark generation.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.18824v1 HTML — §3 multi-agent benchmark generation and solution-graph ground-truth pipeline`；evaluation=`arXiv:2605.18824v1 — §4 expert review and twelve-model evaluation`；limitations/counterevidence=`arXiv:2605.18824v1 — §6 Conclusion — limitations include multiple-choice scope, frontier-model generator/verifier dependence and nonzero residual error`。
<!-- claim:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->

<!-- review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->
#### How Faithful Is Trajectory-Based Data Attribution? Error Sources, Remedies, and Practical Guidelines

问题与机制：We propose AdamW-influence to fully account for AdamW's optimization dynamics, yielding improvements from 10% to over 300% in Spearman correlation between estimated and ground-truth influence across four settings spanning MLP, CNN, GPT-2, and Llama 3.2-1B.。机制 owner=`TRAIN-DATA`。
全文定位：`arXiv:2605.18814v1 HTML — §3 trajectory-data attribution estimator`；evaluation=`arXiv:2605.18814v1 — §4 attribution experiments`；limitations/counterevidence=`arXiv:2605.18814v1 — §5 limitations: causal identifiability and data coverage`。
<!-- claim:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->

<!-- review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->
#### INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference

问题与机制：We present INAR-VL, a lightweight edge-cloud routing system for multimodal inference in a two-tier deployment.。机制 owner=`INFER-SCHEDULING`。
全文定位：`arXiv:2605.18853v1 HTML — §Method / System Design — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->

<!-- review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->
#### Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches

问题与机制：We show that different token types within a prompt, including system prompts, user queries, tool outputs, model responses, and chain-of-thought reasoning, exhibit up to 756x variation in reuse rates, yet no existing eviction policy exploits this signal.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.18825v1 HTML — §3 semantic prefix-cache eviction policy`；evaluation=`arXiv:2605.18825v1 — §4 serving evaluation`；limitations/counterevidence=`arXiv:2605.18825v1 — §5 limitations: semantic estimator, workload and cache budget`。
<!-- claim:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->

<!-- review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->
#### PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines

问题与机制：We present PASC (Pipeline-Aware Split Conformal), which reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.18812v1 HTML — §3 PASC pipeline-conformal evidence contract`；evaluation=`arXiv:2605.18812v1 — §4 calibration/evaluation experiments`；limitations/counterevidence=`arXiv:2605.18812v1 — §5 limitations: exchangeability and pipeline shift`。
<!-- claim:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->

<!-- review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->
#### Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking

问题与机制：We formulate late-stage checkpoint selection as a stability-aware decision problem under evaluation uncertainty and propose a progressive framework combining pointwise filtering, listwise ranking, and pairwise refinement.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.18852v1 HTML — §Method / System Design — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->
#### SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference

问题与机制：We present Spherical KV, a long-context inference method that treats KV allocation as a rate-distortion problem grounded in attention geometry for efficient decoding.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.18856v1 HTML — §Method / System Design — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->

### Legacy V2.1 — Benchmark Contracts

<!-- legacy-validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | exact-v1 evaluation for Operational Memory Architecture for Kubernetes:Preserving Causal Context Across the Evidence Horizon | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-18762 | exact-v1 evaluation for ALDEN: Boosting Private Data Extraction from Retrieval-Augmented Generation Systems via Active Learning and Distribution Estimation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-19755 | exact-v1 evaluation for Operationalising Artificial Intelligence Bills of Materials (AIBOMs) for Verifiable AI Provenance and Lifecycle Assurance | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

### Legacy V2.1 — Deep Analysis Selection

<!-- legacy-validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18755 |
| SF-2026-ARXIV-2605-18762 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18762 |
| SF-2026-ARXIV-2605-18792 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18792 |
| SF-2026-ARXIV-2605-18796 | score_7_9 | selected | DA-20260520-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260520-01 |
| SF-2026-ARXIV-2605-18803 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18803 |
| SF-2026-ARXIV-2605-18859 | score_7_9;forced_review;potential_books_delta | selected | DA-20260520-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260520-02 |
| SF-2026-ARXIV-2605-18891 | score_7_9;forced_review;potential_books_delta | selected | DA-20260520-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260520-03 |
| SF-2026-ARXIV-2605-18899 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18899 |
| SF-2026-ARXIV-2605-18918 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18918 |
| SF-2026-ARXIV-2605-18930 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18930 |
| SF-2026-ARXIV-2605-18991 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18991 |
| SF-2026-ARXIV-2605-19008 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19008 |
| SF-2026-ARXIV-2605-19049 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19049 |
| SF-2026-ARXIV-2605-19099 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19099 |
| SF-2026-ARXIV-2605-19101 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19101 |
| SF-2026-ARXIV-2605-19127 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19127 |
| SF-2026-ARXIV-2605-19140 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19140 |
| SF-2026-ARXIV-2605-19151 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19151 |
| SF-2026-ARXIV-2605-19169 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19169 |
| SF-2026-ARXIV-2605-19192 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19192 |
| SF-2026-ARXIV-2605-19193 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19193 |
| SF-2026-ARXIV-2605-19196 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19196 |
| SF-2026-ARXIV-2605-19218 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19218 |
| SF-2026-ARXIV-2605-19228 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19228 |
| SF-2026-ARXIV-2605-19240 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19240 |
| SF-2026-ARXIV-2605-19242 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19242 |
| SF-2026-ARXIV-2605-19262 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19262 |
| SF-2026-ARXIV-2605-19269 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19269 |
| SF-2026-ARXIV-2605-19276 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19276 |
| SF-2026-ARXIV-2605-19282 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19282 |
| SF-2026-ARXIV-2605-19314 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19314 |
| SF-2026-ARXIV-2605-19319 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19319 |
| SF-2026-ARXIV-2605-19321 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19321 |
| SF-2026-ARXIV-2605-19328 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19328 |
| SF-2026-ARXIV-2605-19335 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19335 |
| SF-2026-ARXIV-2605-19341 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19341 |
| SF-2026-ARXIV-2605-19373 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19373 |
| SF-2026-ARXIV-2605-19407 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19407 |
| SF-2026-ARXIV-2605-19444 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19444 |
| SF-2026-ARXIV-2605-19447 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19447 |
| SF-2026-ARXIV-2605-19461 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19461 |
| SF-2026-ARXIV-2605-19478 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19478 |
| SF-2026-ARXIV-2605-19481 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19481 |
| SF-2026-ARXIV-2605-19537 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19537 |
| SF-2026-ARXIV-2605-19576 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19576 |
| SF-2026-ARXIV-2605-19593 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19593 |
| SF-2026-ARXIV-2605-19604 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19604 |
| SF-2026-ARXIV-2605-19722 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19722 |
| SF-2026-ARXIV-2605-19755 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19755 |
| SF-2026-ARXIV-2605-19769 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19769 |
| SF-2026-ARXIV-2605-19775 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19775 |
| SF-2026-ARXIV-2605-19779 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19779 |
| SF-2026-ARXIV-2605-19811 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19811 |
| SF-2026-ARXIV-2605-19847 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19847 |
| SF-2026-ARXIV-2605-19893 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19893 |
| SF-2026-ARXIV-2605-19932 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19932 |
| SF-2026-ARXIV-2605-19945 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19945 |
| SF-2026-ARXIV-2605-19952 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19952 |
| SF-2026-ARXIV-2605-19999 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19999 |
| SF-2026-ARXIV-2605-20005 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20005 |
| SF-2026-ARXIV-2605-20022 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20022 |
| SF-2026-ARXIV-2605-20023 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20023 |
| SF-2026-ARXIV-2605-20051 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20051 |
| SF-2026-ARXIV-2605-20061 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20061 |
| SF-2026-ARXIV-2605-20084 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20084 |
| SF-2026-ARXIV-2605-20179 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20179 |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF |

<!-- analysis-decision:SF-2026-ARXIV-2605-18755:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18755:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18762:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18762:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18792:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18792:end -->

<!-- analysis:DA-20260520-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-18796

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260520-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18803:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18803:end -->

<!-- analysis:DA-20260520-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-18859

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260520-02:end -->

<!-- analysis:DA-20260520-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-18891

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260520-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18899:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18918:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18930:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18930:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18991:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18991:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19008:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19008:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19049:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19049:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19099:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19099:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19101:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19101:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19127:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19127:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19140:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19140:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19151:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19169:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19169:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19192:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19192:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19193:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19193:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19196:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19196:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19218:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19218:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19228:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19228:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19240:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19240:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19242:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19262:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19262:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19269:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19269:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19276:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19276:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19282:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19282:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19314:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19314:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19319:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19319:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19321:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19321:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19328:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19328:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19335:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19335:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19341:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19341:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19373:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19373:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19407:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19407:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19444:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19444:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19447:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19447:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19461:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19461:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19478:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19478:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19481:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19481:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19537:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19537:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19576:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19576:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19593:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19593:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19604:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19604:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19722:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19722:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19755:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19755:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19769:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19769:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19775:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19775:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19779:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19779:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19811:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19811:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19847:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19893:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19932:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19945:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19945:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19952:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19952:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19999:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19999:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20005:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20022:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20022:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20023:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20023:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20051:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20051:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20061:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20084:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20084:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20179:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20179:end -->

<!-- analysis-decision:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->

<!-- analysis-decision:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->

<!-- analysis-decision:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->

<!-- analysis-decision:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->

<!-- analysis-decision:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->

<!-- analysis-decision:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->

<!-- analysis-decision:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->

<!-- analysis-decision:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- analysis-decision:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->

### Legacy V2.1 — Books Comparison

<!-- legacy-validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | PLATFORM-LOGGING | books/part-06-ai-infrastructure/68-logging.md#L72 (H2: 可靠传输与背压) | books/part-06-ai-infrastructure/67-monitoring.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/69-trace.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-18755 | delta:SF-2026-ARXIV-2605-18755 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18755 |
| SF-2026-ARXIV-2605-18762 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-18762 | delta:SF-2026-ARXIV-2605-18762 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18762 |
| SF-2026-ARXIV-2605-18792 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-18792 | delta:SF-2026-ARXIV-2605-18792 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18792 |
| SF-2026-ARXIV-2605-18796 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#chapter-57 | existing:SF-2026-ARXIV-2605-18796 | delta:SF-2026-ARXIV-2605-18796 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18796 |
| SF-2026-ARXIV-2605-18803 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-18803 | delta:SF-2026-ARXIV-2605-18803 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18803 |
| SF-2026-ARXIV-2605-18859 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18859 | delta:SF-2026-ARXIV-2605-18859 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18859 |
| SF-2026-ARXIV-2605-18891 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-18891 | delta:SF-2026-ARXIV-2605-18891 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18891 |
| SF-2026-ARXIV-2605-18899 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-18899 | delta:SF-2026-ARXIV-2605-18899 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18899 |
| SF-2026-ARXIV-2605-18918 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-18918 | delta:SF-2026-ARXIV-2605-18918 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18918 |
| SF-2026-ARXIV-2605-18930 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18930 | delta:SF-2026-ARXIV-2605-18930 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18930 |
| SF-2026-ARXIV-2605-18991 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-18991 | delta:SF-2026-ARXIV-2605-18991 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18991 |
| SF-2026-ARXIV-2605-19008 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19008 | delta:SF-2026-ARXIV-2605-19008 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19008 |
| SF-2026-ARXIV-2605-19049 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-19049 | delta:SF-2026-ARXIV-2605-19049 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19049 |
| SF-2026-ARXIV-2605-19099 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19099 | delta:SF-2026-ARXIV-2605-19099 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19099 |
| SF-2026-ARXIV-2605-19101 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-19101 | delta:SF-2026-ARXIV-2605-19101 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19101 |
| SF-2026-ARXIV-2605-19127 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19127 | delta:SF-2026-ARXIV-2605-19127 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19127 |
| SF-2026-ARXIV-2605-19140 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-19140 | delta:SF-2026-ARXIV-2605-19140 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19140 |
| SF-2026-ARXIV-2605-19151 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19151 | delta:SF-2026-ARXIV-2605-19151 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19151 |
| SF-2026-ARXIV-2605-19169 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-19169 | delta:SF-2026-ARXIV-2605-19169 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19169 |
| SF-2026-ARXIV-2605-19192 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19192 | delta:SF-2026-ARXIV-2605-19192 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19192 |
| SF-2026-ARXIV-2605-19193 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19193 | delta:SF-2026-ARXIV-2605-19193 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19193 |
| SF-2026-ARXIV-2605-19196 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19196 | delta:SF-2026-ARXIV-2605-19196 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19196 |
| SF-2026-ARXIV-2605-19218 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-19218 | delta:SF-2026-ARXIV-2605-19218 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19218 |
| SF-2026-ARXIV-2605-19228 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19228 | delta:SF-2026-ARXIV-2605-19228 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19228 |
| SF-2026-ARXIV-2605-19240 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19240 | delta:SF-2026-ARXIV-2605-19240 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19240 |
| SF-2026-ARXIV-2605-19242 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-19242 | delta:SF-2026-ARXIV-2605-19242 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19242 |
| SF-2026-ARXIV-2605-19262 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19262 | delta:SF-2026-ARXIV-2605-19262 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19262 |
| SF-2026-ARXIV-2605-19269 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-19269 | delta:SF-2026-ARXIV-2605-19269 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19269 |
| SF-2026-ARXIV-2605-19276 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19276 | delta:SF-2026-ARXIV-2605-19276 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19276 |
| SF-2026-ARXIV-2605-19282 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19282 | delta:SF-2026-ARXIV-2605-19282 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19282 |
| SF-2026-ARXIV-2605-19314 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-19314 | delta:SF-2026-ARXIV-2605-19314 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19314 |
| SF-2026-ARXIV-2605-19319 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-19319 | delta:SF-2026-ARXIV-2605-19319 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19319 |
| SF-2026-ARXIV-2605-19321 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19321 | delta:SF-2026-ARXIV-2605-19321 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19321 |
| SF-2026-ARXIV-2605-19328 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19328 | delta:SF-2026-ARXIV-2605-19328 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19328 |
| SF-2026-ARXIV-2605-19335 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-19335 | delta:SF-2026-ARXIV-2605-19335 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19335 |
| SF-2026-ARXIV-2605-19341 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19341 | delta:SF-2026-ARXIV-2605-19341 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19341 |
| SF-2026-ARXIV-2605-19373 | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#chapter-59 | books/part-06-ai-infrastructure/58-kubeflow.md#chapter-58; books/part-06-ai-infrastructure/60-training-operator.md#chapter-60 | existing:SF-2026-ARXIV-2605-19373 | delta:SF-2026-ARXIV-2605-19373 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19373 |
| SF-2026-ARXIV-2605-19407 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-19407 | delta:SF-2026-ARXIV-2605-19407 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19407 |
| SF-2026-ARXIV-2605-19444 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19444 | delta:SF-2026-ARXIV-2605-19444 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19444 |
| SF-2026-ARXIV-2605-19447 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19447 | delta:SF-2026-ARXIV-2605-19447 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19447 |
| SF-2026-ARXIV-2605-19461 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19461 | delta:SF-2026-ARXIV-2605-19461 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19461 |
| SF-2026-ARXIV-2605-19478 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19478 | delta:SF-2026-ARXIV-2605-19478 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19478 |
| SF-2026-ARXIV-2605-19481 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-19481 | delta:SF-2026-ARXIV-2605-19481 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19481 |
| SF-2026-ARXIV-2605-19537 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19537 | delta:SF-2026-ARXIV-2605-19537 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19537 |
| SF-2026-ARXIV-2605-19576 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19576 | delta:SF-2026-ARXIV-2605-19576 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19576 |
| SF-2026-ARXIV-2605-19593 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19593 | delta:SF-2026-ARXIV-2605-19593 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19593 |
| SF-2026-ARXIV-2605-19604 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19604 | delta:SF-2026-ARXIV-2605-19604 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19604 |
| SF-2026-ARXIV-2605-19722 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19722 | delta:SF-2026-ARXIV-2605-19722 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19722 |
| SF-2026-ARXIV-2605-19755 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-19755 | delta:SF-2026-ARXIV-2605-19755 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19755 |
| SF-2026-ARXIV-2605-19769 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19769 | delta:SF-2026-ARXIV-2605-19769 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19769 |
| SF-2026-ARXIV-2605-19775 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19775 | delta:SF-2026-ARXIV-2605-19775 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19775 |
| SF-2026-ARXIV-2605-19779 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19779 | delta:SF-2026-ARXIV-2605-19779 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19779 |
| SF-2026-ARXIV-2605-19811 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19811 | delta:SF-2026-ARXIV-2605-19811 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19811 |
| SF-2026-ARXIV-2605-19847 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19847 | delta:SF-2026-ARXIV-2605-19847 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19847 |
| SF-2026-ARXIV-2605-19893 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-19893 | delta:SF-2026-ARXIV-2605-19893 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19893 |
| SF-2026-ARXIV-2605-19932 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-19932 | delta:SF-2026-ARXIV-2605-19932 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19932 |
| SF-2026-ARXIV-2605-19945 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19945 | delta:SF-2026-ARXIV-2605-19945 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19945 |
| SF-2026-ARXIV-2605-19952 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-19952 | delta:SF-2026-ARXIV-2605-19952 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19952 |
| SF-2026-ARXIV-2605-19999 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19999 | delta:SF-2026-ARXIV-2605-19999 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19999 |
| SF-2026-ARXIV-2605-20005 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-20005 | delta:SF-2026-ARXIV-2605-20005 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20005 |
| SF-2026-ARXIV-2605-20022 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-20022 | delta:SF-2026-ARXIV-2605-20022 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20022 |
| SF-2026-ARXIV-2605-20023 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20023 | delta:SF-2026-ARXIV-2605-20023 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20023 |
| SF-2026-ARXIV-2605-20051 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20051 | delta:SF-2026-ARXIV-2605-20051 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20051 |
| SF-2026-ARXIV-2605-20061 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20061 | delta:SF-2026-ARXIV-2605-20061 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20061 |
| SF-2026-ARXIV-2605-20084 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-20084 | delta:SF-2026-ARXIV-2605-20084 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20084 |
| SF-2026-ARXIV-2605-20179 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20179 | delta:SF-2026-ARXIV-2605-20179 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20179 |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | delta:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | Direct Evolution | No Change — Existing Coverage | books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | delta:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | Direct Evolution | No Change — Existing Coverage | books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | delta:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | Direct Evolution | No Change — Existing Coverage | books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | delta:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | Direct Evolution | No Change — Existing Coverage | books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55; books/part-05-inference-system/README.md#knowledge-tree | existing:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | delta:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | Direct Evolution | No Change — Existing Coverage | books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | delta:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | Direct Evolution | No Change — Existing Coverage | books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | delta:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | Direct Evolution | No Change — Existing Coverage | books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | delta:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | Direct Evolution | Integrate | books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | delta:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | Direct Evolution | No Change — Existing Coverage | books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF |

<!-- books-review:SF-2026-ARXIV-2605-18755:start -->
<!-- existing:SF-2026-ARXIV-2605-18755:start -->对读 `books/part-06-ai-infrastructure/68-logging.md#L72 (H2: 可靠传输与背压)` 及相邻章节后，现有命题为：本章的核心判断是：**Log 是带时间和上下文的离散事件证据。它能解释状态变化与决策原因，但只有结构、身份、隐私和生命周期都被设计后，才是可靠证据。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-18755:end -->
<!-- delta:SF-2026-ARXIV-2605-18755:start -->Exact-v1 的 source-specific delta 是：We propose OMA, a four-layer framework positioning operational memory as an architectural primitive alongside metrics, logs, and traces in the Kubernetes observability stack (Section IV). 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-18755:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-18755:end -->

<!-- books-review:SF-2026-ARXIV-2605-18762:start -->
<!-- existing:SF-2026-ARXIV-2605-18762:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-18762:end -->
<!-- delta:SF-2026-ARXIV-2605-18762:start -->Exact-v1 的 source-specific delta 是：Here, we propose ALDEN, a novel attack that effectively and efficiently extracts private data from RAGs. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-18762:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-18762:end -->

<!-- books-review:SF-2026-ARXIV-2605-18792:start -->
<!-- existing:SF-2026-ARXIV-2605-18792:start -->已读取 current owner `books/part-07-agent/76-rag.md` 与相邻章节 `['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 参数化知识的边界 → ## Offline Ingestion 不是预处理细节 → ## Online Retrieval Pipeline → ### Tenant Filter 必须在检索内核中前置执行 → ## Retrieval 的基本度量 → ## Chunking 是信息边界设计 → ## Reranking 与 Context Packing → ## Relevance 不等于 Sufficient Context → ## Agentic Retrieval：Relevance 也可以是执行先验 → ### Query、Compression 与 Stopping 是联合 Policy → ## RAG 不消除 Hallucination → ### 长文生成需要把检索、叙事状态与核验分开提交 → ## Freshness、Deletion 与 Consistency。<!-- existing:SF-2026-ARXIV-2605-18792:end -->
<!-- delta:SF-2026-ARXIV-2605-18792:start -->AGENT-RAG already separates parametric belief, retrieved evidence, conflict handling and abstention; SABER provides one representation/probe for the existing trust-or-retrieve decision.<!-- delta:SF-2026-ARXIV-2605-18792:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-18792:end -->

<!-- books-review:SF-2026-ARXIV-2605-18796:start -->
<!-- existing:SF-2026-ARXIV-2605-18796:start -->已读取 current owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 `['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-06-ai-infrastructure/57-what-is-ai-platform.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 调度对象从 request 变成 token state → ## 目标函数不止吞吐 → ## SLO-aware Admission → ### 当前能放下，不等于未来可完成 → ### 不确定输出长度下的 Future-state Reservation → ### 连续 Edge Inference 需要跨窗口携带 Violation-risk Budget → ### 从队列启发式到时间耦合的资源影子价格 → ### Reasoning Budget 必须进入调度与评估身份 → ### Inference-time Process Guidance 也是可调度资源 → ## Iteration Scheduling → ## Routing、Placement 与 Autoscaling → ### 从经验 confidence threshold 到有条件的 Risk Contract → ### 近重复 Workload：先验证兼容，再执行代表项。<!-- existing:SF-2026-ARXIV-2605-18796:end -->
<!-- delta:SF-2026-ARXIV-2605-18796:start -->INFER-SCHEDULING already uses calibrated correctness/cost to commit, defer or escalate across model cascades; UCCI is a bounded uncertainty estimator and threshold solver.<!-- delta:SF-2026-ARXIV-2605-18796:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-18796:end -->

<!-- books-review:SF-2026-ARXIV-2605-18803:start -->
<!-- existing:SF-2026-ARXIV-2605-18803:start -->已读取 current owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 `['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 从三个容易混淆的对象开始 → ### Video generation → ### Predictive environment model → ### Controllable world model → ## 在谈 State 之前，先声明预测 Channel → ## 为什么旧的 Simulator 仍然合理 → ## 演进路线 → ### 从单尺度预测到 Abstraction × Timescale Hierarchy → ### Next-observation generation → ### Action-conditioned transition → ### Goal 属于 Planner Cost，不能成为 Transition 的答案通道 → ### Latent dynamics → ### Imagined rollout。<!-- existing:SF-2026-ARXIV-2605-18803:end -->
<!-- delta:SF-2026-ARXIV-2605-18803:start -->Ch25 已把 planner-induced rare-state coverage 与 prioritized failure discovery 作为训练/评测压力。<!-- delta:SF-2026-ARXIV-2605-18803:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-18803:end -->

<!-- books-review:SF-2026-ARXIV-2605-18859:start -->
<!-- existing:SF-2026-ARXIV-2605-18859:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。正文尚未明确承载本 family 的增量：Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-18859:end -->
<!-- delta:SF-2026-ARXIV-2605-18859:start -->Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告<!-- delta:SF-2026-ARXIV-2605-18859:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18859:end -->

<!-- books-review:SF-2026-ARXIV-2605-18891:start -->
<!-- existing:SF-2026-ARXIV-2605-18891:start -->独立 reviewer 顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8e594c3827c4a7778945dbe71f0c1af1ca4089918dcd0c8998ff54d98ac664a1。<!-- existing:SF-2026-ARXIV-2605-18891:end -->
<!-- delta:SF-2026-ARXIV-2605-18891:start -->reasoning-trace bypass gap 可能由 prefill/parser/format 造成，不能直接证明 weights 仍记忆；unlearning evaluation 必须冻结 parser、prompt head、seed 与 intervention identity。<!-- delta:SF-2026-ARXIV-2605-18891:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18891:end -->

<!-- books-review:SF-2026-ARXIV-2605-18899:start -->
<!-- existing:SF-2026-ARXIV-2605-18899:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-18899:end -->
<!-- delta:SF-2026-ARXIV-2605-18899:start -->continual policy updates bind logged-action propensity and ambiguous no-response feedback to the serving-policy revision<!-- delta:SF-2026-ARXIV-2605-18899:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18899:end -->

<!-- books-review:SF-2026-ARXIV-2605-18918:start -->
<!-- existing:SF-2026-ARXIV-2605-18918:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-18918:end -->
<!-- delta:SF-2026-ARXIV-2605-18918:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18918:end -->
<!-- books-review:SF-2026-ARXIV-2605-18918:end -->

<!-- books-review:SF-2026-ARXIV-2605-18930:start -->
<!-- existing:SF-2026-ARXIV-2605-18930:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18930:end -->
<!-- delta:SF-2026-ARXIV-2605-18930:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18930:end -->
<!-- books-review:SF-2026-ARXIV-2605-18930:end -->

<!-- books-review:SF-2026-ARXIV-2605-18991:start -->
<!-- existing:SF-2026-ARXIV-2605-18991:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-18991:end -->
<!-- delta:SF-2026-ARXIV-2605-18991:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18991:end -->
<!-- books-review:SF-2026-ARXIV-2605-18991:end -->

<!-- books-review:SF-2026-ARXIV-2605-19008:start -->
<!-- existing:SF-2026-ARXIV-2605-19008:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；正文主线 headings=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Batch、tokens 与 optimizer steps 不是同一计量']。<!-- existing:SF-2026-ARXIV-2605-19008:end -->
<!-- delta:SF-2026-ARXIV-2605-19008:start -->当前 pretraining 章有 optimizer/clip/rollback，尚缺 optimizer 之上的 bounded autonomous control envelope、action budget 与 human override；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-19008:end -->
<!-- books-review:SF-2026-ARXIV-2605-19008:end -->

<!-- books-review:SF-2026-ARXIV-2605-19049:start -->
<!-- existing:SF-2026-ARXIV-2605-19049:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-19049:end -->
<!-- delta:SF-2026-ARXIV-2605-19049:start -->当前 KV 章以 Transformer KV 为主，没有明确 linear-attention recurrent state 的 IO-aware buffering/placement owner；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-19049:end -->
<!-- books-review:SF-2026-ARXIV-2605-19049:end -->

<!-- books-review:SF-2026-ARXIV-2605-19099:start -->
<!-- existing:SF-2026-ARXIV-2605-19099:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Pairwise coupling 不能外推 group dynamics']。<!-- existing:SF-2026-ARXIV-2605-19099:end -->
<!-- delta:SF-2026-ARXIV-2605-19099:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19099:end -->
<!-- books-review:SF-2026-ARXIV-2605-19099:end -->

<!-- books-review:SF-2026-ARXIV-2605-19101:start -->
<!-- existing:SF-2026-ARXIV-2605-19101:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；正文主线 headings=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子', 'Data tags 也可能训练一条隐式控制策略', 'Quality filtering 在过滤什么', 'Synthetic data：从“先生成再打分”到 Specification Compilation']。<!-- existing:SF-2026-ARXIV-2605-19101:end -->
<!-- delta:SF-2026-ARXIV-2605-19101:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19101:end -->
<!-- books-review:SF-2026-ARXIV-2605-19101:end -->

<!-- books-review:SF-2026-ARXIV-2605-19127:start -->
<!-- existing:SF-2026-ARXIV-2605-19127:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-19127:end -->
<!-- delta:SF-2026-ARXIV-2605-19127:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19127:end -->
<!-- books-review:SF-2026-ARXIV-2605-19127:end -->

<!-- books-review:SF-2026-ARXIV-2605-19140:start -->
<!-- existing:SF-2026-ARXIV-2605-19140:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-19140:end -->
<!-- delta:SF-2026-ARXIV-2605-19140:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19140:end -->
<!-- books-review:SF-2026-ARXIV-2605-19140:end -->

<!-- books-review:SF-2026-ARXIV-2605-19151:start -->
<!-- existing:SF-2026-ARXIV-2605-19151:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-19151:end -->
<!-- delta:SF-2026-ARXIV-2605-19151:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19151:end -->
<!-- books-review:SF-2026-ARXIV-2605-19151:end -->

<!-- books-review:SF-2026-ARXIV-2605-19169:start -->
<!-- existing:SF-2026-ARXIV-2605-19169:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-19169:end -->
<!-- delta:SF-2026-ARXIV-2605-19169:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19169:end -->
<!-- books-review:SF-2026-ARXIV-2605-19169:end -->

<!-- books-review:SF-2026-ARXIV-2605-19192:start -->
<!-- existing:SF-2026-ARXIV-2605-19192:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-19192:end -->
<!-- delta:SF-2026-ARXIV-2605-19192:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19192:end -->
<!-- books-review:SF-2026-ARXIV-2605-19192:end -->

<!-- books-review:SF-2026-ARXIV-2605-19193:start -->
<!-- existing:SF-2026-ARXIV-2605-19193:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Pairwise coupling 不能外推 group dynamics']。<!-- existing:SF-2026-ARXIV-2605-19193:end -->
<!-- delta:SF-2026-ARXIV-2605-19193:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19193:end -->
<!-- books-review:SF-2026-ARXIV-2605-19193:end -->

<!-- books-review:SF-2026-ARXIV-2605-19196:start -->
<!-- existing:SF-2026-ARXIV-2605-19196:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-19196:end -->
<!-- delta:SF-2026-ARXIV-2605-19196:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19196:end -->
<!-- books-review:SF-2026-ARXIV-2605-19196:end -->

<!-- books-review:SF-2026-ARXIV-2605-19218:start -->
<!-- existing:SF-2026-ARXIV-2605-19218:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-19218:end -->
<!-- delta:SF-2026-ARXIV-2605-19218:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19218:end -->
<!-- books-review:SF-2026-ARXIV-2605-19218:end -->

<!-- books-review:SF-2026-ARXIV-2605-19228:start -->
<!-- existing:SF-2026-ARXIV-2605-19228:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-19228:end -->
<!-- delta:SF-2026-ARXIV-2605-19228:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19228:end -->
<!-- books-review:SF-2026-ARXIV-2605-19228:end -->

<!-- books-review:SF-2026-ARXIV-2605-19240:start -->
<!-- existing:SF-2026-ARXIV-2605-19240:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19240:end -->
<!-- delta:SF-2026-ARXIV-2605-19240:start -->Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents.<!-- delta:SF-2026-ARXIV-2605-19240:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19240:end -->

<!-- books-review:SF-2026-ARXIV-2605-19242:start -->
<!-- existing:SF-2026-ARXIV-2605-19242:start -->`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19242:end -->
<!-- delta:SF-2026-ARXIV-2605-19242:start -->We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training.<!-- delta:SF-2026-ARXIV-2605-19242:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19242:end -->

<!-- books-review:SF-2026-ARXIV-2605-19262:start -->
<!-- existing:SF-2026-ARXIV-2605-19262:start -->`books/part-06-ai-infrastructure/72-security.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19262:end -->
<!-- delta:SF-2026-ARXIV-2605-19262:start -->In this work, we present the first systematic study of training-time backdoor attacks on MDLMs.<!-- delta:SF-2026-ARXIV-2605-19262:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19262:end -->

<!-- books-review:SF-2026-ARXIV-2605-19269:start -->
<!-- existing:SF-2026-ARXIV-2605-19269:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19269:end -->
<!-- delta:SF-2026-ARXIV-2605-19269:start -->We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs.<!-- delta:SF-2026-ARXIV-2605-19269:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19269:end -->

<!-- books-review:SF-2026-ARXIV-2605-19276:start -->
<!-- existing:SF-2026-ARXIV-2605-19276:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19276:end -->
<!-- delta:SF-2026-ARXIV-2605-19276:start -->Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency.<!-- delta:SF-2026-ARXIV-2605-19276:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19276:end -->

<!-- books-review:SF-2026-ARXIV-2605-19282:start -->
<!-- existing:SF-2026-ARXIV-2605-19282:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19282:end -->
<!-- delta:SF-2026-ARXIV-2605-19282:start -->While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable.<!-- delta:SF-2026-ARXIV-2605-19282:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19282:end -->

<!-- books-review:SF-2026-ARXIV-2605-19314:start -->
<!-- existing:SF-2026-ARXIV-2605-19314:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19314:end -->
<!-- delta:SF-2026-ARXIV-2605-19314:start -->We study task-state misalignment, a task-level consistency failure in which the planner's active stage, runtime evidence, remembered context, and delegated executor no longer justify the same next-step decision.<!-- delta:SF-2026-ARXIV-2605-19314:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19314:end -->

<!-- books-review:SF-2026-ARXIV-2605-19319:start -->
<!-- existing:SF-2026-ARXIV-2605-19319:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19319:end -->
<!-- delta:SF-2026-ARXIV-2605-19319:start -->In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout.<!-- delta:SF-2026-ARXIV-2605-19319:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19319:end -->

<!-- books-review:SF-2026-ARXIV-2605-19321:start -->
<!-- existing:SF-2026-ARXIV-2605-19321:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19321:end -->
<!-- delta:SF-2026-ARXIV-2605-19321:start -->In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference.<!-- delta:SF-2026-ARXIV-2605-19321:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19321:end -->

<!-- books-review:SF-2026-ARXIV-2605-19328:start -->
<!-- existing:SF-2026-ARXIV-2605-19328:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19328:end -->
<!-- delta:SF-2026-ARXIV-2605-19328:start -->We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility.<!-- delta:SF-2026-ARXIV-2605-19328:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19328:end -->

<!-- books-review:SF-2026-ARXIV-2605-19335:start -->
<!-- existing:SF-2026-ARXIV-2605-19335:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19335:end -->
<!-- delta:SF-2026-ARXIV-2605-19335:start -->We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows.<!-- delta:SF-2026-ARXIV-2605-19335:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19335:end -->

<!-- books-review:SF-2026-ARXIV-2605-19341:start -->
<!-- existing:SF-2026-ARXIV-2605-19341:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19341:end -->
<!-- delta:SF-2026-ARXIV-2605-19341:start -->To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world.<!-- delta:SF-2026-ARXIV-2605-19341:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19341:end -->

<!-- books-review:SF-2026-ARXIV-2605-19373:start -->
<!-- existing:SF-2026-ARXIV-2605-19373:start -->已逐章读取 `books/part-06-ai-infrastructure/59-model-registry.md` 与相邻章节 ['books/part-06-ai-infrastructure/58-kubeflow.md', 'books/part-06-ai-infrastructure/60-training-operator.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies` 改变的 state/data/control/evidence boundary。 owner_sha256=7691a4f16c4ed6ecd5e5eb8487324292df7cfb82b3c10aee71730bc70a0f4290。<!-- existing:SF-2026-ARXIV-2605-19373:end -->
<!-- delta:SF-2026-ARXIV-2605-19373:start -->Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies 提出的具体变化是：To resolve this, we present a two-layer architecture -- CRDTMergeState -- that wraps any merge strategy in a CRDT-compliant (Conflict-Free Replicated Data Type) layer. 摘要中的长期系统挑战为：distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations。它可能改变 `PLATFORM-MODEL-REGISTRY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We prove that this separation guarantees Strong Eventual Consistency: all replicas receiving the same contributions compute identical merged models, regardless of message ordering.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-19373:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-19373:end -->

<!-- books-review:SF-2026-ARXIV-2605-19407:start -->
<!-- existing:SF-2026-ARXIV-2605-19407:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19407:end -->
<!-- delta:SF-2026-ARXIV-2605-19407:start -->We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime.<!-- delta:SF-2026-ARXIV-2605-19407:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19407:end -->

<!-- books-review:SF-2026-ARXIV-2605-19444:start -->
<!-- existing:SF-2026-ARXIV-2605-19444:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19444:end -->
<!-- delta:SF-2026-ARXIV-2605-19444:start -->We argue these gains are systematically misinterpreted: most reflect sharpening of already-solvable problems rather than genuine learning, while problems corrupted from correct to incorrect outnumber truly learned ones, and this damage is irreversible once majority vote locks onto a wrong answer.<!-- delta:SF-2026-ARXIV-2605-19444:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19444:end -->

<!-- books-review:SF-2026-ARXIV-2605-19447:start -->
<!-- existing:SF-2026-ARXIV-2605-19447:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19447:end -->
<!-- delta:SF-2026-ARXIV-2605-19447:start -->We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework.<!-- delta:SF-2026-ARXIV-2605-19447:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19447:end -->

<!-- books-review:SF-2026-ARXIV-2605-19461:start -->
<!-- existing:SF-2026-ARXIV-2605-19461:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19461:end -->
<!-- delta:SF-2026-ARXIV-2605-19461:start -->We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions.<!-- delta:SF-2026-ARXIV-2605-19461:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19461:end -->

<!-- books-review:SF-2026-ARXIV-2605-19478:start -->
<!-- existing:SF-2026-ARXIV-2605-19478:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19478:end -->
<!-- delta:SF-2026-ARXIV-2605-19478:start -->While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored.<!-- delta:SF-2026-ARXIV-2605-19478:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19478:end -->

<!-- books-review:SF-2026-ARXIV-2605-19481:start -->
<!-- existing:SF-2026-ARXIV-2605-19481:start -->已顺读 `books/part-05-inference-system/55-pd-disaggregation.md` 与相邻章节 ['books/part-05-inference-system/54-gpu-memory.md', 'books/part-05-inference-system/56-inference-scheduling.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19481:end -->
<!-- delta:SF-2026-ARXIV-2605-19481:start -->Leveraging this capability, we present C2CServe, a request-granularity serverless LLM serving system that allows MIG instances to switch models across requests without reloading weights into HBM.<!-- delta:SF-2026-ARXIV-2605-19481:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19481:end -->

<!-- books-review:SF-2026-ARXIV-2605-19537:start -->
<!-- existing:SF-2026-ARXIV-2605-19537:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19537:end -->
<!-- delta:SF-2026-ARXIV-2605-19537:start -->While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation.<!-- delta:SF-2026-ARXIV-2605-19537:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19537:end -->

<!-- books-review:SF-2026-ARXIV-2605-19576:start -->
<!-- existing:SF-2026-ARXIV-2605-19576:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19576:end -->
<!-- delta:SF-2026-ARXIV-2605-19576:start -->Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation.<!-- delta:SF-2026-ARXIV-2605-19576:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19576:end -->

<!-- books-review:SF-2026-ARXIV-2605-19593:start -->
<!-- existing:SF-2026-ARXIV-2605-19593:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19593:end -->
<!-- delta:SF-2026-ARXIV-2605-19593:start -->In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption.<!-- delta:SF-2026-ARXIV-2605-19593:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19593:end -->

<!-- books-review:SF-2026-ARXIV-2605-19604:start -->
<!-- existing:SF-2026-ARXIV-2605-19604:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19604:end -->
<!-- delta:SF-2026-ARXIV-2605-19604:start -->We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state.<!-- delta:SF-2026-ARXIV-2605-19604:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19604:end -->

<!-- books-review:SF-2026-ARXIV-2605-19722:start -->
<!-- existing:SF-2026-ARXIV-2605-19722:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19722:end -->
<!-- delta:SF-2026-ARXIV-2605-19722:start -->We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B.<!-- delta:SF-2026-ARXIV-2605-19722:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19722:end -->

<!-- books-review:SF-2026-ARXIV-2605-19755:start -->
<!-- existing:SF-2026-ARXIV-2605-19755:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-19755:end -->
<!-- delta:SF-2026-ARXIV-2605-19755:start -->Exact-v1 的 source-specific delta 是：方案扩展 CycloneDX，记录 AI provenance、model lineage、disclosure metadata，并用组件 hash、签名、容器运行态和 agent 生成的环境记录绑定 artifact；自动化流水线负责环境发现、漏洞富化、schema 校验和 reproducibility audit，材料不全时保留 partial-attestation 状态。 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-19755:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-19755:end -->

<!-- books-review:SF-2026-ARXIV-2605-19769:start -->
<!-- existing:SF-2026-ARXIV-2605-19769:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19769:end -->
<!-- delta:SF-2026-ARXIV-2605-19769:start -->We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents.<!-- delta:SF-2026-ARXIV-2605-19769:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19769:end -->

<!-- books-review:SF-2026-ARXIV-2605-19775:start -->
<!-- existing:SF-2026-ARXIV-2605-19775:start -->`books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19775:end -->
<!-- delta:SF-2026-ARXIV-2605-19775:start -->By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics.<!-- delta:SF-2026-ARXIV-2605-19775:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19775:end -->

<!-- books-review:SF-2026-ARXIV-2605-19779:start -->
<!-- existing:SF-2026-ARXIV-2605-19779:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19779:end -->
<!-- delta:SF-2026-ARXIV-2605-19779:start -->We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing.<!-- delta:SF-2026-ARXIV-2605-19779:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19779:end -->

<!-- books-review:SF-2026-ARXIV-2605-19811:start -->
<!-- existing:SF-2026-ARXIV-2605-19811:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19811:end -->
<!-- delta:SF-2026-ARXIV-2605-19811:start -->In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods.<!-- delta:SF-2026-ARXIV-2605-19811:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19811:end -->

<!-- books-review:SF-2026-ARXIV-2605-19847:start -->
<!-- existing:SF-2026-ARXIV-2605-19847:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19847:end -->
<!-- delta:SF-2026-ARXIV-2605-19847:start -->We show that this framing understates leakage under same-index account collusion.<!-- delta:SF-2026-ARXIV-2605-19847:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19847:end -->

<!-- books-review:SF-2026-ARXIV-2605-19893:start -->
<!-- existing:SF-2026-ARXIV-2605-19893:start -->已顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19893:end -->
<!-- delta:SF-2026-ARXIV-2605-19893:start -->We present SSV, a sparse speculative-verification framework that turns dynamic sparse attention into a verification-oriented workload.<!-- delta:SF-2026-ARXIV-2605-19893:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19893:end -->

<!-- books-review:SF-2026-ARXIV-2605-19932:start -->
<!-- existing:SF-2026-ARXIV-2605-19932:start -->已顺读 `books/part-07-agent/75-context.md` 与相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19932:end -->
<!-- delta:SF-2026-ARXIV-2605-19932:start -->We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context.<!-- delta:SF-2026-ARXIV-2605-19932:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19932:end -->

<!-- books-review:SF-2026-ARXIV-2605-19945:start -->
<!-- existing:SF-2026-ARXIV-2605-19945:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19945:end -->
<!-- delta:SF-2026-ARXIV-2605-19945:start -->We propose GEM, GPU-variability-aware Expert Mapping, a framework for GPU variability-aware expert to GPU mapping for MoE models.<!-- delta:SF-2026-ARXIV-2605-19945:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19945:end -->

<!-- books-review:SF-2026-ARXIV-2605-19952:start -->
<!-- existing:SF-2026-ARXIV-2605-19952:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19952:end -->
<!-- delta:SF-2026-ARXIV-2605-19952:start -->To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning.<!-- delta:SF-2026-ARXIV-2605-19952:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19952:end -->

<!-- books-review:SF-2026-ARXIV-2605-19999:start -->
<!-- existing:SF-2026-ARXIV-2605-19999:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19999:end -->
<!-- delta:SF-2026-ARXIV-2605-19999:start -->Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs.<!-- delta:SF-2026-ARXIV-2605-19999:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19999:end -->

<!-- books-review:SF-2026-ARXIV-2605-20005:start -->
<!-- existing:SF-2026-ARXIV-2605-20005:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20005:end -->
<!-- delta:SF-2026-ARXIV-2605-20005:start -->We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss.<!-- delta:SF-2026-ARXIV-2605-20005:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20005:end -->

<!-- books-review:SF-2026-ARXIV-2605-20022:start -->
<!-- existing:SF-2026-ARXIV-2605-20022:start -->已顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20022:end -->
<!-- delta:SF-2026-ARXIV-2605-20022:start -->Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel.<!-- delta:SF-2026-ARXIV-2605-20022:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20022:end -->

<!-- books-review:SF-2026-ARXIV-2605-20023:start -->
<!-- existing:SF-2026-ARXIV-2605-20023:start -->`books/part-07-agent/84-agent-platform.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20023:end -->
<!-- delta:SF-2026-ARXIV-2605-20023:start -->Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced.<!-- delta:SF-2026-ARXIV-2605-20023:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20023:end -->

<!-- books-review:SF-2026-ARXIV-2605-20051:start -->
<!-- existing:SF-2026-ARXIV-2605-20051:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20051:end -->
<!-- delta:SF-2026-ARXIV-2605-20051:start -->Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design.<!-- delta:SF-2026-ARXIV-2605-20051:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20051:end -->

<!-- books-review:SF-2026-ARXIV-2605-20061:start -->
<!-- existing:SF-2026-ARXIV-2605-20061:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20061:end -->
<!-- delta:SF-2026-ARXIV-2605-20061:start -->To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning.<!-- delta:SF-2026-ARXIV-2605-20061:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20061:end -->

<!-- books-review:SF-2026-ARXIV-2605-20084:start -->
<!-- existing:SF-2026-ARXIV-2605-20084:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20084:end -->
<!-- delta:SF-2026-ARXIV-2605-20084:start -->In this work, we develop BalanceRAG to certify threshold pairs at a target risk level.<!-- delta:SF-2026-ARXIV-2605-20084:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20084:end -->

<!-- books-review:SF-2026-ARXIV-2605-20179:start -->
<!-- existing:SF-2026-ARXIV-2605-20179:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20179:end -->
<!-- delta:SF-2026-ARXIV-2605-20179:start -->In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block.<!-- delta:SF-2026-ARXIV-2605-20179:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20179:end -->

<!-- books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->
<!-- existing:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->`books/part-04-training-system/36-distributed-training.md` 已以更一般的 TRAIN-DISTRIBUTED-TRAINING 演进链承载 `DynaTrain: Fast Online Parallelism Switching for Elastic LLM Training` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->
<!-- delta:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->We present DynaTrain, a distributed training system for sub-second, online reconfiguration across arbitrary multi-dimensional parallelism.<!-- delta:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->

<!-- books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->
<!-- existing:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；owner 当前主干包含 ['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->
<!-- delta:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->Coding agents accumulate extensive context during long-running tasks, yet fixed context windows force practitioners to choose between truncation and task failure.<!-- delta:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->

<!-- books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->
<!-- existing:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 PLATFORM-EVALUATION-SYSTEM 演进链承载 `Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->
<!-- delta:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->We introduce a framework for automated benchmark generation.<!-- delta:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->

<!-- books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->
<!-- existing:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->`books/part-04-training-system/27-data.md` 已以更一般的 TRAIN-DATA 演进链承载 `How Faithful Is Trajectory-Based Data Attribution? Error Sources, Remedies, and Practical Guidelines` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->
<!-- delta:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->We propose AdamW-influence to fully account for AdamW's optimization dynamics, yielding improvements from 10% to over 300% in Spearman correlation between estimated and ground-truth influence across four settings spanning MLP, CNN, GPT-2, and Llama 3.2-1B.<!-- delta:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->

<!-- books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->
<!-- existing:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->已读取 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；owner 当前主干包含 ['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->
<!-- delta:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->We present INAR-VL, a lightweight edge-cloud routing system for multimodal inference in a two-tier deployment.<!-- delta:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->

<!-- books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->
<!-- existing:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 已以更一般的 INFER-KV-CACHE 演进链承载 `Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->
<!-- delta:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->We show that different token types within a prompt, including system prompts, user queries, tool outputs, model responses, and chain-of-thought reasoning, exhibit up to 756x variation in reuse rates, yet no existing eviction policy exploits this signal.<!-- delta:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->

<!-- books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->
<!-- existing:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 PLATFORM-EVALUATION-SYSTEM 演进链承载 `PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->
<!-- delta:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->We present PASC (Pipeline-Aware Split Conformal), which reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score.<!-- delta:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->

<!-- books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->
<!-- existing:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；owner 当前主干包含 ['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->
<!-- delta:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->We formulate late-stage checkpoint selection as a stability-aware decision problem under evaluation uncertainty and propose a progressive framework combining pointwise filtering, listwise ranking, and pairwise refinement.<!-- delta:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->
<!-- existing:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；owner 当前主干包含 ['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->
<!-- delta:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->We present Spherical KV, a long-context inference method that treats KV allocation as a rate-distortion problem grounded in attention geometry for efficient decoding.<!-- delta:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->

### Legacy V2.1 — Semantic Audit

<!-- legacy-validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260520-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260520 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260520-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260520-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=75；selected=3；all others retain completed reviews | passed |
| SA-20260520-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

### Legacy V2.1 — Ignored Noise

- Pre-denominator closures=652；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

### Legacy V2.1 — Recommended Action

本日全部 Gate 已闭合，无进一步动作。

### Legacy V2.1 — Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260520/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260520/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-20.md`
- Books body: no change for the recovered families on this date.

### Legacy V2.1 — Open Questions

- 无。

### Legacy V2.1 — Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

### Legacy V2.1 — Final Status

Legacy Completion Status: Complete under V2.1 only; superseded by the current V3 Complete result above.
