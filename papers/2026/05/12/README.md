# Daily Research — 2026-05-12

**规范：** V3
**窗口：** 2026-05-11T09:00:00+08:00 ～ 2026-05-12T09:00:00+08:00
**窗口说明：** 用户明确要求仅补遗漏，原窗口、124 条候选及原日期评分保留，不迁移旧归属。
**补充窗口：** 2026-05-11 ～ 2026-05-11
**冻结候选日期：** [补查前原档案](../_sources/daily-20260512/baseline-before-supplement-20261018.md)
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-19T03:59:32+08:00

## 1. 结论

本次May11自然日遗漏补充已完成研究与Books处置：新增46唯一家族，必要证据均完成，34项已实际整合、12项具体已有覆盖，所有必要正文/完整邻接/本人注均经非写入者实际POST并由root接纳。旧124整行、日期评分、47整合/77已有覆盖及连续旧§4保留，现候选共170家族；不迁移旧归属、不重审其有效层。

四个完整有界主题查询去重233只是发现线索，不是当窗233篇或逐项队列；旧47同事件复用，49旧小时外未处理身份与generic共同错误受影响7项按具体贡献恢复，51未命中ledger只作有限查漏。首批准入与后续必要证据、具体排除分层和Books均已独立核验，完整六节DAY在本次实际归并稿上通过，普通研究待办为0。24项潜贡献的公开日期仍跨窗、机构早9小时历史slice受限，已精确隔离且不用于正面Evidence/Books/无遗漏断言。完成态仍须独立实际读回，不沿用旧窗口验收；[唯一来源与研究依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md)保留精确版本、原始字段和停止位。

以下两段是 **2026-09-15原小时窗口的历史结论**：

本窗最重要的信号不是单一发布，而是状态与提交权逐渐成为共同主线：模型侧出现 layer/rank/patch/latent-state 的条件计算，训练侧把更新几何与 reward context 变成可治理对象，推理与 Agent 则把 proposal、缓存、验证和 fallback 显式分权。

arXiv 公告批次为 1146 个唯一身份；分母经有界返修从 110 调整为 124，1022 项以 family-specific 理由在分母前闭合。124 项均有 evidence review 与 Books comparison；47 项 Integrate 现已全部具有 canonical 正文绑定，其中本轮 12 项完成正文写入、2 项为既有正文补 marker；其余 77 项为命题级 No Change。未参与作者返修或 root 写作的 fresh non-author reviewer 已完成写后语义终审，Coverage、Evidence、Books 与 Report Gate 均通过。

## 2. 来源覆盖

原有效小时窗的Source与维护事件闭合保留，重用其中May11 09:00–24:00；本次只补May11 00:00–09:00边界及具体遗漏/含糊事件。下表每行同时说明旧有效范围和本次实际入口、停止与限制；“受阻”是必要历史片段未恢复，不代表零命中或未执行。原件保留于[本日来源目录](../_sources/daily-20260512/SUP_SOURCES_20261018.md)，机构历史slice与24日期保留不授全Coverage。GitHub补窗八查询均固定UTC May10 16:00–May11 01:00（上限以00:59:59秒表达），per_page100、total0/items0、incomplete_results=false，仅支持该committer-time索引查询，不代全研究发布历史。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 原有效小时窗（本次不重审）：https://openai.com/research/；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；检查官方研究/发布目录；未发现可唯一归属本窗且未被 arXiv family 去重的新事件。；**补充May11 00:00–09:00及具名差额：** Research403；Signals/Campus仅官方搜索题名为adoption/活动范围C，原raw也是403挑战壳、未取得正文。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 00–09历史研究slice未重建；题名排除不代表全文审阅。 |
| `SRC-ANTHROPIC` | 原有效小时窗（本次不重审）：https://www.anthropic.com/research；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；检查官方研究/发布目录；未发现可唯一归属本窗且未被 arXiv family 去重的新事件。；**补充May11 00:00–09:00及具名差额：** 当前Research首10非历史归档；精确官方May11搜索的FSR Updates将May11写为旧deadline，实际更新May5，非当日新事件。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 00–09历史研究片段不可完整回放。 |
| `SRC-GOOGLE-AI` | 原有效小时窗（本次不重审）：https://deepmind.google/research/ ; https://research.google/pubs/；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始 DeepMind Research 与补检 Google Research Publications 均已检查；后者只给 publication year/venue，无法将条目唯一归属日级窗口。官方 May 2026 Research blog index 的可见事件为 05-01、05-19、05-27、05-28，本窗无独立发布；不据此证明不存在未标日论文。；**补充May11 00:00–09:00及具名差额：** DeepMind当前页200；Google pubs两次35s超时；May11官方blog辅助查询未恢复事件，不把year/venue当日公开。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 目标日未标日pub/历史slice仍缺；保旧有效blog可见段。 |
| `SRC-META-AI` | 原有效小时窗（本次不重审）：https://ai.meta.com/research/；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；检查官方研究/发布目录；未发现可唯一归属本窗且未被 arXiv family 去重的新事件。；**补充May11 00:00–09:00及具名差额：** 注册Research入口连接重置，未取得补充早9小时历史片段。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 必要历史研究slice不可得，不作零命中。 |
| `SRC-QWEN` | 原有效小时窗（本次不重审）：https://qwenlm.github.io/；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；检查官方研究/发布目录；未发现可唯一归属本窗且未被 arXiv family 去重的新事件。；**补充May11 00:00–09:00及具名差额：** 旧入口跳当前qwen.ai/research壳；WebWorld二手线索的官方精确题名/May11搜索无结果。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | WebWorld原始身份/dated正文与00–09历史slice未恢复。 |
| `SRC-DEEPSEEK` | 原有效小时窗（本次不重审）：https://www.deepseek.com/；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；检查官方研究/发布目录；未发现可唯一归属本窗且未被 arXiv family 去重的新事件。；**补充May11 00:00–09:00及具名差额：** 当前产品首页200无目标日研究归档；第三方阿里云V4Pro托管上架不当官方新机制。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 00–09历史dated研究材料未恢复。 |
| `SRC-MOONSHOT` | 原有效小时窗（本次不重审）：https://platform.kimi.com/blog ; https://github.com/MoonshotAI；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始 Blog 与补检 GitHub 均已检查；GitHub 精确窗口 2026-05-11T01:00Z–2026-05-12T01:00Z 命中 kimi-cli v1.42.0、telemetry/UI/skills/subagent 提示与 SDK 依赖更新，均为版本/维护事件，未改变 Books 长期机制。；**补充May11 00:00–09:00及具名差额：** 当前Blog最近可见2025-11-07不证明后来无研究；官方GitHub MoonshotAI补UTC May10 16:00→May11 01:00 commit搜索0/0，incomplete=false。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | GitHub查询仅索引committer-time；Blog历史日片段仍未恢复。 |
| `SRC-TENCENT-HUNYUAN` | 原有效小时窗（本次不重审）：https://hunyuan.tencent.com/research ; https://github.com/Tencent-Hunyuan ; https://github.com/Tencent/llm.hunyuan.T1；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始 Research 与两个补检 GitHub 入口均已检查；同一 UTC 窗口命中 R-DMesh 文档/test drive、HY-Embodied-0.5-X 默认 thinking 切换、SRPO bf16 保存/import 修复、HY-World-2.0 修复与文档，T1 为 0，没有足以改变长期机制的独立 release/RFC。；**补充May11 00:00–09:00及具名差额：** Research/blog真实SPA同组件，真实publicList all当前en9/9、zh11/11；显示May21→Apr30无May11项。早9h Tencent-Hunyuan与指定Tencent/llm.hunyuan.T1两GitHub查询各0/0。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 已检查 | 仅当前集合与指定索引窗；display/published/created可不同，不能认证历史从未发布。 |
| `SRC-ZAI` | 原有效小时窗（本次不重审）：https://www.zhipuai.cn/zh/research ; https://github.com/zai-org ; https://docs.z.ai/release-notes/new-released；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始 Research、GitHub 与官方 release listing 均已检查；GitHub 精确窗口 0 commit，release listing 未显示可唯一归属本窗的新事件。；**补充May11 00:00–09:00及具名差额：** SSR的May11 updatedAt是Apr20 created旧条；早9h zai-org GitHub0/0。注册release notes实际读全Models日期段，June16→Apr7无May11项。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | release当前集合不替历史Research完整slice；updated≠首公开。 |
| `SRC-BYTEDANCE-SEED` | 原有效小时窗（本次不重审）：https://seed.bytedance.com/en/research ; https://seed.bytedance.com/en/public_papers ; https://github.com/ByteDance-Seed；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始 Research/Blog、论文目录与 GitHub 均已检查；GitHub 精确窗口命中 VeOmni sequence-parallel gather/input-embedding fuse 与 CANN 9 Docker 更新，论文列表未建立另一独立当窗 family，两个工程事件均在候选分母前闭合。；**补充May11 00:00–09:00及具名差额：** 当前research/public_papers均取得；早9h ByteDance-Seed GitHub查询0/0，incomplete=false。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 研究历史slice未日级重建；不从当前集合或commit零授全研究零。 |
| `SRC-BAIDU-ERNIE` | 原有效小时窗（本次不重审）：https://ernie.baidu.com/blog/zh/ ; https://github.com/PaddlePaddle/ERNIE；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始技术博客与补检 GitHub 均已检查；GitHub 精确窗口 0 commit，未建立独立当窗事件。；**补充May11 00:00–09:00及具名差额：** dated Blog可见May9→Apr30段未见May11条目；早9h PaddlePaddle/ERNIE GitHub查询0/0。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 已检查 | 限定当前可见dated集合/指定commit索引；不授全历史完备。 |
| `SRC-XIAOMI-MIMO` | 原有效小时窗（本次不重审）：https://mimo.xiaomi.com/ ; https://github.com/XiaomiMiMo；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始 Paper/Blog 与补检 GitHub 均已检查；GitHub 精确窗口 0 commit，未建立独立当窗事件。；**补充May11 00:00–09:00及具名差额：** 当前8papers/15blog缺公开日；早9h XiaomiMiMo GitHub查询0/0，incomplete=false。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 受阻 | 未标日paper/blog历史片段隔离，不能当0篇。 |
| `SRC-MINIMAX` | 原有效小时窗（本次不重审）：https://www.minimax.io/blog ; https://www.minimaxi.com/blog ; https://github.com/MiniMax-AI ; https://agent.minimax.io/docs/techblog；2026-05-11 09:00–2026-05-12 09:00 Asia/Shanghai；初始英文 Blog 检查未发现独立当窗事件；中文注册入口 `minimaxi.com/blog` 302 到官方 `minimax.cn/blog`，当前完整列表在 2026-04-27 与 2026-05-25 之间无本窗条目；GitHub 精确 UTC 窗口命中 19 个 CLI/audio/proxy/endpoint/SSE 维护提交，均在候选分母前闭合；Agent Tech Blog 注册入口 307 到 `agent.minimaxi.com/docs/techblog`，官方 Markdown 列表首项为 2026-05-13，晚于本窗终点。；**补充May11 00:00–09:00及具名差额：** 当前EN12项与May26→March18段、CN重定向/Agent列表已恢复；早9h MiniMax-AI GitHub查询0/0。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 已检查 | 仅当前列表/指定索引，不证明早9h所有已删除/未标日历史事件不存在。 |
| `SRC-ARXIV` | 原有效小时窗（本次不重审）：official OAI direct datestamp 2026-05-12；announcement 2026-05-12 08:00 Asia/Shanghai；1146 official identities；1146/1146 title screen；124 retained；1022 closures；ordinary revision 0。；**补充May11 00:00–09:00及具名差额：** 补充自然日主题：4窄feed实际94/65/10/97、start0/max200全返回，去重233仅发现；49旧小时外题摘/受影响generic集合及有界51补检，46当窗家族必要Source与34I12NC完成。精确v1/日程/sameDOI findable arxiv.content registered联合限定May11。 [原件/停止依据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A2/A6。 | 已检查 | 24具名跨日包络隔离。月list实际18979前2000仅年月、Advanced官方announcement也仅年月，OAI datestamp非首公开；不遍历全月、不授全学科召回。 |

八个缺失 Source ID 已按注册入口定点返修；GitHub 精确窗口共命中 50 个 commit event，逐源分组后均在候选分母前闭合，未把普通维护提交伪装成研究候选。MiniMax 的中文 Blog 与 Agent Tech Blog 已沿注册 URL 的官方重定向和完整列表定点恢复；Google publications 的日级时间语义不足已明确保留边界，不据此宣称全网零遗漏。

撤回检查：124 个 retained exact-v1 均未显示 withdrawn；普通 revision 0。

## 3. 候选与判断

评分只衡量Design Delta / System Reach / Durability。原124行/日期评分逐字保留；新增46在自然日窗口完成各自必要证据与Books处置，未确定日期的24不混入本表。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Sanity Checks for Long-Form Hallucination Detection](https://arxiv.org/abs/2605.08346v1) | 2026-05-12T08:00:00+08:00 | We introduce a controlled-invariance methodology that exposes this distinction through two oracle tests: \textsc{Force}, which replaces each response's final answer with the ground truth while preserving the reasoning trace, and \textsc{Remove}, which strips answer-announcement steps while leaving the trajectory intact.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria](https://arxiv.org/abs/2605.08354v1) | 2026-05-12T08:00:00+08:00 | We introduce Auto-Rubric as Reward (ARR), a framework that reframes reward modeling from implicit weight optimization to explicit, criteria-based decomposition.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution](https://arxiv.org/abs/2605.08366v1) | 2026-05-12T08:00:00+08:00 | We introduce SWE Atlas, a benchmark suite for coding agents spanning three professional software engineering workflows: Codebase Q&amp;A (124 tasks), Test Writing (90 tasks), and Refactoring (70 tasks).；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [On Distinguishing Capability Elicitation from Capability Creation in Post-Training: A Free-Energy Perspective](https://arxiv.org/abs/2605.08368v1) | 2026-05-12T08:00:00+08:00 | Debates about large language model post-training often treat supervised fine-tuning (SFT) as imitation and reinforcement learning (RL) as discovery.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-GRPO，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [CoCoDA: Co-evolving Compositional DAG for Tool-Augmented Agents](https://arxiv.org/abs/2605.08399v1) | 2026-05-12T08:00:00+08:00 | We propose CoCoDA, a framework that co-evolves the planner and tool library through a single code-native structure: a compositional code DAG.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering](https://arxiv.org/abs/2605.08432v1) | 2026-05-12T08:00:00+08:00 | We introduce Sem-ECE (Semantic-Sampling Expected Calibration Error), a calibration evaluation framework for open-ended QA that samples answers from the model, groups them into semantic classes, and uses the resulting frequencies as confidence.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Child Inherits: Modeling and Exploiting Subagent Spawn in Multi-Agent Networks](https://arxiv.org/abs/2605.08460v1) | 2026-05-12T08:00:00+08:00 | Since the official release of ChatGPT in 2022, large language models (LLMs) have rapidly evolved from chatbot-style interfaces into agentic systems that can delegate work through tools and newly spawned subagents.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MULTI-AGENT，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)，已在正文并有 canonical marker |
| [Do Benchmarks Underestimate LLM Performance? Evaluating Hallucination Detection With LLM-First Human-Adjudicated Assessment](https://arxiv.org/abs/2605.08462v1) | 2026-05-12T08:00:00+08:00 | Hallucination remains a persistent challenge in Large Language Models (LLMs), particularly in context-grounded settings such as RAG and agentic AI systems.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CUDAHercules: Benchmarking Hardware-Aware Expert-level CUDA Optimization for LLMs](https://arxiv.org/abs/2605.08467v1) | 2026-05-12T08:00:00+08:00 | We introduce CUDAHercules, a benchmark that evaluates generated CUDA against end-to-end human-expert SOTA systems.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [PYTHALAB-MERA: Validation-Grounded Memory, Retrieval, and Acceptance Control for Frozen-LLM Coding Agents](https://arxiv.org/abs/2605.08468v1) | 2026-05-12T08:00:00+08:00 | We introduce PYTHALAB-MERA, a lightweight external controller for local validation-conditioned code generation.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [Mid-Training with Self-Generated Data Improves Reinforcement Learning in Language Models](https://arxiv.org/abs/2605.08472v1) | 2026-05-12T08:00:00+08:00 | The effectiveness of Reinforcement Learning (RL) in Large Language Models (LLMs) depends on the nature and diversity of the data used before and during RL.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md) |
| [Do Agents Need to Plan Step-by-Step? Rethinking Planning Horizon in Data-Centric Tool Calling](https://arxiv.org/abs/2605.08477v1) | 2026-05-12T08:00:00+08:00 | Explicit planning is a critical capability for LLM-based agents solving complex data-centric tasks, which require precise tool calling over external data sources.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-PLANNING，[79-planning.md](../../../../books/part-07-agent/79-planning.md) |
| [When Independent Sampling Outperforms Agentic Reasoning](https://arxiv.org/abs/2605.08478v1) | 2026-05-12T08:00:00+08:00 | We study how to allocate inference-time compute for competitive programming under fixed budgets.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MODEL-SAMPLING，[20-sampling.md](../../../../books/part-02-model/20-sampling.md) |
| [Scaling Limits of Long-Context Transformers](https://arxiv.org/abs/2605.08505v1) | 2026-05-12T08:00:00+08:00 | We study the long-context limit of softmax self-attention with a fixed query and a random context of $n$ i.i.d.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[22-long-context.md](../../../../books/part-02-model/22-long-context.md) |
| [A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models](https://arxiv.org/abs/2605.08513v1) | 2026-05-12T08:00:00+08:00 | Safety alignment in language models operates through two mechanistically distinct systems: refusal neurons that gate whether harmful knowledge is expressed, and concept neurons that encode the harmful knowledge itself.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)，已在正文并有 canonical marker |
| [FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration](https://arxiv.org/abs/2605.08520v1) | 2026-05-12T08:00:00+08:00 | We identify that this cost comes from synchronized stage execution and imbalance inside each LLM-heavy stage.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) |
| [Unleashing Scalable Context Parallelism for Foundation Models Pre-Training via FCP](https://arxiv.org/abs/2605.08524v1) | 2026-05-12T08:00:00+08:00 | In this paper, we propose FCP, a flexible context parallelism paradigm that shards and schedules sequences at block-level granularity.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [MARLaaS: Multi-Tenant Asynchronous Reinforcement Learning as a Service](https://arxiv.org/abs/2605.08527v1) | 2026-05-12T08:00:00+08:00 | We propose MARLaaS (Multi-tenant Asynchronous RL as a Service), a system for concurrent RL fine-tuning across multiple users and tasks.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-GRPO，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [Human-Inspired Memory Architecture for LLM Agents](https://arxiv.org/abs/2605.08538v1) | 2026-05-12T08:00:00+08:00 | We present a biologically-grounded memory architecture comprising six cognitive mechanisms: (1) sleep-phase consolidation, (2) interference-based forgetting, (3) engram maturation, (4) reconsolidation upon retrieval, (5) entity knowledge graphs, and (6) hybrid multi-cue retrieval.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Log analysis is necessary for credible evaluation of AI agents](https://arxiv.org/abs/2605.08545v1) | 2026-05-12T08:00:00+08:00 | Agent benchmarks typically report only final outcomes: pass or fail.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Why Retrying Fails: Context Contamination in LLM Agent Pipelines](https://arxiv.org/abs/2605.08563v1) | 2026-05-12T08:00:00+08:00 | We introduce the Context-Contaminated Restart Model (CCRM): a chain of T tool-call steps, each failing with base rate epsilon_0; after any failed attempt, the subsequent attempt operates in contaminated context with elevated error rate epsilon_1 &gt; epsilon_0.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [Different Prompts, Different Ranks: Prompt-aware Dynamic Rank Selection for SVD-based LLM Compression](https://arxiv.org/abs/2605.08568v1) | 2026-05-12T08:00:00+08:00 | We identify two limitations of this static design: the optimal rank varies across individual prompts, and the selected rank is sensitive to the choice of calibration set, leading to suboptimal performance across diverse inputs.；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，已在正文并有 canonical marker |
| [Uncovering Intra-expert Activation Sparsity for Efficient Mixture-of-Expert Model Execution](https://arxiv.org/abs/2605.08575v1) | 2026-05-12T08:00:00+08:00 | Mixture of Experts (MoE) architecture has become the standard for state-of-the-art large language models, owing to its computational efficiency through sparse expert activation.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Slipstream: Trajectory-Grounded Compaction Validation for Long-Horizon Agents](https://arxiv.org/abs/2605.08580v1) | 2026-05-12T08:00:00+08:00 | To cope with the large contexts that long-horizon LLM agents produce, modern frameworks increasingly rely on compaction -- invoking an LLM to rewrite the accumulated trajectory into a shorter summary that the agent resumes from.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY，[77-memory.md](../../../../books/part-07-agent/77-memory.md)，已在正文并有 canonical marker |
| [PRISM: Fast Online LLM Serving via Scheduling-Memory Co-design](https://arxiv.org/abs/2605.08581v1) | 2026-05-12T08:00:00+08:00 | Guided by this, we present PRISM (Prefix Reuse Optimization Integrated Scheduling and Memory), which co-designs a query-aware scheduler (QAS) with a demand-aware radix tree (DART) to align request admission with exact-prefix KV retention.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Computer Science Conferences Should Require Nonrepudiable Experimental Results](https://arxiv.org/abs/2605.08586v1) | 2026-05-12T08:00:00+08:00 | This position paper argues that computer science conferences should require tamper-evident, nonrepudiable attestations of experimental results.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已在正文并有 canonical marker |
| [Kaczmarz Linear Attention](https://arxiv.org/abs/2605.08587v1) | 2026-05-12T08:00:00+08:00 | We propose Kaczmarz Linear Attention (KLA), a one-scalar modification of GDN that preserves the state shape, gates, linear recurrence, and chunkwise parallel algorithm.；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[14-self-attention.md](../../../../books/part-02-model/14-self-attention.md)，已在正文并有 canonical marker |
| [Causal Stories from Sensor Traces: Auditing Epistemic Overreach in LLM-Generated Personal Sensing Explanations](https://arxiv.org/abs/2605.08590v1) | 2026-05-12T08:00:00+08:00 | We introduce epistemic overreach (EO) as a measure for cases where a generated explanation implies more than the available sensing evidence can justify.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FLARE: One-Shot PE-Level Fault Localization in Systolic Arrays via Algebraic Test Vectors](https://arxiv.org/abs/2605.08594v1) | 2026-05-12T08:00:00+08:00 | In this paper, we propose a lightweight, purely algorithmic remedy based on coprime test vectors.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-MONITORING，[67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)，已在正文并有 canonical marker |
| [DSPE: An Energy-Efficient Edge Processor for DeepSeek Inference with MerkleTree-based Incremental Pruning, Multi-Stage Boothing Lookup and Dynamic Adaptive Posit Processing](https://arxiv.org/abs/2605.08615v1) | 2026-05-12T08:00:00+08:00 | In recent years, DeepSeek has achieved strong inference performance but remains hard to deploy on energy-constrained edge devices.；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [EvidenT: An Evidence-Preserving Framework for Iterative System-Level Package Repair](https://arxiv.org/abs/2605.08621v1) | 2026-05-12T08:00:00+08:00 | Motivated by these insights, we propose EvidenT, an evidence-preserving repair framework that decouples iteration-aware evidence management from tool execution.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [PARD-2: Target-Aligned Parallel Draft Model for Dual-Mode Speculative Decoding](https://arxiv.org/abs/2605.08632v1) | 2026-05-12T08:00:00+08:00 | Speculative decoding accelerates Large Language Models (LLMs) inference by using a lightweight draft model to propose candidate tokens that are verified in parallel by the target model.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [EdgeFlowerTune: Evaluating Federated LLM Fine-Tuning Under Realistic Edge System Constraints](https://arxiv.org/abs/2605.08636v1) | 2026-05-12T08:00:00+08:00 | We present EdgeFlowerTune, a deployment-oriented benchmark for federated LLM fine-tuning under realistic edge-system constraints.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已在正文并有 canonical marker |
| [ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning](https://arxiv.org/abs/2605.08639v1) | 2026-05-12T08:00:00+08:00 | We propose ReLibra, an MoE RL training system that exploits a unique opportunity in RL's rollout-training workflow, routing replay, to enable fine-grained load balancing at micro-batch granularity.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [PAAC: Privacy-Aware Agentic Device-Cloud Collaboration](https://arxiv.org/abs/2605.08646v1) | 2026-05-12T08:00:00+08:00 | Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators](https://arxiv.org/abs/2605.08647v1) | 2026-05-12T08:00:00+08:00 | To make these vulnerabilities measurable before deployment, we introduce AgentCollabBench, a diagnostic benchmark of 900 human-validated tasks spanning software engineering, DevOps, and data engineering.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MULTI-AGENT，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)，已在正文并有 canonical marker |
| [Sketch-and-Verify: Structured Inference-Time Scaling via Program Sketching](https://arxiv.org/abs/2605.08658v1) | 2026-05-12T08:00:00+08:00 | SKETCHVERIFY is a within-tier cost-performance policy, not a universal accuracy improvement.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-PLANNING，[79-planning.md](../../../../books/part-07-agent/79-planning.md) |
| [The Cancellation Hypothesis in Critic-Free RL: From Outcome Rewards to Token Credits](https://arxiv.org/abs/2605.08666v1) | 2026-05-12T08:00:00+08:00 | In contrast, we study critic-free RL from a token-level perspective, revealing the token-flipping phenomenon: positive and negative rollouts exhibit remarkably similar proportions of tokens whose probabilities are boosted or suppressed during RL training.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-GRPO，[33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) |
| [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703v1) | 2026-05-12T08:00:00+08:00 | We present RewardHarness, a self-evolving agentic reward framework that reframes reward modeling as context evolution rather than weight optimization.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-RLHF，[31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md)，已在正文并有 canonical marker |
| [The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs](https://arxiv.org/abs/2605.08737v1) | 2026-05-12T08:00:00+08:00 | On-policy distillation (OPD) is widely used for LLM post-training.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-DPO，[34-dpo.md](../../../../books/part-04-training-system/34-dpo.md) |
| [Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows](https://arxiv.org/abs/2605.08761v1) | 2026-05-12T08:00:00+08:00 | We introduce \textsc{EntCollabBench}, a benchmark for evaluating enterprise multi-agent collaboration.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) |
| [EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems](https://arxiv.org/abs/2605.08769v1) | 2026-05-12T08:00:00+08:00 | We propose EvoMAS, a framework for execution-time multi-agent workflow construction.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md) |
| [AgentSlimming: Towards Efficient and Cost-Aware Multi-Agent Systems](https://arxiv.org/abs/2605.08813v1) | 2026-05-12T08:00:00+08:00 | To address this problem, we introduce \textbf{AgentSlimming}, a plug-and-play compression framework for graph-structured multi-agent workflows.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) |
| [SynerDiff: Synergetic Continuous Batching for Fast and Parallel Diffusion Model Inference](https://arxiv.org/abs/2605.08835v1) | 2026-05-12T08:00:00+08:00 | To address these, we propose SynerDiff, an efficient continuous batching system built on intra-inter level synergy.；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-CONTINUOUS-BATCHING，[46-continuous-batching.md](../../../../books/part-05-inference-system/46-continuous-batching.md)，已在正文并有 canonical marker |
| [Generating Leakage-Free Benchmarks for Robust RAG Evaluation](https://arxiv.org/abs/2605.08838v1) | 2026-05-12T08:00:00+08:00 | We introduce SeedRG, a semi-synthetic benchmark generation pipeline that mitigates knowledge leakage and addresses the issue of benchmark aging.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-RAG，[76-rag.md](../../../../books/part-07-agent/76-rag.md)，已在正文并有 canonical marker |
| [ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing](https://arxiv.org/abs/2605.08840v1) | 2026-05-12T08:00:00+08:00 | In this paper, we propose ReST-KV, a robust KV eviction method that combines layer-wise output Reconstruction and Spatial-Temporal smoothing to provide a more comprehensive perspective for the KV cache eviction task.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [BubbleSpec: Turning Long-Tail Bubbles into Speculative Rollout Drafts for Synchronous Reinforcement Learning](https://arxiv.org/abs/2605.08862v1) | 2026-05-12T08:00:00+08:00 | Instead, we propose BubbleSpec, a novel framework that accelerates RL rollouts while strictly keeping the mathematical exactness.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [Rennala MVR: Improved Time Complexity for Parallel Stochastic Optimization via Momentum-Based Variance Reduction](https://arxiv.org/abs/2605.08871v1) | 2026-05-12T08:00:00+08:00 | We show that, under a mean-squared smoothness assumption, variance reduction can improve time complexity in relevant parameter regimes.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md) |
| [Why Do Aligned LLMs Remain Jailbreakable: Refusal-Escape Directions, Operator-Level Sources, and Safety-Utility Trade-off](https://arxiv.org/abs/2605.08878v1) | 2026-05-12T08:00:00+08:00 | We study this question through a continuous input-transformation view.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)，已在正文并有 canonical marker |
| [Quantitative Comparison of Credible Compilation and Verification In Coding Agent Compiler Development](https://arxiv.org/abs/2605.08927v1) | 2026-05-12T08:00:00+08:00 | We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md)，已在正文并有 canonical marker |
| [When and Why Grouping Attention Heads Accelerates Muon Optimization](https://arxiv.org/abs/2605.08933v1) | 2026-05-12T08:00:00+08:00 | We study this question through a one-step descent comparison between full-matrix Muon and group-wise Muon.；3 + 1 + 3 = 7 | 深入完成 | 整合：TRAIN-PRETRAINING，[28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)，已在正文并有 canonical marker |
| [MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production](https://arxiv.org/abs/2605.08962v1) | 2026-05-12T08:00:00+08:00 | As the foundational component of versatile AI applications, training an multimodal large language model (MLLM) relies on multimodal datasets with dynamic modality mixture proportions and sample length distributions.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [Using Semantic Distance to Estimate Uncertainty in LLM-Based Code Generation](https://arxiv.org/abs/2605.09023v1) | 2026-05-12T08:00:00+08:00 | LLMs show strong performance in code generation, but their outputs lack correctness guarantees.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Octopus Protocol: One-Shot Hardware Discovery and Control for AI Agents via Infrastructure-as-Prompts](https://arxiv.org/abs/2605.09055v1) | 2026-05-12T08:00:00+08:00 | We present Octopus Protocol, a system that collapses that cost to a single shell command.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) |
| [Single-Configuration Attack Success Rate Is Not Enough: Jailbreak Evaluations Should Report Distributional Attack Success](https://arxiv.org/abs/2605.09070v1) | 2026-05-12T08:00:00+08:00 | We propose two new measures for jailbreak attacks: the Variant Sensitivity Measure (VSM) and Union Coverage (UC).；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Communication-Theoretic Framework for LLM Agents: Cost-Aware Adaptive Reliability](https://arxiv.org/abs/2605.09121v1) | 2026-05-12T08:00:00+08:00 | Agents built on large language models (LLMs) rely on a range of reliability techniques, including retry, majority voting, and self-consistency, that have been developed in parallel rather than within a common analytical framework.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) |
| [Cosine-Gated Adam-Decay: Drop-In Staleness-Aware Outer Optimization for Decoupled DiLoCo](https://arxiv.org/abs/2605.09126v1) | 2026-05-12T08:00:00+08:00 | We propose Cosine Gated Adam Decay (CGAD), a simple, drop-in, age-aware outer optimizer that scales each incoming pseudo-gradient by $σ(τ) = γ(τ) e^{-ατ}$ before it enters Adam's first- and second-moment buffers; the exponential models information decay and the cosine gate $γ(τ)$ smoothly zeroes contributions past a chosen cutoff.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [CIVeX: Causal Intervention Verification for Language Agents](https://arxiv.org/abs/2605.09168v1) | 2026-05-12T08:00:00+08:00 | We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-TOOL-CALLING，[78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)，已在正文并有 canonical marker |
| [LBI: Parallel Scan Backpropagation via Latent Bounded Interfaces](https://arxiv.org/abs/2605.09204v1) | 2026-05-12T08:00:00+08:00 | We introduce Latent Bounded Interfaces (LBI), an algorithmic formulation that makes scan-based backpropagation tractable by restricting inter-region communication to a low-dimensional latent interface, $ m_k \in \mathbb{R}^{r}$, where $r \ll d$.；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [Flame3D: Zero-shot Compositional Reasoning of 3D Scenes with Agentic Language Models](https://arxiv.org/abs/2605.09218v1) | 2026-05-12T08:00:00+08:00 | We propose Flame3D, a training-free framework that represents scenes as editable visual-textual 3D memories and exposes them to an off-the-shelf MLLM through composable spatial tools.；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，已在正文并有 canonical marker |
| [The Art of the Jailbreak: Formulating Jailbreak Attacks for LLM Security Beyond Binary Scoring](https://arxiv.org/abs/2605.09225v1) | 2026-05-12T08:00:00+08:00 | Jailbreak attacks -- adversarial prompts that bypass LLM alignment through purely linguistic manipulation -- pose a growing operational security threat, yet the field lacks large-scale, reproducible infrastructure for generating, categorizing, and evaluating them systematically.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Two Ways to De-Bias an LLM-as-a-Judge: A Continuous-Score Comparison of Hierarchical Bayesian Calibration and Neural-ODE Score Transport](https://arxiv.org/abs/2605.09227v1) | 2026-05-12T08:00:00+08:00 | [Abridged] Using a Large Language Model (LLM) as an automatic rater (LLM-as-a-judge) is cheap but potentially biased: some judges run lenient, others strict, the middle of the scale gets compressed, and verbose answers may be over-rewarded.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models](https://arxiv.org/abs/2605.09241v1) | 2026-05-12T08:00:00+08:00 | Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be alleviated bysimply constraining latent embeddings with an isotropic Gaussian prior.However, latent representations inherently lie on low-dimensional manifoldswithin a high-dimensional ambient space, and enforcing an isotropic Gaussianprior directly in th；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，已在正文并有 canonical marker |
| [DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification](https://arxiv.org/abs/2605.09269v1) | 2026-05-12T08:00:00+08:00 | To address this, we introduce $\textbf{DeltaRubric}$, an approach that reformulates multimodal preference evaluation as a plan-and-execute process within a single MLLM.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium](https://arxiv.org/abs/2605.09278v1) | 2026-05-12T08:00:00+08:00 | Guided by this equilibrium, we propose EquiMem, an inference-time calibration mechanism that quantifies each update algorithmically against the shared memory state, using agents' existing retrieval queries and traversal paths as evidence rather than soliciting any LLM judgment.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [TileQ: Efficient Low-Rank Quantization of Mixture-of-Experts with 2D Tiling](https://arxiv.org/abs/2605.09281v1) | 2026-05-12T08:00:00+08:00 | To address these limitations, we propose \textsc{TileQ}, a fine-tuning-free post-training quantization (PTQ) method that employs 2D-tiling structured low-rank quantization to share low-rank factors across both input and output dimensions of MoE experts.；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，已在正文并有 canonical marker |
| [BetaEdit: Null-Space Constrained Sequential Model Editing](https://arxiv.org/abs/2605.09285v1) | 2026-05-12T08:00:00+08:00 | Building on these insights, we propose BetaEdit, a refined framework that effectively controls the knowledge leakage and integrates history-aware updates into the null-space paradigm.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Path-Dependent Denoising: A Non-Conservative Field Perspective on Order Collapse in Diffusion Language Models](https://arxiv.org/abs/2605.09303v1) | 2026-05-12T08:00:00+08:00 | Diffusion language models (DLMs) offer a structural alternative to autoregressive generation: denoising can update tokens in arbitrary orders or in parallel rather than along a fixed left-to-right chain.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation](https://arxiv.org/abs/2605.09315v1) | 2026-05-12T08:00:00+08:00 | However, we show that such self-evolution is often non-monotonic: adapting to new task distributions can progressively degrade previously acquired capabilities across all major evolution channels.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-PLATFORM，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)，已在正文并有 canonical marker |
| [Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1) | 2026-05-12T08:00:00+08:00 | We introduce Mem-W, a series of latent-memory-native GUI agents that treat memory as part of the agent's continuous context rather than as an auxiliary symbolic scaffold.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [The Trap of Trajectory: Towards Understanding and Mitigating Spurious Correlations in Agentic Memory](https://arxiv.org/abs/2605.09330v1) | 2026-05-12T08:00:00+08:00 | Second, we propose CAMEL, a plug-and-play calibration method that operates across diverse memory architectures at both write and retrieval time.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Skill-R1: Agent Skill Evolution via Reinforcement Learning](https://arxiv.org/abs/2605.09359v1) | 2026-05-12T08:00:00+08:00 | We propose Skill-R1, a reinforcement learning framework for instance-level recurrent skill optimization from verifiable rewards.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) |
| [31.1 A 14.08-to-135.69Token/s ReRAM-on-Logic Stacked Outlier-Free Large-Language-Model Accelerator with Block-Clustered Weight-Compression and Adaptive Parallel-Speculative-Decoding](https://arxiv.org/abs/2605.09375v1) | 2026-05-12T08:00:00+08:00 | This work presents a 55nm speculative decoding-based LLM accelerator with bumping-based face-to-face ReRAM-on-logic stacking technology.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [NEXUS: Continual Learning of Symbolic Constraints for Safe and Robust Embodied Planning](https://arxiv.org/abs/2605.09387v1) | 2026-05-12T08:00:00+08:00 | While Large Language Models (LLMs) have catalyzed progress in embodied intelligence, a fundamental gap between their inherent probabilistic uncertainty and the strict determinism and verifiable safety required in the physical world.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [BadDLM: Backdooring Diffusion Language Models with Diverse Targets](https://arxiv.org/abs/2605.09397v1) | 2026-05-12T08:00:00+08:00 | We propose BadDLM, a unified framework for studying backdoor attacks against DLMs with diverse targets.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SWIFT: Prompt-Adaptive Memory for Efficient Interactive Long Video Generation](https://arxiv.org/abs/2605.09442v1) | 2026-05-12T08:00:00+08:00 | Motivated by this observation, we present SWIFT, Semantic Windowing and Injection for Flexible Transitions, a training-free framework for multi-prompt long-video generation that enables efficient semantic switching while preserving temporal coherence in causal video diffusion models.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Not All Thoughts Need HBM: Semantics-Aware Memory Hierarchy for LLM Reasoning](https://arxiv.org/abs/2605.09490v1) | 2026-05-12T08:00:00+08:00 | We introduce a semantics-aware memory hierarchy that sorts tokens into four tiers -- HBM, DDR, compressed, and evicted -- using cumulative attention scoring.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces](https://arxiv.org/abs/2605.09497v1) | 2026-05-12T08:00:00+08:00 | We introduce RUC (Real UI Clickboxes), a benchmark of 1,407 scenarios spanning four domains and deception categories.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-TOOL-CALLING，[78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) |
| [Mixture of Layers with Hybrid Attention](https://arxiv.org/abs/2605.09516v1) | 2026-05-12T08:00:00+08:00 | We introduce Mixture of Layers (MoL), which replaces full-width transformer blocks (d_model) with K parallel thin blocks at reduced dimensionality (d_thin &lt;&lt; d_model), connected via learned down/up projections and composed via top-k block routing.；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-MOE，[21-moe.md](../../../../books/part-02-model/21-moe.md)，已在正文并有 canonical marker |
| [TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM](https://arxiv.org/abs/2605.09536v1) | 2026-05-12T08:00:00+08:00 | To address this limitation, we propose TAD, a Temporal-Aware trajectory self-Distillation framework.；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，已在正文并有 canonical marker |
| [TIDE-Bench: Task-Aware and Diagnostic Evaluation of Tool-Integrated Reasoning](https://arxiv.org/abs/2605.09544v1) | 2026-05-12T08:00:00+08:00 | In this work, we introduce TIDE-Bench, a holistic and efficient benchmark for evaluating TIR methods, featuring three key advantages.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Trust Me, Import This: Dependency Steering Attacks via Malicious Agent Skills](https://arxiv.org/abs/2605.09594v1) | 2026-05-12T08:00:00+08:00 | In this paper, we show that this risk is not only a passive model failure.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Edit-Based Refinement for Parallel Masked Diffusion Language Models](https://arxiv.org/abs/2605.09603v1) | 2026-05-12T08:00:00+08:00 | In this paper, we propose ME-DLM, an edit-based refinement framework that augments diffusion generation with lightweight post-editing steps.；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，已在正文并有 canonical marker |
| [Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training](https://arxiv.org/abs/2605.09608v1) | 2026-05-12T08:00:00+08:00 | In this work, we study LLM continual post-training through three questions: What drives forgetting?；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-PRETRAINING，[28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)，已在正文并有 canonical marker |
| [Scratchpad Patching: Decoupling Compute from Patch Size in Byte-Level Language Models](https://arxiv.org/abs/2605.09630v1) | 2026-05-12T08:00:00+08:00 | We introduce Scratchpad Patching (SP), which inserts transient scratchpads inside each patch to aggregate the bytes seen so far and refresh patch-level context for subsequent predictions.；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-TOKENIZER，[11-tokenizer.md](../../../../books/part-02-model/11-tokenizer.md)，已在正文并有 canonical marker |
| [Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction](https://arxiv.org/abs/2605.09649v1) | 2026-05-12T08:00:00+08:00 | We introduce a global retention-based KV eviction method that learns each token's future utility under a unified memory budget.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Workspace Optimization: How to Train Your Agent](https://arxiv.org/abs/2605.09650v1) | 2026-05-12T08:00:00+08:00 | We propose a principled way to evolve the workspace, mirroring the structure of weight-space training: artifacts in place of parameters, evidence in place of data, counterexamples in place of losses, and textual feedback in place of gradients.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) |
| [Forcing-KV: Hybrid KV Cache Compression for Efficient Autoregressive Video Diffusion Models](https://arxiv.org/abs/2605.09681v1) | 2026-05-12T08:00:00+08:00 | Autoregressive (AR) video diffusion models adopt a streaming generation framework, enabling long-horizon video generation with real-time responsiveness, as exemplified by the Self Forcing training paradigm.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring](https://arxiv.org/abs/2605.09684v1) | 2026-05-12T08:00:00+08:00 | We introduce a red-teaming methodology that exposes harder-to-catch attacks for coding-agent monitors, suggesting that current practices may under-elicit attacks and overstate monitor performance.；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MONITORING，[67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)，已在正文并有 canonical marker |
| [DriveFuture: Future-Aware Latent World Models for Autonomous Driving](https://arxiv.org/abs/2605.09701v1) | 2026-05-12T08:00:00+08:00 | In this work, we propose DriveFuture, a future-aware latent world modeling framework for autonomous driving that explicitly learns planning-oriented foresight by conditioning the current latent state modeling process on future world states.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Calibrate, Don't Curate: Label-Efficient Estimation from Noisy LLM Judges](https://arxiv.org/abs/2605.09702v1) | 2026-05-12T08:00:00+08:00 | We show that this heuristic can reverse when the target is not point accuracy, but calibrated probabilistic evaluation from a labeled calibration set.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Security Risks in Tool-Enabled AI Agents: A Systematic Analysis of Privileged Execution Environments](https://arxiv.org/abs/2605.09721v1) | 2026-05-12T08:00:00+08:00 | We introduce a taxonomy of risk categories, illustrate these risks through three representative agent scenarios, and discuss mitigation strategies along with their tradeoffs.；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Dystruct: Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference](https://arxiv.org/abs/2605.09820v1) | 2026-05-12T08:00:00+08:00 | In this paper, we propose a training-free, Bayesian structured decoding framework that formulates flexible-length generation as a dynamic structural inference problem.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Oracle Poisoning: Corrupting Knowledge Graphs to Weaponise AI Agent Reasoning](https://arxiv.org/abs/2605.09822v1) | 2026-05-12T08:00:00+08:00 | We define Oracle Poisoning, an attack class in which an adversary corrupts a structured knowledge graph that AI agents query at runtime via tool-use protocols, causing incorrect conclusions through correct reasoning.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents](https://arxiv.org/abs/2605.09863v1) | 2026-05-12T08:00:00+08:00 | We present Nautilus Compass, a black-box persona drift detector and agent memory layer for production coding agents.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Continuous Latent Contexts Enable Efficient Online Learning in Transformers](https://arxiv.org/abs/2605.09867v1) | 2026-05-12T08:00:00+08:00 | Motivated by this, we study whether continuous latent context tokens equip transformers to more effectively realize online learning.；3 + 2 + 3 = 8 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[22-long-context.md](../../../../books/part-02-model/22-long-context.md)，已在正文并有 canonical marker |
| [Network-Efficient World Model Token Streaming](https://arxiv.org/abs/2605.09886v1) | 2026-05-12T08:00:00+08:00 | We study network-efficient streaming of a discrete world model state, where a stride-16 VQ-U-Net tokenizer (codebook size 8,192) maps each 288x512 frame to an 18x32 grid of token IDs (576 tokens/frame), equivalent to 936 bytes/frame under fixed-length coding.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Skill Description Deception Attack against Task Routing in Internet of Agents](https://arxiv.org/abs/2605.09889v1) | 2026-05-12T08:00:00+08:00 | To characterize this threat, we propose and formalize a new attack model, termed \emph{Skill Description Deception} (SDD) attack.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [TRACER: Verifiable Generative Provenance for Multimodal Tool-Using Agents](https://arxiv.org/abs/2605.09934v1) | 2026-05-12T08:00:00+08:00 | We introduce TRACER, a framework for verifiable generative provenance in multimodal tool-using agents.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md) |
| [Attention Drift: What Autoregressive Speculative Decoding Models Learn](https://arxiv.org/abs/2605.09992v1) | 2026-05-12T08:00:00+08:00 | We identify a previously-unreported phenomenon we call \textbf{attention drift}: as the drafter generates successive tokens within a speculation chain, attention progressively moves from the prompt onto its own recently-generated tokens.；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)，已在正文并有 canonical marker |
| [Sketch-based Access Control: A Multimodal Interface for Translating User Preferences into Intent-Aligned Policies](https://arxiv.org/abs/2605.10012v1) | 2026-05-12T08:00:00+08:00 | We present Sketch-based Access Control (SBAC), a sketch-based, AI-assisted access control authoring system that combines the expressive power of sketching with the interpretive capabilities of multimodal large language models (MLLMs) to support the interpretation and validation of policy specifications as they are iteratively refined.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GELATO: Generative Entropy- and Lyapunov-based Adaptive Token Offloading for Device-Edge Speculative LLM Inference](https://arxiv.org/abs/2605.10124v1) | 2026-05-12T08:00:00+08:00 | The recent growth of on-device Large Language Model (LLM) inference has driven significant interest in device-edge collaborative LLM inference.；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)，已在正文并有 canonical marker |
| [Usability as a Weapon: Attacking the Safety of LLM-Based Code Generation via Usability Requirements](https://arxiv.org/abs/2605.10133v1) | 2026-05-12T08:00:00+08:00 | Large Language Models (LLMs) are increasingly used for automated software development, making their ability to preserve secure coding practices critical.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)，已在正文并有 canonical marker |
| [How Should LLMs Listen While Speaking? A Study of User-Stream Routing in Full-Duplex Spoken Dialogue](https://arxiv.org/abs/2605.10199v1) | 2026-05-12T08:00:00+08:00 | Full-duplex spoken dialogue requires a model to keep listening while generating its own spoken response.；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，已在正文并有 canonical marker |
| [Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution](https://arxiv.org/abs/2605.10223v1) | 2026-05-12T08:00:00+08:00 | We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) |
| [Foundations of Reliable Inference: Reliability-Efficiency Co-Design](https://arxiv.org/abs/2605.10351v1) | 2026-05-12T08:00:00+08:00 | Reliable inference requires that artificial intelligence (AI) models provide trustworthy uncertainty estimates, not merely accurate predictions.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EGL-SCA: Structural Credit Assignment for Co-Evolving Instructions and Tools in Graph Reasoning Agents](https://arxiv.org/abs/2605.10366v1) | 2026-05-12T08:00:00+08:00 | We propose EGL-SCA, a verifier-centric dual-space framework that models a graph reasoning agent using two collaborative components: an instruction-side policy space for reasoning strategies, and a tool-side program space for executable algorithmic tools.；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[81-workflow.md](../../../../books/part-07-agent/81-workflow.md)，已在正文并有 canonical marker |
| [Agent-X: Full Pipeline Acceleration of On-device AI Agents](https://arxiv.org/abs/2605.10380v1) | 2026-05-12T08:00:00+08:00 | We introduce Agent-X, a software-only, accuracy-preserving framework that accelerates both the prefill and decode stages of on-device agent workloads.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-REQUEST-LIFECYCLE，[42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md) |
| [Valid Best-Model Identification for LLM Evaluation via Low-Rank Factorization](https://arxiv.org/abs/2605.10405v1) | 2026-05-12T08:00:00+08:00 | In this work, we propose a principled framework that combines MAB with cheap predicted scores without compromising statistical validity.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Can Agent Benchmarks Support Their Scores? Evidence-Supported Bounds for Interactive-Agent Evaluation](https://arxiv.org/abs/2605.10448v1) | 2026-05-12T08:00:00+08:00 | Interactive agent benchmarks map an agent run to a binary outcome through outcome checks.；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已在正文并有 canonical marker |
| [Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.10481v1) | 2026-05-12T08:00:00+08:00 | We propose Constraint State Governance as a research paradigm for LLM-based multi-agent systems.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md) |
| [Accelerating Compound LLM Training Workloads with Maestro](https://arxiv.org/abs/2605.10501v1) | 2026-05-12T08:00:00+08:00 | In this paper, we introduce Maestro, a section-centric training framework that addresses both challenges.；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)，已在正文并有 canonical marker |
| [Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability](https://arxiv.org/abs/2605.10516v1) | 2026-05-12T08:00:00+08:00 | This paper establishes a rigorous measurement science for AI agent reliability, providing a foundational framework for quantifying consistency under semantically preserving perturbations.；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Acceptance Cards:A Four-Diagnostic Standard for Safe Fine-Tuning Defense Claims](https://arxiv.org/abs/2605.10575v1) | 2026-05-12T08:00:00+08:00 | We introduce Acceptance Cards: an evaluation protocol, a documentation object, an executable audit package, and a claim-specific evidential standard for safe fine-tuning defense claims.；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已在正文并有 canonical marker |
| [PRISM: Generation-Time Detection and Mitigation of Secret Leakage in Multi-Agent LLM Pipelines](https://arxiv.org/abs/2605.10614v1) | 2026-05-12T08:00:00+08:00 | To resolve these issues, we propose PRISM, a real-time defence that treats credential leakage as a sequential risk accumulation problem during generation.；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)，已在正文并有 canonical marker |
| [Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference](https://arxiv.org/abs/2605.10670v1) | 2026-05-12T08:00:00+08:00 | We present EEP, a communication and runtime substrate that represents membership as explicit, mutable runtime state.；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-DYNAMO，[52-dynamo.md](../../../../books/part-05-inference-system/52-dynamo.md)，已在正文并有 canonical marker |
| [MATRA: Modeling the Attack Surface of Agentic AI Systems -- OpenClaw Case Study](https://arxiv.org/abs/2605.10763v1) | 2026-05-12T08:00:00+08:00 | We present MATRA, a pragmatic threat modeling framework for agentic AI systems that adapts established risk assessment methodology to systematically assess how known LLM threats translate into deployment-specific risks.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments](https://arxiv.org/abs/2605.10779v1) | 2026-05-12T08:00:00+08:00 | We present LITMUS (LLM-agents In-OS Testing for Measuring Unsafe Subversion), a benchmark addressing both gaps via a semantic-physical dual verification mechanism and OS-level state rollback.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)，已在正文并有 canonical marker |
| [Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge](https://arxiv.org/abs/2605.10805v1) | 2026-05-12T08:00:00+08:00 | Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational cost.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Verification Mirage: Mapping the Reliability Boundary of Self-Verification in Medical VQA](https://arxiv.org/abs/2605.10850v1) | 2026-05-12T08:00:00+08:00 | We introduce [METHOD NAME], a diagnostic framework for mapping the reliability boundary of medical VLM self-verification by decomposing verifier behavior into discrimination capability and agreement bias.；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870v1) | 2026-05-12T08:00:00+08:00 | Motivated by this decision-centric view of memory, we propose DeMem, an online memory learner that refines its partition only when data certify that a shared state would induce decision conflict, and prove near-minimax regret guarantees.；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[77-memory.md](../../../../books/part-07-agent/77-memory.md) |
| [Compute Where it Counts: Self Optimizing Language Models](https://arxiv.org/abs/2605.10875v1) | 2026-05-12T08:00:00+08:00 | We study dynamic budget allocation for autoregressive decoding: learning how much computation to spend per token from within a single model.；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，已在正文并有 canonical marker |
| [Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers](https://arxiv.org/abs/2605.10901v1) | 2026-05-12T08:00:00+08:00 | To formally evaluate these classifiers, we propose two constructions of such regions: SVD-aligned hyper-rectangles, which yield exact SAT/UNSAT certificates, and Gaussian Mixture Models, which yield probabilistic certificates over semantically coherent clusters.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)，已在正文并有 canonical marker |
| [WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation](https://arxiv.org/abs/2605.10912v1) | 2026-05-12T08:00:00+08:00 | This work presents WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks spanning six thematic categories.；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已在正文并有 canonical marker |
| [Towards Closing the Autoregressive Gap in Language Modeling via Entropy-Gated Continuous Bitstream Diffusion](https://arxiv.org/abs/2605.07013v1) | 2026-05-11 | 词表维输出与质量/熵互相牵制 → bitstream解析posterior+context residual，entropy grid改变effective churn → 重新配置输出接口与采样预算；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.1 |
| [SmellBench: Evaluating LLM Agents on Architectural Code Smell Repair](https://arxiv.org/abs/2605.07001v1) | 2026-05-11 | detector消失/测试通过不等结构修复 → expert FP/partial/TP、direct/cascading与新增smell分账 → 重考虑修复目标oracle和net impact；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.5 |
| [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890v1) | 2026-05-11 | 执行后才见tool error → pre-action last32 hidden→SAE→tool-need/risk probes → 重考虑sensor告警而非执行授权；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[owner](../../../../Books/part-06-ai-infrastructure/67-monitoring.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.3 |
| [Agentick: A Unified Benchmark for General Sequential Decision-Making Agents](https://arxiv.org/abs/2605.06869v1) | 2026-05-11 | 跨范式榜单混入观察/harness收益 → same-seeded任务暴露五观测格式/可组合harness → 重考虑接口与模型的比较identity；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.4 |
| [Self-Consolidating Language Models: Continual Knowledge Incorporation from Context](https://arxiv.org/abs/2605.07076v1) | 2026-05-11 | 静态更新集合难兼顾累计保持 → current model提出where-update、inner候选择优commit、outer改round-start → 重考虑selector与写入参数同环；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-SFT，[owner](../../../../Books/part-04-training-system/29-sft.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.7 |
| [MAGIQ: A Post-Quantum Multi-Agentic AI Governance System with Provable Security](https://arxiv.org/abs/2605.06933v1) | 2026-05-11 | PQ-TLS认证不控制task-msg总预算 → user签session-bound hashchain、Merkle子额/ACL/clock分责 → 重考虑传输/联系许可/额度/语义四边界；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MCP，[owner](../../../../Books/part-07-agent/83-mcp.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.8 |
| [PolarVLM: Bridging the Semantic-Physical Gap in Vision-Language Models](https://arxiv.org/abs/2605.07574v1) | 2026-05-11 | RGB缺反射/透明物理辨别 → 新偏振观测+双branch周期/尺度接口及两阶段适配 → 重考虑补证与放大旧encoder的区别；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[owner](../../../../Books/part-03-multimodal-world-models/23-multimodal-representation.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.9 |
| [Vaporizer: Breaking Watermarking Schemes for Large Language Model Outputs](https://arxiv.org/abs/2605.07481v1) | 2026-05-11 | 只报removal混淆信号与文本保持 → lexical/translation/paraphrase双目标评价 → 重考虑detector operating point与transform范围；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../Books/part-06-ai-infrastructure/72-security.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.12 |
| [Attention Transfer Is Not Universally Effective for Vision Transformers](https://arxiv.org/abs/2605.07191v1) | 2026-05-11 | 少数family attention-only收益被外推 → native norm/scale/position恢复student计算context可逆转失败 → 重考虑routing权重不是可移植完整函数；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-SFT，[owner](../../../../Books/part-04-training-system/29-sft.md)；[具体链](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.13 |
| [DiffRetriever: Parallel Representative Tokens for Retrieval with Diffusion Language Models](https://arxiv.org/abs/2605.07210v1) | 2026-05-11 | 单代表检索受限→同pass多个mask代表与MaxSim/hybrid→重考虑producer与索引成本；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.10 |
| [On the Robustness of Distribution Support under Diffusion Guidance](https://arxiv.org/abs/2605.07220v1) | 2026-05-11 | guidance被误作任意条件正确→理想score下target support终点定理→重考虑support与density/有限步保证；2 + 1 + 3 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.11 |
| [SREGym: A Live Benchmark for AI SRE Agents with High-Fidelity Failure Scenarios](https://arxiv.org/abs/2605.07161v1) | 2026-05-11 | 撤去故障被当恢复→持续client probe与独立注入plane/两oracle→重考虑动态恢复验收；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.14 |
| [Theoretical Limits of Language Model Alignment](https://arxiv.org/abs/2605.07105v1) | 2026-05-11 | 把KL预算当稳定收益→精确tilt gain/Jeffreys与proxy error条件→重考虑目标与估计资格；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.15 |
| [SpecBlock: Block-Iterative Speculative Decoding with Dynamic Tree Drafting](https://arxiv.org/abs/2605.07243v1) | 2026-05-11 | 静态draft树难适应漂移→层移位/跨块缓存与interval adaptation→重考虑draft信号producer和rollback；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[owner](../../../../books/part-05-inference-system/48-speculative-decoding.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.16 |
| [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://arxiv.org/abs/2605.07308v1) | 2026-05-11 | 固定视觉节拍不足接触反应→contact gate切action query并复用slow K/V→重考虑双时钟责任；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.17 |
| [GEM: Generating LiDAR World Model via Deformable Mamba](https://arxiv.org/abs/2605.07326v1) | 2026-05-11 | 普通时空scan混运动信息→frame cues驱动三path/Mamba门控→重考虑ego/control与生成proxy；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.18 |
| [Membership Inference Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2605.07088v1) | 2026-05-11 | 只有token likelihood才泄漏→action error或trajectory smoothness MIA→重考虑privacy unit和低FPR人口；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.19 |
| [Signal Reshaping for GRPO in Weak-Feedback Agentic Code Repair](https://arxiv.org/abs/2605.07276v1) | 2026-05-11 | 零反馈被混为失败→semantic/step credit与资源exit provenance分层→重考虑训练机会人口；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.20 |
| [What Matters for Diffusion-Friendly Latent Manifold? Prior-Aligned Autoencoders for Latent Diffusion](https://arxiv.org/abs/2605.07915v1) | 2026-05-11 | 重构好被当生成latent好→VFM anchor/detailmodulator与邻域decode consistency→重考虑tokenizer三种property；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.21 |
| [Teaching Language Models to Think in Code](https://arxiv.org/abs/2605.07237v1) | 2026-05-11 | 代码中间量被当推理真值→code-only执行轨迹与自然恢复对照→重考虑解释器与逻辑验证；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.22 |
| [HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents](https://arxiv.org/abs/2605.07177v1) | 2026-05-11 | 只数turn掩盖单turn刷调用→grounded bbox query/同turn并行及TRACE双账→重考虑round与call共同预算；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.23 |
| [Teacher-Feature Drifting: One-Step Diffusion Distillation with Pretrained Diffusion Representations](https://arxiv.org/abs/2605.07327v1) | 2026-05-11 | drift依外部encoder→冻结diffusion teacher feature与anchor侧density缺口→重考虑metric producer；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.24 |
| [GPO-V: Jailbreak Diffusion Vision Language Model by Global Probability Optimization](https://arxiv.org/abs/2605.07399v1) | 2026-05-11 | AR强迫prefix被当全程服从→masked后续progressive refusal→重考虑完整sequence/decoder成功判据；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.25 |
| [Beyond Linear Attention: Softmax Transformers Implement In-Context Reinforcement Learning](https://arxiv.org/abs/2605.07333v1) | 2026-05-11 | softmax只作匹配→指定memory rows与temporal shift实现weighted TD→重考虑计算由参数/prompt共同定义；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[owner](../../../../books/part-02-model/14-self-attention.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.26 |
| [Approximation Error Upper and Lower Bounds for Hölder Class with Transformers](https://arxiv.org/abs/2605.07463v1) | 2026-05-11 | 单attention足够被当浅网络足够→量化/context ID/深value map存在性→重考虑计算藏在何处；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-SELF-ATTENTION，[owner](../../../../books/part-02-model/14-self-attention.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.27 |
| [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](https://arxiv.org/abs/2605.07509v1) | 2026-05-11 | 长trace直接归因昂贵→两prefill选择性恢复/NLL与attention候选→重考虑观测proposal和真实cause；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-TRACE，[owner](../../../../books/part-06-ai-infrastructure/69-trace.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.28 |
| [Post-training makes large language models less human-like](https://arxiv.org/abs/2605.07632v1) | 2026-05-11 | assistant更好被当更像人→human response likelihood与persona预测反侧→重考虑规范目标和行为目标；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：TRAIN-RLHF，[owner](../../../../books/part-04-training-system/31-rlhf.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.29 |
| [Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States](https://arxiv.org/abs/2605.07579v1) | 2026-05-11 | value需独立critic→历史固定feature probe与other rollout baseline→重考虑信息泄漏及无偏边界；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-PPO，[owner](../../../../books/part-04-training-system/32-ppo.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.30 |
| [MemCompiler: Compile, Don't Inject -- State-Conditioned Memory for Embodied Agents](https://arxiv.org/abs/2605.07594v1) | 2026-05-11 | memory直接注入context→state-conditioned guidance与brief-state分开→重考虑advice更新和soft-token消费；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.31 |
| [Bringing Multimodal Large Language Models to Infrared-Visible Image Fusion Quality Assessment](https://arxiv.org/abs/2605.06969v1) | 2026-05-11 | 均值评分掩盖冲突→属性分歧proxy定soft-label宽度与内外组ranking→重考虑标注/监督对象；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.32 |
| [Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models](https://arxiv.org/abs/2605.07721v1) | 2026-05-11 | loop depth令KV线性增长→shared per-layer latent gate覆写KV→重考虑context与loop内存边界；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-KV-CACHE，[owner](../../../../books/part-02-model/19-kv-cache.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.33 |
| [Tools as Continuous Flow for Evolving Agentic Reasoning](https://arxiv.org/abs/2605.07339v1) | 2026-05-11 | 离散工具序列成本→latent conditional flow路径/最近embedding decode/首tool commit→重考虑计划表示和执行粒度；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-PLANNING，[owner](../../../../books/part-07-agent/79-planning.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.34 |
| [SARC: A Governance-by-Architecture Framework for Agentic AI Systems](https://arxiv.org/abs/2605.07728v1) | 2026-05-11 | child缺state可能丢规则→最近可判断层rescue/预算拒绝与authority交集→重考虑约束检查owner；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.35 |
| [Operating Within the Operational Design Domain: Zero-Shot Perception with Vision-Language Models](https://arxiv.org/abs/2605.07649v1) | 2026-05-11 | coarse高分被当fine ODD就绪→标签粒度/完备度与两侧风险人口→重考虑sensor接controller验收；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.36 |
| [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990v1) | 2026-05-11 | tool routing可读被当原生因果→fixed menu steering/unembedding与schema controls→重考虑sensor及授权；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.37 |
| [SOD: Step-wise On-policy Distillation for Small Language Model Agents](https://arxiv.org/abs/2605.07725v1) | 2026-05-11 | 多turn指导被等权→sampled abs-logratio调step蒸馏/排除observation→重考虑teacher指导时间资格；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.38 |
| [LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling](https://arxiv.org/abs/2605.08083v1) | 2026-05-11 | 反复在线试controller昂贵→冻结branch/probe replay搜索程序→重考虑离线搜索/真实验收；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-SAMPLING，[owner](../../../../books/part-02-model/20-sampling.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.39 |
| [Dooly: Configuration-Agnostic, Redundancy-Aware Profiling for LLM Inference Simulation](https://arxiv.org/abs/2605.07985v1) | 2026-05-11 | 跨配置反复profile→tainted symbolic签名/动态sweep分离→重考虑复用单位；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.40 |
| [On Privacy Leakage in Tabular Diffusion Models: Influential Factors, Attacker Knowledge, and Metrics](https://arxiv.org/abs/2605.06835v1) | 2026-05-11 | 合成数据距离被当隐私→不完备知识MIA与DCR失配→重考虑威胁/metric与privacy unit；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.41 |
| [Semantic Smoothing for Language Models via Distribution Estimation and Embeddings](https://arxiv.org/abs/2605.07994v1) | 2026-05-11 | 独立count估计→logit-Lipschitz下语义近邻KL sideinfo→重考虑统计共享资格；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-EMBEDDING，[owner](../../../../books/part-02-model/12-embedding.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.42 |
| [Is a team only as strong as its weakest link? Quantifying the short-board effect with AI Agents](https://arxiv.org/abs/2605.07773v1) | 2026-05-11 | 只修最弱成员→受限SOP的noncore影响与debug效率反侧→重考虑composition对照；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.43 |
| [Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions](https://arxiv.org/abs/2605.07984v1) | 2026-05-11 | 可读planning被当native必要→rhyme位置patch分离readable/intervenable→重考虑解释证据资格；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.44 |
| [SARA: Semantically Adaptive Relational Alignment for Video Diffusion Models](https://arxiv.org/abs/2605.07800v1) | 2026-05-11 | 全局alignment忽略关系→text-conditioned entity pair路由→重考虑蒸馏监督对象；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.45 |
| [One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy](https://arxiv.org/abs/2605.07931v1) | 2026-05-11 | 未来condition带宽大→每frame/view一token与joint latent/action flow→重考虑producer/consumer；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.46 |
| [DVD: Discrete Voxel Diffusion for 3D Generation and Editing](https://arxiv.org/abs/2605.07971v1) | 2026-05-11 | binary连续近似或硬提交→categorical uniform反复更新/BSP→重考虑known voxel与decoder保真；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.47 |
| [AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents](https://arxiv.org/abs/2605.07926v1) | 2026-05-11 | 只看endtask→DAG/disclosure与resolved/discovered/provenance分账→重考虑工具依赖评价；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；[具体证据](../_sources/daily-20260512/SUP_SOURCES_20261018.md) A4.48 |

## 4. 证据与知识整合

每项采用 exact-v1；下面记录实际 Method、Evaluation 与反证位置，Books 判断以现有正文命题对读而非关键词命中为依据。

### [Sanity Checks for Long-Form Hallucination Detection](https://arxiv.org/abs/2605.08346v1)

**采用版本与机制证据：** `arXiv:2605.08346v1`；https://arxiv.org/html/2605.08346v1 §3 Force/Remove sanity checks; TRACT — mechanism: We introduce a controlled-invariance methodology that exposes this distinction through two oracle tests: \textsc{Force}, which replaces each response's final answer with the ground truth while preserving the reasoning trace, and \textsc{Remove}, which strips answer-announcement steps while leaving the trajectory intact.。

**评估证据：** https://arxiv.org/html/2605.08346v1 §4 five-model/four-benchmark evaluation — disclosed scope: Hallucination detection methods for large language models increasingly operate on chain-of-thought reasoning traces, yet it remains unclear whether they evaluate the reasoning itself or merely exploit surface correlates of the final answer. We introduce a controlled-invariance methodology that exposes this distinction through two oracle tests: \textsc{Force},…。

**反证与边界：** https://arxiv.org/html/2605.08346v1 Limitations: necessary not sufficient; canonical-answer task scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Evaluation 章已要求 target-preserving invariance、endpoint/trajectory 分层与独立 outcome oracle；Force/Remove 是该原则的一个受限实例。；无需改稿。

### [Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria](https://arxiv.org/abs/2605.08354v1)

**采用版本与机制证据：** `arXiv:2605.08354v1`；https://arxiv.org/html/2605.08354v1 §3 Auto-Rubric as Reward methodology — mechanism: We introduce Auto-Rubric as Reward (ARR), a framework that reframes reward modeling from implicit weight optimization to explicit, criteria-based decomposition.。

**评估证据：** https://arxiv.org/html/2605.08354v1 §4 multimodal evaluation and RPO ablations — disclosed scope: This conversion of implicit preference structure into inspectable, interpretable constraints substantially suppresses evaluation biases including positional bias, enabling both zero-shot deployment and few-shot conditioning on minimal supervision.。

**反证与边界：** https://arxiv.org/html/2605.08354v1 Discussion limitations; rubric/judge and modality boundary; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“`Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria` 通过“We introduce Auto-Rubric as Reward (ARR), a framework that reframes reward modeling from implicit weight optimization to explicit, criteria-based decomposition.”改变 platform evaluation system 的可观察机制或决策边界；exact-v1 的证明范围限于“This conversion of implicit preference structure into inspectable, interpretable constraints substantially suppresses evaluation biases including positional bias, enabling both zero-shot deployment and few-shot conditioning on minimal supervision.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution](https://arxiv.org/abs/2605.08366v1)

**采用版本与机制证据：** `arXiv:2605.08366v1`；https://arxiv.org/html/2605.08366v1 §3 SWE Atlas construction — mechanism: We introduce SWE Atlas, a benchmark suite for coding agents spanning three professional software engineering workflows: Codebase Q&amp;A (124 tasks), Test Writing (90 tasks), and Refactoring (70 tasks).。

**评估证据：** https://arxiv.org/html/2605.08366v1 §4–§5 coding-agent evaluation — disclosed scope: SWE Atlas differs from prior SWE benchmarks in three key ways: it targets underrepresented but practically important task categories, uses comprehensive category-specific evaluation protocols, and adopts under-specified, agentic task formulations that better reflect real-world usage.。

**反证与边界：** https://arxiv.org/html/2605.08366v1 Appendix A limitations; single-turn and omitted DevOps/security; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Evaluation 章已把 coding-agent 验收从 issue resolution 扩展到 artifact、process、environment、runtime coverage 与 side effect；SWE Atlas 扩展任务面，但未改变评测 owner。；无需改稿。

### [On Distinguishing Capability Elicitation from Capability Creation in Post-Training: A Free-Energy Perspective](https://arxiv.org/abs/2605.08368v1)

**采用版本与机制证据：** `arXiv:2605.08368v1`；https://arxiv.org/html/2605.08368v1 — §2 Capability Debate；§3 Free-Energy Perspective；§4 Accessible Support and Four Regimes。

**评估证据：** https://arxiv.org/html/2605.08368v1 — 无独立 benchmark；§4 的四种 regime 与 §5 Alternative Views 构成理论/概念检验。

**反证与边界：** https://arxiv.org/html/2605.08368v1 — §5 Alternative Views and Counterarguments；§6 Conclusion；Appendix A derivation；不证明 frontier post-training 的经验因果；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-GRPO` → [33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)；已读取 `books/part-04-training-system/33-grpo.md` 及同 Part 前后相邻章节；当前主线已覆盖sequence reward、token credit、group/batch composition 与 verifier 约束。本 family 的 exact-v1 增量为“`On Distinguishing Capability Elicitation from Capability Creation in Post-Training: A Free-Energy Perspective` 通过“We develop this argument through a free-energy view of post-training.”改变 train grpo 的可观察机制或决策边界；exact-v1 的证明范围限于“Within this framework, the central question is no longer whether post-training is framed as SFT or RL, but whether it reweights behaviors already within reach, or instead expands the model's reachable behavioral space through…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [CoCoDA: Co-evolving Compositional DAG for Tool-Augmented Agents](https://arxiv.org/abs/2605.08399v1)

**采用版本与机制证据：** `arXiv:2605.08399v1`；https://arxiv.org/html/2605.08399v1 — §3 Proposed Method；§3.2 Typed DAG Retrieval；§3.3 Co-Evolution；§3.4 Theory。

**评估证据：** https://arxiv.org/html/2605.08399v1 — §4 Experiments；§4.2 main；§4.3 scalability/efficiency；§4.4 ablation；Appendix I–K。

**反证与边界：** https://arxiv.org/html/2605.08399v1 — 无独立 limitations；§3.4 assumptions、Appendix H.3 rejected cases 与 §5 Conclusion 限定主张；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。本 family 的 exact-v1 增量为“`CoCoDA: Co-evolving Compositional DAG for Tool-Augmented Agents` 通过“We propose CoCoDA, a framework that co-evolves the planner and tool library through a single code-native structure: a compositional code DAG.”改变 agent workflow 的可观察机制或决策边界；exact-v1 的证明范围限于“Across mathematical reasoning, tabular analysis, and code task benchmarks, CoCoDA enables an 8B student to match or exceed a 32B teacher on GSM8K and MATH and consistently improves over strong tool-use and library-learning baselines.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering](https://arxiv.org/abs/2605.08432v1)

**采用版本与机制证据：** `arXiv:2605.08432v1`；https://arxiv.org/html/2605.08432v1 — §4 Semantic-Sampling Framework；§4.1 Sem1；§4.2 Sem2；§5 Theory。

**评估证据：** https://arxiv.org/html/2605.08432v1 — §6 Experiments；§6.1–§6.4。

**反证与边界：** https://arxiv.org/html/2605.08432v1 — §5.2 low-margin regime 与 theorem assumptions；无独立 limitations，不能外推未测 semantic clusterer/evaluator；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“`A Semantic-Sampling Framework for Evaluating Calibration in Open-Ended Question Answering` 通过“We introduce Sem-ECE (Semantic-Sampling Expected Calibration Error), a calibration evaluation framework for open-ended QA that samples answers from the model, groups them into semantic classes, and uses the resulting frequencies as confidence.”改变 platform evaluation system 的可观察机制或决策边界；exact-v1 的证明范围限于“Open-ended question answering (QA), the most common deployment setting for modern LLMs, is where existing evaluation methods fall short: logit-based metrics need restricted output formats and internal probabilities; verbalized confidence is self-reported and often…”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [When Child Inherits: Modeling and Exploiting Subagent Spawn in Multi-Agent Networks](https://arxiv.org/abs/2605.08460v1)

**采用版本与机制证据：** `arXiv:2605.08460v1`；https://arxiv.org/html/2605.08460v1 §III spawn/authority/isolation/resource model — mechanism: We demonstrate these risks in real agent frameworks and propose defenses based on explicit security invariants.。

**评估证据：** https://arxiv.org/html/2605.08460v1 §V real-system exploit evaluation — disclosed scope: We demonstrate these risks in real agent frameworks and propose defenses based on explicit security invariants.。

**反证与边界：** https://arxiv.org/html/2605.08460v1 §III-F limitations; role-based structural model excludes execution semantics; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MULTI-AGENT` → [82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；当前 Multi-Agent 章记录 parent link、authority 与 task identity，但未明确把 inherited memory 视为可跨 spawn 传播污染的 tainted input。；正文已存在。

### [Do Benchmarks Underestimate LLM Performance? Evaluating Hallucination Detection With LLM-First Human-Adjudicated Assessment](https://arxiv.org/abs/2605.08462v1)

**采用版本与机制证据：** `arXiv:2605.08462v1`；https://arxiv.org/html/2605.08462v1 PDF §4 LLM inference and human adjudication — mechanism: Hallucination remains a persistent challenge in Large Language Models (LLMs), particularly in context-grounded settings such as RAG and agentic AI systems. This study focuses on contextual hallucination detection in summarization tasks. We analyze the QAGS-C and SummEval datasets by comparing original benchmark annotations with reason and…。

**评估证据：** https://arxiv.org/html/2605.08462v1 PDF §5 results; QAGS-C and SummEval — disclosed scope: Following this re-evaluation, triple agreement (between human, GPT, and Gemini) increased by 6.38% for QAGS-C and 7.62% for SummEval.。

**反证与边界：** https://arxiv.org/html/2605.08462v1 PDF conclusion; two adjudicators, capped conflict subset and summarization-only scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Evaluation 章已要求先审计 reference coverage、再区分 detector miss 与 reference omission，并限制 LLM judge 的裁决权；该人机复核协议是现有测量边界的实例。；无需改稿。

### [CUDAHercules: Benchmarking Hardware-Aware Expert-level CUDA Optimization for LLMs](https://arxiv.org/abs/2605.08467v1)

**采用版本与机制证据：** `arXiv:2605.08467v1`；https://arxiv.org/html/2605.08467v1 — §3 Benchmark Design；§3.1 task classes；§3.3 protocol/metrics；§3.4 anti-cheating。

**评估证据：** https://arxiv.org/html/2605.08467v1 — §4 Experiments；§4.1–§4.4；Appendix C architecture stress results。

**反证与边界：** https://arxiv.org/html/2605.08467v1 — 无独立 limitations；task catalog、模型、GPU、correctness harness 与 expert reference 限定 benchmark 结论；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；已读取 `books/part-05-inference-system/49-tensorrt-llm.md` 及同 Part 前后相邻章节；当前主线已覆盖execution plan、kernel/quantization contract、精度边界与 fallback。本 family 的 exact-v1 增量为“`CUDAHercules: Benchmarking Hardware-Aware Expert-level CUDA Optimization for LLMs` 通过“We introduce CUDAHercules, a benchmark that evaluates generated CUDA against end-to-end human-expert SOTA systems.”改变 infer tensorrt llm 的可观察机制或决策边界；exact-v1 的证明范围限于“Large language models show promise for automated CUDA programming, however even the strongest coding models (e.g., Claude-Opus-4.6) may still fall short of expert-level, architecture-aware optimization.”，不能外推到未披露 workload、model、hardware、precision、evaluator 或 SLO”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [PYTHALAB-MERA: Validation-Grounded Memory, Retrieval, and Acceptance Control for Frozen-LLM Coding Agents](https://arxiv.org/abs/2605.08468v1)

**采用版本与机制证据：** `arXiv:2605.08468v1`；https://arxiv.org/html/2605.08468v1 §3 validation-grounded memory/retrieval/acceptance control — mechanism: We introduce PYTHALAB-MERA, a lightweight external controller for local validation-conditioned code generation.。

**评估证据：** https://arxiv.org/html/2605.08468v1 §4 coding-agent evaluation — disclosed scope: Local LLM-based coding agents increasingly work in settings where correctness is earned through execution feedback, persistent state, and bounded repair, not through a single fluent answer. Static retrieval, long-context prompting, self-refinement, execution-feedback repair, and reinforcement learning over model weights each address part of this setting, but…。

**反证与边界：** https://arxiv.org/html/2605.08468v1 §5 limitations; frozen-model and benchmark boundary; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；Workflow 章已把 memory/retrieval proposal、deterministic verifier、acceptance gate 与 clean-state retry 分开；该 frozen-LLM coding-agent pipeline 未改变这些状态 owner。；无需改稿。

### [Mid-Training with Self-Generated Data Improves Reinforcement Learning in Language Models](https://arxiv.org/abs/2605.08472v1)

**采用版本与机制证据：** `arXiv:2605.08472v1`；https://arxiv.org/html/2605.08472v1 §3 self-generated mid-training procedure — mechanism: The effectiveness of Reinforcement Learning (RL) in Large Language Models (LLMs) depends on the nature and diversity of the data used before and during RL. In particular, reasoning problems can often be approached in multiple ways that rely on different forms of reasoning, and exposure to…。

**评估证据：** https://arxiv.org/html/2605.08472v1 §5–§6 RL transfer evaluation — disclosed scope: We then empirically demonstrate that RL-trained models initialized with our mid-training data achieve consistent improvements across various mathematical reasoning benchmarks and other OOD tasks like code generation and narrative reasoning.。

**反证与边界：** https://arxiv.org/html/2605.08472v1 Appendix A.1 limitations; math-centric heuristics and pass@1 boundary; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-PRETRAINING` → [28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)；Pretraining 章已将 self-generated data 视为带 lineage、teacher/policy identity 与独立 held-out gate 的训练资产；mid-training 实例未改变 data/objective owner。；无需改稿。

### [Do Agents Need to Plan Step-by-Step? Rethinking Planning Horizon in Data-Centric Tool Calling](https://arxiv.org/abs/2605.08477v1)

**采用版本与机制证据：** `arXiv:2605.08477v1`；https://arxiv.org/html/2605.08477v1 §3 planning-horizon variants — mechanism: Our experiments across Knowledge Base Question Answering and Multi-hop QA show that FH planning with lazy replanning achieves accuracy parity with SH across varying depths, breadths, and robustness levels, while using 2-3x fewer tokens.。

**评估证据：** https://arxiv.org/html/2605.08477v1 §4–§5 data-centric tool-calling evaluation — disclosed scope: Explicit planning is a critical capability for LLM-based agents solving complex data-centric tasks, which require precise tool calling over external data sources. Existing strategies fall into two paradigms based on planning horizon: (1) full-horizon (FH), which generates a complete plan before execution, and (2) single-step horizon…。

**反证与边界：** https://arxiv.org/html/2605.08477v1 Discussion boundary; task/tool and horizon scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-PLANNING` → [79-planning.md](../../../../books/part-07-agent/79-planning.md)；Planning 章已把 plan horizon 作为随任务状态、可验证反馈与执行成本变化的控制变量，而非固定逐步展开；该 tool-calling 研究提供受限分支。；无需改稿。

### [When Independent Sampling Outperforms Agentic Reasoning](https://arxiv.org/abs/2605.08478v1)

**采用版本与机制证据：** `arXiv:2605.08478v1`；https://arxiv.org/html/2605.08478v1 §2 matched-budget methods — mechanism: Our results show that, for self-contained algorithmic tasks, independent exploration can outperform deeper agentic reasoning under realistic resource constraints.。

**评估证据：** https://arxiv.org/html/2605.08478v1 §3–§5 Codeforces cost/query evaluation — disclosed scope: Our results show that, for self-contained algorithmic tasks, independent exploration can outperform deeper agentic reasoning under realistic resource constraints.。

**反证与边界：** https://arxiv.org/html/2605.08478v1 §7 future directions; self-contained programming task boundary; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MODEL-SAMPLING` → [20-sampling.md](../../../../books/part-02-model/20-sampling.md)；Sampling 章已区分独立样本、搜索/推理结构、相关错误与总预算；独立采样何时优于 agentic reasoning 属于已有 budget-allocation 分支。；无需改稿。

### [Scaling Limits of Long-Context Transformers](https://arxiv.org/abs/2605.08505v1)

**采用版本与机制证据：** `arXiv:2605.08505v1`；https://arxiv.org/html/2605.08505v1 — §2 Setup；§3 attention-weight scaling regimes；§4 outputs。

**评估证据：** https://arxiv.org/html/2605.08505v1 — §5 Numerical Experiments；Appendix A supporting lemmas。

**反证与边界：** https://arxiv.org/html/2605.08505v1 — 固定 query、i.i.d. spherical keys 与 temperature scaling 是强假设；不等同真实 trained long-context transformer；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MODEL-LONG-CONTEXT` → [22-long-context.md](../../../../books/part-02-model/22-long-context.md)；Long Context 章已经分开名义长度、position extrapolation、effective utilization、attention/KV 成本与训练分布；该 scaling-limit 分析没有改变这组能力边界。；无需改稿。

### [A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models](https://arxiv.org/abs/2605.08513v1)

**采用版本与机制证据：** `arXiv:2605.08513v1`；https://arxiv.org/html/2605.08513v1 PDF §2 feature selection, reranking and intervention — mechanism: Safety alignment in language models operates through two mechanistically distinct systems: refusal neurons that gate whether harmful knowledge is expressed, and concept neurons that encode the harmful knowledge itself. By targeting a single neuron in each system, we demonstrate both directions of failure -- bypassing safety…。

**评估证据：** https://arxiv.org/html/2605.08513v1 PDF §2.4–§5 seven-model evaluation — disclosed scope: By targeting a single neuron in each system, we demonstrate both directions of failure -- bypassing safety on explicit harmful requests via suppression, and inducing harmful content from innocent prompts via amplification -- across seven models spanning two families and 1.7B to 70B parameters, without any…。

**反证与边界：** https://arxiv.org/html/2605.08513v1 PDF §6 limitations; two families and one concept-neuron case; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；当前 Security 章覆盖模型/运行时多层防线，但未写明安全行为可能集中在极少 activation gate、单点干预即可绕过或反转拒答的 white-box failure boundary。；正文已存在。

### [FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration](https://arxiv.org/abs/2605.08520v1)

**采用版本与机制证据：** `arXiv:2605.08520v1`；https://arxiv.org/html/2605.08520v1 §3 asynchronous stage orchestration — mechanism: We present FlashEvolve, an efficient framework that replaces synchronized execution with asynchronous workers and queues, allowing different stages and steps to overlap.。

**评估证据：** https://arxiv.org/html/2605.08520v1 §4 agent-evolution workloads — disclosed scope: LLM-based evolution has emerged as a promising way to improve agents by refining non-parametric artifacts, but its wall-clock cost remains a major bottleneck. We identify that this cost comes from synchronized stage execution and imbalance inside each LLM-heavy stage. We present FlashEvolve, an efficient framework that…。

**反证与边界：** https://arxiv.org/html/2605.08520v1 Limitations: limited algorithms and integration-specific artifact state; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-PLATFORM` → [84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)；Agent Platform 已把 self-evolution 拆成候选生成、异步执行、独立 acceptor、版本化 artifact 与 rollback；stage orchestration 是既有平台状态机的实现分支。；无需改稿。

### [Unleashing Scalable Context Parallelism for Foundation Models Pre-Training via FCP](https://arxiv.org/abs/2605.08524v1)

**采用版本与机制证据：** `arXiv:2605.08524v1`；https://arxiv.org/html/2605.08524v1 §3 Fully Connected Parallelism — mechanism: In this paper, we propose FCP, a flexible context parallelism paradigm that shards and schedules sequences at block-level granularity.。

**评估证据：** https://arxiv.org/html/2605.08524v1 §5 distributed-training evaluation — disclosed scope: Context parallelism (CP) has been widely adopted to support the growing context length in foundation model pretraining. However, existing designs fail to handle the large variation in sequence length from training datasets, resulting in suboptimal performance. These methods often over-shard short sequences, leading to compute inefficiency…。

**反证与边界：** https://arxiv.org/html/2605.08524v1 §7 limitations; arbitrary P2P/all-to-all and topology assumptions; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；Context Parallel 的 topology-aware exchange plan 已写入 Distributed Training 正文：plan 绑定 sequence/head ownership、topology revision、buffer budget 与 plan epoch，并保留规则 collective fallback。；正文已存在。

### [MARLaaS: Multi-Tenant Asynchronous Reinforcement Learning as a Service](https://arxiv.org/abs/2605.08527v1)

**采用版本与机制证据：** `arXiv:2605.08527v1`；https://arxiv.org/html/2605.08527v1 §3 disaggregated asynchronous RLaaS — mechanism: We propose MARLaaS (Multi-tenant Asynchronous RL as a Service), a system for concurrent RL fine-tuning across multiple users and tasks.。

**评估证据：** https://arxiv.org/html/2605.08527v1 §4 up-to-32-task evaluation — disclosed scope: Reinforcement Learning from Verifiable Rewards (RLVR) has significantly improved the reasoning capabilities of large language models (LLMs), particularly in multi-turn agentic settings involving environment interaction like tool use. However, fine-tuning such models remains prohibitively expensive due to high computational requirements, limiting accessibility. We propose MARLaaS (Multi-tenant…。

**反证与边界：** https://arxiv.org/html/2605.08527v1 Limitations: serialized policy updates and KV capacity; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-GRPO` → [33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)；GRPO 章已经把 rollout、environment 与 policy training 分池，并要求 policy/adapter identity、staleness 与多租户隔离；MARLaaS 未增加新的 commit authority。；无需改稿。

### [Human-Inspired Memory Architecture for LLM Agents](https://arxiv.org/abs/2605.08538v1)

**采用版本与机制证据：** `arXiv:2605.08538v1`；https://arxiv.org/html/2605.08538v1 — §3 Technical Architecture；§4 Memory Consolidation Pipeline；§5 Adaptive Forgetting；§7.2 Reconsolidation。

**评估证据：** https://arxiv.org/html/2605.08538v1 — §8 Experimental Methodology；§9 Evaluation（VSCode 与 LongMemEval S/M tier）。

**反证与边界：** https://arxiv.org/html/2605.08538v1 — §11 Limitations：机制未被独立消融、统计功效、领域宽度与 benchmark-architecture alignment；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MEMORY` → [77-memory.md](../../../../books/part-07-agent/77-memory.md)；当任务跨会话累积时，单层 append-only memory 会同时放大存储与旧信息干扰；论文用 hot/warm/long-term 分层、consolidation、importance/干扰遗忘和 reconsolidation 形成生命周期。现有 Ch77 已把 consolidation、forgetting、provenance、revalidation 与 memory-budget/decision-quality operating curve写成同一状态机，因此该实现不改变 commit owner。；无需改稿。

### [Log analysis is necessary for credible evaluation of AI agents](https://arxiv.org/abs/2605.08545v1)

**采用版本与机制证据：** `arXiv:2605.08545v1`；https://arxiv.org/html/2605.08545v1 §2 validity threats; §3 log-analysis taxonomy — mechanism: In this paper, we (1) present a taxonomy of threats to credible evaluation documented through log analysis, and (2) develop a set of guiding principles for log analysis.。

**评估证据：** https://arxiv.org/html/2605.08545v1 §4 tau-Bench Airline case study — disclosed scope: This threatens evaluation credibility in three ways.。

**反证与边界：** https://arxiv.org/html/2605.08545v1 §6 recommendations; illustrative case is not universal coverage; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Evaluation 章已区分 final outcome、完整 trajectory、外部 effect 与危险副作用，日志分析 taxonomy 是已有 evidence contract 的应用。；无需改稿。

### [Why Retrying Fails: Context Contamination in LLM Agent Pipelines](https://arxiv.org/abs/2605.08563v1)

**采用版本与机制证据：** `arXiv:2605.08563v1`；https://arxiv.org/html/2605.08563v1 §2 CCRM; §3–§6 theorems — mechanism: We introduce the Context-Contaminated Restart Model (CCRM): a chain of T tool-call steps, each failing with base rate epsilon_0; after any failed attempt, the subsequent attempt operates in contaminated context with elevated error rate epsilon_1 &gt; epsilon_0.。

**评估证据：** https://arxiv.org/html/2605.08563v1 §7 SWE-bench and synthetic validation — disclosed scope: When an LLM agent fails a multi-step tool-augmented task and retries, the failed attempt typically remains in its context window -- contaminating the next attempt and elevating the per-step error rate beyond the base level. This context-contaminated restart phenomenon is widely observed in practice yet entirely…。

**反证与边界：** https://arxiv.org/html/2605.08563v1 §8 limitations; binary contamination and independence assumptions; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；Workflow 章已要求 retry 绑定 checkpoint、证据与新的 clean execution context；CCRM 形式化了已承载的 contamination 风险但未改变 owner。；无需改稿。

### [Different Prompts, Different Ranks: Prompt-aware Dynamic Rank Selection for SVD-based LLM Compression](https://arxiv.org/abs/2605.08568v1)

**采用版本与机制证据：** `arXiv:2605.08568v1`；https://arxiv.org/html/2605.08568v1 — §4 Method；§4.1 rank experts；§4.2 router；§4.3 prefill retrieval/decode reuse；§4.4 aggregation/kernel fusion。

**评估证据：** https://arxiv.org/html/2605.08568v1 — §5 Experiment；§5.2 Main Results；§5.3 Ablations。

**反证与边界：** https://arxiv.org/html/2605.08568v1 — Appendix B Limitations：router/cache preprocessing、额外 memory，且未覆盖 multimodal、encoder-decoder 与生产负载；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；现有 Ch49 覆盖静态低秩压缩和量化 execution plan，却没有让 prompt-conditioned router 在 prefill 选择 rank pattern、decode 复用该 pattern，并把 expert aggregation 与 fused kernel 一起纳入可回退执行身份。；已在正文并有 canonical marker。

### [Uncovering Intra-expert Activation Sparsity for Efficient Mixture-of-Expert Model Execution](https://arxiv.org/abs/2605.08575v1)

**采用版本与机制证据：** `arXiv:2605.08575v1`；https://arxiv.org/html/2605.08575v1 §3 intra-expert sparsity analysis and vLLM execution — mechanism: Mixture of Experts (MoE) architecture has become the standard for state-of-the-art large language models, owing to its computational efficiency through sparse expert activation. However, sparsity through finer expert granularity is becoming increasingly difficult to achieve due to fundamental training challenges such as expert collapse and load…。

**评估证据：** https://arxiv.org/html/2605.08575v1 §4 eight-model/runtime evaluation — disclosed scope: Mixture of Experts (MoE) architecture has become the standard for state-of-the-art large language models, owing to its computational efficiency through sparse expert activation. However, sparsity through finer expert granularity is becoming increasingly difficult to achieve due to fundamental training challenges such as expert collapse and load…。

**反证与边界：** https://arxiv.org/html/2605.08575v1 Discussion limitations; activation threshold and hardware/kernel scope; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；Execution 章已把稀疏计算收益约束在可执行 kernel/layout、路由分布、正确性和 fallback 之内；intra-expert activation sparsity 是该执行计划的一条受限优化分支。；无需改稿。

### [Slipstream: Trajectory-Grounded Compaction Validation for Long-Horizon Agents](https://arxiv.org/abs/2605.08580v1)

**采用版本与机制证据：** `arXiv:2605.08580v1`；https://arxiv.org/html/2605.08580v1 §3 asynchronous compaction and trajectory-grounded validator — mechanism: To cope with the large contexts that long-horizon LLM agents produce, modern frameworks increasingly rely on compaction -- invoking an LLM to rewrite the accumulated trajectory into a shorter summary that the agent resumes from. Today, compaction runs synchronously on the critical path of agent execution…。

**评估证据：** https://arxiv.org/html/2605.08580v1 §4 SWE-bench/BrowseComp evaluation — disclosed scope: To cope with the large contexts that long-horizon LLM agents produce, modern frameworks increasingly rely on compaction -- invoking an LLM to rewrite the accumulated trajectory into a shorter summary that the agent resumes from. Today, compaction runs synchronously on the critical path of agent execution…。

**反证与边界：** https://arxiv.org/html/2605.08580v1 Discussion limitations; judge quality and delayed-validation budget; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MEMORY` → [77-memory.md](../../../../books/part-07-agent/77-memory.md)；当前 Memory 章讨论 compaction/sufficiency，但未把旧轨迹上的异步 shadow compaction、未来 resumed actions 的 counterfactual validation 与 failback 组合成提交协议。；正文已存在。

### [PRISM: Fast Online LLM Serving via Scheduling-Memory Co-design](https://arxiv.org/abs/2605.08581v1)

**采用版本与机制证据：** `arXiv:2605.08581v1`；https://arxiv.org/html/2605.08581v1 §3 PRISM QAS+DART co-design — mechanism: Guided by this, we present PRISM (Prefix Reuse Optimization Integrated Scheduling and Memory), which co-designs a query-aware scheduler (QAS) with a demand-aware radix tree (DART) to align request admission with exact-prefix KV retention.。

**评估证据：** https://arxiv.org/html/2605.08581v1 §4 A800/4B/13B serving evaluation — disclosed scope: Our evaluation results show that, versus the strongest baseline, PRISM reduces average per-QPS P99 TTFT by 23.3\% and 37.1\% while increasing exact-prefix KV-cache hit rate by 5.9 and 12.2 percentage points on 4B and 13B models, respectively.。

**反证与边界：** https://arxiv.org/html/2605.08581v1 Limitations: fixed workload, single A800, no multi-GPU/heterogeneous pool; exact-v1 §6 / Appendix non-proof boundary check — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-SCHEDULING` → [56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)；Scheduling 与 KV 章已把 segment identity、hot-prefix locality、admission、residency/freshness 与 fallback 联合；PRISM 是一个具体 co-design 实现点。；无需改稿。

### [Computer Science Conferences Should Require Nonrepudiable Experimental Results](https://arxiv.org/abs/2605.08586v1)

**采用版本与机制证据：** `arXiv:2605.08586v1`；https://arxiv.org/html/2605.08586v1 §3 Problem and Security Properties; §4 Threat Model; §5 K-Veritas — mechanism: To show that the problem is solvable, we built K-Veritas, a reference implementation in Go that produces signed reports without accessing training data.。

**评估证据：** https://arxiv.org/html/2605.08586v1 §5 Reference Implementation and Protocol Walkthrough — disclosed scope: We name the underlying problem experiment nonrepudiation: a compliant protocol must bind the numbers in a paper to an actual executed computation in a way the author cannot later alter or deny.。

**反证与边界：** https://arxiv.org/html/2605.08586v1 §6 Discussion; position-paper and prototype boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：实验结论需要把论文数字、实际执行、代码身份与签名收据绑定为不可抵赖的 evidence chain。；正文已存在。

### [Kaczmarz Linear Attention](https://arxiv.org/abs/2605.08587v1)

**采用版本与机制证据：** `arXiv:2605.08587v1`；https://arxiv.org/html/2605.08587v1 §3 Kaczmarz Linear Attention — mechanism: We revisit the online-regression objective underlying GDN and, inspired by the Kaczmarz projection method, derive the key-norm-normalized dynamic step size $β_t = η_t / (\/k_t\/_2^2 + ε)$ for residual updates.。

**评估证据：** https://arxiv.org/html/2605.08587v1 §5 Experiments — disclosed scope: Long-context language modeling remains central to modern sequence modeling, but the quadratic cost of Transformer attention makes scaling computationally prohibitive. Linear recurrent models address this bottleneck by compressing the context into a fixed-size state, making the rule that forgets, writes, and edits information a central design…。

**反证与边界：** https://arxiv.org/html/2605.08587v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MODEL-SELF-ATTENTION` → [14-self-attention.md](../../../../books/part-02-model/14-self-attention.md)；已读取 `books/part-02-model/14-self-attention.md` 及同 Part 前后相邻章节；当前主线已覆盖full attention、线性/递归状态压缩及其写入、遗忘与容量边界。但正文尚未明确承载本 family 的增量边界：线性注意力的 recurrent state update 应由 online-regression objective 推导步长，而不是只学习无归一化更新系数。；正文已存在。

### [Causal Stories from Sensor Traces: Auditing Epistemic Overreach in LLM-Generated Personal Sensing Explanations](https://arxiv.org/abs/2605.08590v1)

**采用版本与机制证据：** `arXiv:2605.08590v1`；https://arxiv.org/html/2605.08590v1 §3 Study Design and Methods; §3.4 Evaluation Methodology — mechanism: We introduce epistemic overreach (EO) as a measure for cases where a generated explanation implies more than the available sensing evidence can justify.。

**评估证据：** https://arxiv.org/html/2605.08590v1 §4 Results — disclosed scope: These findings suggest that evidential grounding should be a first-order evaluation criterion for LLM-generated personal sensing explanations, alongside fluency and plausibility.。

**反证与边界：** https://arxiv.org/html/2605.08590v1 §5.5 Limitations and Future Directions — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“生成式解释需要把 observation、inference、unknown 分层；增加 context 或 bounded prompt 不能替代 claim-level evidence gate”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [FLARE: One-Shot PE-Level Fault Localization in Systolic Arrays via Algebraic Test Vectors](https://arxiv.org/abs/2605.08594v1)

**采用版本与机制证据：** `arXiv:2605.08594v1`；https://arxiv.org/html/2605.08594v1 §4 One-Round Localization; §5 Two-Round Localization — mechanism: In this paper, we propose a lightweight, purely algorithmic remedy based on coprime test vectors.。

**评估证据：** https://arxiv.org/html/2605.08594v1 §6 Evaluation — disclosed scope: Systolic arrays are the dominant compute fabric for neural network inference. Prior work has addressed column-level fault detection efficiently with uniform test patterns, but row-level (PE-level) fault localization within a faulty column remains open without resorting to hardware redundancy. The fundamental obstacle is that uniform test…。

**反证与边界：** https://arxiv.org/html/2605.08594v1 §7 Discussion and Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-MONITORING` → [67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及同 Part 前后相邻章节；当前主线已覆盖信号采集、传感器身份、silent-data-corruption 检测与失效升级路径。但正文尚未明确承载本 family 的增量边界：AI accelerator 的 silent-fault sensor 可用代数测试向量保留 PE 行身份；单轮概率定位失败时必须升级到比值型两轮 fallback。；正文已存在。

### [DSPE: An Energy-Efficient Edge Processor for DeepSeek Inference with MerkleTree-based Incremental Pruning, Multi-Stage Boothing Lookup and Dynamic Adaptive Posit Processing](https://arxiv.org/abs/2605.08615v1)

**采用版本与机制证据：** `arXiv:2605.08615v1`；https://arxiv.org/html/2605.08615v1 — §3 Proposed DSPE Processor；§3.1 MIPS；§3.2 MBLM；§3.3 DAPPM。

**评估证据：** https://arxiv.org/html/2605.08615v1 — §4 Evaluation Results：Verilog、28nm synthesis/P&R、area/power/frequency/peak throughput。

**反证与边界：** https://arxiv.org/html/2605.08615v1 — 正文没有独立 limitations；只证明作者 RTL/P&R 与模拟配置，不证明流片、端到端服务质量或跨模型通用性；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；exact-v1 实际是 DeepSeek edge processor，而不是旧审计描述的 ReRAM/speculative 论文；其 MerkleTree incremental pruning、近似乘法复用与 dynamic posit 是特定 28nm RTL/P&R operating point。Ch49 已要求 precision、pruning、layout、kernel、正确性与 hardware profile 共同形成 execution plan，并保留 supported precision fallback，因此该芯片设计没有改变通用 owner。；无需改稿。

### [EvidenT: An Evidence-Preserving Framework for Iterative System-Level Package Repair](https://arxiv.org/abs/2605.08621v1)

**采用版本与机制证据：** `arXiv:2605.08621v1`；https://arxiv.org/html/2605.08621v1 §4 EvidenT Framework — mechanism: While recent LLM-based repair methods show promise for project-level source fixes, they struggle with system-level repair, where failures span multi-language artifacts such as build recipes, scripts, and source archives, and require iterative validation through external build services.。

**评估证据：** https://arxiv.org/html/2605.08621v1 §5 Evaluation — disclosed scope: Frequent toolchain updates and growing ISA diversity have made system-level software package repair increasingly important. Diagnosing and repairing build failures remains challenging because failures involve heterogeneous evidence, dependency constraints, and architecture-specific build conventions. While recent LLM-based repair methods show promise for project-level source fixes, they struggle…。

**反证与边界：** https://arxiv.org/html/2605.08621v1 §5.6 Failure Analysis and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。本 family 的 exact-v1 增量为“迭代修复必须把 build artifact、历史尝试与环境反馈保存为 durable evidence state，并把 tool execution 与 diagnosis/reasoning 分离”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [PARD-2: Target-Aligned Parallel Draft Model for Dual-Mode Speculative Decoding](https://arxiv.org/abs/2605.08632v1)

**采用版本与机制证据：** `arXiv:2605.08632v1`；https://arxiv.org/html/2605.08632v1 §3 PARD-2; §3.2 Confidence-Adaptive Token Optimization — mechanism: Speculative decoding accelerates Large Language Models (LLMs) inference by using a lightweight draft model to propose candidate tokens that are verified in parallel by the target model.。

**评估证据：** https://arxiv.org/html/2605.08632v1 §4 Experiments — disclosed scope: Experiments across diverse models and tasks demonstrate that PARD-2 achieves up to 6.94$\times$ lossless acceleration, surpassing EAGLE-3 by 1.9$\times$ and PARD by 1.3$\times$ on Llama3.1-8B.。

**反证与边界：** https://arxiv.org/html/2605.08632v1 §5 Limitations and Conclusion — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-SPECULATIVE-DECODING` → [48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)；已读取 `books/part-05-inference-system/48-speculative-decoding.md` 及同 Part 前后相邻章节；当前主线已覆盖draft/target 身份、target verification、acceptance accounting 与回退边界。本 family 的 exact-v1 增量为“draft model 训练目标应对齐连续 acceptance length，并显式区分 target-dependent 与 target-independent mode”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [EdgeFlowerTune: Evaluating Federated LLM Fine-Tuning Under Realistic Edge System Constraints](https://arxiv.org/abs/2605.08636v1)

**采用版本与机制证据：** `arXiv:2605.08636v1`；https://arxiv.org/html/2605.08636v1 §2 EdgeFlowerTune Benchmark Design; §2.2 Benchmarking Protocols — mechanism: We present EdgeFlowerTune, a deployment-oriented benchmark for federated LLM fine-tuning under realistic edge-system constraints.。

**评估证据：** https://arxiv.org/html/2605.08636v1 §3 Experimental Settings; §4 Results — disclosed scope: Our benchmark results show that accuracy-only evaluation can lead to misleading conclusions: methods with similar final quality may differ substantially in deployability once realistic system constraints are considered.。

**反证与边界：** https://arxiv.org/html/2605.08636v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：edge federated fine-tuning 的结论必须同时通过 quality-under-budget、cost-to-target 与 perturbation robustness，不能用 simulation 或 final accuracy 代替真实设备 deployability。；正文已存在。

### [ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning](https://arxiv.org/abs/2605.08639v1)

**采用版本与机制证据：** `arXiv:2605.08639v1`；https://arxiv.org/html/2605.08639v1 §3 Design; §4 Routing-Replay-Guided Load Balancing — mechanism: We propose ReLibra, an MoE RL training system that exploits a unique opportunity in RL's rollout-training workflow, routing replay, to enable fine-grained load balancing at micro-batch granularity.。

**评估证据：** https://arxiv.org/html/2605.08639v1 §5 Evaluation — disclosed scope: Load imbalance is a long-standing challenge in Mixture-of-Experts (MoE) training and is exacerbated in reinforcement learning (RL) for LLMs, where hot experts can shift frequently across micro-batches. Existing MoE training systems rely on historical loads to predict future expert demand, making them less effective under sharp…。

**反证与边界：** https://arxiv.org/html/2605.08639v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：MoE RL 可把 rollout 已知 routing replay 提升为训练期 placement input，在 inter-batch 重排与 intra-batch replication 间分配控制权。；正文已存在。

### [PAAC: Privacy-Aware Agentic Device-Cloud Collaboration](https://arxiv.org/abs/2605.08646v1)

**采用版本与机制证据：** `arXiv:2605.08646v1`；https://arxiv.org/html/2605.08646v1 §3 PAAC — mechanism: In this work, we develop PAAC, a privacy-aware agentic framework that aligns planner--executor decomposition with the device-cloud boundary so that role specialization itself becomes the privacy mechanism.。

**评估证据：** https://arxiv.org/html/2605.08646v1 §4 Experiments — disclosed scope: Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability. Existing device-cloud designs treat this boundary as a compute split rather than a trust boundary suited to…。

**反证与边界：** https://arxiv.org/html/2605.08646v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；已读取 `books/part-06-ai-infrastructure/72-security.md` 及同 Part 前后相邻章节；当前主线已覆盖typed capability、trust boundary、policy enforcement 与 least-privilege action commit。本 family 的 exact-v1 增量为“device-cloud agent 的 compute split 本质是 trust boundary；typed placeholder identity 与 deterministic reversal 必须留在设备端”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators](https://arxiv.org/abs/2605.08647v1)

**采用版本与机制证据：** `arXiv:2605.08647v1`；https://arxiv.org/html/2605.08647v1 §3 Benchmark Design; §4 Process Metrics — mechanism: To make these vulnerabilities measurable before deployment, we introduce AgentCollabBench, a diagnostic benchmark of 900 human-validated tasks spanning software engineering, DevOps, and data engineering.。

**评估证据：** https://arxiv.org/html/2605.08647v1 §5 Experiments — disclosed scope: Evaluating four modern LLMs (GPT 4.1 mini, Gemini 2.5 Flash Lite, Qwen-3.5-35B-A3B, and Llama 3.1 8B Instruct), we expose model-specific vulnerability profiles invisible to outcome-only evaluation; Qwen-3.5-35B-A3B, for example, leads on tracer durability and instruction stability, while GPT 4.1 mini leads on leakage containment and false-belief…。

**反证与边界：** https://arxiv.org/html/2605.08647v1 Appendix K Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MULTI-AGENT` → [82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；已读取 `books/part-07-agent/82-multi-agent.md` 及同 Part 前后相邻章节；当前主线已覆盖role、permission、coordination topology、错误传播与 Byzantine containment。但正文尚未明确承载本 family 的增量边界：多 Agent 可靠性必须测量约束跨 hop 生存、错误传播与 converging-DAG synthesis bottleneck，而不只看最终答案。；正文已存在。

### [Sketch-and-Verify: Structured Inference-Time Scaling via Program Sketching](https://arxiv.org/abs/2605.08658v1)

**采用版本与机制证据：** `arXiv:2605.08658v1`；https://arxiv.org/html/2605.08658v1 §2 Sketch-and-Verify — mechanism: We characterize the K-vs-M trade-off via a Flash Lite scaling sweep, report HumanEval+ saturation on Flash and Pro, and show the method composes cleanly with execution-based selection from the concurrent Semantic Voting line of work.。

**评估证据：** https://arxiv.org/html/2605.08658v1 §3 Evaluation — disclosed scope: SKETCHVERIFY is a within-tier cost-performance policy, not a universal accuracy improvement. The operational question: a practitioner stuck with a small, cheap code model (here, Gemini 3.1 Flash Lite) for latency, deployment, or budget reasons -- how should they spend a small amount of extra test-time compute?…。

**反证与边界：** https://arxiv.org/html/2605.08658v1 §4 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-PLANNING` → [79-planning.md](../../../../books/part-07-agent/79-planning.md)；已读取 `books/part-07-agent/79-planning.md` 及同 Part 前后相邻章节；当前主线已覆盖proposal/search/verifier budget、执行反馈和 action commit 的分层。本 family 的 exact-v1 增量为“inference-time search 应分离 strategy sketch、candidate completion、execution verification 与 selection，并承认升级模型 tier 的替代边界”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [The Cancellation Hypothesis in Critic-Free RL: From Outcome Rewards to Token Credits](https://arxiv.org/abs/2605.08666v1)

**采用版本与机制证据：** `arXiv:2605.08666v1`；https://arxiv.org/html/2605.08666v1 §3 Token-Level Analysis; §4 Cancellation Hypothesis — mechanism: To explain this phenomenon, we further show that a token's change in probability is not fully determined by its own advantage; coupled gradient interactions with other tokens also play a non-negligible role.。

**评估证据：** https://arxiv.org/html/2605.08666v1 §5 Experiments — disclosed scope: Building upon this analysis, we propose the cancellation hypothesis: as a result of coupling, opposing signals cancel out for tokens shared by positive and negative rollouts, while tokens more specific to successful rollouts receive stronger reinforcement, thereby inducing hidden token-level credit assignment from rollout-level rewards.。

**反证与边界：** https://arxiv.org/html/2605.08666v1 Appendix A Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-GRPO` → [33-grpo.md](../../../../books/part-04-training-system/33-grpo.md)；已读取 `books/part-04-training-system/33-grpo.md` 及同 Part 前后相邻章节；当前主线已覆盖sequence reward、token credit、group/batch composition 与 verifier 约束。本 family 的 exact-v1 增量为“sequence-level outcome reward 通过共享低置信 token 的梯度耦合产生隐式 token credit；batch composition 因而成为训练语义的一部分”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [RewardHarness: Self-Evolving Agentic Post-Training](https://arxiv.org/abs/2605.08703v1)

**采用版本与机制证据：** `arXiv:2605.08703v1`；https://arxiv.org/html/2605.08703v1 — §2 Method；§2.2 Skills and Tools Library；§2.3 Orchestrator；§2.5 Self-Evolution Loop。

**评估证据：** https://arxiv.org/html/2605.08703v1 — §3 Experiments；§3.1–§3.3；Appendix B evolution trajectory/cases。

**反证与边界：** https://arxiv.org/html/2605.08703v1 — §5 Limitation：专有 Claude orchestrator、仅 image editing、small validation overfit 风险；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-RLHF` → [31-rlhf.md](../../../../books/part-04-training-system/31-rlhf.md)；现有 Ch31 主要把 reward 视为 scorer/model 输出；论文把 reward competence 外化为可演化的 skill/tool library，由 orchestrator 评估、归因、提出 library revision，再经验证 gate 提交，形成与权重更新不同的 post-training 分支。；已在正文并有 canonical marker。

### [The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs](https://arxiv.org/abs/2605.08737v1)

**采用版本与机制证据：** `arXiv:2605.08737v1`；https://arxiv.org/html/2605.08737v1 §3 Base-Relative Clip-Safety Threshold; §4 K-ary Extension — mechanism: In a single-position Bernoulli reduction, we derive a closed-form base-relative clip-safety threshold lambda*(p,b,c) determined by three measurable quantities: the teacher modal probability, the warm-start mass, and the importance-sampling clip strength.。

**评估证据：** https://arxiv.org/html/2605.08737v1 §5 Experiments — disclosed scope: On-policy distillation (OPD) is widely used for LLM post-training. When pushed with a reward-extrapolation coefficient lambda &gt; 1, the student can lift past the teacher in domain, but past a threshold lambda* the same step violates the output contract on structured-output tasks. In a single-position Bernoulli…。

**反证与边界：** https://arxiv.org/html/2605.08737v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DPO` → [34-dpo.md](../../../../books/part-04-training-system/34-dpo.md)；已读取 `books/part-04-training-system/34-dpo.md` 及同 Part 前后相邻章节；当前主线已覆盖preference pair、reference policy、objective boundary 与 distribution shift。本 family 的 exact-v1 增量为“near-deterministic structured output 的 on-policy distillation 存在可测 extrapolation cliff，格式合同应成为训练控制约束”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows](https://arxiv.org/abs/2605.08761v1)

**采用版本与机制证据：** `arXiv:2605.08761v1`；https://arxiv.org/html/2605.08761v1 §3 EntCollabBench; Role-specialized workflow design — mechanism: We introduce \textsc{EntCollabBench}, a benchmark for evaluating enterprise multi-agent collaboration.。

**评估证据：** https://arxiv.org/html/2605.08761v1 §4 Experiments; Appendix G Failure Analysis — disclosed scope: \textsc{EntCollabBench} simulates a permission-isolated organization with 11 role-specialized agents across six departments and contains two evaluation subsets: a Workflow subset, where agents collaboratively modify enterprise system states, and an Approval subset, where agents make policy-grounded decisions.。

**反证与边界：** https://arxiv.org/html/2605.08761v1 Appendix H Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MULTI-AGENT` → [82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；已读取 `books/part-07-agent/82-multi-agent.md` 及同 Part 前后相邻章节；当前主线已覆盖role、permission、coordination topology、错误传播与 Byzantine containment。本 family 的 exact-v1 增量为“企业多 Agent 评测需要把 role permission、stateful service transition、approval commitment 与 coordination cost 放进同一 executable workflow contract”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems](https://arxiv.org/abs/2605.08769v1)

**采用版本与机制证据：** `arXiv:2605.08769v1`；https://arxiv.org/html/2605.08769v1 §2 Formulation; §3 EvoMAS — mechanism: We propose EvoMAS, a framework for execution-time multi-agent workflow construction.。

**评估证据：** https://arxiv.org/html/2605.08769v1 §4 Experiments — disclosed scope: Large language model (LLM)-based multi-agent systems have shown strong potential on complex tasks through agent specialization, tool use, and collaborative reasoning. However, most automated multi-agent system design methods still follow a one-shot paradigm: a workflow is optimized or selected before execution and then reused unchanged throughout…。

**反证与边界：** https://arxiv.org/html/2605.08769v1 Appendix G Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。本 family 的 exact-v1 增量为“固定工作流在 task state 变化时会错配；execution-time workflow policy 可选择 agent/edge，但必须版本化 agent pool、depth、reward 与 evaluator”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [AgentSlimming: Towards Efficient and Cost-Aware Multi-Agent Systems](https://arxiv.org/abs/2605.08813v1)

**采用版本与机制证据：** `arXiv:2605.08813v1`；https://arxiv.org/html/2605.08813v1 — §3 Methodology；§3.2 pipeline 与 iterative remove/replace/rollback。

**评估证据：** https://arxiv.org/html/2605.08813v1 — §4 Experiments；§4.2–§4.4；Appendix E break-even、F sensitivity、G generalization。

**反证与边界：** https://arxiv.org/html/2605.08813v1 — §5 Limitations：搜索成本、有限 workflow/task/model，且优化器依赖 probe 与 baseline gate；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MULTI-AGENT` → [82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；论文的 remove/replace 操作与 baseline-anchored rollback把 workflow topology 当作候选状态；Ch82 已要求在同预算下比较 single/multi-agent、对 topology revision 进行独立验收，并在收益不足时回退较小图，因此 AgentSlimming 是既有 topology/cost frontier 的实现实例。；无需改稿。

### [SynerDiff: Synergetic Continuous Batching for Fast and Parallel Diffusion Model Inference](https://arxiv.org/abs/2605.08835v1)

**采用版本与机制证据：** `arXiv:2605.08835v1`；https://arxiv.org/html/2605.08835v1 §III SynerDiff Design — mechanism: To address these, we propose SynerDiff, an efficient continuous batching system built on intra-inter level synergy.。

**评估证据：** https://arxiv.org/html/2605.08835v1 §IV-B Evaluation — disclosed scope: The expansion of Artificial Intelligence-generated content service requires diffusion model serving to simultaneously achieve high throughput and low task end-to-end (E2E) latency. However, existing continuous batching methods suffer from severe resource contention during UNet-VAE concurrency, leading to latency spikes. Furthermore, concurrent multi-task scheduling entails a trade-off…。

**反证与边界：** https://arxiv.org/html/2605.08835v1 §V Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-CONTINUOUS-BATCHING` → [46-continuous-batching.md](../../../../books/part-05-inference-system/46-continuous-batching.md)；已读取 `books/part-05-inference-system/46-continuous-batching.md` 及同 Part 前后相邻章节；当前主线已覆盖admission、batch membership、queue feedback、stage contention 与 SLO。但正文尚未明确承载本 family 的增量边界：diffusion serving 的 continuous batching 要联合控制 UNet throughput、VAE latency、component contention 与 queue feedback。；正文已存在。

### [Generating Leakage-Free Benchmarks for Robust RAG Evaluation](https://arxiv.org/abs/2605.08838v1)

**采用版本与机制证据：** `arXiv:2605.08838v1`；https://arxiv.org/html/2605.08838v1 §3 Leakage-Free Benchmark Generation — mechanism: We introduce SeedRG, a semi-synthetic benchmark generation pipeline that mitigates knowledge leakage and addresses the issue of benchmark aging.。

**评估证据：** https://arxiv.org/html/2605.08838v1 §4 Experiments and Robustness Evaluation — disclosed scope: This leads to unreliable evaluation.。

**反证与边界：** https://arxiv.org/html/2605.08838v1 §5 Discussion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-RAG` → [76-rag.md](../../../../books/part-07-agent/76-rag.md)；已读取 `books/part-07-agent/76-rag.md` 及同 Part 前后相邻章节；当前主线已覆盖corpus snapshot、retrieval provenance、answer/evidence binding 与 freshness。但正文尚未明确承载本 family 的增量边界：RAG benchmark 生成必须以受控 corpus transformation 构造可验证 answer/evidence pair，并隔离训练污染与 retrieval leakage；高分只有在冻结 corpus 与 verifier 时可解释。；正文已存在。

### [ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing](https://arxiv.org/abs/2605.08840v1)

**采用版本与机制证据：** `arXiv:2605.08840v1`；https://arxiv.org/html/2605.08840v1 §3 ReST-KV — mechanism: In this paper, we propose ReST-KV, a robust KV eviction method that combines layer-wise output Reconstruction and Spatial-Temporal smoothing to provide a more comprehensive perspective for the KV cache eviction task.。

**评估证据：** https://arxiv.org/html/2605.08840v1 §4 Experiments — disclosed scope: Large language models (LLMs) face growing challenges in efficient generative inference due to the increasing memory demands of Key-Value (KV) caches, especially for long sequences. Existing eviction methods typically retain KV pairs with high attention weights but overlook the impact of attention redistribution caused by token…。

**反证与边界：** https://arxiv.org/html/2605.08840v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-KV-CACHE` → [45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及同 Part 前后相邻章节；当前主线已覆盖KV identity、生命周期、容量、eviction quality 与 correctness fallback。本 family 的 exact-v1 增量为“KV eviction 的 commit quality 可由 layer-wise output reconstruction 与 spatial-temporal smoothing共同约束，而不能只按局部 attention proxy”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [BubbleSpec: Turning Long-Tail Bubbles into Speculative Rollout Drafts for Synchronous Reinforcement Learning](https://arxiv.org/abs/2605.08862v1)

**采用版本与机制证据：** `arXiv:2605.08862v1`；https://arxiv.org/html/2605.08862v1 §3 BubbleSpec — mechanism: Instead, we propose BubbleSpec, a novel framework that accelerates RL rollouts while strictly keeping the mathematical exactness.。

**评估证据：** https://arxiv.org/html/2605.08862v1 Appendix A Evaluation — disclosed scope: Extensive evaluations demonstrate that BubbleSpec reduces decoding steps by 50% and increases rollout throughput by up to 1.8x.。

**反证与边界：** https://arxiv.org/html/2605.08862v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：同步 RL 的 long-tail bubble 可作为 speculative rollout draft capacity，但必须保留 policy-version verification 与失败回退。；正文已存在。

### [Rennala MVR: Improved Time Complexity for Parallel Stochastic Optimization via Momentum-Based Variance Reduction](https://arxiv.org/abs/2605.08871v1)

**采用版本与机制证据：** `arXiv:2605.08871v1`；https://arxiv.org/html/2605.08871v1 §3 Rennala MVR — mechanism: We show that, under a mean-squared smoothness assumption, variance reduction can improve time complexity in relevant parameter regimes.。

**评估证据：** https://arxiv.org/html/2605.08871v1 §4 Experiments — disclosed scope: Large-scale machine learning models are trained on clusters of machines that exhibit heterogeneous performance due to hardware variability, network delays, and system-level instabilities. In such environments, time complexity rather than iteration complexity becomes the relevant performance metric for optimization algorithms. Recent work by Tyurin and Richtárik…。

**反证与边界：** https://arxiv.org/html/2605.08871v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-PRETRAINING` → [28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)；已读取 `books/part-04-training-system/28-pretraining.md` 及同 Part 前后相邻章节；当前主线已覆盖data/objective/optimizer coupling、收敛证据与 scale 外推边界。本 family 的 exact-v1 增量为“parallel stochastic optimization 可用 momentum variance reduction 改变同步轮次复杂度，但证据仍限 stochastic quadratic 与 inexact-neural variant”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [Why Do Aligned LLMs Remain Jailbreakable: Refusal-Escape Directions, Operator-Level Sources, and Safety-Utility Trade-off](https://arxiv.org/abs/2605.08878v1)

**采用版本与机制证据：** `arXiv:2605.08878v1`；https://arxiv.org/html/2605.08878v1 — §2 continuous transformation；§3 RED/operator decomposition；§4 elimination 与 safety-utility trade-off。

**评估证据：** https://arxiv.org/html/2605.08878v1 — §5 Experiments；§5.2–§5.3；Appendix E attack/model-specific results。

**反证与边界：** https://arxiv.org/html/2605.08878v1 — Appendix B Limitations and future work：白盒分解、模型/攻击集合与参考子空间约束；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 已区分 refusal behavior 与知识删除，但尚未解释 jailbreak trajectory 如何沿 harmful-semantics-sensitive subspace 形成 refusal-escape direction，以及 residual/attention/MLP/normalization operator 对该方向的可分解贡献与消除它的 utility 代价。；已在正文并有 canonical marker。

### [Quantitative Comparison of Credible Compilation and Verification In Coding Agent Compiler Development](https://arxiv.org/abs/2605.08927v1)

**采用版本与机制证据：** `arXiv:2605.08927v1`；https://arxiv.org/html/2605.08927v1 §3 Credible Compilation and Verification Workflows — mechanism: We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification.。

**评估证据：** https://arxiv.org/html/2605.08927v1 §5–§6 Quantitative Comparison — disclosed scope: Formal program verification is a longstanding goal in the field. We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification. Working with the first verified compiler developed by a coding agent (operating under human supervision), we present…。

**反证与边界：** https://arxiv.org/html/2605.08927v1 §8 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。但正文尚未明确承载本 family 的增量边界：coding Agent 生成 compiler optimization 时，proof-producing translation validation 与 credible compilation 是不同 verification contracts；supervision 工时与 compile-time overhead 必须分开比较。；正文已存在。

### [When and Why Grouping Attention Heads Accelerates Muon Optimization](https://arxiv.org/abs/2605.08933v1)

**采用版本与机制证据：** `arXiv:2605.08933v1`；https://arxiv.org/html/2605.08933v1 — §3 gain versus norm cost；§4 Group Muon Algorithm。

**评估证据：** https://arxiv.org/html/2605.08933v1 — Appendix C GPT-2 Small/FineWeb setup；Appendix D observations；Appendix E aligned low-rank counterexample。

**反证与边界：** https://arxiv.org/html/2605.08933v1 — §3 与 Appendix E 给出 over-splitting failure；实验只覆盖小模型与披露 grouping rules；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-PRETRAINING` → [28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)；Ch28 已解释 Muon whitening，却没有把 full matrix 与 attention-head grouping 的 gain/norm-cost 条件写清：近满秩梯度可通过 grouping 获得更快更新，而对齐低秩梯度会因过度分组付出额外范数成本。；已在正文并有 canonical marker。

### [MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production](https://arxiv.org/abs/2605.08962v1)

**采用版本与机制证据：** `arXiv:2605.08962v1`；https://arxiv.org/html/2605.08962v1 §3 System Overview; §4 Model Parallelization; §5 Workload Balancing — mechanism: As the foundational component of versatile AI applications, training an multimodal large language model (MLLM) relies on multimodal datasets with dynamic modality mixture proportions and sample length distributions. However, existing MLLM systems remain inefficient under dynamic workloads, due to statically coupled decisions of resource allocation and…。

**评估证据：** https://arxiv.org/html/2605.08962v1 §7 Evaluation — disclosed scope: Our experimental results demonstrate $1.27\times$-$7.57\times$ throughput improvement under production-grade dynamic workloads, as compared to four state-of-the-art systems.。

**反证与边界：** https://arxiv.org/html/2605.08962v1 §8 Discussion; undisclosed production-cluster specifications — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：多模态训练要把 encoder/LLM 异构并行、sample reshaping 与动态 modality workload 视为共同 runtime control problem。；正文已存在。

### [Using Semantic Distance to Estimate Uncertainty in LLM-Based Code Generation](https://arxiv.org/abs/2605.09023v1)

**采用版本与机制证据：** `arXiv:2605.09023v1`；https://arxiv.org/html/2605.09023v1 §3 Semantic-Distance Uncertainty — mechanism: LLMs show strong performance in code generation, but their outputs lack correctness guarantees.。

**评估证据：** https://arxiv.org/html/2605.09023v1 §4 Experiments — disclosed scope: Across LiveCodeBench, MBPP, HumanEval-X and BigCodeBench, spanning Python, Java and C++, our metrics provide strong proxies for correctness, and consistently outperform state-of-the-art sample-based baselines across both closed-source models (GPT-3.5-Turbo, GPT-4o-mini, Gemini-2.5-Flash-Lite, Claude Opus 4.5) and an open-source model (DeepSeek-Coder-V2).。

**反证与边界：** https://arxiv.org/html/2605.09023v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“code-generation uncertainty 可以用可执行 outputs 的 semantic distance 作为 sensor，但不能被提升为通用 truth confidence”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [Octopus Protocol: One-Shot Hardware Discovery and Control for AI Agents via Infrastructure-as-Prompts](https://arxiv.org/abs/2605.09055v1)

**采用版本与机制证据：** `arXiv:2605.09055v1`；https://arxiv.org/html/2605.09055v1 §2 Octopus Protocol — mechanism: We present Octopus Protocol, a system that collapses that cost to a single shell command.。

**评估证据：** https://arxiv.org/html/2605.09055v1 §3 Demonstration — disclosed scope: Recent agentic-robotics systems, from Code-asPolicies to modern vision-language-action (VLA) foundation models, presuppose that drivers, SDKs, or ROS-style primitives for the target hardware already exist. Writing those primitives is the dominant engineering cost of bringing up new hardware for agent control. We present Octopus Protocol, a system…。

**反证与边界：** https://arxiv.org/html/2605.09055v1 §4 Conclusion; no dedicated evaluation or limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-TOOL-CALLING` → [78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)；已读取 `books/part-07-agent/78-tool-calling.md` 及同 Part 前后相邻章节；当前主线已覆盖tool proposal、typed capability、least privilege 与 high-risk commit authority。本 family 的 exact-v1 增量为“hardware discovery 可编码为一次性 capability prompt，但没有独立 evaluation 或长期 protocol evidence 支持其成为新 owner”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [Single-Configuration Attack Success Rate Is Not Enough: Jailbreak Evaluations Should Report Distributional Attack Success](https://arxiv.org/abs/2605.09070v1)

**采用版本与机制证据：** `arXiv:2605.09070v1`；https://arxiv.org/html/2605.09070v1 §3 Distributional ASR — mechanism: We propose two new measures for jailbreak attacks: the Variant Sensitivity Measure (VSM) and Union Coverage (UC).。

**评估证据：** https://arxiv.org/html/2605.09070v1 §5 Experiments — disclosed scope: We empirically demonstrate the importance of these measures using two attack families across three open-source target models.。

**反证与边界：** https://arxiv.org/html/2605.09070v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“jailbreak evaluation 应报告攻击配置分布而非单点 ASR，并冻结 judge、variant grid 与 generation count”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [A Communication-Theoretic Framework for LLM Agents: Cost-Aware Adaptive Reliability](https://arxiv.org/abs/2605.09121v1)

**采用版本与机制证据：** `arXiv:2605.09121v1`；https://arxiv.org/html/2605.09121v1 — §3 agent channel model；§4 AgentCodec；§5.4 adaptive router。

**评估证据：** https://arxiv.org/html/2605.09121v1 — §5 evaluation；Appendix D methodology、H validation、L synthesis integrity。

**反证与边界：** https://arxiv.org/html/2605.09121v1 — §6 Limitations；Appendix I/J/O.11：analogy、judge/synthesis、correlated branches 与 operating-point dependence；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MULTI-AGENT` → [82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；论文把 retry、diverse sampling、critic refinement 与 adaptive routing统一为 cost/quality operating point；Ch82 已把相关错误、独立性、judge reliability、retry budget 与 topology selection绑定到同一验收曲线，且明确 router 只拥有 proposal、verifier 保留 commit，因此通信类比未改变责任边界。；无需改稿。

### [Cosine-Gated Adam-Decay: Drop-In Staleness-Aware Outer Optimization for Decoupled DiLoCo](https://arxiv.org/abs/2605.09126v1)

**采用版本与机制证据：** `arXiv:2605.09126v1`；https://arxiv.org/html/2605.09126v1 §3 Method — mechanism: We propose Cosine Gated Adam Decay (CGAD), a simple, drop-in, age-aware outer optimizer that scales each incoming pseudo-gradient by $σ(τ) = γ(τ) e^{-ατ}$ before it enters Adam's first- and second-moment buffers; the exponential models information decay and the cosine gate $γ(τ)$ smoothly zeroes contributions past a…。

**评估证据：** https://arxiv.org/html/2605.09126v1 §5 Experiments — disclosed scope: Asynchronous DiLoCo systems may receive pseudo-gradients computed several outer rounds earlier, yet the standard Nesterov outer optimizer does not explicitly condition its update on per-update age. This can make the outer momentum buffer brittle under large controlled delays. We propose Cosine Gated Adam Decay (CGAD), a…。

**反证与边界：** https://arxiv.org/html/2605.09126v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：decoupled DiLoCo outer optimizer 应根据 update cosine/staleness gate 衰减，而不是把所有迟到 update 等价接收。；正文已存在。

### [CIVeX: Causal Intervention Verification for Language Agents](https://arxiv.org/abs/2605.09168v1)

**采用版本与机制证据：** `arXiv:2605.09168v1`；https://arxiv.org/html/2605.09168v1 §3 CIVeX; §5 Evaluation Protocol — mechanism: We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN.。

**评估证据：** https://arxiv.org/html/2605.09168v1 §6 Experiments — disclosed scope: We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN.。

**反证与边界：** https://arxiv.org/html/2605.09168v1 §7 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-TOOL-CALLING` → [78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)；已读取 `books/part-07-agent/78-tool-calling.md` 及同 Part 前后相邻章节；当前主线已覆盖tool proposal、typed capability、least privilege 与 high-risk commit authority。但正文尚未明确承载本 family 的增量边界：高风险 action commit 应咨询显式 causal graph，并用 intervention consistency 区分相关性证据与可执行因果依据。；正文已存在。

### [LBI: Parallel Scan Backpropagation via Latent Bounded Interfaces](https://arxiv.org/abs/2605.09204v1)

**采用版本与机制证据：** `arXiv:2605.09204v1`；https://arxiv.org/html/2605.09204v1 §2 Scan Formulation; §3 Model Realization — mechanism: We introduce Latent Bounded Interfaces (LBI), an algorithmic formulation that makes scan-based backpropagation tractable by restricting inter-region communication to a low-dimensional latent interface, $ m_k \in \mathbb{R}^{r}$, where $r \ll d$.。

**评估证据：** https://arxiv.org/html/2605.09204v1 §4 Experiments — disclosed scope: We demonstrate that LBI maintains model quality across four architectures (Mamba-2, Mamba-3, Transformer, and a Mamba--Transformer hybrid) at 47--61M block parameters.。

**反证与边界：** https://arxiv.org/html/2605.09204v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：depth-parallel backprop 可通过模型原生 bounded interface 把跨 region adjoint transport 压缩为 exact suffix scan，但会牺牲表示自由度。；正文已存在。

### [Flame3D: Zero-shot Compositional Reasoning of 3D Scenes with Agentic Language Models](https://arxiv.org/abs/2605.09218v1)

**采用版本与机制证据：** `arXiv:2605.09218v1`；https://arxiv.org/html/2605.09218v1 §3 Flame3D Editable Scene Memory and Spatial Tools — mechanism: We propose Flame3D, a training-free framework that represents scenes as editable visual-textual 3D memories and exposes them to an off-the-shelf MLLM through composable spatial tools.。

**评估证据：** https://arxiv.org/html/2605.09218v1 §4 Experiments; Compose3D — disclosed scope: 3D scene understanding spans reasoning about free space, object grounding, hypothetical object insertions, complex geometric relationships, and integrating all of these with external tools and data sources. Existing 3D understanding methods typically rely on large-scale 3D-language training or focus on object grounding and simple spatial relationships.…。

**反证与边界：** https://arxiv.org/html/2605.09218v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-WORLD-MODELS` → [25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及同 Part 前后相邻章节；当前主线已覆盖action-conditioned transition、persistent/revisable world state 与 planning handoff。但正文尚未明确承载本 family 的增量边界：可编辑 3D scene memory 应把 geometry、free space、hypothetical insertion 与外部修正保存为 typed world state，并让 Agent 只通过 composable spatial tools 读写。；正文已存在。

### [The Art of the Jailbreak: Formulating Jailbreak Attacks for LLM Security Beyond Binary Scoring](https://arxiv.org/abs/2605.09225v1)

**采用版本与机制证据：** `arXiv:2605.09225v1`；https://arxiv.org/html/2605.09225v1 §3.3 Robust Evaluation Metric; §4 Method — mechanism: Jailbreak attacks -- adversarial prompts that bypass LLM alignment through purely linguistic manipulation -- pose a growing operational security threat, yet the field lacks large-scale, reproducible infrastructure for generating, categorizing, and evaluating them systematically. This paper addresses that gap with three contributions. (1) Large-scale compositional jailbreak…。

**评估证据：** https://arxiv.org/html/2605.09225v1 §5 Evaluation — disclosed scope: Experiments across 114,000 prompts confirm that OPTIMUS separates Weak, Moderate, and Optimal jailbreaks with category-level evidence binary evaluation cannot supply.。

**反证与边界：** https://arxiv.org/html/2605.09225v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“jailbreak 评测需要连续质量函数同时刻画 harmfulness 与语义保真，binary ASR 只保留为受限指标”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [Two Ways to De-Bias an LLM-as-a-Judge: A Continuous-Score Comparison of Hierarchical Bayesian Calibration and Neural-ODE Score Transport](https://arxiv.org/abs/2605.09227v1)

**采用版本与机制证据：** `arXiv:2605.09227v1`；https://arxiv.org/html/2605.09227v1 §IV Hierarchical Bayesian Calibration; §V Neural-ODE Score Transport — mechanism: [Abridged] Using a Large Language Model (LLM) as an automatic rater (LLM-as-a-judge) is cheap but potentially biased: some judges run lenient, others strict, the middle of the scale gets compressed, and verbose answers may be over-rewarded. A common remedy is post-hoc calibration: leave the cheap judge…。

**评估证据：** https://arxiv.org/html/2605.09227v1 §VI Experiments — disclosed scope: The headline result is that the choice between methods is primarily a data-budget question.。

**反证与边界：** https://arxiv.org/html/2605.09227v1 §VIII-C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“LLM-judge calibration 应按 paired-anchor budget 与非线性程度选择 hierarchical linear 或 score-transport corrector”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。；无需改稿。

### [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models](https://arxiv.org/abs/2605.09241v1)

**采用版本与机制证据：** `arXiv:2605.09241v1`；https://arxiv.org/html/2605.09241v1 §3 Method — mechanism: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be…。

**评估证据：** https://arxiv.org/html/2605.09241v1 §4 Experiments — disclosed scope: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be…。

**反证与边界：** https://arxiv.org/html/2605.09241v1 §5 Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-WORLD-MODELS` → [25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及同 Part 前后相邻章节；当前主线已覆盖action-conditioned transition、persistent/revisable world state 与 planning handoff。但正文尚未明确承载本 family 的增量边界：JEPA anti-collapse regularization 应在多个低维 subspace 中约束分布，而非强迫 full ambient representation 服从 isotropic prior。；正文已存在。

### [DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification](https://arxiv.org/abs/2605.09269v1)

**采用版本与机制证据：** `arXiv:2605.09269v1`；https://arxiv.org/html/2605.09269v1 — §3 plan-and-execute DeltaRubric；Disagreement Planner 与 Checklist Verifier 的联合 RL。

**评估证据：** https://arxiv.org/html/2605.09269v1 — §4 experiments；Qwen3-VL 4B/8B、VL-RewardBench 与 MM RewardBench。

**反证与边界：** https://arxiv.org/html/2605.09269v1 — §4.3 ablation 与 Appendix；只支持所测 MLLM、reward benchmark 和 rubric generator，不能证明自生成 checklist 等于独立真值；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已要求 multimodal judge 把 rubric、claim、visual artifact 与 verifier identity分开，并禁止自生成评分规则直接成为真值；DeltaRubric 的 planner/verifier 联合训练提高作者 benchmark 分数，但 checklist 仍由同一模型生成与执行，没有改变独立 evidence/release authority。；无需改稿。

### [EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium](https://arxiv.org/abs/2605.09278v1)

**采用版本与机制证据：** `arXiv:2605.09278v1`；https://arxiv.org/html/2605.09278v1 — §3 EquiMem；shared-memory reliability calibration 与 game-theoretic equilibrium。

**评估证据：** https://arxiv.org/html/2605.09278v1 — §4 experiments；6-agent debate、Qwen3-VL-8B、MiniLM 与共享记忆。

**反证与边界：** https://arxiv.org/html/2605.09278v1 — §6 limitations；早期记忆稀疏、相关 hallucination、graph semantics 含糊，收益受 memory quality/diversity 限定；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MEMORY` → [77-memory.md](../../../../books/part-07-agent/77-memory.md)；Ch77 已把 shared-memory entry 视为带 provenance/dependency 的 tainted derived state，写入前需独立 verification，且相关 agent 不能靠多数票洗净同源错误；EquiMem 用 query/traversal equilibrium 估计 trust，是该零信任写入 gate 的一种 sensor。；无需改稿。

### [TileQ: Efficient Low-Rank Quantization of Mixture-of-Experts with 2D Tiling](https://arxiv.org/abs/2605.09281v1)

**采用版本与机制证据：** `arXiv:2605.09281v1`；https://arxiv.org/html/2605.09281v1 — §3 Method；§3.1 2D tiling；§3.2 fused sparse low-rank inference；§3.3 analysis。

**评估证据：** https://arxiv.org/html/2605.09281v1 — §4 Evaluation；Appendix B–D（rank/tile、other GPU/MoE methods）。

**反证与边界：** https://arxiv.org/html/2605.09281v1 — Appendix E Limitations and Future Work：模型、GPU、tile/rank choice 与 fusion path 限制；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；Ch49 有低秩量化与 MoE execution，但未承载 TileQ 的二维 expert/rank tiling、activation-aware subspace sharing，以及把 global input projection、routing-weighted accumulation 和 reconstruction 融成 single-pass sparse kernel 的机制。；已在正文并有 canonical marker。

### [BetaEdit: Null-Space Constrained Sequential Model Editing](https://arxiv.org/abs/2605.09285v1)

**采用版本与机制证据：** `arXiv:2605.09285v1`；https://arxiv.org/html/2605.09285v1 — §3 BetaEdit；null-space constrained sequential model editing。

**评估证据：** https://arxiv.org/html/2605.09285v1 — §4 experiments；顺序编辑、知识保持与 subject-token setting。

**反证与边界：** https://arxiv.org/html/2605.09285v1 — Limitations；依赖 subject-token anchoring，共享 subject 与复杂 prompt 会破坏假设；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已明确连续 model editing 的非交换性：每次新 revision 都要随 edit order 重验旧 forget/retain claim 与 probe distribution。BetaEdit 的 approximate-null-space leakage 和 history-aware update 是该顺序回归合同的机制实例，不足以让编辑方法自行拥有 release authority。；无需改稿。

### [Path-Dependent Denoising: A Non-Conservative Field Perspective on Order Collapse in Diffusion Language Models](https://arxiv.org/abs/2605.09303v1)

**采用版本与机制证据：** `arXiv:2605.09303v1`；https://arxiv.org/html/2605.09303v1 — §3 path-dependent denoising 的 non-conservative field 分解。

**评估证据：** https://arxiv.org/html/2605.09303v1 — §4 diagnostics 与 order-collapse analysis。

**反证与边界：** https://arxiv.org/html/2605.09303v1 — Limitations；主要是形式诊断与假设，缺少广泛实证，场估计昂贵且分解不唯一；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24 已把 denoising order、parallel proposal 与 correction/commit schedule 视为生成机制的一部分，而不是可任意交换的实现细节；local circulation 将已有 path-dependence 边界形式化，但没有改变兼容性失败时回退受控顺序或 AR 的分支。；无需改稿。

### [Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation](https://arxiv.org/abs/2605.09315v1)

**采用版本与机制证据：** `arXiv:2605.09315v1`；https://arxiv.org/html/2605.09315v1 — §3 capability preservation/evolution procedure。

**评估证据：** https://arxiv.org/html/2605.09315v1 — §4 controlled lifelong-agent adaptation experiments。

**反证与边界：** https://arxiv.org/html/2605.09315v1 — Limitations；CPE 实例轻量且领域化，顺序 shift 受控，不代表 open-world self-evolution；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-PLATFORM` → [84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)；Ch84 现有正文已把 lifelong self-evolution 的新能力增量与旧能力 regression 分开，并以 capability matrix、held-out gate 和 rollback 约束 adaptation；该 exact-v1 语义已经存在，本轮只缺 canonical Source Family binding。；已在正文并有 canonical marker。

### [Mem-W: Latent Memory-Native GUI Agents](https://arxiv.org/abs/2605.09317v1)

**采用版本与机制证据：** `arXiv:2605.09317v1`；https://arxiv.org/html/2605.09317v1 — §3 latent memory-native GUI agent architecture。

**评估证据：** https://arxiv.org/html/2605.09317v1 — §4 web/mobile evaluation。

**反证与边界：** https://arxiv.org/html/2605.09317v1 — 正文未设独立 Limitations；结果限于披露的 GUI benchmark、视觉 backbone 与交互长度；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MEMORY` → [77-memory.md](../../../../books/part-07-agent/77-memory.md)；Ch77 已区分 human-readable evidence store 与 policy-facing latent memory，并要求压缩只保存 decision-sufficient state、原 evidence/provenance 仍可追溯；Mem-W 的 trajectory-to-latent compressor是该分层的一种实现，不能让 latent token 取得事实 authority。；无需改稿。

### [The Trap of Trajectory: Towards Understanding and Mitigating Spurious Correlations in Agentic Memory](https://arxiv.org/abs/2605.09330v1)

**采用版本与机制证据：** `arXiv:2605.09330v1`；https://arxiv.org/html/2605.09330v1 — §3 trajectory-grounded memory correlation diagnosis and mitigation。

**评估证据：** https://arxiv.org/html/2605.09330v1 — §4 experiments、ablation 与 failure analysis。

**反证与边界：** https://arxiv.org/html/2605.09330v1 — 结果只支持所测 agent-memory tasks；不能证明相关性识别器在开放环境或分布漂移下可靠；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-MEMORY` → [77-memory.md](../../../../books/part-07-agent/77-memory.md)；Ch77 已要求把 trajectory memory 的 source、selection path 与 downstream decision dependency写入 lineage，并在 correlated evidence 下阻止重复投票；CAMEL 的 write/read calibration降低作者 benchmark 的 spurious reliance，但没有改变 provenance-first memory contract。；无需改稿。

### [Skill-R1: Agent Skill Evolution via Reinforcement Learning](https://arxiv.org/abs/2605.09359v1)

**采用版本与机制证据：** `arXiv:2605.09359v1`；https://arxiv.org/html/2605.09359v1 — §3 recurrent skill evolution、bi-level advantage 与 GRPO editor。

**评估证据：** https://arxiv.org/html/2605.09359v1 — §4 experiments；frozen GPT-4o-mini task model 与 Qwen editor。

**反证与边界：** https://arxiv.org/html/2605.09359v1 — 无独立 Limitations；收益绑定所测 reasoning/tool benchmarks、editor 与多代 rollout budget；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-PLATFORM` → [84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)；Agent Platform 已把 trajectory-derived skill 作为带适用域、held-out gate、版本与 retirement 的受治理 artifact；该 recurrent editor 未改变 commit authority。；无需改稿。

### [31.1 A 14.08-to-135.69Token/s ReRAM-on-Logic Stacked Outlier-Free Large-Language-Model Accelerator with Block-Clustered Weight-Compression and Adaptive Parallel-Speculative-Decoding](https://arxiv.org/abs/2605.09375v1)

**采用版本与机制证据：** `arXiv:2605.09375v1`；https://arxiv.org/pdf/2605.09375v1 — 3-page ISSCC digest pp.532–533；local rotation、ReRAM-stacked PNM/BVQ、adaptive parallel SD 与四队列 out-of-order scheduler。

**评估证据：** https://arxiv.org/pdf/2605.09375v1 — 测量结果绑定 55nm chip、4 stacked ReRAM dies、63.5–285MHz、所测 LLM/precision 与 draft policy。

**反证与边界：** https://arxiv.org/pdf/2605.09375v1 — 短篇 digest 未给通用 limitations；14.08–135.69 token/s 与 4.46–7.17x 仅属于披露芯片、模型和基线，不能外推通用 accelerator；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；Ch49 已把 low-bit transform、layout、memory hierarchy、scheduler 与 speculative proposal/target commit绑定为 hardware-specific execution plan；该 55nm ReRAM-stacked digest 是一个受限 operating point，未改变只有目标模型拥有 token commit 权及不支持硬件时的通用 GPU fallback。；无需改稿。

### [NEXUS: Continual Learning of Symbolic Constraints for Safe and Robust Embodied Planning](https://arxiv.org/abs/2605.09387v1)

**采用版本与机制证据：** `arXiv:2605.09387v1`；https://arxiv.org/html/2605.09387v1 — §3 NEXUS continual symbolic constraint learning。

**评估证据：** https://arxiv.org/html/2605.09387v1 — §5 experiments；SafeAgentBench-derived dataset 与 safety/task metrics。

**反证与边界：** https://arxiv.org/html/2605.09387v1 — 受限于定制 benchmark、symbolic artifact 与 perception assumptions；不证明真实机器人安全；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-EMBODIED-VLA` → [26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；Ch26 已把 probabilistic action proposal、deterministic safety envelope、physical feasibility、environment feedback 与 human override分权；NEXUS 的 symbolic constraint accumulation落在该 pre-action gate，SafeAgentBench 不证明真实机器人 perception/calibration 或 hard constraint 完备。；无需改稿。

### [BadDLM: Backdooring Diffusion Language Models with Diverse Targets](https://arxiv.org/abs/2605.09397v1)

**采用版本与机制证据：** `arXiv:2605.09397v1`；https://arxiv.org/html/2605.09397v1 — §3 BadDLM backdoor threat/model and attack。

**评估证据：** https://arxiv.org/html/2605.09397v1 — §4 experiments 与 Appendix B additional experiments。

**反证与边界：** https://arxiv.org/html/2605.09397v1 — Appendix D Limitations；结论仅属于所测 DLM、trigger/target 与 evaluator；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 已把 diffusion masking/scheduler/denoising state 视为区别于 AR next-token path 的攻击面，并要求 release matrix覆盖触发、语义属性、alignment 与 payload slice；BadDLM 扩展攻击实例，但没有改变训练 artifact、行为 probe 与 effect gate 分离的防线。；无需改稿。

### [SWIFT: Prompt-Adaptive Memory for Efficient Interactive Long Video Generation](https://arxiv.org/abs/2605.09442v1)

**采用版本与机制证据：** `arXiv:2605.09442v1`；https://arxiv.org/html/2605.09442v1 — §3 SWIFT prompt-adaptive memory。

**评估证据：** https://arxiv.org/html/2605.09442v1 — §4 experiments 与 §4.5 additional experiments。

**反证与边界：** https://arxiv.org/html/2605.09442v1 — Figure 11 failure case；继承 pretrained video diffusion backbone 限制，复杂 multi-prompt 不保证一致性；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24 已要求 prompt revision使 cached generation state 失效或定点更新，并把短窗连续性与长程 semantic anchor分层；SWIFT 的 head-wise injection/window allocation实现该状态迁移，但没有改变 cache identity 与质量回退原则。；无需改稿。

### [Not All Thoughts Need HBM: Semantics-Aware Memory Hierarchy for LLM Reasoning](https://arxiv.org/abs/2605.09490v1)

**采用版本与机制证据：** `arXiv:2605.09490v1`；https://arxiv.org/html/2605.09490v1 — §3 semantics-aware GPU/CPU KV memory hierarchy。

**评估证据：** https://arxiv.org/html/2605.09490v1 — §4 experiments；7B/14B fp16、32B NF4、RTX 6000 Ada/A100/RTX 5080。

**反证与边界：** https://arxiv.org/html/2605.09490v1 — §4 Limitations and future work；结果受 reasoning workload、importance predictor、PCIe 与量化配置限定；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-GPU-MEMORY` → [54-gpu-memory.md](../../../../books/part-05-inference-system/54-gpu-memory.md)；Ch54 已区分 HBM residency、host tier、compression 与 destructive eviction，并要求按 relevance、transfer latency 和 SLO管理迁移；该论文的 full-precision prefetch证明特定 GPU/PCIe 配置下可保精度，但未改变超时或带宽不足时保守 admission/eviction 的边界。；无需改稿。

### [Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces](https://arxiv.org/abs/2605.09497v1)

**采用版本与机制证据：** `arXiv:2605.09497v1`；https://arxiv.org/html/2605.09497v1 — §4 DUDE deception-aware web-agent training/inference。

**评估证据：** https://arxiv.org/html/2605.09497v1 — §5 experiments 与 Appendix B implementation；Qwen3-VL/UI-TARS/GLM、4xA100。

**反证与边界：** https://arxiv.org/html/2605.09497v1 — Limitations；增加 per-step latency，训练/迁移只覆盖披露网站、欺骗类型和 evaluator；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-TOOL-CALLING` → [78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)；Ch78 已把 GUI observation 当不可信 sensor、把 click 作为 side-effect proposal，并要求 action policy/authorization独立于页面说服文本；DUDE 的 deception detector与经验摘要降低作者场景误点，但 detector 不能获得执行权。；无需改稿。

### [Mixture of Layers with Hybrid Attention](https://arxiv.org/abs/2605.09516v1)

**采用版本与机制证据：** `arXiv:2605.09516v1`；https://arxiv.org/html/2605.09516v1 — §2 MoL Architecture；§3 Hybrid Attention（shared softmax + routed DeltaNet）。

**评估证据：** https://arxiv.org/html/2605.09516v1 — §4 setup；§5 results；Appendix D–J granularity、crossover、multi-seed、latency。

**反证与边界：** https://arxiv.org/html/2605.09516v1 — §5.7 Limitations：规模、训练量、kernel/analytic sharding 与 rank ceiling 适用前提；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MODEL-MOE` → [21-moe.md](../../../../books/part-02-model/21-moe.md)；Ch21 以 token-to-expert routing 为主；论文把稀疏单位提升为 thin layer block，并以 shared softmax attention 保底全局覆盖、routed DeltaNet 承担稀疏状态更新，形成 layer-level conditional compute 的独立架构分支。；已在正文并有 canonical marker。

### [TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM](https://arxiv.org/abs/2605.09536v1)

**采用版本与机制证据：** `arXiv:2605.09536v1`；https://arxiv.org/html/2605.09536v1 — §3 Method；§3.2 privileged trajectory；§3.3 temporal-aware self-distillation。

**评估证据：** https://arxiv.org/html/2605.09536v1 — §4 Experiments；§4.2–§4.3；Appendix D throughput/trajectory results。

**反证与边界：** https://arxiv.org/html/2605.09536v1 — §6 Limitations：teacher trajectory、任务/模型与训练开销限制；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24 已比较 parallel denoising 与 correction，却没有区分 diffusion trajectory 中相邻时刻的局部变化与远时刻的全局变化；TAD 用 privileged trajectory 收集和 temporal-aware distillation 把两类监督分开，形成速度/质量可选 operating mode。；已在正文并有 canonical marker。

### [TIDE-Bench: Task-Aware and Diagnostic Evaluation of Tool-Integrated Reasoning](https://arxiv.org/abs/2605.09544v1)

**采用版本与机制证据：** `arXiv:2605.09544v1`；https://arxiv.org/html/2605.09544v1 — §3 TIDE-Bench task-aware tool-integrated reasoning protocol。

**评估证据：** https://arxiv.org/html/2605.09544v1 — §4/§5 benchmark results，含 tool-grounded experimental design。

**反证与边界：** https://arxiv.org/html/2605.09544v1 — 无独立 Limitations；统一分数仍受任务集合、tool environment、rubric/judge 与模型版本限定；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已要求 tool-agent evaluation同时保存 final outcome、trajectory/tool correctness、成本与副作用，并按 task type使用不同 verifier；TIDE-Bench 增加任务和过滤低区分样本，但未改变多轴 evidence contract。；无需改稿。

### [Trust Me, Import This: Dependency Steering Attacks via Malicious Agent Skills](https://arxiv.org/abs/2605.09594v1)

**采用版本与机制证据：** `arXiv:2605.09594v1`；https://arxiv.org/html/2605.09594v1 — §IV attack formulation 与 §V optimization/evaluation protocol。

**评估证据：** https://arxiv.org/html/2605.09594v1 — §VI experiments；四组 Python prompt data、THR/GHR 与 optimization budget。

**反证与边界：** https://arxiv.org/html/2605.09594v1 — §IX-C Limitations；以开源 coding model 与 Python 为主，不能代表商业 agent 与真实 workflow 分布；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Security 章已把 Skill、dependency、requirement 与 tool metadata 视为不可信 supply-chain input，并以真实 side effect 与最小 authority 验收；该攻击是已有威胁模型实例。；无需改稿。

### [Edit-Based Refinement for Parallel Masked Diffusion Language Models](https://arxiv.org/abs/2605.09603v1)

**采用版本与机制证据：** `arXiv:2605.09603v1`；https://arxiv.org/html/2605.09603v1 — §3 Methodology；§3.1 Edit-based Diffusion；§3.2–§3.3 model/train/inference。

**评估证据：** https://arxiv.org/html/2605.09603v1 — §4 Experiments；§4.2–§4.3；Appendix B/C timing、generalization 与 ablation。

**反证与边界：** https://arxiv.org/html/2605.09603v1 — 无独立 limitations；只覆盖 LLaDA/code/math 与披露 edit construction，不能证明任意 DLM 或开放式文本收益；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；并行 masked decoding 只能替换 mask 时，早期错误会固化；论文增加 sequence-level edit phase，让模型提出 insertion/deletion/replacement 式修正，再由后续 refinement 收敛，补全 parallel proposal 后的可撤销 correction branch。；已在正文并有 canonical marker。

### [Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training](https://arxiv.org/abs/2605.09608v1)

**采用版本与机制证据：** `arXiv:2605.09608v1`；https://arxiv.org/html/2605.09608v1 — §3 geometry-conflict account and continual-post-training control。

**评估证据：** https://arxiv.org/html/2605.09608v1 — §4 experiments/ablations across sequential updates。

**反证与边界：** https://arxiv.org/html/2605.09608v1 — 结论限于披露模型、task sequence、optimizer 与 intervention；几何相关不自动构成普适因果；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `TRAIN-PRETRAINING` → [28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md)；Ch28 已解释 update geometry、optimizer state与稳定性，却没有把 continual post-training 的新任务更新定义为相对当前 model state 的 covariance geometry，并据 conflict决定 transfer、interference或 merge gate。；已在正文并有 canonical marker。

### [Scratchpad Patching: Decoupling Compute from Patch Size in Byte-Level Language Models](https://arxiv.org/abs/2605.09630v1)

**采用版本与机制证据：** `arXiv:2605.09630v1`；https://arxiv.org/html/2605.09630v1 — §3 Scratchpad Patching；§3.1 selective update；§3.2 training/inference implementation。

**评估证据：** https://arxiv.org/html/2605.09630v1 — §4 Experiments；§5 analyses；Appendix E Pareto/ablation。

**反证与边界：** https://arxiv.org/html/2605.09630v1 — §7 Limitations：模型规模、byte architecture、patchifier、训练和实现路径限定；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MODEL-TOKENIZER` → [11-tokenizer.md](../../../../books/part-02-model/11-tokenizer.md)；Ch11 说明 byte patch 与动态边界，但未解决 patch lag：大 patch 降低序列长度却延迟局部计算。Scratchpad patching 在 patch 内按 entropy 更新短暂隐状态，使 patch boundary 与 compute frequency 解耦，同时引入额外 KV/attention 与调度成本。；已在正文并有 canonical marker。

### [Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction](https://arxiv.org/abs/2605.09649v1)

**采用版本与机制证据：** `arXiv:2605.09649v1`；https://arxiv.org/html/2605.09649v1 — §3 DBTrimKV layer/output-aware eviction。

**评估证据：** https://arxiv.org/html/2605.09649v1 — Appendix B experiments。

**反证与边界：** https://arxiv.org/html/2605.09649v1 — Appendix D Limitations and Future Work；只支持披露模型、长上下文任务、budget 与实现；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `INFER-KV-CACHE` → [45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；Ch45 已将 KV eviction写成 layer/token-specific quality-budget optimization，并要求 reconstruction error、long-context accuracy与真实 memory saving共同验收；DBTrimKV 的 output reconstruction/smoothing 是该策略实例，未改变 full-cache fallback。；无需改稿。

### [Workspace Optimization: How to Train Your Agent](https://arxiv.org/abs/2605.09650v1)

**采用版本与机制证据：** `arXiv:2605.09650v1`；https://arxiv.org/html/2605.09650v1 — §3–§4 workspace optimization and trainable external substrate。

**评估证据：** https://arxiv.org/html/2605.09650v1 — §5 experiments。

**反证与边界：** https://arxiv.org/html/2605.09650v1 — §6 Limitations and Conclusion；不是 weight training 的替代，收益受 workspace/tool/verifier 设计限定；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `AGENT-PLATFORM` → [84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)；Ch84 已把 workspace、instruction、tool、test feedback与版本化 artifact作为可训练外部 substrate，并要求独立 acceptance/rollback；论文优化 workspace 而非 weights，正是现有 platform evolution branch，不新增 commit authority。；无需改稿。

### [Forcing-KV: Hybrid KV Cache Compression for Efficient Autoregressive Video Diffusion Models](https://arxiv.org/abs/2605.09681v1)

**采用版本与机制证据：** `arXiv:2605.09681v1`；https://arxiv.org/html/2605.09681v1 — §4 Forcing-KV hybrid cache compression。

**评估证据：** https://arxiv.org/html/2605.09681v1 — §5 experiments on autoregressive video diffusion。

**反证与边界：** https://arxiv.org/html/2605.09681v1 — 无独立 Limitations；结果限于所测 video backbone、prompt switching、cache budget 与 quality evaluator；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24 已区分 video diffusion 的 temporal cache、prompt-conditioned state与局部重算，并要求质量/延迟共同验收；Forcing-KV 是具体 compression branch，未改变 prompt switch 时 invalidation/correction 的原则。；无需改稿。

### [MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring](https://arxiv.org/abs/2605.09684v1)

**采用版本与机制证据：** `arXiv:2605.09684v1`；https://arxiv.org/html/2605.09684v1 — §3 staged red-team pipeline、taxonomy 与 trajectory refinement。

**评估证据：** https://arxiv.org/html/2605.09684v1 — §4 experiments；五个 frontier monitors、三次 scorer runs。

**反证与边界：** https://arxiv.org/html/2605.09684v1 — §4.1 Limitations；单 agent、单 episode、persistent attacks，不覆盖 timing/backdoor/monitor jailbreak/multi-agent coordination；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-MONITORING` → [67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；Ch67 现有正文已把 monitor red-team 拆为攻击生成、trajectory 记录、scorer 重复运行与 taxonomy refinement，并保留单-agent/单-episode边界；该 exact-v1 语义已经存在，本轮只缺 canonical Source Family binding。；已在正文并有 canonical marker。

### [DriveFuture: Future-Aware Latent World Models for Autonomous Driving](https://arxiv.org/abs/2605.09701v1)

**采用版本与机制证据：** `arXiv:2605.09701v1`；https://arxiv.org/html/2605.09701v1 — §3 future-aware latent world-model learning and planning coupling。

**评估证据：** https://arxiv.org/html/2605.09701v1 — §4 autonomous-driving experiments。

**反证与边界：** https://arxiv.org/html/2605.09701v1 — 无独立 Limitations；驾驶数据、simulator、latent/action schema 与 planning evaluator 限定结论；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-WORLD-MODELS` → [25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；Ch25 已把 action-conditioned future state、imagined rollout 与 planner coupling写成 world-model 的核心责任，并区分生成逼真度与决策有效性；DriveFuture 的驾驶结果是该机制的领域证据，不足以外推真实安全。；无需改稿。

### [Calibrate, Don't Curate: Label-Efficient Estimation from Noisy LLM Judges](https://arxiv.org/abs/2605.09702v1)

**采用版本与机制证据：** `arXiv:2605.09702v1`；https://arxiv.org/html/2605.09702v1 — §3 calibrated aggregation of noisy LLM judges。

**评估证据：** https://arxiv.org/html/2605.09702v1 — §4 experiments 与 Appendix H additional experiments。

**反证与边界：** https://arxiv.org/html/2605.09702v1 — 无独立 Limitations；需要目标分布、少量 gold labels 与稳定 judge identity，不能把校准后估计当逐样本真值；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已把 judge identity、相关性、校准集和 proper scoring rule绑定，弱 judge只有在偏差可学习且信号非冗余时才可保留；该论文的 full-panel结果收窄 top-k heuristic，但不改变校准 owner。；无需改稿。

### [Security Risks in Tool-Enabled AI Agents: A Systematic Analysis of Privileged Execution Environments](https://arxiv.org/abs/2605.09721v1)

**采用版本与机制证据：** `arXiv:2605.09721v1`；https://arxiv.org/html/2605.09721v1 — §IV–§V privileged tool-execution threat model and architecture analysis。

**评估证据：** https://arxiv.org/html/2605.09721v1 — §VI controlled representative scenarios。

**反证与边界：** https://arxiv.org/html/2605.09721v1 — §VIII Limitations；small-scale、architecture-level，不测生产 prevalence、training/hardware vulnerability；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 已要求 privileged tool最小权限、credential scope、sandbox、effect-time authorization与审计；该 taxonomy 将 ambient authority leakage映射到三类场景，但没有改变 reference monitor 持有最终 side-effect 权。；无需改稿。

### [Dystruct: Dynamically Structured Diffusion Language Model Decoding via Bayesian Inference](https://arxiv.org/abs/2605.09820v1)

**采用版本与机制证据：** `arXiv:2605.09820v1`；https://arxiv.org/html/2605.09820v1 — §3–§4 Bayesian structural inference for dynamic DLM decoding。

**评估证据：** https://arxiv.org/html/2605.09820v1 — §5 experiments。

**反证与边界：** https://arxiv.org/html/2605.09820v1 — Limitations paragraph；纯 inference-time，结构 inference 与训练尚未联合，结果限于所测 DLM/tasks；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Ch24 已把 flexible length、block boundary、decode order与 EOS/commit视为同一结构状态，local confidence不得单独裁决；Dystruct 的 Bayesian inference 是该结构 controller 实例，训练免费不等于风险免费。；无需改稿。

### [Oracle Poisoning: Corrupting Knowledge Graphs to Weaponise AI Agent Reasoning](https://arxiv.org/abs/2605.09822v1)

**采用版本与机制证据：** `arXiv:2605.09822v1`；https://arxiv.org/html/2605.09822v1 — §3 Oracle Poisoning preconditions and attack variants。

**评估证据：** https://arxiv.org/html/2605.09822v1 — §5–§7 experiments、prefix-free/control and budget escalation。

**反证与边界：** https://arxiv.org/html/2605.09822v1 — §8.2 Limitations；模型 API/version、graph setup、prefix confound 与有限 trials 限定绝对 ASR；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Security 章已覆盖检索/知识资产投毒、provenance、reference coverage 与 tool-mediated effect；Oracle Poisoning 未改变 KG 输入的信任边界。；无需改稿。

### [Nautilus Compass: Black-box Persona Drift Detection for Production LLM Agents](https://arxiv.org/abs/2605.09863v1)

**采用版本与机制证据：** `arXiv:2605.09863v1`；arXiv:2605.09863v1 §3 Method/System Design — We present Nautilus Compass, a black-box persona drift detector and agent memory layer for production coding agents.。

**评估证据：** arXiv:2605.09863v1 §4 Evaluation/Experiments — Code, anchors, frozen test data, and audit-log tooling are MIT-licensed at github.com/chunxiaoxx/nautilus-compass.。

**反证与边界：** arXiv:2605.09863v1 Scope and Limitations: model, hardware, precision, length, batch, concurrency, SLO and evaluator not explicitly disclosed remain Not Disclosed；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-MONITORING` → [67-monitoring.md](../../../../books/part-06-ai-infrastructure/67-monitoring.md)；Monitoring 章已将 drift signal 视为需校准、需绑定 identity 和分布的 sensor，而非自动修复权；persona drift detector 是该原则的 agent 实例。；无需改稿。

### [Continuous Latent Contexts Enable Efficient Online Learning in Transformers](https://arxiv.org/abs/2605.09867v1)

**采用版本与机制证据：** `arXiv:2605.09867v1`；https://arxiv.org/html/2605.09867v1 — §3 Weighted Majority construction；§4 tabular Q-learning construction；Appendix C/D proofs/verification。

**评估证据：** https://arxiv.org/html/2605.09867v1 — §5 experiments；Appendix E synthetic、Q-learning 与 LLM inference settings。

**反证与边界：** https://arxiv.org/html/2605.09867v1 — Limitations and Future Work：构造性理论与小规模/合成实验，未证明 frontier model 自发学会或稳定部署该 state；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `MODEL-LONG-CONTEXT` → [22-long-context.md](../../../../books/part-02-model/22-long-context.md)；Ch22 讨论 recurrent state 与有效上下文，却未把 continuous latent context 明确为跨 step 更新的 compact algorithmic state；论文构造 transformer 恢复 multiplicative weights 和 tabular Q-learning，说明 online adaptation 可由持久 latent state 承担而非不断增长 token history。；已在正文并有 canonical marker。

### [Network-Efficient World Model Token Streaming](https://arxiv.org/abs/2605.09886v1)

**采用版本与机制证据：** `arXiv:2605.09886v1`；arXiv:2605.09886v1 §II System Model; §III Proposed Method — We study network-efficient streaming of a discrete world model state, where a stride-16 VQ-U-Net tokenizer (codebook size 8,192) maps each 288x512 frame to an 18x32 grid of token IDs (576 tokens/frame), equivalent to 936 bytes/frame under fixed-length coding.。

**评估证据：** arXiv:2605.09886v1 §IV Evaluation。

**反证与边界：** arXiv:2605.09886v1 §VI Discussion and Limitations；The exact-v1 body supports the mechanism under §IV Evaluation. Counterevidence/scope was checked at §VI Discussion and Limitations. It does not prove that “Network-Efficient World Model Token Streaming” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `MULTIMODAL-WORLD-MODELS` → [25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；Ch25 已把 world-state token、keyframe/delta、network loss、receiver revision与 downstream dynamics一起管理；论文给出驾驶 token stream operating point，但未改变丢包漂移时 keyframe resync/fallback。；无需改稿。

### [Skill Description Deception Attack against Task Routing in Internet of Agents](https://arxiv.org/abs/2605.09889v1)

**采用版本与机制证据：** `arXiv:2605.09889v1`；arXiv:2605.09889v1 §III System Model; §IV Skill Description Deception Attack — To characterize this threat, we propose and formalize a new attack model, termed \emph{Skill Description Deception} (SDD) attack.。

**评估证据：** arXiv:2605.09889v1 §V Experiment Results。

**反证与边界：** arXiv:2605.09889v1 No dedicated limitations section; the nine disclosed routing domains are the evidence boundary；The exact-v1 body supports the mechanism under §V Experiment Results. Counterevidence/scope was checked at No dedicated limitations section; the nine disclosed routing domains are the evidence boundary. It does not prove that “Skill Description Deception Attack against Task Routing in Internet of Agents” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Security 章已把 Skill description 与 discovery metadata 作为不可信路由输入，要求 authenticated identity、capability boundary 与 effect-time authorization；该 deception attack 未改变 owner。；无需改稿。

### [TRACER: Verifiable Generative Provenance for Multimodal Tool-Using Agents](https://arxiv.org/abs/2605.09934v1)

**采用版本与机制证据：** `arXiv:2605.09934v1`；arXiv:2605.09934v1 §3 Method (§3.1–§3.3); §4 Dataset — We introduce TRACER, a framework for verifiable generative provenance in multimodal tool-using agents.。

**评估证据：** arXiv:2605.09934v1 §5 Experiments。

**反证与边界：** arXiv:2605.09934v1 Limitations section and representative provenance-failure cases；The exact-v1 body supports the mechanism under §5 Experiments. Counterevidence/scope was checked at Limitations section and representative provenance-failure cases. It does not prove that “TRACER: Verifiable Generative Provenance for Multimodal Tool-Using Agents” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `AGENT-TOOL-CALLING` → [78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)；Ch78 已要求每个 claim绑定 tool observation、source identity、transformation relation与 verifier，tool trace 本身不等于证据；TRACER 的 Quotation/Compression/Inference schema具体化该 provenance graph，但不改变 verifier 权限。；无需改稿。

### [Attention Drift: What Autoregressive Speculative Decoding Models Learn](https://arxiv.org/abs/2605.09992v1)

**采用版本与机制证据：** `arXiv:2605.09992v1`；arXiv:2605.09992v1 §3 Attention Drift; §4 What Causes Attention Drift? (§4.1–§4.5) — drafter hidden-state scale and attention drift change speculative-decoding robustness contract。

**评估证据：** arXiv:2605.09992v1 §5 Performance Impact; Appendix B Benchmarks; Appendix C Training。

**反证与边界：** arXiv:2605.09992v1 §7 Limitations；The exact-v1 body supports the mechanism under §5 Performance Impact; Appendix B Benchmarks; Appendix C Training. Counterevidence/scope was checked at §7 Limitations. It does not prove that “Attention Drift: What Autoregressive Speculative Decoding Models Learn” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `INFER-SPECULATIVE-DECODING` → [48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)；Speculative 章覆盖 drafter quality/acceptance，却未解释 chain depth 导致 hidden-norm growth 与 attention drift 的失效机制及 normalization fallback。；正文已存在。

### [Sketch-based Access Control: A Multimodal Interface for Translating User Preferences into Intent-Aligned Policies](https://arxiv.org/abs/2605.10012v1)

**采用版本与机制证据：** `arXiv:2605.10012v1`；arXiv:2605.10012v1 §3 Formative Study and SBAC system design — We present Sketch-based Access Control (SBAC), a sketch-based, AI-assisted access control authoring system that combines the expressive power of sketching with the interpretive capabilities of multimodal large language models (MLLMs) to support the interpretation and validation of policy specifications as they are iteratively refined.。

**评估证据：** arXiv:2605.10012v1 §5 Evaluation。

**反证与边界：** arXiv:2605.10012v1 §6.4 Limitations；The exact-v1 body supports the mechanism under §5 Evaluation. Counterevidence/scope was checked at §6.4 Limitations. It does not prove that “Sketch-based Access Control: A Multimodal Interface for Translating User Preferences into Intent-Aligned Policies” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 已将自然语言/多模态 policy输入限制为 proposal，typed policy compiler、scenario test与 reference monitor持有生效权；SBAC改善人类表达与发现歧义，但小样本 usability study不证明自动生成 policy安全。；无需改稿。

### [GELATO: Generative Entropy- and Lyapunov-based Adaptive Token Offloading for Device-Edge Speculative LLM Inference](https://arxiv.org/abs/2605.10124v1)

**采用版本与机制证据：** `arXiv:2605.10124v1`；arXiv:2605.10124v1 §II System Model; §III GELATO adaptive scheduling algorithm — The recent growth of on-device Large Language Model (LLM) inference has driven significant interest in device-edge collaborative LLM inference.。

**评估证据：** arXiv:2605.10124v1 §IV Simulation and Evaluation。

**反证与边界：** arXiv:2605.10124v1 No dedicated limitations section; device-edge topology, draft/target pair and simulated resource envelope bound the result；The exact-v1 body supports the mechanism under §IV Simulation and Evaluation. Counterevidence/scope was checked at No dedicated limitations section; device-edge topology, draft/target pair and simulated resource envelope bound the result. It does not prove that “GELATO: Generative Entropy- and Lyapunov-based Adaptive Token Offloading for Device-Edge Speculative LLM Inference” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `INFER-SPECULATIVE-DECODING` → [48-speculative-decoding.md](../../../../books/part-05-inference-system/48-speculative-decoding.md)；当前章节没有把 device/edge speculative path 的每 token entropy、energy debt 与 offload action 写成在线约束控制；需与 target-only commit 分离。；正文已存在。

### [Usability as a Weapon: Attacking the Safety of LLM-Based Code Generation via Usability Requirements](https://arxiv.org/abs/2605.10133v1)

**采用版本与机制证据：** `arXiv:2605.10133v1`；https://arxiv.org/html/2605.10133v1 §3.1–§3.3 Threat Model and UPAttack formulation; §4.1–§4.3 U-Sploit Attack Framework — an external contributor injects benign-looking functionality, implementation or trade-off requirements; U-Sploit selects initially secure tasks, derives the usability reward of insecure alternatives, refines the pressure, and verifies a functionality-preserving security regression with existing tests or generated distinguishing payloads。

**评估证据：** https://arxiv.org/html/2605.10133v1 §5.1–§5.4 Experiments; Appendix B.1 Dataset Construction; Appendix E Manual Verification — 75 seed scenarios from 25 CWEs across Python, C and JavaScript; four victim models; CRbaseline/ASR/CRattacked; 33 common secure-baseline cases for transfer; repeated-attempt and dynamic-payload ablations; 30+30 sampled tasks manually checked。

**反证与边界：** https://arxiv.org/html/2605.10133v1 §5.1–§5.4; Appendix B.1; Appendix E; Impact Statement — exact-v1 has no dedicated Limitations section; the evidence is bounded to 75 benchmark scenarios, 25 CWEs, four named models, the disclosed Analyzer/Judge, mostly Python main results, 33-case transfer intersection and sampled manual validation; one Type-1 sample was unsatisfiable, and controlled benchmark attacks do not prove production prevalence, causal internal reward hacking or defense efficacy；Requirement intake is a security boundary: a coding model may preserve secure behavior under the original task yet drop implicit security constraints when explicit functionality, implementation or trade-off wording becomes the higher-salience objective. The exact-v1 evidence supports this failure mode only for the disclosed benchmark, models, attack generator/judge and verification protocol; it does not prove all issue-tracker requests are adversarial, all coding models fail, the internal cause is identified, or the proposed defenses are effective.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；exact-v1 已恢复且正文已写入：显式 usability proxy 可压过隐式 security constraint；需保留 75 场景/25 CWE/四模型和未发布 artifact 的边界。；正文已存在。

### [How Should LLMs Listen While Speaking? A Study of User-Stream Routing in Full-Duplex Spoken Dialogue](https://arxiv.org/abs/2605.10199v1)

**采用版本与机制证据：** `arXiv:2605.10199v1`；arXiv:2605.10199v1 §4 Method and user-stream routing policies; §5 training data — full-duplex user-stream placement changes interruption latency and generation coherence。

**评估证据：** arXiv:2605.10199v1 §6.1–§6.4 Experiments。

**反证与边界：** arXiv:2605.10199v1 §8 Limitations；The exact-v1 body supports the mechanism under §6.1–§6.4 Experiments. Counterevidence/scope was checked at §8 Limitations. It does not prove that “How Should LLMs Listen While Speaking? A Study of User-Stream Routing in Full-Duplex Spoken Dialogue” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `MULTIMODAL-REPRESENTATION` → [23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；Current MULTIMODAL-REPRESENTATION outline establishes the surrounding owner and fallback but does not make this exact mechanism explicit: full-duplex user-stream placement changes interruption latency and generation coherence. Integrate only the long-lived state/control/evidence delta; retain the source's non-proof boundary from REVIEW-20260512-2605-10199-V1.；正文已存在。

### [Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution](https://arxiv.org/abs/2605.10223v1)

**采用版本与机制证据：** `arXiv:2605.10223v1`；arXiv:2605.10223v1 §3 Core Principles; §4 Dynamic Tiered AgentRunner Architecture — We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform.。

**评估证据：** arXiv:2605.10223v1 §6 Evaluation。

**反证与边界：** arXiv:2605.10223v1 Limitations discussion after results; evidence is from the disclosed SaaS execution setting；The exact-v1 body supports the mechanism under §6 Evaluation. Counterevidence/scope was checked at Limitations discussion after results; evidence is from the disclosed SaaS execution setting. It does not prove that “Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `AGENT-PLATFORM` → [84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md)；Ch84 已按 risk tier分配模型、工具、review/verification budget，并将 proposal-review-execution-verification分权和 recovery loop写成 runtime contract；AgentRunner是现有治理路径的实例。；无需改稿。

### [Foundations of Reliable Inference: Reliability-Efficiency Co-Design](https://arxiv.org/abs/2605.10351v1)

**采用版本与机制证据：** `arXiv:2605.10351v1`；arXiv:2605.10351v1 Reliability–efficiency co-design chapters: inference reliability, uncertainty and system co-design — Recent advances in Bayesian learning have made significant progress toward this goal, and growing concerns about computational overhead have jointly shifted the design criterion from reliability alone to the co-design of reliability and efficiency, i.e., reducing computational overhead while preserving trustworthy uncertainty quantification.。

**评估证据：** arXiv:2605.10351v1 Worked analyses and case studies across the monograph。

**反证与边界：** arXiv:2605.10351v1 No single controlled evaluation contract; this is a synthesis and design framework, not comparative proof of one implementation；The exact-v1 body supports the mechanism under Worked analyses and case studies across the monograph. Counterevidence/scope was checked at No single controlled evaluation contract; this is a synthesis and design framework, not comparative proof of one implementation. It does not prove that “Foundations of Reliable Inference: Reliability-Efficiency Co-Design” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；这篇 thesis 的中心是可靠不确定性与计算效率协同；Ch66 已要求 calibration/coverage与 latency/cost在同一 operating curve上，并禁止以准确率替代 uncertainty validity。综述性统一框架没有提供足以改变当前 release contract 的单一新机制。；无需改稿。

### [EGL-SCA: Structural Credit Assignment for Co-Evolving Instructions and Tools in Graph Reasoning Agents](https://arxiv.org/abs/2605.10366v1)

**采用版本与机制证据：** `arXiv:2605.10366v1`；arXiv:2605.10366v1 §3 Method (§3.1–§3.5): graph credit assignment and co-evolution loop — verifier-centric credit assignment changes instruction and tool trajectory control。

**评估证据：** arXiv:2605.10366v1 Experiments and ablations。

**反证与边界：** arXiv:2605.10366v1 Appendix J Limitations；The exact-v1 body supports the mechanism under Experiments and ablations. Counterevidence/scope was checked at Appendix J Limitations. It does not prove that “EGL-SCA: Structural Credit Assignment for Co-Evolving Instructions and Tools in Graph Reasoning Agents” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `AGENT-WORKFLOW` → [81-workflow.md](../../../../books/part-07-agent/81-workflow.md)；当前 Workflow 章有 verifier gate，但未把失败 evidence 结构化分配给 instruction policy 与 executable tool program 两个独立更新空间。；正文已存在。

### [Agent-X: Full Pipeline Acceleration of On-device AI Agents](https://arxiv.org/abs/2605.10380v1)

**采用版本与机制证据：** `arXiv:2605.10380v1`；arXiv:2605.10380v1 §3 Pipeline Characterization; §4 Agent-X prefix cache and LLM-free drafting — We introduce Agent-X, a software-only, accuracy-preserving framework that accelerates both the prefill and decode stages of on-device agent workloads.。

**评估证据：** arXiv:2605.10380v1 §5 Evaluation。

**反证与边界：** arXiv:2605.10380v1 No dedicated limitations section; on-device models, devices and agent pipelines disclosed in §5 bound generality；The exact-v1 body supports the mechanism under §5 Evaluation. Counterevidence/scope was checked at No dedicated limitations section; on-device models, devices and agent pipelines disclosed in §5 bound generality. It does not prove that “Agent-X: Full Pipeline Acceleration of On-device AI Agents” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `INFER-REQUEST-LIFECYCLE` → [42-what-happens-during-inference.md](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)；Ch42 已把 agent request拆成 prompt/prefix identity、prefill、decode、tool round与端到端 SLO；Ch45/Ch48 分别拥有 prefix cache和 speculative commit。Agent-X把两者组合到 on-device workload，未改变任何机制 owner或 target-verification fallback。；无需改稿。

### [Valid Best-Model Identification for LLM Evaluation via Low-Rank Factorization](https://arxiv.org/abs/2605.10405v1)

**采用版本与机制证据：** `arXiv:2605.10405v1`；arXiv:2605.10405v1 §3 Low-rank best-model identification method — In this work, we propose a principled framework that combines MAB with cheap predicted scores without compromising statistical validity.。

**评估证据：** arXiv:2605.10405v1 §4 Experiments。

**反证与边界：** arXiv:2605.10405v1 §5 Conclusion: low-rank-quality dependence and binary-score scope；The exact-v1 body supports the mechanism under §4 Experiments. Counterevidence/scope was checked at §5 Conclusion: low-rank-quality dependence and binary-score scope. It does not prove that “Valid Best-Model Identification for LLM Evaluation via Low-Rank Factorization” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已要求 adaptive sample allocation不能把预测分数当真值，selection/stopping rule与 confidence interval必须一起保存，并在 estimator失效时回退独立 holdout；low-rank doubly-robust MAB具体化该原则但未改变 evaluation authority。；无需改稿。

### [Can Agent Benchmarks Support Their Scores? Evidence-Supported Bounds for Interactive-Agent Evaluation](https://arxiv.org/abs/2605.10448v1)

**采用版本与机制证据：** `arXiv:2605.10448v1`；arXiv:2605.10448v1 §3 Method/System Design — Benchmark quality thus depends not only on task design, but also on the reliability of outcome detection.。

**评估证据：** arXiv:2605.10448v1 §4 Evaluation/Experiments — The resulting reports separate several empirically distinct failure modes.。

**反证与边界：** arXiv:2605.10448v1 Scope and Limitations: model, hardware, precision, length, batch, concurrency, SLO and evaluator not explicitly disclosed remain Not Disclosed；只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；当前章要求 outcome state，却未把 checker 的可观测 witness 覆盖度转成 score 的 evidence-supported lower/upper bound。；正文已存在。

### [Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.10481v1)

**采用版本与机制证据：** `arXiv:2605.10481v1`；arXiv:2605.10481v1 §2 Constraint Drift; §4 Paradigm Design (§4.1 CSG, §4.2 constraint-native RL, §4.3 closed loop) — We propose Constraint State Governance as a research paradigm for LLM-based multi-agent systems.。

**评估证据：** arXiv:2605.10481v1 §5 Empirical Case Study。

**反证与边界：** arXiv:2605.10481v1 §6 Alternative Views and Objections; §7 Research Agenda; §4 states the blueprint is not a complete verifier or RL algorithm；The exact-v1 body supports the mechanism under §5 Empirical Case Study. Counterevidence/scope was checked at §6 Alternative Views and Objections; §7 Research Agenda; §4 states the blueprint is not a complete verifier or RL algorithm. It does not prove that “Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `AGENT-MULTI-AGENT` → [82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)；PLATFORM-SECURITY and AGENT-MULTI-AGENT already require constraints to remain versioned execution state across delegation, tool calls and audit; this position paper names that known preservation failure without a new validated mechanism.；无需改稿。

### [Accelerating Compound LLM Training Workloads with Maestro](https://arxiv.org/abs/2605.10501v1)

**采用版本与机制证据：** `arXiv:2605.10501v1`；arXiv:2605.10501v1 §2 Compound Training Challenges; §3 Maestro Design (§3.1–§3.4) — In this paper, we introduce Maestro, a section-centric training framework that addresses both challenges.。

**评估证据：** arXiv:2605.10501v1 §4 Evaluations and Case Study (§4.1 VLM training, §4.2 distillation)。

**反证与边界：** arXiv:2605.10501v1 No dedicated limitations section; the disclosed compound workloads, cluster and framework integration bound the result；The exact-v1 body supports the mechanism under §4 Evaluations and Case Study (§4.1 VLM training, §4.2 distillation). Counterevidence/scope was checked at No dedicated limitations section; the disclosed compound workloads, cluster and framework integration bound the result. It does not prove that “Accelerating Compound LLM Training Workloads with Maestro” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `TRAIN-DISTRIBUTED-TRAINING` → [36-distributed-training.md](../../../../books/part-04-training-system/36-distributed-training.md)；Current TRAIN-DISTRIBUTED-TRAINING outline establishes the surrounding owner and fallback but does not make this exact mechanism explicit: In this paper, we introduce Maestro, a section-centric training framework that addresses both challenges.. Integrate only the long-lived state/control/evidence delta; retain the source's non-proof boundary from REVIEW-20260512-2605-10501-V1.；正文已存在。

### [Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability](https://arxiv.org/abs/2605.10516v1)

**采用版本与机制证据：** `arXiv:2605.10516v1`；arXiv:2605.10516v1 §2 output-consistency U-statistics; §3 execution trajectories as stochastic processes — This paper establishes a rigorous measurement science for AI agent reliability, providing a foundational framework for quantifying consistency under semantically preserving perturbations.。

**评估证据：** arXiv:2605.10516v1 §4 Experiments; §5 reliability-failure diagnostics; Appendices B–D。

**反证与边界：** arXiv:2605.10516v1 §6 Discussion; small-sample and multiple-valid-solution boundaries in Appendices B and D；The exact-v1 body supports the mechanism under §4 Experiments; §5 reliability-failure diagnostics; Appendices B–D. Counterevidence/scope was checked at §6 Discussion; small-sample and multiple-valid-solution boundaries in Appendices B and D. It does not prove that “Consistency as a Testable Property: Statistical Methods to Evaluate AI Agent Reliability” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；当前章已有语义保持扰动、trajectory identity、重复运行方差与 capability/robustness 分离；该统计框架细化而不改变合同。；无需改稿。

### [Acceptance Cards:A Four-Diagnostic Standard for Safe Fine-Tuning Defense Claims](https://arxiv.org/abs/2605.10575v1)

**采用版本与机制证据：** `arXiv:2605.10575v1`；arXiv:2605.10575v1 §2 Four-Diagnostic Acceptance Standard; §3 Audit Procedure — We introduce Acceptance Cards: an evaluation protocol, a documentation object, an executable audit package, and a claim-specific evidential standard for safe fine-tuning defense claims.。

**评估证据：** arXiv:2605.10575v1 §5 Artifact and case audit。

**反证与边界：** arXiv:2605.10575v1 §6 Limitations；The exact-v1 body supports the mechanism under §5 Artifact and case audit. Counterevidence/scope was checked at §6 Limitations. It does not prove that “Acceptance Cards:A Four-Diagnostic Standard for Safe Fine-Tuning Defense Claims” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；当前 safe fine-tuning 评价缺少把统计显著性、新语义泛化、机制一致性和跨任务迁移同时作为 promotion diagnostics 的 claim-specific acceptance card。；正文已存在。

### [PRISM: Generation-Time Detection and Mitigation of Secret Leakage in Multi-Agent LLM Pipelines](https://arxiv.org/abs/2605.10614v1)

**采用版本与机制证据：** `arXiv:2605.10614v1`；arXiv:2605.10614v1 §3 Threat Model; §4 PRISM generation-time leakage control — Multi-agent LLM systems introduce a security risk in which sensitive information accessed by one agent can propagate through shared context and reappear in downstream outputs, even without explicit adversarial intent.。

**评估证据：** arXiv:2605.10614v1 Evaluation and attack/utility experiments。

**反证与边界：** arXiv:2605.10614v1 Explicit scope and behavioral Limitations section；The exact-v1 body supports the mechanism under Evaluation and attack/utility experiments. Counterevidence/scope was checked at Explicit scope and behavioral Limitations section. It does not prove that “PRISM: Generation-Time Detection and Mitigation of Secret Leakage in Multi-Agent LLM Pipelines” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；当前章覆盖 secret 与 multi-agent 边界，但未把跨 agent 重复暴露导致 propagation amplification、generation-time detector 与 replacement policy 写成一条实时防线。；正文已存在。

### [Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference](https://arxiv.org/abs/2605.10670v1)

**采用版本与机制证据：** `arXiv:2605.10670v1`；arXiv:2605.10670v1 §3 System Design (§3.1–§3.6); §4 membership-elastic communication; §5 expert-coverage repair — We present EEP, a communication and runtime substrate that represents membership as explicit, mutable runtime state.。

**评估证据：** arXiv:2605.10670v1 Evaluation sections on failure/recovery and serving overhead。

**反证与边界：** arXiv:2605.10670v1 §3.1 Failure Model and Scope; no claim beyond disclosed partial-rank failures and redundant expert state；The exact-v1 body supports the mechanism under Evaluation sections on failure/recovery and serving overhead. Counterevidence/scope was checked at §3.1 Failure Model and Scope; no claim beyond disclosed partial-rank failures and redundant expert state. It does not prove that “Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `INFER-DYNAMO` → [52-dynamo.md](../../../../books/part-05-inference-system/52-dynamo.md)；Dynamo 章已写入 mutable membership、communicator/expert-placement versioning、partial-rank failure 与 degraded-mode fallback；该 exact-v1 的长期机制已真实存在于 Ch52 正文。；正文已存在。

### [MATRA: Modeling the Attack Surface of Agentic AI Systems -- OpenClaw Case Study](https://arxiv.org/abs/2605.10763v1)

**采用版本与机制证据：** `arXiv:2605.10763v1`；arXiv:2605.10763v1 §2 MATRA attack-surface framework — We present MATRA, a pragmatic threat modeling framework for agentic AI systems that adapts established risk assessment methodology to systematically assess how known LLM threats translate into deployment-specific risks.。

**评估证据：** arXiv:2605.10763v1 §3 OpenClaw use case。

**反证与边界：** arXiv:2605.10763v1 No controlled comparative evaluation; the single-system case study is explanatory, not prevalence evidence；The exact-v1 body supports the mechanism under §3 OpenClaw use case. Counterevidence/scope was checked at No controlled comparative evaluation; the single-system case study is explanatory, not prevalence evidence. It does not prove that “MATRA: Modeling the Attack Surface of Agentic AI Systems -- OpenClaw Case Study” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 已以 asset、trust boundary、attack path、authority与 blast radius组织 Agent threat model，并将 network sandbox/least privilege作为可验证控制；MATRA/OpenClaw case为应用实例，没有增加新的信任边界。；无需改稿。

### [LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments](https://arxiv.org/abs/2605.10779v1)

**采用版本与机制证据：** `arXiv:2605.10779v1`；arXiv:2605.10779v1 §3 Dataset and real-OS threat construction; §4 evaluation framework — semantic and physical checks plus OS rollback redefine safe computer-action commit。

**评估证据：** arXiv:2605.10779v1 §5 Experiments。

**反证与边界：** arXiv:2605.10779v1 §6 Limitations；The exact-v1 body supports the mechanism under §5 Experiments. Counterevidence/scope was checked at §6 Limitations. It does not prove that “LITMUS: Benchmarking Behavioral Jailbreaks of LLM Agents in Real OS Environments” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；当前章的 agent sandbox 仍缺 semantic verdict + physical OS effect 双验证，以及每 case OS snapshot rollback 防止跨测试污染的 evaluation boundary。；正文已存在。

### [Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge](https://arxiv.org/abs/2605.10805v1)

**采用版本与机制证据：** `arXiv:2605.10805v1`；arXiv:2605.10805v1 §2 reasoning-judge cost study; §3 RACER; §4 theoretical results — Through controlled comparisons between reasoning and non-reasoning judges, we show that explicit reasoning substantially improves judgment accuracy on tasks requiring structured verification (e.g., math and coding), while offering limited or even negative gains on simpler evaluations and incurring significantly higher computational cost.。

**评估证据：** arXiv:2605.10805v1 §5 Experiments; Appendix B evaluation protocol。

**反证与边界：** arXiv:2605.10805v1 §7 Conclusion and Limitation；The exact-v1 body supports the mechanism under §5 Experiments; Appendix B evaluation protocol. Counterevidence/scope was checked at §7 Conclusion and Limitation. It does not prove that “Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 已要求按 task complexity、judge competence、cost、calibration与 distribution shift路由 evaluator，reasoning judge不能统一启用；RACER给出特定 KL-robust router，但未改变固定预算下的独立 outcome gate。；无需改稿。

### [Verification Mirage: Mapping the Reliability Boundary of Self-Verification in Medical VQA](https://arxiv.org/abs/2605.10850v1)

**采用版本与机制证据：** `arXiv:2605.10850v1`；arXiv:2605.10850v1 §3 VeriMap: task taxonomy, two-axis behavior model and statistical testing — self-verifier agreement bias invalidates agreement-as-confidence without calibration。

**评估证据：** arXiv:2605.10850v1 Experiments and calibration analyses。

**反证与边界：** arXiv:2605.10850v1 Limitations section; medical-VQA datasets and verifier families bound transfer；The exact-v1 body supports the mechanism under Experiments and calibration analyses. Counterevidence/scope was checked at Limitations section; medical-VQA datasets and verifier families bound transfer. It does not prove that “Verification Mirage: Mapping the Reliability Boundary of Self-Verification in Medical VQA” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Evaluation 与 Sampling 已拒绝 self-confidence/self-agreement 作为 calibrated truth，并要求外部 verifier；该研究提供受限测量，不改变合同。；无需改稿。

### [Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory](https://arxiv.org/abs/2605.10870v1)

**采用版本与机制证据：** `arXiv:2605.10870v1`；arXiv:2605.10870v1 §3 decision-distortion setup and forgetting boundary; §4 certified online memory splits — Motivated by this decision-centric view of memory, we propose DeMem, an online memory learner that refines its partition only when data certify that a shared state would induce decision conflict, and prove near-minimax regret guarantees.。

**评估证据：** arXiv:2605.10870v1 §5 Experiments on synthetic tasks, LoCoMo and LongMemEval。

**反证与边界：** arXiv:2605.10870v1 No dedicated limitations section; theorem assumptions and the disclosed memory tasks bound operational claims；The exact-v1 body supports the mechanism under §5 Experiments on synthetic tasks, LoCoMo and LongMemEval. Counterevidence/scope was checked at No dedicated limitations section; theorem assumptions and the disclosed memory tasks bound operational claims. It does not prove that “Remember the Decision, Not the Description: A Rate-Distortion Framework for Agent Memory” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `AGENT-MEMORY` → [77-memory.md](../../../../books/part-07-agent/77-memory.md)；Ch77 已明确压缩目标不是描述相似度，而是在预算下保留会改变下一步行动的 decision-sufficient distinctions，并要求绘制 memory-budget/decision-quality frontier；DeMem的 rate-distortion形式化支持这一命题，不改变 memory write authority。；无需改稿。

### [Compute Where it Counts: Self Optimizing Language Models](https://arxiv.org/abs/2605.10875v1)

**采用版本与机制证据：** `arXiv:2605.10875v1`；arXiv:2605.10875v1 §4 per-token self-optimizing runtime policy — per-token policy jointly controls sparsity, pruning and precision at runtime。

**评估证据：** arXiv:2605.10875v1 §5 Experiments and ablations。

**反证与边界：** arXiv:2605.10875v1 No dedicated limitations section; evaluated models, accelerator and policy-action space bound the runtime conclusion；The exact-v1 body supports the mechanism under §5 Experiments and ablations. Counterevidence/scope was checked at No dedicated limitations section; evaluated models, accelerator and policy-action space bound the runtime conclusion. It does not prove that “Compute Where it Counts: Self Optimizing Language Models” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `INFER-TENSORRT-LLM` → [49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；当前 Execution 章未把 token 级 difficulty signal、动态 layer/compute budget、边界校验和 static fallback 组织为 versioned execution-plan action。；正文已存在。

### [Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers](https://arxiv.org/abs/2605.10901v1)

**采用版本与机制证据：** `arXiv:2605.10901v1`；arXiv:2605.10901v1 §3 Method and formal guardrail guarantee — To formally evaluate these classifiers, we propose two constructions of such regions: SVD-aligned hyper-rectangles, which yield exact SAT/UNSAT certificates, and Gaussian Mixture Models, which yield probabilistic certificates over semantically coherent clusters.。

**评估证据：** arXiv:2605.10901v1 §4 Experiments。

**反证与边界：** arXiv:2605.10901v1 §5.2 Limitations；The exact-v1 body supports the mechanism under §4 Experiments. Counterevidence/scope was checked at §5.2 Limitations. It does not prove that “Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-SECURITY` → [72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)；Ch72 目前有 empirical red-team、probabilistic certificate 与 reference monitor，但未写出 guardrail classifier 可在 pre-activation harmful region 上用 monotonic head证明整个 convex region的最坏点，也未区分 exact hyper-rectangle 与 probabilistic mixture certificate。；已在正文并有 canonical marker。

### [WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation](https://arxiv.org/abs/2605.10912v1)

**采用版本与机制证据：** `arXiv:2605.10912v1`；arXiv:2605.10912v1 §3 benchmark construction, native-runtime tasks and evaluation contract — native-runtime long-horizon tasks expose tool side effects as evaluation evidence。

**评估证据：** arXiv:2605.10912v1 §4 Experiments。

**反证与边界：** arXiv:2605.10912v1 Appendix B Limitations；The exact-v1 body supports the mechanism under §4 Experiments. Counterevidence/scope was checked at Appendix B Limitations. It does not prove that “WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

**Books：** `PLATFORM-EVALUATION-SYSTEM` → [66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；当前 Agent 评测仍缺真实 CLI harness、长时 wall-clock/tool trace、容器化 state 与 graded outcome 联合形成的 native-runtime workload contract。；正文已存在。

### Books Decision 汇总

- Integrate：47；47 项均已在唯一 owner 正文中具有 canonical Source Family binding；本轮 12 项正文与 2 项 marker-only 写回已经 fresh non-author 终审。
- No Change — Existing Coverage：77；均已改为命题级比较。
- Weekly Only / Blocked / Disputed：0。未披露 artifact 只限制复现强度，不冒充正文受阻。

### 2026-10-18遗漏补充：已实际闭合项

以下为本次46项补充的必要证据与具体Books处置，34实际整合/12已有覆盖均已独立通过；前述连续旧§4与旧124候选/日期评分保留。共同日期资格为精确v1、当期公告日程下界及sameDOI findable/arxiv.content registered上界将整个可能区间限定May11，不能把Submitted/created单字段当公告。长证据与实际阅读范围沿唯一SUP和reader有效层复用，不为排版重复全文审阅。

### [Towards Closing the Autoregressive Gap in Language Modeling via Entropy-Gated Continuous Bitstream Diffusion](https://arxiv.org/abs/2605.07013v1)

**贡献与Source：** 词表维输出与质量/熵互相牵制 → bitstream解析posterior+context residual，entropy grid改变effective churn → 重新配置输出接口与采样预算。双方§3.1–3.6、§4.1–4.4/T1–3、§6、D.5–6与F.1/F.5。主干仍处理T位置，输出边界O(TV)→O(T logV)，并非所有FLOPs同降；Langevin解释仅小步极限。130M/LM1B/OWT、GPT2-large GenPPL+unigram entropy和10seeds，不采v2 462M。GH200/BF16 synthetic128NFE排除codec/transfer，不能与256NFE质量拼生产加速。 [精确v1原文](https://arxiv.org/html/2605.07013v1)；本地完整原件和双方范围见[唯一SUP A4.1](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（整合）：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [owner](../../../../Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；LangFlow已有categorical路径但缺bitstream posterior/grid-churn耦合；指定单段已真实保存，reader R10 POST、root接纳释放。

### [SmellBench: Evaluating LLM Agents on Architectural Code Smell Repair](https://arxiv.org/abs/2605.07001v1)

**贡献与Source：** detector消失/测试通过不等结构修复 → expert FP/partial/TP、direct/cascading与新增smell分账 → 重考虑修复目标oracle和net impact。双方§3–7/T1–7。单scikit-learn1.7.2/PyExamine，65hard tasks=11TP/41FP/13partial；消失受任务顺序/连带效应影响，net count不代人工架构质量。无重复trials/nativeCLI混model-scaffold、GEPA proxy未验证真实outcome、top8 pairwise无显著差；不推广63.1%FP或47.7%为通用修复率。 [精确v1原文](https://arxiv.org/html/2605.07001v1)；本地完整原件和双方范围见[唯一SUP A4.5](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（整合）：** `PLATFORM-EVALUATION-SYSTEM` → [owner](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)；code-test已区分测试与语义，但缺detector目标本身误报和新增smell；指定单段已保存，reader R8 POST、root接纳释放。

### [Beyond the Black Box: Interpretability of Agentic AI Tool Use](https://arxiv.org/abs/2605.06890v1)

**贡献与Source：** 执行后才见tool error → pre-action last32 hidden→SAE→tool-need/risk probes → 重考虑sensor告警而非执行授权。双方§3.1–3.5、§4/T2–10、§5/T11、§6。两open backbones/Nemotron/BFCL，risk标签heuristic且协议shift混杂；latent ablation改变probe不是policy因果。T11 56.3/98.5%属runtime Expected–Actual，不是probe误报率。未核实现/复现或monitor完整服务费。 [精确v1原文](https://arxiv.org/html/2605.06890v1)；本地完整原件和双方范围见[唯一SUP A4.3](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（已有覆盖）：** `PLATFORM-MONITORING` → [owner](../../../../Books/part-06-ai-infrastructure/67-monitoring.md)；Ch67原生probe/SAE段和受限sensor段已绑定model/layer/SAE/checkpoint、域移/阈值、读出成本与独立policy；Ch78另own admission。reader R7 actual具体NC通过，未写书。

### [Agentick: A Unified Benchmark for General Sequential Decision-Making Agents](https://arxiv.org/abs/2605.06869v1)

**贡献与Source：** 跨范式榜单混入观察/harness收益 → same-seeded任务暴露五观测格式/可组合harness → 重考虑接口与模型的比较identity。双方§3.1–3.3、4.1–4.5、§5与必要AppA。37个2D turn-based任务/四难度/25seed/27configs；PPO pixel与LLM ASCII不是信息等价，同seed不是总费用相等。ONS strongest reference可>1，不是绝对上界；非VLM/finetune/旗舰全景，不授范式普遍排序。 [精确v1原文](https://arxiv.org/html/2605.06869v1)；本地完整原件和双方范围见[唯一SUP A4.4](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（已有覆盖）：** `PLATFORM-EVALUATION-SYSTEM` → [owner](../../../../Books/part-06-ai-infrastructure/66-evaluation-system.md)；Ch66 Evaluation Runtime已有model×benchmark×harness×environment×scorer、adapter语义与同turn非同API/token/time预算；Ch23 shape非信息等价。reader R7 actual具体NC通过。

### [Self-Consolidating Language Models: Continual Knowledge Incorporation from Context](https://arxiv.org/abs/2605.07076v1)

**贡献与Source：** 静态更新集合难兼顾累计保持 → current model提出where-update、inner候选择优commit、outer改round-start → 重考虑selector与写入参数同环。双方§3/4/T1–2、§5/T3、§6、A.10/A.13；作者另A.11–12/A.14与B.1–B.3。K10 meta-training≠SQuAD eval K1，Fisher非因果；fixed-last10保持接近是替代、长流BatchTTT41.5>SCoL37。A13表/文归属冲突不采精确recipe；copies/适配/reward/顺序更新均计费。 [精确v1原文](https://arxiv.org/html/2605.07076v1)；本地完整原件和双方范围见[唯一SUP A4.7](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（整合）：** `TRAIN-SFT` → [owner](../../../../Books/part-04-training-system/29-sft.md)；Ch29静态layer选择与continual subspace之间缺当前selector/updated weights反馈与round-start区别；指定一段已保存，reader R13 POST、root接纳释放。

### [MAGIQ: A Post-Quantum Multi-Agentic AI Governance System with Provable Security](https://arxiv.org/abs/2605.06933v1)

**贡献与Source：** PQ-TLS认证不控制task-msg总预算 → user签session-bound hashchain、Merkle子额/ACL/clock分责 → 重考虑传输/联系许可/额度/语义四边界。双方§2.3/3、4.1、§5 theorem/sketch、6.1–2/6.8；作者另4.2–4.4/6.3–6.7，未称完整F proof/实现已核。UC限static corruption、trustedCA/user软件、HB-curious可用provider、PQ-TLS/globalRO/clock及至少一honest端，不授双方恶意/内容安全/DoS。XMSS约36s预计算/框架不同，6.8数值矛盾不采constant开销。 [精确v1原文](https://arxiv.org/html/2605.06933v1)；本地完整原件和双方范围见[唯一SUP A4.8](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（整合）：** `AGENT-MCP` → [owner](../../../../Books/part-07-agent/83-mcp.md)；Ch83 workspace协议后缺session-bound可核销msg预算，未扩为任意task全局；指定一段已保存，reader R13 POST、root接纳释放。

### [PolarVLM: Bridging the Semantic-Physical Gap in Vision-Language Models](https://arxiv.org/abs/2605.07574v1)

**贡献与Source：** RGB缺反射/透明物理辨别 → 新偏振观测+双branch周期/尺度接口及两阶段适配 → 重考虑补证与放大旧encoder的区别。双方§3–6/T1–2、§7与AppC/E T3–4。只采dual-stream合同，不照录AoLP/S0/近零DoLP未闭recipe；RGB冻结不等共享LLM/旧能力保持，attention ratio非因果路由。GPT4o-mini合成标注+text-reference judge非物理真值，reflection编码4.09<raw角4.44；sensor/两路token/训练与独立回归全费。 [精确v1原文](https://arxiv.org/html/2605.07574v1)；本地完整原件和双方范围见[唯一SUP A4.9](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（整合）：** `MULTIMODAL-REPRESENTATION` → [owner](../../../../Books/part-03-multimodal-world-models/23-multimodal-representation.md)；Ch23异质sensor fusion已讲选择性对齐，但缺新增物理测量与先对齐新branch防RGB捷径；指定一段已保存，reader R13 POST、root接纳释放。

### [Vaporizer: Breaking Watermarking Schemes for Large Language Model Outputs](https://arxiv.org/abs/2605.07481v1)

**贡献与Source：** 只报removal混淆信号与文本保持 → lexical/translation/paraphrase双目标评价 → 重考虑detector operating point与transform范围。双方§3–6/T2–7，安全反证必要深入。仅100 ChatGPT写作prompts，BERT/readability/grammar不是逐样本人语义等价；PRW Z<0/SynthID g<0.5未匹配FPR，model/关键配置未闭，不合并100/23/14排序或推翻原形式robustness。4070Super12GB/512chunk的minutes费用非通用；hybrid检测只是提议。 [精确v1原文](https://arxiv.org/html/2605.07481v1)；本地完整原件和双方范围见[唯一SUP A4.12](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（已有覆盖）：** `PLATFORM-SECURITY` → [owner](../../../../Books/part-06-ai-infrastructure/72-security.md)；Ch72 regeneration/内容保持、posthoc文本功能人口、soundness/不可伪造与Hamming每块条件已具体分责；弱校准新结果不改变这些选择。reader R15 actual具体NC通过，非旧generic复用。

### [Attention Transfer Is Not Universally Effective for Vision Transformers](https://arxiv.org/abs/2605.07191v1)

**贡献与Source：** 少数family attention-only收益被外推 → native norm/scale/position恢复student计算context可逆转失败 → 重考虑routing权重不是可移植完整函数。双方§2–6/T1–6/Fig3–6必要文本，reader另AppC。matched-size softmax ViT、20teachers/11families、3seeds/20epochs+部分100；standard晚层KL spike，不能写全部attention精确matched仍无效或借v2结论。native-scratch更差支持interaction，recipe单因素反例非穷尽因果；不外推LLM/linearattention。 [精确v1原文](https://arxiv.org/html/2605.07191v1)；本地完整原件和双方范围见[唯一SUP A4.13](../_sources/daily-20260512/SUP_SOURCES_20261018.md)。

**Books（已有覆盖）：** `TRAIN-SFT` → [owner](../../../../Books/part-04-training-system/29-sft.md)；Ch29计算责任/latent相似非held-out行为、跨架构末层不保、原student/配对预算已具体覆盖，Ch23也界定mask/position改变函数。reader R15 actual具体NC通过。

### [DiffRetriever: Parallel Representative Tokens for Retrieval with Diffusion Language Models](https://arxiv.org/abs/2605.07210v1)

**贡献、证据与边界：** 单代表检索受限→同pass多个mask代表与MaxSim/hybrid→重考虑producer与索引成本。采用[精确v1](https://arxiv.org/html/2605.07210v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.10](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。同pass非同FLOPs；16代表索引与多query搜索全费。AR cap/额外diffusion训练不构成只改解码因果，per-query oracle不可部署。

**Books（整合）：** `AGENT-RAG` → [Ch76](../../../../books/part-07-agent/76-rag.md)；multivector总论后、局部重排前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [On the Robustness of Distribution Support under Diffusion Guidance](https://arxiv.org/abs/2605.07220v1)

**贡献、证据与边界：** guidance被误作任意条件正确→理想score下target support终点定理→重考虑support与density/有限步保证。采用[精确v1](https://arxiv.org/html/2605.07220v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.11](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。compact convex/interior、positive weights/density下界与exact score假设；无限步网格收敛不授finite NFE/真实分布正确，非凸仅toy。

**Books（整合）：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；Blinddenoiser完整段后、h estimator前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [SREGym: A Live Benchmark for AI SRE Agents with High-Fidelity Failure Scenarios](https://arxiv.org/abs/2605.07161v1)

**贡献、证据与边界：** 撤去故障被当恢复→持续client probe与独立注入plane/两oracle→重考虑动态恢复验收。采用[精确v1](https://arxiv.org/html/2605.07161v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.14](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。90 curated非3623全验证；3runs/1800s失败封顶纳mean，noise可帮助slice；诊断专家只核100，未授生产安全。

**Books（整合）：** `PLATFORM-EVALUATION-SYSTEM` → [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；Failure Catchability后、数值Fault前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Theoretical Limits of Language Model Alignment](https://arxiv.org/abs/2605.07105v1)

**贡献、证据与边界：** 把KL预算当稳定收益→精确tilt gain/Jeffreys与proxy error条件→重考虑目标与估计资格。采用[精确v1](https://arxiv.org/html/2605.07105v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.15](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。仅exact KL-regularized optimum；self-normalized需可积性非有限样本无偏，ensemble须iid pointwise unbiased bounded。选highest+smooth/漏画noisy runs、全部搜索费用保留。

**Books（整合）：** `TRAIN-RLHF` → [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；beta强弱后、人口惩罚前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [SpecBlock: Block-Iterative Speculative Decoding with Dynamic Tree Drafting](https://arxiv.org/abs/2605.07243v1)

**贡献、证据与边界：** 静态draft树难适应漂移→层移位/跨块缓存与interval adaptation→重考虑draft信号producer和rollback。采用[精确v1](https://arxiv.org/html/2605.07243v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.16](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。信号是target chosen token加drafter对其概率，不是target概率；两copy/sync/rollback全费，A5抽象verify不足证明exact rejection/cache等分布。

**Books（整合）：** `INFER-SPECULATIVE-DECODING` → [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)；两online分支后、跨进程协议前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://arxiv.org/abs/2605.07308v1)

**贡献、证据与边界：** 固定视觉节拍不足接触反应→contact gate切action query并复用slow K/V→重考虑双时钟责任。采用[精确v1](https://arxiv.org/html/2605.07308v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.17](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。30–50 demos/task、15trials/6task；VTLA/RDP只contact理想起始，表间baseline身份不可混。Inactive接口非旧函数不变，40ms未闭完整tail，gate/传感器/标注全费。

**Books（已有覆盖）：** `MULTIMODAL-EMBODIED-VLA` → [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；contact gate与双时钟、controller边界已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [GEM: Generating LiDAR World Model via Deformable Mamba](https://arxiv.org/abs/2605.07326v1)

**贡献、证据与边界：** 普通时空scan混运动信息→frame cues驱动三path/Mamba门控→重考虑ego/control与生成proxy。采用[精确v1](https://arxiv.org/html/2605.07326v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.18](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。cue不是运动真值；GT未来ego与integrated planner不同，BEV what-if非物理反事实。多数据集部分指标落后，全部tokenizer/paths/diffusion/planner费，局部FPS非SLO。

**Books（已有覆盖）：** `MULTIMODAL-WORLD-MODELS` → [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；ego-conditioning、代理评价与控制责任已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [Membership Inference Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2605.07088v1)

**贡献、证据与边界：** 只有token likelihood才泄漏→action error或trajectory smoothness MIA→重考虑privacy unit和低FPR人口。采用[精确v1](https://arxiv.org/html/2605.07088v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.19](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。GT-action误差仍需示教真值；无GT trajectory信号在某VLA近随机。每类100轨迹的误报分辨率1%，不能认证表列0.1%；LIBERO微调非pretraining/真实用户，扰动非DP。

**Books（整合）：** `PLATFORM-SECURITY` → [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；membership后、PII前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Signal Reshaping for GRPO in Weak-Feedback Agentic Code Repair](https://arxiv.org/abs/2605.07276v1)

**贡献、证据与边界：** 零反馈被混为失败→semantic/step credit与资源exit provenance分层→重考虑训练机会人口。采用[精确v1](https://arxiv.org/html/2605.07276v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.20](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。fullmasked仍进group mean/variance，非完全不影响更新；Missing含judge failure。分层400人审不能无权重外推精确偏差/校正，单model/internal C++与全judge/训练费保留。

**Books（整合）：** `TRAIN-GRPO` → [Ch33](../../../../books/part-04-training-system/33-grpo.md)；sample-relative后、SPRO前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [What Matters for Diffusion-Friendly Latent Manifold? Prior-Aligned Autoencoders for Latent Diffusion](https://arxiv.org/abs/2605.07915v1)

**贡献、证据与边界：** 重构好被当生成latent好→VFM anchor/detailmodulator与邻域decode consistency→重考虑tokenizer三种property。采用[精确v1](https://arxiv.org/html/2605.07915v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.21](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。单ImageNet256/classcond；metrics含GT segment K/小扰动与有限类相关非生成保证。CFG/ODE/SDE schedule不同，W0后LayerNorm不保raw feature恒等；所有prior/DAM/loss/采样费。

**Books（整合）：** `MULTIMODAL-REPRESENTATION` → [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；串行bottleneck后、Cheers前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Teaching Language Models to Think in Code](https://arxiv.org/abs/2605.07237v1)

**贡献、证据与边界：** 代码中间量被当推理真值→code-only执行轨迹与自然恢复对照→重考虑解释器与逻辑验证。采用[精确v1](https://arxiv.org/html/2605.07237v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.22](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。99.2%只是answer出现在任意output的proxy；Recovery@k是自然错误条件子集非注入因果。SFT/RL/过滤/budget共同改变，avg@16非best-of，全部工具/teacher/训练费。

**Books（已有覆盖）：** `AGENT-TOOL-CALLING` → [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；受控program/interpreter与AST/授权语义已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents](https://arxiv.org/abs/2605.07177v1)

**贡献、证据与边界：** 只数turn掩盖单turn刷调用→grounded bbox query/同turn并行及TRACE双账→重考虑round与call共同预算。采用[精确v1](https://arxiv.org/html/2605.07177v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.23](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。failed-only reverseKL是loss mask非共享参数下成功行为不变；主表accuracy外源而turn本地，工具/summary/temp/checkpoint混杂，不采Pareto/5.3倍延迟。教师额外调用全费。

**Books（整合）：** `AGENT-TOOL-CALLING` → [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；tool architecture总论后、harness反侧前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Teacher-Feature Drifting: One-Step Diffusion Distillation with Pretrained Diffusion Representations](https://arxiv.org/abs/2605.07327v1)

**贡献、证据与边界：** drift依外部encoder→冻结diffusion teacher feature与anchor侧density缺口→重考虑metric producer。采用[精确v1](https://arxiv.org/html/2605.07327v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.24](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。p=q⇒field0单向非identifiability；重复SSIM非完整coverage。U-Net层/noise敏感，多加U1反退、FID与CLIP不可并胜，正样本teacher50步CFG6和训练全费。

**Books（整合）：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；drift两段后、SnapFlow前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [GPO-V: Jailbreak Diffusion Vision Language Model by Global Probability Optimization](https://arxiv.org/abs/2605.07399v1)

**贡献、证据与边界：** AR强迫prefix被当全程服从→masked后续progressive refusal→重考虑完整sequence/decoder成功判据。采用[精确v1](https://arxiv.org/html/2605.07399v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.25](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。latent whitebox与pixel transfer另协议；FPO人为100% prefix非GCG等预算排名。Eq7方向未闭不搬recipe，token injection残余且无adaptive/benign回归，judge proxy非真实harm。

**Books（整合）：** `PLATFORM-SECURITY` → [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；白盒prefix后、良性反事实前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Beyond Linear Attention: Softmax Transformers Implement In-Context Reinforcement Learning](https://arxiv.org/abs/2605.07333v1)

**贡献、证据与边界：** softmax只作匹配→指定memory rows与temporal shift实现weighted TD→重考虑计算由参数/prompt共同定义。采用[精确v1](https://arxiv.org/html/2605.07333v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.26](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。仅finite ergodic fixed-policy MRP与每state kernel diagonal条件；context先无限再depth非SGD保证，3层Boyan/5seeds/float64构造不证明任意LLM学会TD或删head。

**Books（整合）：** `MODEL-SELF-ATTENTION` → [Ch14](../../../../books/part-02-model/14-self-attention.md)；featurizer两段后、可解码标题前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Approximation Error Upper and Lower Bounds for Hölder Class with Transformers](https://arxiv.org/abs/2605.07463v1)

**贡献、证据与边界：** 单attention足够被当浅网络足够→量化/context ID/深value map存在性→重考虑计算藏在何处。采用[精确v1](https://arxiv.org/html/2605.07463v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.27](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。固定width/ReLU+softmax/PE与Hölder smoothness/维度假设；上/下界未闭，不授训练可达、Norm迁移、删层配方或工程最优深度。

**Books（整合）：** `MODEL-SELF-ATTENTION` → [Ch14](../../../../books/part-02-model/14-self-attention.md)；单层能力后、featurizer标题前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals](https://arxiv.org/abs/2605.07509v1)

**贡献、证据与边界：** 长trace直接归因昂贵→两prefill选择性恢复/NLL与attention候选→重考虑观测proposal和真实cause。采用[精确v1](https://arxiv.org/html/2605.07509v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.28](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。只failed traces未校准混合人口false positive；短trace反退、OOM与配置混杂；本地SLM/hostedAPI不同协议不可独归算法。全部prefill/储存/人工复原费。

**Books（整合）：** `PLATFORM-TRACE` → [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)；structure-guided attribution后、rule auditor前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Post-training makes large language models less human-like](https://arxiv.org/abs/2605.07632v1)

**贡献、证据与边界：** assistant更好被当更像人→human response likelihood与persona预测反侧→重考虑规范目标和行为目标。采用[精确v1](https://arxiv.org/html/2605.07632v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.29](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。teacher-forced history不是自由个体模拟；response-span NLL跨tokenizer不可统一绝对比。10%/max100 participant与模板/任务混杂，Centaur行为训练是反侧，不推所有post-training必损。

**Books（已有覆盖）：** `TRAIN-RLHF` → [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；p_H与r_P、likelihood/生成/prompt独立验收已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States](https://arxiv.org/abs/2605.07579v1)

**贡献、证据与边界：** value需独立critic→历史固定feature probe与other rollout baseline→重考虑信息泄漏及无偏边界。采用[精确v1](https://arxiv.org/html/2605.07579v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.30](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。actor更新后再训probe避免当前target泄漏；仅raw score-function项条件无偏，非PPO clip/length/multiepoch。MAE/Var(A)非gradient variance，batch/steps/rollouts齐变与4B均值反侧保留。

**Books（整合）：** `TRAIN-PPO` → [Ch32](../../../../books/part-04-training-system/32-ppo.md)；prompt scalar/critic局部后、GenAC前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [MemCompiler: Compile, Don't Inject -- State-Conditioned Memory for Embodied Agents](https://arxiv.org/abs/2605.07594v1)

**贡献、证据与边界：** memory直接注入context→state-conditioned guidance与brief-state分开→重考虑advice更新和soft-token消费。采用[精确v1](https://arxiv.org/html/2605.07594v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.31](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。固定pool/每步retrieve、Executor训练/冻结描述不一致不搬recipe；cosine/tSNE非语义互补，logit非attention。总compiler+executor tokens未减半，局部均时非SLO，完整训练/teacher费用。

**Books（整合）：** `AGENT-MEMORY` → [Ch77](../../../../books/part-07-agent/77-memory.md)；transition/advice/state条件后、repository前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Bringing Multimodal Large Language Models to Infrared-Visible Image Fusion Quality Assessment](https://arxiv.org/abs/2605.06969v1)

**贡献、证据与边界：** 均值评分掩盖冲突→属性分歧proxy定soft-label宽度与内外组ranking→重考虑标注/监督对象。采用[精确v1](https://arxiv.org/html/2605.06969v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.32](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。宽度非真实rater分布；high-delta窄range不构成SRCC理论上限，手工floor不采。Mean与overall混杂、rank/width非各slice全胜，校准协议/ensemble和重复encoder费用保留。

**Books（整合）：** `PLATFORM-EVALUATION-SYSTEM` → [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；lowrank consensus后、candidate pool前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models](https://arxiv.org/abs/2605.07721v1)

**贡献、证据与边界：** loop depth令KV线性增长→shared per-layer latent gate覆写KV→重考虑context与loop内存边界。采用[精确v1](https://arxiv.org/html/2605.07721v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.33](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。内存只对loop常数非context常数，下一token依前token最终loop有chunk训练代价。理论缓存量非完整VRAM；Ouro作者默认early-exit只选logit不省loop，MELT adaptive仍未来。

**Books（整合）：** `MODEL-KV-CACHE` → [Ch19](../../../../books/part-02-model/19-kv-cache.md)；HLA两段后、Position标题前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Tools as Continuous Flow for Evolving Agentic Reasoning](https://arxiv.org/abs/2605.07339v1)

**贡献、证据与边界：** 离散工具序列成本→latent conditional flow路径/最近embedding decode/首tool commit→重考虑计划表示和执行粒度。采用[精确v1](https://arxiv.org/html/2605.07339v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.34](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。只窄receding-horizon接口，不采理论：margin平方/证明不一、未见tool error缺训练残差、openloop自定义。状态修改成功远低oracle/部分RAG指标更高，多ODE与所有训练费，未授SLO。

**Books（整合）：** `AGENT-PLANNING` → [Ch79](../../../../books/part-07-agent/79-planning.md)；commitment完整段后、learned transition前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [SARC: A Governance-by-Architecture Framework for Agentic AI Systems](https://arxiv.org/abs/2605.07728v1)

**贡献、证据与边界：** child缺state可能丢规则→最近可判断层rescue/预算拒绝与authority交集→重考虑约束检查owner。采用[精确v1](https://arxiv.org/html/2605.07728v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.35](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。有限predicate/完整trace下审计不证bypass或规范真值；rescued state可stale，synthetic baseline与modelled21ms非实测，mean wait不授tail deadline，完整state/trace/审计费。

**Books（整合）：** `AGENT-MULTI-AGENT` → [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；delegation后、Spawn前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Operating Within the Operational Design Domain: Zero-Shot Perception with Vision-Language Models](https://arxiv.org/abs/2605.07649v1)

**贡献、证据与边界：** coarse高分被当fine ODD就绪→标签粒度/完备度与两侧风险人口→重考虑sensor接controller验收。采用[精确v1](https://arxiv.org/html/2605.07649v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.36](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。单主要label只能recall非classification FP；静态昼间/Mapillary不同任务，提示非factorial且prompt-only费用漏输出/多图。.73非认证阈值，不授部署推荐/合规/物理安全。

**Books（整合）：** `PLATFORM-EVALUATION-SYSTEM` → [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；CFHR后、原构形段前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Tool Calling is Linearly Readable and Steerable in Language Models](https://arxiv.org/abs/2605.07990v1)

**贡献、证据与边界：** tool routing可读被当原生因果→fixed menu steering/unembedding与schema controls→重考虑sensor及授权。采用[精确v1](https://arxiv.org/html/2605.07990v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.37](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。natural parallel仅3%/0、norm-matched可覆盖输出非唯一机制；base cos.998/.999小argmax，IT读出低generation。PCA topic对照/同义词失败/multiturn -30..+10，schema可能伪造参数，全部校准费。

**Books（已有覆盖）：** `AGENT-TOOL-CALLING` → [Ch78](../../../../books/part-07-agent/78-tool-calling.md)；prefix/参数续写、provisional routing与Ch67校准已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [SOD: Step-wise On-policy Distillation for Small Language Model Agents](https://arxiv.org/abs/2605.07725v1)

**贡献、证据与边界：** 多turn指导被等权→sampled abs-logratio调step蒸馏/排除observation→重考虑teacher指导时间资格。采用[精确v1](https://arxiv.org/html/2605.07725v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.38](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。proxy非真实KL/正确性；权重乘积可望远镜化，未采D4/5理论。Python/有限模型，大teacher普通OPD退步、mask错后损恢复，全部teacher/logprob/训练费。

**Books（整合）：** `TRAIN-GRPO` → [Ch33](../../../../books/part-04-training-system/33-grpo.md)；OPD总论三段后、peer marker前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling](https://arxiv.org/abs/2605.08083v1)

**贡献、证据与边界：** 反复在线试controller昂贵→冻结branch/probe replay搜索程序→重考虑离线搜索/真实验收。采用[精确v1](https://arxiv.org/html/2605.08083v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.39](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。128预采与64池重用非独立线上人口，unrevealed probe不入state/池外非真反事实。AIME24用于搜索，更多tokens仍有反退；discovery费用不含precollection和完整在线运行。

**Books（整合）：** `MODEL-SAMPLING` → [Ch20](../../../../books/part-02-model/20-sampling.md)；distinct-leaf双段后、程序重采前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Dooly: Configuration-Agnostic, Redundancy-Aware Profiling for LLM Inference Simulation](https://arxiv.org/abs/2605.07985v1)

**贡献、证据与边界：** 跨配置反复profile→tainted symbolic签名/动态sweep分离→重考虑复用单位。采用[精确v1](https://arxiv.org/html/2605.07985v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.40](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。hash同非物理同速，未决维度/valuebranch/customdispatcher保fallback。MoE随机路由非真负载/noop非通信，DoolySim只vLLM；完整trace/profile/regression费用不授SLO。

**Books（整合）：** `INFER-TENSORRT-LLM` → [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；图优化原理后、WebGPU前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [On Privacy Leakage in Tabular Diffusion Models: Influential Factors, Attacker Knowledge, and Metrics](https://arxiv.org/abs/2605.06835v1)

**贡献、证据与边界：** 合成数据距离被当隐私→不完备知识MIA与DCR失配→重考虑威胁/metric与privacy unit。采用[精确v1](https://arxiv.org/html/2605.06835v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.41](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。FPR为10%非0.1%，balanced rows非用户；distance组合攻击仍可有效。TF单shadow不等Ensemble无需16 RMIA/background；全部训练/2100噪声特征/Optuna费，未授无泄漏或DP缓解。

**Books（整合）：** `PLATFORM-SECURITY` → [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；MIA marker后、action-output前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Semantic Smoothing for Language Models via Distribution Estimation and Embeddings](https://arxiv.org/abs/2605.07994v1)

**贡献、证据与边界：** 独立count估计→logit-Lipschitz下语义近邻KL sideinfo→重考虑统计共享资格。采用[精确v1](https://arxiv.org/html/2605.07994v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.42](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。真实process L/eps/outputnorm假设不能由任意embedding近邻替代；min界端点不保证启发混合达界，fixed-d渐近不泛化任意d/n，bigram/oracle合成非现代LM全面PPL收益。

**Books（整合）：** `MODEL-EMBEDDING` → [Ch12](../../../../books/part-02-model/12-embedding.md)；距离非语义后、矩阵表示前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [Is a team only as strong as its weakest link? Quantifying the short-board effect with AI Agents](https://arxiv.org/abs/2605.07773v1)

**贡献、证据与边界：** 只修最弱成员→受限SOP的noncore影响与debug效率反侧→重考虑composition对照。采用[精确v1](https://arxiv.org/html/2605.07773v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.43](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。MetaGPT/Snake/约10rep；换role同时换model/style/cost，递增组合非product因果律。LOC/token与T/LOC方向冲突，少debug可能虚高效率，功能proxy非生产软件正确性。

**Books（已有覆盖）：** `AGENT-MULTI-AGENT` → [Ch82](../../../../books/part-07-agent/82-multi-agent.md)；role/model/scaffold与equal-budget baseline已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions](https://arxiv.org/abs/2605.07984v1)

**贡献、证据与边界：** 可读planning被当native必要→rhyme位置patch分离readable/intervenable→重考虑解释证据资格。采用[精确v1](https://arxiv.org/html/2605.07984v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.44](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。5prompt pairs×20非100独立prompt，tokens相关与peak/topk选择未全校正；三family位置不同。Top5 patch足改输出不证native必要/唯一回路，作者仍要求scrub/ablation，完整probe/patch费。

**Books（已有覆盖）：** `PLATFORM-EVALUATION-SYSTEM` → [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；内部可分/干预基线与组件交换、Ch67 sensor已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

### [SARA: Semantically Adaptive Relational Alignment for Video Diffusion Models](https://arxiv.org/abs/2605.07800v1)

**贡献、证据与边界：** 全局alignment忽略关系→text-conditioned entity pair路由→重考虑蒸馏监督对象。采用[精确v1](https://arxiv.org/html/2605.07800v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.45](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。内部topentity/maskcaption/三同源VLM judge不独立，偏差非constantoffset。High/low专家shift未因果隔离，fidelity/physics部分反退，完整teacher/aligner/stage训练费。

**Books（整合）：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；TFD后、SnapFlow前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy](https://arxiv.org/abs/2605.07931v1)

**贡献、证据与边界：** 未来condition带宽大→每frame/view一token与joint latent/action flow→重考虑producer/consumer。采用[精确v1](https://arxiv.org/html/2605.07931v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.46](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。原visionencoder未删除，fixed fusion非动态view权重；表格/均值/套件配置冲突不采统一rank。1token结论限30KLoRA，OOM/timeout混杂、horizon非单调，全部未来ODE费。

**Books（整合）：** `MULTIMODAL-EMBODIED-VLA` → [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；occupancy后、路径深度前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [DVD: Discrete Voxel Diffusion for 3D Generation and Editing](https://arxiv.org/abs/2605.07971v1)

**贡献、证据与边界：** binary连续近似或硬提交→categorical uniform反复更新/BSP→重考虑known voxel与decoder保真。采用[精确v1](https://arxiv.org/html/2605.07971v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.47](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。仅stage1离散/stage2连续；entropy是model/time proxy非固有uncertainty。GT voxel/不等训练预算和指标反退保留，known回写不保mesh；后续decode/render及训练全费。

**Books（整合）：** `MULTIMODAL-GENERATIVE-PARADIGMS` → [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；uniform两段后、locality前。该指定唯一段与本人来源注已经真实保存，非写入者实际完整新增/直接两侧/本人注POST通过，root接纳释放。

### [AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents](https://arxiv.org/abs/2605.07926v1)

**贡献、证据与边界：** 只看endtask→DAG/disclosure与resolved/discovered/provenance分账→重考虑工具依赖评价。采用[精确v1](https://arxiv.org/html/2605.07926v1)，必要方法/关键评价/直接反侧的实际域与本地原件见[唯一SUP A4.48](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；未变化的独立研究直接复用，不冒双份附件通读或实现复现。nodecount非pathdepth，human可解声明/一次成绩不一，cap actions/calls单位未闭，单trial/不同thinking非同费。Graph验证不证明文本充分或生产因果，不采效率rank。

**Books（已有覆盖）：** `PLATFORM-EVALUATION-SYSTEM` → [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；versioned constraint graph/disclosure/state predicates与ready依赖已有。已实际比较该具体论点与新证据，独立NC通过并由root接纳；局部新验证/反侧保在报告，不以主题相似或不改书反推贡献排除。

## 5. 缺口与下一步

普通研究/候选Source/Books落实与六节DAY待办为0；V3、旧内容冻结、引用和限定差异检查已通过，完成态按独立实际读回验收；发现新具体问题只恢复受影响层。以下为本窗终态保留项（外部），不支持正面证据、Books或无遗漏断言，不支撑性能/安全保证，也不被记成窗外或已审重复；各项定点重开条件见下。

日期请求（同一身份一次）：2605.08279/08301/08310/08314/16341/16342/16343、2606.20582、2605.30359、2605.08292/08300/08322/08268/08271/10966/13874，以及2607.14107/14108/14112/00011/00012、2608.20342、2605.08334/08288，共24项。精确v1 history的日程下界与sameDOI findable/arxiv.content registered上界跨May11～May12/May19或June/July/August；不能截取目标日、按ID月份排除，也不能把OAI metadata当正文首发。后8为原233中最后13含糊题摘的潜贡献，另5已具体贡献前关闭，不纳入确定46；SalesSim v1不继承CustomerSim v2。实际月list仅年月、官方Advanced说明公告仅年月、OAI与有限官方日搜索未给目标日公告，目前无已识别可继续产生所需历史日组的原入口。可接受替代为该身份真实dated首公告/历史new listing或其他原始联合约束把整个区间限定同日；得到后只重开其日期、精确版本与必要贡献审阅。具名原字段/原件与查询见[SUP A3/A6](../_sources/daily-20260512/SUP_SOURCES_20261018.md)；不为假想早稿渠道无限请求。

来源请求：OpenAI/Anthropic/DeepMind-Google/Meta/Qwen/DeepSeek/Kimi/ZAI/Seed/MiMo的早9小时历史研究slice或未标日材料；Hunyuan/ERNIE/MiniMax只恢复了指定当前集合/日期段而非完整历史。14到期入口、注册GitHub补窗及ZAI发布说明均按§2实际范围处理；GitHub8×0只代表明确索引窗，403/连接重置/timeout或当前shell不代零研究。OpenAI Signals正文仍403，仅搜索题名范围关闭；Qwen WebWorld原始dated材料未恢复。替代材料为官方可定位目标日的归档、dated正文/版本与精确paper/event身份；一旦到达只重开相关来源/事件，不重扫机构历年或整月。Hunyuan当前API9/11项显示日期可能与published/created相差数月，ZAI updatedAt不是release；这些限制不互相补造Coverage。

## 6. 复核

复核者：`/root/may12_supp_reader`（非报告作者、非Books写入者）。结论：通过；本次实际完整六节DAY为独核R49，不沿用原窗口通过。2026-10-19T03:59:32+08:00保存完成态，实际FINAL读回结果由同一独立复核者记入下述唯一记录，不预签。

已完成范围：首批准入与后续46确定家族全部准入/日期/必要Source，34项实际Books完整新增/直接两侧/本人注POST，12项具体已有覆盖；安全/设计反证和generic共同误闭局部恢复均已独立核。其余明确排除按主题、来源、理由分层抽检，未把233宽发现或86旧preclosed称全量二次审阅；最后13精确题摘的5C/8日期线索与机构/日期有限恢复亦单独校准。详细实际范围、纠错和未检查域见[唯一独核记录](../_sources/daily-20260512/SUP_REVIEW_20261018.md)。V3与限定cached/unstaged diff-check通过，457本地引用零缺失；原124整行/日期评分按序exact、原§4连续161669字符exact（SHA256 3546927b24dcba33f82497630e99992904c917cb4fbd4cd1c3778be0dc85b7e8），170=124+46。机器结果不冒充上述语义验收，未stage/commit/push。

下述为2026-09-15原窗口历史验收，只复用其未变化有效层，不移作本轮DAY/FINAL。

复核者：Codex fresh non-author reviewer（未参与本轮作者返修或 root 的 14 项 Books 写回）

结论：通过

- 14 个新 marker 区间均唯一成对、位于对应章节最后一个 `## Review notes` 之前；逐段复核确认旧方案、约束变化、state/control owner、证据边界、trade-off、failure/fallback 与相邻衔接完整。详细记录见 [fresh post-write final review](../_sources/daily-20260512/V3_FRESH_NONAUTHOR_POSTWRITE_FINAL_REVIEW_20260915.md)。
- 独立复算：1146 = 124 retained + 1022 closures；124 = 124 Evidence = 124 Books comparison；47 Integrate + 77 No Change = 124；47 Integrate 均已在 Books 正文具备 canonical binding；root pending=0。
- 本轮识别并纠正 `2605.08615` 的旧错误摘要；未把该错配带入 Books。

### Sources

- [arXiv](https://arxiv.org/)：05-12 公告批次及 exact-v1 HTML。
- [ROADMAP](../../../../ROADMAP.md)：Stable Knowledge Node owner。
- [有界来源返修审计](../_sources/daily-20260512/V3_SOURCE_ENDPOINT_WINDOW_AUDIT_20260915.json)。
- [Active V3 ledger](../_sources/daily-20260512/V3_AUTHOR_REBUILD_LEDGER.json)。
- [Evidence reviews](../_sources/daily-20260512/V3_AUTHOR_EVIDENCE_REVIEWS.json)。
- [Books comparison](../_sources/daily-20260512/V3_AUTHOR_BOOKS_COMPARISON.json)。
