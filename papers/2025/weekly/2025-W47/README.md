# AI Research Weekly — 2025-W47

> Coverage Window: 2025-11-17～2025-11-23
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：Gemini 3、Real-time speech-to-speech translation。重点是约束、机制、trade-off 与演进关系。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；revision 回链 first-public week。
- Scholar、OpenAlex、DBLP 用于 discovery/去重；论文回到正文。Crossref 只做 metadata 交叉检验。
- 历史回填不创建 Daily；Accessed 为 2026-07-31。
- benchmark 缺完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外一线模型公司、研究机构与 Hugging Face Blog。

- 保留：Gemini 3（2025-11-18）。
- 保留：Real-time speech-to-speech translation（2025-11-19）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1/官方论文正文。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程项目顺序扫描训练、编译、推理、平台与硬件 runtime。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemini 3 | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；产品信号 Weekly only |
| Real-time speech-to-speech translation | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Must Read；作为 pipeline fusion 的跨域演进案例 |

### Deep Analysis 1 — Gemini 3

- First Public: 2025-11-18
- Status: Official proprietary release; vendor evaluation
- Primary Source: https://blog.google/products-and-platforms/products/gemini/gemini-3/
- Evolution Relationship: Direct Evolution

#### Why

模型发布与 agentic development environment 同日集成，能力边界更难与 harness、tools 和 UI 分离。

#### Principle and Mechanism

官方页面证明模型/产品形态和工具集成，训练与 agent runtime 实现未公开。

#### Trade-off and Evidence Boundary

day-one integration 改善可用性，也放大 evaluation attribution、权限和平台锁定问题。

#### Connection and Evolution

知识树位置：第 20、62、74～77、80 章。Worth Watching；产品信号 Weekly only。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

### Deep Analysis 2 — Real-time speech-to-speech translation

- First Public: 2025-11-19
- Status: Google Research official research/deployment case
- Primary Source: https://research.google/blog/real-time-speech-to-speech-translation/
- Evolution Relationship: Direct Evolution

#### Why

级联 ASR→translation→TTS 便于模块替换，却累积 latency、错误和声纹丢失；实时交互迫使系统重构端到端 dataflow。

#### Principle and Mechanism

研究采用 streaming end-to-end S2ST 与 time-synchronized data，报告部署案例。

#### Trade-off and Evidence Boundary

端到端降低 pipeline latency 和误差累积，却降低模块可解释/可替换性，并引入声纹隐私、滥用和实时 SLO 风险。

#### Connection and Evolution

知识树位置：第 9、38、52、69 章。Must Read；作为 pipeline fusion 的跨域演进案例。进入 Books 时保留旧方案条件，并区分官方事实、作者实验和本项目推断。

## Full Source Review

### Gemini 3

- **Candidate / Week / Score:** Gemini 3 / 2025-W47 / 22/30。
- **Source Family ID:** `GOOGLE-GEMINI-3-PRO-2025-11`。
- **Source Type:** official product announcement、model card及评测说明。
- **First-public Date / Revision History:** 2025-11-18；Gemini 3 Pro model card当日发布、2026-05更新。后续 card 增补内容明确标为 revision evidence，不倒写成 launch 当日披露。
- **Direct Primary Sources:** Google announcement；Google DeepMind Gemini 3 Pro model card及 eval methodology links。
- **Related Primary Sources:** Antigravity product announcement；只用于拆分 model、tools、IDE/harness attribution。
- **Access and Verification Status:** Verified for public model/product facts；参数规模、expert配置、训练算力、routing/runtime implementation Not Disclosed。
- **Full-read Coverage:** 已阅读announcement的model/product integration与benchmark notes；阅读全文model card的model/data、sparse MoE、1M/64K、TPU/JAX/Pathways、distribution、limitations、安全与frontier evaluations，并记录2026 revision边界。
- **Original Problem:** frontier model越来越通过agentic IDE、computer use、tools与UI交付，单个产品分数很难归因于模型本身。
- **Why the Previous Design Was Reasonable:** 模型API与agent harness分开评测能保持可替换性、复现性和清晰 failure domain；发布时深度集成可缩短用户路径但牺牲归因。
- **Changed Constraint:** multimodal、1M context与复杂开发任务要求模型、tool permission、artifact viewer和execution environment协同，产品价值不再来自裸模型一次调用。
- **Mechanism:** model card确认Gemini 3 Pro为native multimodal sparse-MoE Transformer，输入text/image/audio/video、最多1M context与64K text output；Deep Think是可选test-time模式。Antigravity等是外部agent platform，不是模型内部机制。
- **State Ownership:** 模型服务拥有context与reasoning generation；agent平台拥有tools、workspace、permissions与trajectory；产品UI拥有interaction/compaction；evaluator拥有harness与grader。
- **Control Flow / Data Flow:** user task → platform构造context/tools → model reasoning/tool proposal → environment执行 → observation回填 → artifact/response；任一层变化都可能改变agent benchmark。
- **Implementation Details:** 训练使用TPU、JAX与ML Pathways；pre/post-training data只给类别，包含RL multi-step reasoning、human preference与synthetic data；exact recipe和serving topology未披露。
- **Evaluation Setup:** announcement/model card覆盖reasoning、multimodal、agentic tool use、multilingual与long context；部分详细methodology另页，vendor harness与产品集成共同影响结果。
- **Baselines / Ablations / Sensitivity:** 与Gemini 2.5 Pro及其他模型比较；没有公开model-only vs Antigravity/tool stack、Deep Think compute budget或1M context retrieval sensitivity的完整消融。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** TPU/JAX/Pathways、1M input、64K output已披露；TPU generation/count、precision、batch、concurrency、TTFT/ITL与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明产品在launch时提供特定model family、context/modalities与agent integration；model card证明sparse MoE这一架构类别和训练/安全评测范围。
- **What It Does Not Prove:** 不公开内部expert/router机制，不证明Antigravity表现等于模型能力，也不证明vendor benchmark能代表生产agent reliability。
- **Limitations / Threats to Validity:** proprietary mechanism、产品与模型耦合、model card后续revision、benchmark attribution、hallucination/timeout/multiturn degradation。
- **Trade-offs / New Failure Modes:** day-one integration提升可用性，却增加permission blast radius、tool side effects、platform lock-in、trajectory不可复现与model/harness版本耦合。
- **Where the Previous Design Still Applies:** 需要可移植、可审计、可比较的系统仍应把model endpoint与agent runtime分层；简单任务无需承担完整agent platform。
- **Evolution Relationship:** `Direct Evolution`：model API → tool-using model → integrated agentic development environment；后者是系统组合，不是模型单层替代。
- **ROADMAP Node:** Ch20、Ch62、Ch74～77、Ch80。
- **Target and Adjacent Chapters Read:** 已读 Ch20、Ch62、Ch74～77、Ch80；仅支持版本/产品事实。
- **Existing Coverage:** Ch62 已明确 subject identity 包含 model、harness、environment 与 runtime；Gemini 3 仅保留为产品信号。
- **Integration Decision:** `Weekly Only — Version/Product Fact`。
- **Changed Files or Rejection Reason:** 不改 Books；model/Deep Think/tools/platform 的分层归因已由 Ch62/74～77/80 覆盖。
- **Open Questions:** Deep Think compute contract、tool permission/failure semantics、model-only对照与model-card revision diff。

### Real-time speech-to-speech translation

- **Candidate / Week / Score:** Real-time speech-to-speech translation / 2025-W47 / 23/30。
- **Source Family ID:** `GOOGLE-S2ST-2025-11`。
- **Source Type:** Google Research official engineering/research Blog与deployment case。
- **First-public Date / Revision History:** 2025-11-19；无独立论文链接，当前证据为官方研究说明，后续产品版本不回写为该系统实验。
- **Direct Primary Sources:** Google Research《Real-time speech-to-speech translation》全文。
- **Related Primary Sources:** AudioLM、SpectroStream与量化/streaming references；只用于机制背景。
- **Access and Verification Status:** Verified for公开架构、数据构建与部署策略；训练规模、完整质量/latency表、server/device hardware details Not Disclosed。
- **Full-read Coverage:** 已阅读cascade motivation、time-synchronized data pipeline、streaming architecture、AudioLM/SpectroStream tokens、lookahead、quantization/CFG precompute、语言范围、Meet/Pixel部署与限制。
- **Original Problem:** ASR→MT→TTS级联每层等待和误差累积，端到端延迟约4～5秒且常丢失说话者声音；实时对话需要边听边译边合成。
- **Why the Previous Design Was Reasonable:** 模块级级联可独立训练、替换、监控和覆盖更多语言，错误可定位；离线或弱实时场景不需承担端到端耦合。
- **Changed Constraint:** conversational turn-taking对latency与voice preservation敏感，移动端算力又限制模型大小；等待完整utterance不再满足交互SLO。
- **Mechanism:** 通过ASR/TTS/alignment/filter构造time-synchronized speech pairs；streaming encoder使用前10秒上下文，autoregressive decoder生成SpectroStream二维RVQ audio tokens（约每100ms 16 tokens）并附加text token用于BLEU；target shift引入可调lookahead，默认约2秒。
- **State Ownership:** streaming encoder拥有滑动audio context；decoder拥有autoregressive acoustic/text token state；runtime拥有lookahead buffer、quantization与CFG precompute；产品拥有capture/playback与fallback。
- **Control Flow / Data Flow:** source audio chunks → synchronized encoder context → target acoustic/text token stream → vocoder/playback；默认2秒lookahead在翻译质量、音质与latency间取舍。
- **Implementation Details:** server路径用于Google Meet；Pixel 10使用int8/int4量化与classifier-free-guidance预计算，覆盖不足时仍保留cascade路径。两种deployment strategy共享data/architecture但runtime contract不同。
- **Evaluation Setup:** 五个拉丁语系语言双向翻译；官方比较cascade与streaming quality/latency并描述Meet/Pixel deployment；没有可复现的完整hardware、network、concurrency与tail-latency表。
- **Baselines / Ablations / Sensitivity:** 讨论lookahead、quantization与cascade；缺各语言/噪声/说话人、packet loss、device thermal与并发sensitivity完整公开数据。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** Pixel端int8/int4、encoder前10秒、默认2秒lookahead已披露；server/device型号、batch/concurrency、网络、P95/P99 SLO Not Disclosed。2秒不等于端到端latency。
- **What the Evidence Actually Proves:** end-to-end streaming data/architecture可减少级联等待并保留voice特征，且同一模型可通过不同runtime策略落到server与device。
- **What It Does Not Prove:** 不证明级联普遍过时、不证明所有语言/口音/噪声下更优，也不证明2秒是完整用户感知延迟。
- **Limitations / Threats to Validity:** 语言范围窄、官方部署证据、训练/评测细节不全；端到端模型难以局部纠错，声纹保留带来privacy/impersonation风险。
- **Trade-offs / New Failure Modes:** fusion减少latency与error propagation，却降低模块可替换/可解释性，并新增stream drift、声纹泄露、packet jitter、lookahead buffer与device thermal failure。
- **Where the Previous Design Still Applies:** 长尾语言、离线高质量、强可解释/可替换、资源允许或需要独立合规过滤时cascade仍合理；Pixel也实际保留其作为coverage分支。
- **Evolution Relationship:** `Direct Evolution`：离线级联 → streaming级联 → end-to-end streaming S2ST；演进由latency/voice约束驱动，旧方案仍是coverage与可控性分支。
- **ROADMAP Node:** Ch9、Ch38、Ch52、Ch69。
- **Target and Adjacent Chapters Read:** 已读 Ch9、Ch38～40、Ch52、Ch62、Ch69；Ch38 为 pipeline-fusion 主 owner。
- **Existing Coverage:** Books是否已有pipeline fusion的跨域演进原则待逐段去重；不得把speech产品细节孤立加入。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch38，作为 cascade→streaming fusion 的受限演进案例。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/38-what-happens-during-inference.md`。
- **Open Questions:** P95/P99端到端latency、声纹privacy、network jitter/fallback、非拉丁语系与human evaluation。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系为本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper、model card 与工程集成按证据角色回链，不重复形成 Books 观点。
- 新方案不覆盖旧方案；保留适用条件、新增状态与 failure modes。

## Knowledge Tree Position

- Gemini 3 → 第 20、62、74～77、80 章（Direct Evolution）
- Real-time speech-to-speech translation → 第 9、38、52、69 章（Direct Evolution）

## Recommended Action

- Gemini 3：Worth Watching；产品信号 Weekly only
- Real-time speech-to-speech translation：Must Read；作为 pipeline fusion 的跨域演进案例

## Event-Date Daily Decision

历史回填不创建 Daily；证据直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、榜单、缺条件 benchmark 与无新机制的价格/可用性变化。
- 不以“更新”自动否定旧设计。

## Repository Changes

- 新增 papers/2025/weekly/2025-W47/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- Gemini 3 的 model、Deep Think、tools与Antigravity如何做可重复的分层归因？
- 实时S2ST的tail latency、声纹privacy与fallback contract如何验证？

## Sources

- Gemini 3 — https://blog.google/products-and-platforms/products/gemini/gemini-3/（First Public: 2025-11-18；Accessed: 2026-07-31）
- Gemini 3 Pro model card — https://deepmind.google/models/model-cards/gemini-3-pro/（Model Release: 2025-11；Last Updated: 2026-05；Accessed: 2026-07-31）
- Real-time speech-to-speech translation — https://research.google/blog/real-time-speech-to-speech-translation/（First Public: 2025-11-19；Accessed: 2026-07-31）
