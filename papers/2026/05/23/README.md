# Daily Research — 2026-05-23

**规范：** V3
**窗口：** 2026-05-22T09:00:00+08:00 ～ 2026-05-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-21T09:06:25+08:00

**补充窗口：** 2026-05-22 ～ 2026-05-22
**窗口说明：** 用户授权保留旧小时窗、原3候选完整行/日期评分及连续有效旧§4，只补前一北京时间完整自然日的遗漏；旧归属不搬移。旧完成声明与旧来源原件仅承载历史小时窗，本轮结果按当前合同重新验收，不沿用旧arXiv 08:00排除或Anthropic精确时刻缺口。

## 1. 结论

本日补查恢复了旧小时窗漏掉的08:00 arXiv公告及两篇Anthropic日期级官方文章。研究重点是把不同证据接口分开：语言指代与视觉定位、引用候选与时间精测、瞬态内容与稳定语义身份、模型评分与真实artifact/状态，以及训练对手人口与物理交互条件。局部负面结果不能被总体分数或“单次调用”“冻结权重”“已匹配能量”替代。

本轮新增27项（25个arXiv家族及2篇Anthropic）＝17项实际Books整合＋8项具体已有覆盖＋2项中心主张争议；旧3项不搬移、不重评分，合30项＝19整合＋9已有覆盖＋2争议。17项新增正文/完整直接两侧/本人注均经独立一次实际POST通过，9个唯一owner均无待写窄位。早期21项封口已被局部false-negative校准纠正，不以工作量维持旧数量。完整证据和精确停点见[唯一作者记录](../_sources/daily-20260523/SUP_SOURCES_20261020.md)及[独立复核](../_sources/daily-20260523/SUP_REVIEW_20261020.md)。

旧3项的有效Source/POST分层复用：VeOmni #779→Ch40、#781→Ch39已整合，Hy-MT2 #1的完整variant identity由Ch66覆盖。下方连续旧§4前三项及其旧收据保留历史时态，不表示本次作者未改Books。本轮没有启动Live、Weekly或2025，也未stage/commit/push。

原宽库存只作主题查漏，不成为全量逐项队列；实际42个具名完整题摘经两入口准入及局部纠错，另定点读一篇安全评价的决定协议。21553 TONIC与21565 SPCL存在跨日公开资格区间，22183 AVP官方撤回，均不作为本窗候选/评分/Books。Meta/Google/MiMo日级目录和Precise公开资格限制仍被隔离，完成不等于互联网无遗漏或所有主张成立。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 官方Research/RSS旧同身份条目覆盖05-22；补读08:00的Gartner认定与Virgin Atlantic两页核心，下一条05-25即停。reader实际核心抽检通过。 | 已检查 | 两项无本篇新增机制/受控边界，贡献关闭；不是旧小时窗时间排除。 |
| `SRC-ANTHROPIC` | 官方Research两篇May22全文实际读完；日期口径直接落自然日。snapshot属于自身，不替代文章日期。 | 已检查 | 两项候选具体已有覆盖；不再请求不必要时分秒。 |
| `SRC-GOOGLE-AI` | 复用DeepMind Research/Blog05-19→05-28相邻日期；本轮实际打开Google Publications，停于仍仅年/venue的记录。 | 受阻 | 日级完整历史目录不可由年/venue补造，需官方日公告/相应archive。 |
| `SRC-META-AI` | 官方Research/Publications本轮有限重开，仍明确content unavailable，未把空响应作零更新。 | 受阻 | 可读官方日期目录/等价同期archive。 |
| `SRC-QWEN` | 复用官方EN/ZH article API各37项完整列表及05-20→05-29相邻记录，无需重抓未变目录。 | 已检查 | 无新增具名日级线索；不声称全网零遗漏。 |
| `SRC-DEEPSEEK` | 复用官方News/Research04-24→06-24相邻记录，停止于覆盖目标日的相邻界。 | 已检查 | 无新增具名线索。 |
| `SRC-MOONSHOT` | Kimi Blog旧日目录及kimi-code有效公开/关闭层复用；早段官方org PR-created/commit-date搜索各0，page1/count<100即停。 | 已检查 | 当前索引不能证明删失/私转公全历史，未用repo创建时间推公开。 |
| `SRC-TENCENT-HUNYUAN` | publicList全部5项日期均非05月、Hy-MT2旧有效层复用；早段org两类搜索各0。Precise当前官方repo/news有限恢复。 | 受阻 | 其余已处理；Precise只有repo created/可回填commit与09月news，缺May22公开证据，只隔离该family。 |
| `SRC-ZAI` | 官方Research05-20→06-16与旧小时窗Synapse普通事件关闭层复用；补早段org两类搜索各0。 | 已检查 | 62是旧小时窗计数，不冒充整日分母或新增release。 |
| `SRC-BYTEDANCE-SEED` | Research/PublicPapers05-16→05-29与旧有效事件复用；早段org PR1=#778、commit1=#772，均读完整核心/身份，page1已穷尽。 | 已检查 | #772先前已公开、仅merge不新计；#778本日封装/实际ViT测试纠错，贡献关闭不等同#779身份。 |
| `SRC-BAIDU-ERNIE` | 官方有日Blog止05-09；早段精确PaddlePaddle/ERNIE repo两类搜索各0，旧小时窗事件层复用。 | 已检查 | 零仅属明确查询；不从旧commit=0推早段。 |
| `SRC-XIAOMI-MIMO` | 当前官方Paper/Blog实际打开，已知有日论文03-13→06-29；早段org两类搜索各0。 | 受阻 | Blog卡未标日，不能据此证明未标日条目不存在。 |
| `SRC-MINIMAX` | EN/ZH/Agent Tech Blog03-18→05-26/27相邻目录复用；旧2个CLI维护事件关闭层、早段org两类搜索各0。 | 已检查 | 2是旧小时窗计数；不推全历史公开完整性。 |
| `SRC-ARXIV` | 仅本日主题查漏；复用05-22报告254个既有身份作去重、不迁移。原42完整AB，其中安全代表项另定点读决定段；新25个精确v1逐项ABS/DC核，公告前不发号规则与findable/arxiv.content/registered联合限定日。 | 已检查 | 两个跨日资格单独受阻、1官方撤回；月库存不作逐项队列，未声明无遗漏。 |

早段补查为UTC05-21T16:00～05-22T00:59:59（北京时间05-22 00:00～08:59:59），官方GitHub Search按七个具名org/repo分别查committer-date与PR created，全部page1/per_page100、incomplete=false、count<100；精确q、执行时间、原件与停止见[作者A8](../_sources/daily-20260523/SUP_SOURCES_20261020.md#a8--机构源自然日差额原始查询与停止)。旧[`source-coverage-v3.json`](../_sources/daily-20260523/source-coverage-v3.json)仍只标原小时窗，不以其arXiv0/Anthropic时刻限制支撑本轮结论。Daily之外每周来源未扫描；必要原始论文/对应repo按需打开，不扩机构全站。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [VeOmni PR #779 — host-side multimodal metadata precompute](https://github.com/ByteDance-Seed/VeOmni/pull/779) | 2026-05-22T09:04:11+08:00 | 把 qwen2-family ViT 的 varlen/window metadata 从 GPU forward 中的 D2H 同步移至可复算的 host collator producer/consumer contract；`2 + 2 + 2 = 6` | 深入完成 | 整合：`TRAIN-MEGATRON`，[第40章](../../../../books/part-04-training-system/40-megatron.md)，root 写回已通过 fresh 写后语义复核 |
| [VeOmni PR #781 — HSDP accumulation sync elision](https://github.com/ByteDance-Seed/VeOmni/pull/781) | 2026-05-22T10:37:48+08:00 | HSDP 的 sharded `reduce_scatter` 每个 micro-step 保留，而 replicated `all_reduce` 仅最后一步需要；`2 + 2 + 3 = 7` | 深入完成 | 整合：`TRAIN-ZERO`，[第39章](../../../../books/part-04-training-system/39-zero.md)，root 写回已通过 fresh 写后语义复核 |
| [Hy-MT2 PR #1 — multilingual evaluator identity correction](https://github.com/Tencent-Hunyuan/Hy-MT2/pull/1) | 2026-05-22T18:20:42+08:00 | 同一 `md5` 可对应多个 `instruction_lang` 时，response join 必须使用复合 item identity，legacy fallback 要显式隔离且 coverage 按 test item 计算；评价纠错触发深入审阅；`2 + 2 + 2 = 6` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Measuring LLMs’ ability to develop exploits](https://www.anthropic.com/research/exploit-evals) | 2026-05-22 | PoC到端到端exploit需分阶段程序验证，并绑定harness、mitigation与尝试预算；`2 + 2 + 3 = 7` | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章“从答案评分到可执行证据”](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据) |
| [Project Glasswing: An initial update](https://www.anthropic.com/research/glasswing-initial-update) | 2026-05-22 | 模型估计、人工确认、披露和修补必须分账，发现吞吐不等于修补吞吐；`2 + 2 + 2 = 6` | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[第72章](../../../../books/part-06-ai-infrastructure/72-security.md)的proposal/reproduction/disclosure与维护者负担论证 |
| [AttuneBench: A Conversation-Based Benchmark for LLM Emotional Intelligence](https://arxiv.org/abs/2605.21739v1) | 2026-05-22 | 识别情绪、本人偏好与第三方response quality不构成一个排序；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MM-Conv: A Multimodal Dataset and Benchmark for Context-Aware Grounding in 3D Dialogue](https://arxiv.org/abs/2605.21796v1) | 2026-05-22 | 历史指代重写与当前视觉定位分责，保额外对象清单；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions](https://arxiv.org/abs/2605.21827v1) | 2026-05-22 | vague intensity的动作幅度依赖给定state与容量，而非固定词典顺序；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[第78章](../../../../books/part-07-agent/78-tool-calling.md) |
| [Thermo-VL: Extending Vision-Language Models to Thermal Infrared Perception](https://arxiv.org/abs/2605.21882v1) | 2026-05-22 | 冻结RGB接口可消费query-conditioned thermal残差，但行为不自动不变；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Foresee-to-Ground: From Predictive Temporal Perception to Evidence-Driven Reasoning for Video Temporal Grounding](https://arxiv.org/abs/2605.21973v1) | 2026-05-22 | proposal引用与局部时间精测可在同一structured response分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Diverse Yet Consistent: Context-Guided Diffusion with Energy-Based Joint Refinement for Multi-Agent Motion Prediction](https://arxiv.org/abs/2605.22017v1) | 2026-05-22 | joint energy重加权的marginal与训练定义需另证；2 + 1 + 2 = 5 | 争议 | 暂缓：Eq18–19中心定义未闭合，见§4/5 |
| [OPERA: An Agent for Image Restoration with End-to-End Joint Planning-Execution Optimization](https://arxiv.org/abs/2605.22104v1) | 2026-05-22 | complete-plan优化与可微toolchain终态梯度拥有不同接口；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[第81章](../../../../books/part-07-agent/81-workflow.md) |
| [Relational Linear Properties in Language Models: An Empirical Investigation](https://arxiv.org/abs/2605.22532v1) | 2026-05-22 | 拟合模型分布≠GT，CSS collapse与KL符号冲突限制linear probe解释；2 + 1 + 2 = 5 | 争议 | 暂缓：v1 PDF/HTML Eq8与minimize冲突，见§4/5 |
| [Enhancing Gaze Reasoning in Vision Foundation Models for Gaze Following](https://arxiv.org/abs/2605.22607v1) | 2026-05-22 | head-conditioned软LoRA gate与中间gaze-evidence OOC监督分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance](https://arxiv.org/abs/2605.22664v1) | 2026-05-22 | 当前数值正确可掩盖硬编码/公式依赖错误；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SceneGraphGrounder: Zero-Shot 3D Visual Grounding via Structured Scene Graph Matching](https://arxiv.org/abs/2605.21788v1) | 2026-05-22 | marker关系lift、query graph软映射与有条件view tie-break；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Hypergraph as Language](https://arxiv.org/abs/2605.21858v1) | 2026-05-22 | 显式vertex/hyperedge共同归属不能由pairwise展开完整替代；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization](https://arxiv.org/abs/2605.21948v1) | 2026-05-22 | 语义防御sensor在域/攻击家族外漏检，不由无害标签认证排序完整性；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[第72章](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Format-Constraint Coupling in Knowledge Graph Construction from Statistical Tables](https://arxiv.org/abs/2605.21974v1) | 2026-05-22 | serialization与schema非独立，检索QA可掩盖graph value-binding错；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-RAG`，[第76章](../../../../books/part-07-agent/76-rag.md) |
| [EasyVFX: Frequency-Driven Decoupling for Resource-Efficient VFX Generation](https://arxiv.org/abs/2605.22051v1) | 2026-05-22 | 共享FEI软路由LoRA与每reference仅条件tokens适配分责；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[第24章](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [What are the Right Symmetries for Formal Theorem Proving?](https://arxiv.org/abs/2605.22257v1) | 2026-05-22 | 证明rewrite等变与搜索success invariance不同，极限覆盖不等有限budget保证；2 + 2 + 3 = 7 | 深入完成 | 整合：`AGENT-PLANNING`，[第79章](../../../../books/part-07-agent/79-planning.md) |
| [Supervised Classification Heads as Semantic Prototypes: Unlocking Vision-Language Alignment via Weight Recycling](https://arxiv.org/abs/2605.22484v1) | 2026-05-22 | 同冻结feature坐标的监督head/class-name可作配对anchor；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [COCOTree: A Dataset and Benchmark for Open Tree-Structured Visual Decomposition](https://arxiv.org/abs/2605.22068v1) | 2026-05-22 | mask/label/部分层级结构的复合metric需独立扰动审计；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation](https://arxiv.org/abs/2605.22536v1) | 2026-05-22 | 较强空间任务能力与明确退化提示均不认证当前输入可靠；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Flat-Pack Bench: Evaluating Spatio-Temporal Understanding in Large Vision-Language Models through Furniture Assembly](https://arxiv.org/abs/2605.21625v1) | 2026-05-22 | 视觉part-ID/视频移除与编号shuffle揭示时间利用和identity捷径；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FLUID: From Ephemeral IDs to Multimodal Semantic Codes for Industrial-Scale Livestreaming Recommendation](https://arxiv.org/abs/2605.21832v1) | 2026-05-22 | 短寿命ID迁移须分transient/stable语义码与consumer预热；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[第23章](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [LLM Retrieval for Stable and Predictable Ad Recommendations](https://arxiv.org/abs/2605.21969v1) | 2026-05-22 | shadow小扰动稳定性须与检索正确/语义保持分验；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [From Recognition to Reasoning: Benchmarking and Enhancing MLLMs on Real-World Receipt Document Understanding](https://arxiv.org/abs/2605.22413v1) | 2026-05-22 | 字段相似、数值/结构保真和reward改善不等价；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.22748v1) | 2026-05-22 | 训练对手人口/集合encoder/物理交互修正单机与同伙伴泛化判断；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[第26章](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts](https://arxiv.org/abs/2605.22720v1) | 2026-05-22 | balance framing与规范目标可冲突，但adaptive propensity不识别单一prompt因果；2 + 1 + 2 = 5 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[第66章](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

旧小时窗逐项 raw ledger 见 [`screening-ledger-v3.json`](../_sources/daily-20260523/screening-ledger-v3.json)，三项原候选完整行/日期评分保持；Kimi Code/#780/#784旧关闭层有效，不作为本轮新候选数。新增25个arXiv身份/日期与必要证据见[本日唯一补充记录](../_sources/daily-20260523/SUP_SOURCES_20261020.md)，逐项ABS/精确DOI原字段与合证分开，不以submitted或created改名公开时间。官方撤回22183与跨日21553/21565仅列§5，未进表。

## 4. 证据与知识整合

### [VeOmni PR #779 — host-side multimodal metadata precompute](https://github.com/ByteDance-Seed/VeOmni/pull/779)

采用 exact event `PR #779` 与 merge commit `d13637a1c8266c4a6b6a14a07923392e91ccbf9a`。PR 的 “What does this PR do?”/“Design & Code Changes” 明示：collator 从 packed `grid_thw` 在 host 侧导出 `cu_seqlens`、`window_index` 与 max-seqlen；ViT forward 消费 versioned `vit_metadata`，未提供 metadata 时保留 runtime fallback。评价证据是单台 A100 上 sync gate `18/18`、同模型 metadata/fallback logits `rtol=0, atol=0`、Qwen lineage logits `26/26`；它没有报告端到端 step time、CPU collator cost、多节点 scale 或生产 tail。配置依赖的 host port 可能漂移，剩余 HF rotary/mRoPE sync 仍被 allowlist；fallback 是恢复 device-side metadata 计算。第40章已说明 multimodal encoder 会改变真实 layout，却未说明“把 layout metadata 作为 host producer/device consumer 的显式合同，并用等价 gate 防止 silent divergence”，故形成精确 Integrate；root 的 paired binding 已通过 fresh 写后语义复核。

### [VeOmni PR #781 — HSDP accumulation sync elision](https://github.com/ByteDance-Seed/VeOmni/pull/781)

采用 exact event `PR #781` 与 merge commit `4c42062b6bf68a68c8b009764eec0de929c7a3d3`。PR 核心说明 HSDP 梯度需要 sharded 维的 `reduce_scatter` 与 replicated 维的 `all_reduce`；gradient accumulation 时后者只在最后 micro-step 才是必要同步。披露日志绑定 Qwen3.5-35B-A3B、FSDP2、offload、EP=8、MBS=1、GBS=128，三个 iteration 的总时间由 24:25 到 24:03；节点/GPU 数、重复次数和统计不确定性未披露，因此不采用通用加速数字，只采用通信时序机制。若 accumulation boundary、replica membership 或 gradient reduction convention 不一致，延后同步会造成 silent divergence；fallback 是每个 micro-step 完整同步。第39章只说 accumulation boundary 会影响 reduce-scatter timing，尚未分离 HSDP 的 shard/replica 两个 collective 维度，故形成精确 Integrate；root 的 paired binding 已通过 fresh 写后语义复核。

### [Hy-MT2 PR #1 — multilingual evaluator identity correction](https://github.com/Tencent-Hunyuan/Hy-MT2/pull/1)

采用 exact event `PR #1` 与 merge commit `fd271bebbe493144a1f4c258cc9be07c80db5e03`。补丁给 scorer entry 增加 `instruction_lang`，把 response map 从 `{md5: response}` 改为 `{(md5, instruction_lang): response}`，仅为旧输入保留显式 md5-only fallback，并把 coverage 从 unique-md5 intersection 改为 matched test-items / test-data。采用命题不是某个 benchmark 分数，而是 evaluator join 必须保存完整 item variant identity：否则同一内容 hash 的不同语言版本会覆盖或误接 response，在所有行仍合法时静默污染语言切片与 coverage。

该机制只由 IFMTBench 的 exact patch 支持；PR 未披露受影响行数、修正前后分数、重复语言数量或受控 regression，因此不采用影响幅度或 benchmark-wide 提升。复合 key 增加 schema/ingestion 要求；md5-only fallback 会掩盖缺失语言并重新折叠 variant。安全 fallback 是仅在证明 hash 唯一或显式 legacy schema 时启用 md5-only，否则把条目标为 missing/unscorable 并保留 raw response。唯一 owner 是 `PLATFORM-EVALUATION-SYSTEM`：第66章已要求贯穿 cohort 到 analysis artifact 的完整 run identity、保存 per-example 与 language/region slice，并在跨语言派生 benchmark 中保留 label/choice identity、language-specific invalid cases 与 source-to-target lineage；这些具体命题已直接排除 content-only join，因此判定 `No Change — Existing Coverage`，不生成 root Books queue。

完整 Evidence 与 non-proof locator 见 [`exact-v1-evidence-v3.json`](../_sources/daily-20260523/exact-v1-evidence-v3.json)，现有正文对读见 [`books-current-content-comparison-v3.json`](../_sources/daily-20260523/books-current-content-comparison-v3.json)。两项写回及 root-applied 状态见 [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260523/BOOKS_WRITEBACK_QUEUE_V3.json)；本次 repair author 没有写共享 Books。

### [Measuring LLMs’ ability to develop exploits](https://www.anthropic.com/research/exploit-evals)

补充自然日新增。官方页面日期05-22；采用本次保存的全文，原件与独核见[补充A1](../_sources/daily-20260523/SUP_SOURCES_20261020.md#a1--首批语义校准日期与已准备好的两篇)。ExploitBench以16能力/五tier分离触发漏洞、构建原语和取得控制，低层使用patched差分，高层使用随机heap challenge-response，另查作弊；41个已修漏洞、相同300-turn harness的baseline/nudged各三次不等于无限预算。ExploitGym要求动态flag与intended-vulnerability判断同时满足；其两小时、关闭mitigation、各厂商推荐harness的比较不能只归权重。SCONE仅12个cutoff后案例、模拟收益与Best@8，不能外推真实收入或全域攻击能力。

这里采用“实际可执行目标与阶段验证不可被PoC替代、评价条件必须绑定”的命题，不采用厂商通用能力排名。第66章既有`artifact + environment + execution trace`、真实触发目标、N-day软件/patch/network/time/success冻结及verifier可错论证已直接承载；16项协议只是本例具体化，不必再造正文。reader已实际核Source与具体已有覆盖；未运行攻击、未复现实验。

### [Project Glasswing: An initial update](https://www.anthropic.com/research/glasswing-initial-update)

补充自然日新增，与benchmark文章是不同材料家族。官方正文“Open-source software”把模型估计6,202个高/危漏洞与已复核1,752项分开；90.6%有效和62.4%确认高/危是后者子集比例，不是全部6,202已确认。直接依维护者请求披露的未审项又是不同人口；确认、披露、patch与public advisory不是同一完成状态。人工复现/重评、维护者处理能力与embargo解释了为何发现更快未等于修补更快；文章不披露受控总扫描成本、抽样可代表性或完整漏洞细节，不能推总体安全保证。

第72章现有proposal/reproduction/disclosure分层、隔离最小复现、去重、人类severity/responsible disclosure、denominator/false-positive/修复接受率和maintainer/embargo直接承载这一采用边界，因此已有覆盖。reader实际读全文并核该具体位置；不采用未复核外部客户宣传数字，也不因发现能力授予模型披露或生产修改权限。


### [AttuneBench: A Conversation-Based Benchmark for LLM Emotional Intelligence](https://arxiv.org/abs/2605.21739v1)

采用v1 §3–8的200段真实多轮对话与有限参与者标签，分开emotion recognition、本人偏好及第三方draft quality；5/11排序方向不一致不能推出所有测量无效，emotion F1的p=.099与cluster相关亦不支持独立普遍改善。Default/Verbose/Omniscient样本不同，格式与judge可能混杂，非临床真值；全部对话/judge调用付费。Ch66原score条件段没有这三个测量对象的明确分责，已在排行榜问题段后补一段，6分加深/实际POST通过；不授情绪安全或实现复现。

### [MM-Conv: A Multimodal Dataset and Benchmark for Context-Aware Grounding in 3D Dialogue](https://arxiv.org/abs/2605.21796v1)

采用v1 §4.3/T7–8/AppB–C及Discussion：先重写历史指代、再由既有grounder定位。Stage1另给visible-object list，不能把收益全归纯语言推理；GroundingDINO原baseline为N/A，不采用正文猜测的约5→56.7%同detector提升。partitive保留仅67.4%，wrong-object/missing-part仍在；2D图文评测不验证所采gaze/motion/3D。额外调用/重写校验付费，歧义回原表达/Unknown。Ch23实例定位论证中已补referent-preservation与定位分责，实际POST通过。

### [Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions](https://arxiv.org/abs/2605.21827v1)

采用v1 §3–7：claude-haiku-4-5-20251001、T=0/.7共6620 runs、fresh30/cell及每温度10个exact-number控制，vague词的数值变化受prompt给定state/容量影响。没有human/no-word控制或预先验证的10词顺序，posthoc区间与重复词依赖使p仅descriptive，KW两epsilon不可相加作因果分解；zero-tool-call abstention不是可靠语义拒答率，Tier3独立state读取未做。Ch78 description/schema后已加入真实数值意图/state/unit/幅度验收与澄清回退；配对控制和调用成本近文，实际POST通过。

### [Thermo-VL: Extending Vision-Language Models to Thermal Infrared Perception](https://arxiv.org/abs/2605.21882v1)

采用v1 §3–5.5/T2–4/Limit：冻结Molmo RGB tower/LM，训练thermal尾4层及query/RGB条件attention-gated residual。已对齐配对、QA构造和未专门优化paired-input的基线限制归因；H10080GB、B4、3epoch约34h不能省略。局部RGB-only保持不证明冻结权重在任意输入下行为不变，misalignment/missing/sensor shift未测。Ch23 Cross-attention/fusion已补thermal→冻结RGB consumer接口、费用与原RGB/专用热成像回退，实际POST通过。

### [Foresee-to-Ground: From Predictive Temporal Perception to Evidence-Driven Reasoning for Video Temporal Grounding](https://arxiv.org/abs/2605.21973v1)

采用v1 §3–5/T1–6：Qwen3-VL8B在220K/4A6000下训练proposal与LoRA，TopK8/SEE4，ID与timestamps在同一structured response内，不是两次LLM调用。bestIoU-ID监督不让candidate成为真值；Refined可超过cite-only界，非绝对时间精度上界。VideoMME overall71.4→70.9，只有两次inference稳定性，<5%latency缺完整serving条件。Ch23 temporal provenance后已补candidate/citation/refinement分责；单primary visual interval、全训练/调用费与重新候选/精测回退均保留，实际POST通过。

### [Diverse Yet Consistent: Context-Guided Diffusion with Energy-Based Joint Refinement for Multi-Agent Motion Prediction](https://arxiv.org/abs/2605.22017v1)

采用v1 §3–5/Eq18–19/T6的双方证据。作者用P_diff×exp(-E)构造joint并声称保持marginals，但式18没有展示相应约束；式19仅列positive energy最小化，没有闭合normalizer/negative项的解释，不能补写正确归一训练recipe。局部对照有joint/diversity收益，但full JADE/JFDE1.671/3.283略劣JDR-only1.665/3.273；SDD正文误称NBA，不照录全SOTA。原式/相邻解释/损失与消融已有限核足，中心定义仍争议，暂缓Books。重开仅需作者勘误、明确保marginal约束或对应公开实现消除冲突，不把普通未读藏成争议。

### [OPERA: An Agent for Image Restoration with End-to-End Joint Planning-Execution Optimization](https://arxiv.org/abs/2605.22104v1)

采用v1 §3–6/T1–3：complete-plan GRPO reward为Rq×Rd×Rf×Rc，含退化/格式/一致性，不仅final quality；固定plan下终态loss沿可微toolchain训练工具，不适用于任意API。340plans/120合成inputs/4tools≤4只是小型机制校准，部署16tools；Full部分MANIQA/MUSIQ及RTTS55.78<Planning56.91反退。一次VLM调用不等一次token forward，实际2.8/3.8/4.4工具调用与训练均计费。Ch81 instruction/tool协同优化后已补planner与tool梯度分责、非名义工具和完整成本/回退，实际POST通过。

### [Relational Linear Properties in Language Models: An Empirical Investigation](https://arxiv.org/abs/2605.22532v1)

采用v1 §3–5/Eq8/T1–2，拟合模型输出与GT、CSS distribution-collapse必须分验，8-bit两模型/四集/<250字符/80–20与LRE不同prompt限制归因。关键Eq8实际HTML、LaTex及官方PDF第5页均写sum p_model log(p_probe/p_model)，与minimize KL/Adam文字方向相反。为排除转写已看完整对应PDF页，官方v2只定点核同式仍未改，不把窗外v2回填实验。中心优化定义暂缓，不写Books公式；重开为勘误或可核实现及对应实验。可选代码未声称已核，未复现。

### [Enhancing Gaze Reasoning in Vision Foundation Models for Gaze Following](https://arxiv.org/abs/2605.22607v1)

采用v1 §3–5/T1–4：head-conditioned Gaussian软LoRA gate不等head外update全零，后续attention仍传播；OOC作用于中间辅助gaze-evidence图，最终heatmap仍按BCE任务目标训练。Qwen3-VL32B划salience subsets是启发式，非人类causal真值；ViT-L变化不是纯方法收益，部分cone/OOC指标有反侧，VAT ViT-L角18.83劣ViT-B18.34。硬件/时延/方差Not Disclosed。Ch23 Grid2Matrix后已补局部适配与最终任务监督分责，原VFM回退/训练费近文，实际POST通过。

### [WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance](https://arxiv.org/abs/2605.22664v1)

采用exact-v1正式标题WorkstreamBench，§3–6的rubric/judge、受控gold扰动和408专家annotations。数值碰巧正确可伴off-by-one、硬编码和缺formula；accuracy/formula/format需分账，judge校准非完备oracle，金融域/权重/最难级仅7任务及GUI/API异质限制外推。受控改输入/独立重算是项目验收推断，不冒充论文全测。Ch66 SlidesGen之后已补原生可编辑以外的公式依赖差额；独立重算、人工/judge及全部交互成本明确，实际POST通过。

### [SceneGraphGrounder: Zero-Shot 3D Visual Grounding via Structured Scene Graph Matching](https://arxiv.org/abs/2605.21788v1)

采用v1 §III–VII/TI–IV：marker标记2D对象、VLM预测关系，依RGBD/depth/pose提升scene graph，以query图的软score/DFS匹配，歧义时复读view。DFS可跳landmark，不是hard几何约束；14ScanRefer scans/991queries/static map，graph与VLM分支人口不同不能比均值识别因果。Spot远端3090两次43/84、42/88为不同grounding实验，不授动作成功。Ch23 OpenVoxel后已补关系proposal/query映射接口，重建/模型/搜索成本与原view/Unknown退路近文，实际POST通过。

### [Hypergraph as Language](https://arxiv.org/abs/2605.21858v1)

采用v1 §3–5/T1–5/AppF：vertex/hyperedge alternating identities/incidence经HIP projector进冻结LLM，解决pairwise展开无法保共同归属的接口。完整incidence bipartite无损不等8×8采样/160tokens/overview无损；同结构text Details亦贡献输入，joint VC76.9略劣single77.0。AppF pairwise相同/三元joint不同仅支持局部诊断。Ch23共享token/codebook治理后已补高阶关系consumer；采样/projector/辅助训练全费与原图/显式incidence回退保留，实际POST通过。

### [SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization](https://arxiv.org/abs/2605.21948v1)

采用v1 §3–7/T1–7的窄负面边界：perplexity/语义结构/GPT4o打分及候选比较sensor在Web Review recall约.008，新30 Automotive相关性膨胀攻击多项漏检。主表FPR0与T4 .02、5+6漏检实际改rank却全block、T3/T5 paraphrase口径均不一致，故不采零FPR/100%block或恢复原文真实性。阈值人口、ICD n²、FP/降rank效用与模型成本均保留。Ch72 mitigation后已补排序完整性≠无害/显式指令层级，原文provenance/独立审计与人工退路，实际POST通过。

### [Format-Constraint Coupling in Knowledge Graph Construction from Statistical Tables](https://arxiv.org/abs/2605.21974v1)

采用v1 §3–4.6/Limit：矩阵CSV中serialization与schema的factorial交互、建图数字/实体错绑可被普通retrieval QA掩盖。TypeII偏置、同entity相关、6组仅4组CI正、2hop/substring命名、Gemini部分不激活与long-format Schema-only反优都保留；deterministic parser5/7≥.96，e/n比例会漏结构正常错值，非worst-case保证。CDS/TTF是事后阈值，T0有限host约$450不授线上通律。Ch76三层消融首段后已补ingestion内交互/graph事实/最终QA分验与原表/parser回退，实际POST通过。

### [EasyVFX: Frequency-Driven Decoupling for Resource-Efficient VFX Generation](https://arxiv.org/abs/2605.22051v1)

采用v1 §3–4/T1–2/AppD：noisy-latent时间均值/帧差的6维频带能量descriptor软路由固定total-rank LoRA；Stage1训router/experts，Stage2冻结它们仅适配reference conditioning tokens。不是top-k跳算或test-time更新专家，能量ratio不认证phase/对象/真实motion分离。CogVideoX5B约200testvideos、offline5000步8H20及每reference50–100步1H20均计费；复杂非刚体与prompt/reference冲突未解。Ch24多原型条件后已补参数路由/每参考条件更新分责，不混SVD谱/SNR监督，实际POST通过。

### [What are the Right Symmetries for Formal Theorem Proving?](https://arxiv.org/abs/2605.22257v1)

采用v1 §3–6/8、Assumptions7/13、Prop14/15/T1–2：有Lean等价证书的rewrite搜索再提升proof，与普通自然语言近义不同。proof-equivariance不等success-invariance；采样coverage且N(K)/K→∞才有极限，不是固定预算保证，单调性另有reciprocal category/独立prior/attempt条件。GoedelSFT/DPO及DeepSeek部分模型题集反退，rewrite/scoring/全部尝试/Lean全费。Ch79 Search-based预算段后已补representation空间搜索与原statement/solver回退，实际POST通过。

### [Supervised Classification Heads as Semantic Prototypes: Unlocking Vision-Language Alignment via Weight Recycling](https://arxiv.org/abs/2605.22484v1)

采用v1 §3–5/T1–3：把同冻结feature坐标的监督head行向量与class-name配对作轻量跨空间anchor，亦可加真实pair。不是无监督/零数据/免预训练；NeuralCollapse仅条件解释，weight/image gap与简单中心化无益、1K/21K语义覆盖和real-pair足够时收益趋零均保留。跨head坐标不同不可直接合并，2GPU分钟不抹全部数据/预训/回归。Ch23 M2M后已补监督参数anchor分支、独立encoder/map及真实pair退路，实际POST通过。

### [COCOTree: A Dataset and Benchmark for Open Tree-Structured Visual Decomposition](https://arxiv.org/abs/2605.22068v1)

采用v1 §4.1–4.5/T5–6/Limit：OTQ联合mask×label与matched skeleton、nearest matched common parent及TP/FP/FN恢复，允许中间节点变化但missing仍计罚；1K GT erosion/remove/rewire只校有限oracle敏感性，单reference/多解和label backend不确定。拟采用的判断是mask IoU不能代签结构、应有独立structure predicate与受控mutation校验，而不是把OTQ公式写成通用真值。Ch66 Compound Artifact Preservation Contract已明确content/format/structure分验、人工切片与deliberate mutations，已有覆盖；不假称原文已有nearest-parent算法，未核实现/复现。

### [SpaceDG: Benchmarking Spatial Intelligence under Visual Degradation](https://arxiv.org/abs/2605.22536v1)

采用v1 §4.1–5/T2–4：type/severity metadata对部分group有反向项，不能从跨模型组差异因果归于spatial-FT；GeminiFlashLite两stage48.8→47.0仅局部提示失败，人类900subset不能认证全10K超人。当前Ch23任务贡献与当前可靠性Gate已分长期有用和当前噪声/缺失/domain shift，sensor可漂移且不是真值，后续entropy-only反退亦明确。故该采用判断已有覆盖，不重复SpaceDG数据或宣称CoT普遍有害；数据构造、提示/模型调用和单模态回退成本保留。

### [Flat-Pack Bench: Evaluating Spatio-Temporal Understanding in Large Vision-Language Models through Furniture Assembly](https://arxiv.org/abs/2605.21625v1)

采用v1 §3/4setup/§5全部：50视频/343补标frames的part mask+ID，image-only与IDshuffle揭示局部视觉/编号shortcut不能代替时间利用；CoT/self-consistency亦反退。TVA62.29%abstain、3.32%programfail、answered-only31.27%不是原分母，SAM2 IoU .28和Yes-contact52.93%暴露工具误差。keyframes人工选取、prompt方式、self-thought错误分类均限制因果解释。Ch66既有video-QA同题输入消融/时间必要性/原分母与cue混杂完整论证已承载该选择，已有覆盖；不把人类高分认证真实动作，不复现工具。

### [FLUID: From Ephemeral IDs to Multimodal Semantic Codes for Industrial-Scale Livestreaming Recommendation](https://arxiv.org/abs/2605.21832v1)

采用v1 §3–4/T3/6/7：跨域encoder的RQ-KMeans层级码分别给slice/累计room consumer，prefix寻址保残差路径，逐level投票不代表实体真值。直接替换/融合失败，独立token无warmup亦ΔAUC0；先预热slice、再退ID、后独立room初始化，Stage2 .7793比Stage1 .7801低，最终.7802的小差额无普遍保证。在线指标不提供完整方差/全部署费，预训练/多表/聚合/分阶段训练均计。Ch23当前共享codebook段没有瞬态/稳定consumer与迁移竞争，已补一段，Source/逐字PRE及实际正文/完整直接两侧/本人注POST已通过，指定窄位生效释放。

### [LLM Retrieval for Stable and Predictable Ad Recommendations](https://arxiv.org/abs/2605.21969v1)

采用v1 §2–5完整：unique-ID shadow加小key-feature扰动，以normalized conversion StatSigDiff与逐日MAD诊断稳定性；LLM属性phrase→token Jaccard建立候选扩展。小扰动未证语义/auction等价，低变动不认证正确，fine-tuned描述与§5 zero-shot Llama3-8B口径不同；θ/遍历/天数/总费Not Disclosed，overlap非quality。Ch66稳定与任务正确分验、内容保持/配对人口与控制不足仅联合效应的现有正文承载该采用边界，已有覆盖；不把广告统计recipe或未披露serving写Books。

### [From Recognition to Reasoning: Benchmarking and Enhancing MLLMs on Real-World Receipt Document Understanding](https://arxiv.org/abs/2605.22413v1)

采用v1 §3.4–5/T3–4、AppB/D2–3：list Hungarian配对的金额hard constraint与语义相似不可混；普通numeric 1e-6和detail .05是不同合同。FP负奖励只覆盖gold空/pred非空，TN=.3不保证不collapse；结构F1在Qwen4/8B GRPO后.6478→.6215/.6462→.6373，precision升不抵消此反退，2B异构模型不识别容量阈值。400人审只校有限weights，4A800/16samples/judge与数据全费。Ch66 artifact predicates与Workstream值/依赖/格式分账已直接承载视觉字段/结构/reward分别验，已有覆盖；不采用本篇强保真或全部结构改善说法。

### [Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2605.22748v1)

采用v1 Results/Discussion/Methods及S1–S3：历史checkpoint+固定20策略league、集合Perceiver与近距交互物理改变训练人口，单机快/同组成功不等陌生对手稳。显式近距/终止reward仍在，8机completion仅56%；sim crash减少不是实机通用安全。真实依赖42-camera MOCAP全对手state、离机50Hz、单赛道及单人FPV感知不对称，不能授人类策略普遍超越。27h4090+CPU假设league已预训，全部对手/rollout/闭环费另计；downwash粗代理。Ch26 sim-to-real已加交互人口接口，Source/逐字PRE及实际正文/完整直接两侧/本人注POST已通过，指定窄位生效释放。

### [Can AI Make Conflicts Worse? An Alignment Failure in LLM Deployment Across Conflict Contexts](https://arxiv.org/abs/2605.22720v1)

采用v1 §3.1–3.4/4.3/5–6：15 base/90个三turn synthetic scenarios显示balance framing与所声明norm可能冲突。adaptive followup不是固定事实的matched因果对照；5次judge在同90transcripts的α=.810不等独立rollout，2实践者subset未给完整n，English/OpenRouter/April snapshot不授全域harm率。作者承认norm coverage/helpfulness/sycophancy不可区分，故撤销初筛“已知sycophancy”关闭，保局部行为反例而不作法律truth或机制因果。Ch66任务目标/人工anchor/控制不足只报联合效应已有覆盖，安全定点深入及独核通过。

## 5. 缺口与下一步

无普通研究或Books待办。全部候选均已获得必要证据处置，具体Books决定及17项新增真实POST已完成，全部Books窄位已释放；本轮完整六节DAY通过。下列外部保留不等于正面Evidence/Coverage通过，也不支持无遗漏。

本窗终态保留项仅限下列边界，不用于正面证据、Books或“无遗漏”：

- [2605.21553 TONIC](https://arxiv.org/abs/2605.21553v1)与[2605.21565 SPCL](https://arxiv.org/abs/2605.21565v1)：v1均早于Wed14EDT cutoff，最早可能公告05-21 08BJT，而各registered最晚界在05-22，完整区间跨日。已核精确ABS/DC与官方公告规则，有限官方目录恢复仅月列表、不能给逐项公告日；不截取其中05-22、不先评分/入表。恢复需同身份官方日公告、同期可公开正文或能把完整联合界收窄单日的原始依据，只重开这两资格。
- [2605.22017](https://arxiv.org/abs/2605.22017v1)：Eq18 energy tilt的marginal保持条件、Eq19训练归一/negative定义与正文中心声明未闭合。已读原式/解释/损失/直接消融，保局部指标和反侧；重开为作者勘误、明确约束或可核对应实现消除中心冲突，不采用未证数学保证。
- [2605.22532](https://arxiv.org/abs/2605.22532v1)：v1 HTML/LaTex及官方PDF第5页负KL分式与minimize方向冲突；官方v2只为该式窄核仍未改，不回填本日。需作者勘误或公开实现/对应实验说明实际优化方向后，只重开该采用命题。
- Meta Publications历史日级目录仍不可读，Google Publications仅年/venue记录、MiMo undated Blog卡仍不能支持本日完整性。已有限恢复当前官方入口，需可读官方日期列表、同期archive/feed或具名事件页；只补相应来源本日缺段，不扩大整月。
- [Tencent-Hunyuan/Precise](https://github.com/Tencent-Hunyuan/Precise)：repo created/可回填initial commit与当前09月news不能证明May22已公开。需同期官方公告/release/archive或外部public event；只重开该family资格，不因当前可读而授历史证据。

[2605.22183 AVP](https://arxiv.org/abs/2605.22183)当前官方v4明确withdrawn，已按合同排除，不评分/入表/Books；这不是访问故障，不为旧v1可读反向恢复采用。

旧508 submitted-window ledger与其跨日crosswalk只保历史路由，不是本日待办或public-owner分母；已经有效属于05-22旧报告的254项不移到本报告重数。未来材料到达按实际归属只重开受影响身份，本轮不启动其他日期、Live或Weekly。

## 6. 复核

复核者：`supp_may23_reader`（本日报告/Books非作者，仅维护本日独核记录）

结论：通过

本轮完整六节DAY已由reader实际通过，完成态结果见同一独核记录；争议与外部保留继续隔离，不授正面证据或覆盖保证。旧三项Source/实际POST与历史fresh终审有效复用；原3完整行、日期/评分、小时窗和连续原§4保留。当前reader已实际核25个arXiv候选的完整AB/必要Source及2篇Anthropic全文，并逐项检查精确日期、当前撤回信号和Books具体采用边界；17项新增真实正文、完整直接两侧与本人注一次非writer POST均已通过，全部窄位生效释放。未运行论文实现、攻击或复现实验，Books为证据限定的设计判断。

排除复核按来源/主题/风险分层：原42个AB中reader实际读36个（25候选、2资格、1撤回、8明确排除样本）；8样本为21491/22681/21902/22586/22013/21901/21773/22478，其余6明确关闭未声称双读。22720从安全代表排除恢复准入，21565/21625等6项局部false-negative校准修复了过粗“已有组合”理由，不推倒无关旧层。另实际读OpenAI2官方core、VeOmni#778纠错核心/#772创建与merge事件、早段14个官方查询响应与精确q停止；没有把抽检写成全量库存审计。

实际独核与阶段结果见[唯一reader记录](../_sources/daily-20260523/SUP_REVIEW_20261020.md) R1–R24；作者具体原域、逐字窄稿、有限恢复/停止及纠错轨迹见[唯一作者记录](../_sources/daily-20260523/SUP_SOURCES_20261020.md)。旧[`V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260916.md`](../_sources/daily-20260523/V3_FRESH_NONAUTHOR_FINAL_REVIEW_20260916.md)只证明旧小时窗，不代本次DAY。当前V3接口校验通过；原3完整行各一次、原小时窗及3137字符连续原§4实际比对保持；30候选唯一，19整合/9覆盖/2暂缓，41个本地引用零缺失。限定本报告/两SUP及9目标章cached/unstaged diff-check通过，不改无关既有差异；机器检查不代语义验收。
