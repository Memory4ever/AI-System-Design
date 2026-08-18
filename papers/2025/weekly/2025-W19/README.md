# AI Research Weekly — 2025-W19

> Coverage Window: 2025-05-05～2025-05-11
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-24
> Audit Status: Discovery and Candidate Evidence Gate Passed
> Historical Books Gate: Closed

## Executive Summary

原档案把本周写成“0 个候选”的空周；重新按事件日期回放后，这一结论不成立。本轮最终定位 **27 个唯一 owner Source Family**，全部完成身份、事件日期、revision、六维评分与 disposition：26 个达到 `20+` 并完成非模板化 Full Source Review，1 个低分完成可信 closure。`Review Pending = 0`、`Unverified / Blocked = 0`、`Disputed = 0`。Candidate Evidence Gate 已通过；Historical Books Gate 仍按年度规则关闭，本周不修改 Books。

本周形成六条可追踪演进线：多模态从离线整段输入走向流式 memory / activation 分权；评测从任务平均分走向跨任务、跨范式与跨模态的覆盖/协同约束；后训练把 reward reasoning、统一 reasoner-verifier 与可控预算纳入策略状态；可验证 RL 从人工题库走向 environment-grounded curriculum；长上下文 KV 从分页/稀疏选择走向 attention-aware vector storage；检索与代码 Agent 则分别把训练 simulator 与真实 evidence、repository retrieve 与 patch verification 分开。所有结论均保留作者实验与产品公开边界，不外推为生产通用事实。

## Coverage Window and Limitations

- owner week 由 official event date 或 arXiv v1 first-public date 决定；后续 revision 只记录演进节点，不重复计分。
- 固定机构顺序、arXiv first-public metadata、论文项目页/代码入口与 AI Infra release/tag 日期已重放；Scholar/OpenAlex/DBLP/Crossref 只用于身份与去重交叉检验，不把搜索摘要当正文证据。
- 固定 AI Infra 在窗口内没有形成新的 owner mechanism event；vLLM `v0.8.5.post1` 的 2025-05-02 release 留在 W18，SGLang `v0.4.5` 在 W15，Transformers 下一次机制性 minor release 与 KServe `v0.15.1` 均进入 W20。W19 不重复计分。
- 26 个 `20+` family 均覆盖 event-time source 的 Method/contract、state/data/control flow、implementation、evaluation、ablation/sensitivity/overhead、limitations 与可取得 artifact；未公开 workload 字段逐项写 `Not Disclosed`。
- 历史回填不补造 Daily；性能结论必须绑定模型、硬件、精度、长度、batch、并发和 SLO，未公开字段写 `Not Disclosed`。

## 1. 模型与研究机构

按固定机构顺序重放官方发布。最终 owner 候选为 Gemini 2.5 Pro I/O preview、Anthropic Web Search API 和 Anthropic AI for Science Program；其余固定机构在窗口内未形成可唯一定位的新 owner event。产品条目只证明公开行为，未披露的训练与 runtime 机制保持未知。

## 2. 论文与学术来源

最终发现 24 个 owner 论文 family，全部按 event-time v1 完成全文审计；后续 revision 仅记录为 family evolution node，不倒灌为 v1 机制证据。

## 3. AI Infra 与工程项目

固定工程项目的 Release / RFC / PR 日期扫描已闭合。窗口内未出现达到独立 owner 条件的 AI Infra 事件；相邻周 release 只记录 dedup 边界，不回填为 W19 新事件。

## Candidate Scoring

| Candidate / Source Family | Event Date / Primary ID | TN | SI | PV | SR | PR | L | Total | Evidence / Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemini 2.5 Pro I/O Preview update | 2025-05-06 / official | 2 | 3 | 4 | 5 | 4 | 2 | 20/30 | Full Source Review Complete — Weekly Only / Mechanism Not Disclosed |
| Anthropic Web Search API | 2025-05-07 / official | 3 | 4 | 5 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Books Pending |
| Anthropic AI for Science Program | 2025-05-05 / official | 1 | 2 | 2 | 5 | 2 | 2 | 14/30 | Low-score closure — Program Fact |
| Voila | 2025-05-05 / 2505.02707v1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Books Pending |
| LLaMA-Omni 2 | 2025-05-05 / 2505.02625v1 | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Full Source Review Complete — Books Pending |
| RM-R1 | 2025-05-05 / 2505.02387v1 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — revision-sensitive |
| FormalMATH | 2025-05-05 / 2505.02735v1 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Books Pending |
| R1-Reward | 2025-05-05 / 2505.02835v1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Books Pending |
| RetroInfer | 2025-05-05 / 2505.02922v1 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review Complete |
| ReplaceMe | 2025-05-05 / 2505.02819v1 | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Full Source Review Complete — Books Pending |
| Absolute Zero | 2025-05-06 / 2505.03335v1 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Source Review Complete |
| VITA-Audio | 2025-05-06 / 2505.03739v1 | 4 | 4 | 5 | 4 | 4 | 4 | 25/30 | Full Source Review Complete — Books Pending |
| OpenHelix | 2025-05-06 / 2505.03912v1 | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Books Pending |
| OSUniverse | 2025-05-06 / 2505.03570v1 | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Source Review Complete — Books Pending |
| X-Reasoner | 2025-05-06 / 2505.03981v1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Books Pending |
| ZeroSearch | 2025-05-07 / 2505.04588v1 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Source Review Complete |
| HunyuanCustom | 2025-05-07 / 2505.04512v1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Books Pending |
| OpenVision | 2025-05-07 / 2505.04601v1 | 4 | 4 | 5 | 4 | 4 | 5 | 26/30 | Full Source Review Complete — Books Pending |
| General-Level / General-Bench | 2025-05-07 / 2505.04620v1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| RL^V | 2025-05-07 / 2505.04842v1 | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Full Source Review Complete — Books Pending |
| SweRank | 2025-05-07 / 2505.07849v1 | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | Full Source Review Complete — W20 chronology correction |
| Flow-GRPO | 2025-05-08 / 2505.05470v1 | 5 | 4 | 4 | 4 | 4 | 5 | 26/30 | Full Source Review Complete |
| Elastic Reasoning | 2025-05-08 / 2505.05315v1 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — Books Pending |
| ICon: In-Context Contribution | 2025-05-08 / 2505.05327v1 | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Source Review Complete — identity corrected; Books Pending |
| StreamBridge | 2025-05-08 / 2505.05467v1 | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review Complete — Books Pending |
| Toxicity in LLaVA pretraining data | 2025-05-09 / 2505.06356v1 | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Full Source Review Complete — Emerging / Experimental |
| Seed1.5-VL Technical Report | 2025-05-11 / 2505.07062v1 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Books Pending |

账目：27 个 scored owner rows；26 个 `20+`、1 个低分；26/26 strict Full Source Review、1/1 low-score closure；Review Pending 0、Blocked 0、Disputed 0。六维总分由机器复算，均与 `Total` 列一致。

## Full Source Review

### Absolute Zero — environment-grounded self-proposed curriculum

- **Identity / coverage**：`absolute-zero-reasoner-2505.03335`；v1 2025-05-06，v2 05-07，v3 10-16。本 packet 只使用 v1 的 metadata、Method、公式、Algorithm、implementation、evaluation、ablation、Appendix B–D 和 discussion。
- **Problem / previous design / changed constraint**：RLVR 不再需要 rationale label，却仍依赖人工题目与答案分布。专家题库和 verifier 语义稳定、易比较、便于设安全边界；变化的约束是可验证任务供给成为扩展瓶颈。
- **Mechanism / ownership / flow**：同一 policy 以 prompt 区分 proposer 与 solver。proposer 围绕 program/input/output 构造 deduction、abduction、induction；executor 校验或补全 ground truth；solver rollout 后由执行结果给二值 reward；proposer reward 用 solver Monte Carlo 成功率近似 learnability；TRR++ 联合更新，buffer 保存历史 curriculum。控制流为 `sample → propose → execute/validate → solve → verify → reward both roles → update → evolve buffer`。
- **Implementation / evaluation**：veRL 与 QwQ Python executor；Qwen2.5 3B/7B/14B、Llama-3.1-8B；A800 数量未披露，batch `64×6`，prompt/response 上限 6144/8096，LR `1e-6`，500 steps；precision、并发、SLO 未披露。评测含 HumanEval+、MBPP+、LiveCodeBench v5、AIME24/25、AMC23、MATH500、Minerva、OlympiadBench，并做任务类型、proposer、规模和 base/coder ablation。
- **Evidence boundary / trade-offs**：证明作者代码执行环境中，自生成 curriculum 可优于所列 baselines 并迁移到部分数学/代码任务；不证明零预训练数据、无人工 environment specification、通用自改进或生产安全。新增 proposer compute、sandbox、难度估计、specification exploit、curriculum drift、buffer collapse 与 policy/verifier 共适应。
- **Owner / coexistence / disposition**：开放式、安全关键任务仍需专家题库和独立 verifier。Owner `TRAIN-GRPO`，Ch33 / Legacy Ch29；Ch32、Ch34 已读。Books Pending — `Refine — Existing Argument` 候选。

### RetroInfer — attention-aware vector storage for long-context KV

- **Identity / coverage**：`retroinfer-wave-kv-storage-2505.02922`；v1 2025-05-05；已读 architecture、index/buffer algorithms、CUDA/Triton implementation、evaluation、sensitivity 与 overhead。
- **Problem / previous design**：长上下文 KV 线性增长，decode 扫描全部 KV；稀疏 offload 又引入检索和 PCIe 搬运。GPU-resident full attention 精确、简单，在短上下文和小 batch 下仍是正确基线。
- **Mechanism / ownership / flow**：wave index 对 KV segment 聚类；GPU meta-index 保存 centroid 与 `sum(V)`；tripartite attention 对检索块精确计算、非检索块估算并聚合；wave buffer 异步协调 CPU 完整 KV/block mapping、GPU meta-index、hot cache 和 execution buffer。decode query 驱动 cluster selection、block fetch、exact/estimated merge 与 async update。
- **Implementation / evaluation**：Triton segmented k-means、约 1000 LoC CUDA copy/update kernel、修改 FlashAttention。单 A100 80GB、EPYC 7V12、1.9TB RAM、PCIe4 x16、CUDA12.4、PyTorch2.4；Llama-3.1-8B、Qwen2.5-7B、Llama-3-8B-1048K；RULER/LongBench；比较 FlashInfer、Quest、MagicPIG、InfiniGen，并扫描 60K～1M context、batch、retrieval budget、1%～5% GPU cache、segment size 和 async update。precision、output length、生产并发/SLO 未披露。
- **Evidence boundary / trade-offs**：只证明上述单机合同内的作者结果；不证明通用 exactness、多 GPU/fleet、公平性或故障恢复。新增 index cost、近似误差、CPU/NUMA/PCIe 压力、mapping staleness、异步 race 与碎片。
- **Owner / disposition**：`INFER-KV-CACHE`，Ch45 / Legacy Ch41；Ch44、Ch46 已读。Books Pending — `Integrate — New Mechanism` 候选。

### ZeroSearch — simulated training environment, real deployment evidence

- **Identity / coverage**：`zerosearch-simulated-search-2505.04588`；v1 2025-05-07；已读 Method、训练协议、implementation、evaluation、ablation 与 limitations。
- **Problem / previous design**：在线 search RL 的 API 成本与 nondeterminism 使训练难复现。live search 适合 freshness；固定 corpus/retriever 适合可审计训练。
- **Mechanism / ownership / flow**：先 SFT 冻结 LLM 作为 retrieval simulator；policy 在 think/search/information/answer 协议中多轮交互；curriculum 逐步降低 simulated document quality；GRPO/PPO 依据 answer F1 更新。训练时 simulator 持有文档响应，部署时切换 SerpAPI；policy 保存 query/action trajectory，trainer 保存 curriculum、reward 与 policy version。
- **Evaluation**：Qwen2.5 3B/7B/14B simulator；Qwen2.5 与 Llama-3.2-3B policy；NQ/HotpotQA 训练，评测扩展到 TriviaQA、PopQA、2Wiki、Musique、Bamboogle；比较 Direct、CoT、RAG、RA-Agent、Search-o1、R1、Search-R1；扫描 simulator size、turns、PPO/GRPO、reverse curriculum 和 loss masking。除作者披露的单 A100 约 12h 外，多数 workload 字段未披露。
- **Evidence boundary / trade-offs**：不证明 simulator 可替代真实搜索、citation/freshness 正确、企业检索或普遍消除 hallucination。节省 API 成本但引入 simulator bias、格式 exploitation、F1 shortcut 与 train/deploy distribution shift。
- **Owner / coexistence / disposition**：需要 freshness 时仍用 live search，需要审计时仍用固定 corpus。Owner `AGENT-RAG` Ch76 / Legacy Ch72，handoff `TRAIN-GRPO` Ch33；Ch75、Ch77 已读。Books Pending — `Refine — Existing Argument` 候选。

### Flow-GRPO — stochastic training branch for deterministic flow models

- **Identity / coverage**：`flow-grpo-2505.05470`；v1 2025-05-08；已读 ODE-to-SDE derivation、MDP、implementation、evaluation、ablation、sensitivity 与 discussion。
- **Problem / previous design**：确定性 probability-flow ODE 没有在线 policy gradient 需要的 stochastic transition 与 tractable log probability。无需在线 RL 时，ODE sampling 高效且可复现；offline preference/distillation 也避开奖励不稳定。
- **Mechanism / ownership / flow**：将 denoising 表示为 MDP，把 probability-flow ODE 转成同 marginal 的 reverse SDE，再用 Euler–Maruyama 得到 stochastic policy；终局 scorer 产生 group-relative reward，GRPO 更新；训练减少 denoising steps，推理恢复默认 sampler。state 为 `x_t + timestep + prompt`，action 为 `x_(t-1)`。
- **Evaluation**：SD3.5-M；训练10 steps、默认推理40 steps；GenEval、OCR/text rendering、PickScore、DrawBench 与多种 reward model；24×A800。扫描 steps、noise `a=0.1～1.0`、KL/no-KL、reward hacking 与 diversity；precision、batch、并发、SLO 未披露。
- **Evidence boundary / trade-offs**：只证明作者 flow-matching model/scorer 合同；不证明所有 diffusion/flow 模型、真实人类偏好或生产性能。新增 exploration-quality collapse、train/inference mismatch、scorer overfit、diversity collapse 和 sampler-version compatibility。
- **Owner / disposition**：`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff `TRAIN-GRPO` Ch33；相邻 Ch23/25、Ch32/34 已读。Books Pending — `Refine — Existing Argument` 候选。

### SweRank — issue-conditioned repository localization

- **Identity / coverage**：`swerank-2505.07849`；v1 2025-05-07。W20 replay 曾按读取日期误归 W20，本次按 first-public date 回拨 W19；已读 event-time Method、training pairs、two-stage ranking、evaluation 与 repository artifact 入口。
- **Problem / previous design / changed constraint**：代码 Agent 逐步浏览 repository 通用但 token 与 tool-call 成本随代码库增长；generic code retriever 便宜，却难把冗长 issue、failure description 与实际修改位置对齐。约束变化是 SWE issue 与真实 changed files 可以组成 supervision，使 localization 成为独立、可评测的前置阶段。
- **Mechanism / ownership / flow**：SweLoc 从 issue 到 actual modifications 构造训练对；先 retrieve file/function candidates，再 rerank。repository index 拥有 code snapshot，retriever 只产生候选集合，reranker拥有排序 state，coding Agent 或人工 reviewer 才拥有最终修改与验证权。
- **Evaluation / evidence boundary**：作者在 SWE-Bench-Lite、LocBench 及所列 retriever/closed-agent baselines 上报告 localization 改善；这证明 issue-conditioned ranking 在这些 repositories 中缩小搜索空间，不证明 patch correctness、训练 repository 无 leakage，亦不证明 ranking 可以替代 Agent exploration 或 executable tests。
- **Trade-off / coexistence / owner**：新增 index freshness、changed-file label bias、跨 revision identity 与 reranker compute；小 repository、明确 stack trace 或已知 symbol 时直接 search 仍更简单。Owner `AGENT-RAG` Ch76，handoff `AGENT-TOOL-CALLING` Ch78；Books Pending — `Refine — Existing Argument` 候选。

### Gemini 2.5 Pro I/O Preview update — product capability without disclosed mechanism

- **Candidate / Week / Score; identity:** Gemini 2.5 Pro I/O Preview update / W19 / 20；`gemini-2.5-pro-io-preview-2025-05-06`，official product announcement，2025-05-06 first public，无可核验的独立 technical/system card revision。
- **Direct / related sources; access / coverage:** 已读官方公告、可用入口与所列 benchmark context；公告未公开 architecture、training、routing、serving 或 safety mechanism，故 Full-read coverage 仅能闭合 product contract，不能制造论文级机制。
- **Problem / previous design / changed constraint:** 旧版 2.5 Pro 已覆盖 coding 与 multimodal reasoning；本次变化是面向 interactive web-app、code transformation/editing 与 agentic workflow 的 preview 行为更新。preview 快速暴露能力有利于反馈，但版本可变且 contract 较弱。
- **Mechanism; state ownership; control/data flow; implementation:** Google 只披露新 preview 经 Gemini API、AI Studio、Vertex AI 与 Gemini app 暴露；模型参数、训练数据、推理控制流、缓存与调度均 `Not Disclosed`，不得从产品输出反推。
- **Evaluation contract / baselines / workload:** 公告给出 WebDev Arena 相对旧版 `+147 Elo`、VideoMME `84.8%`；human preference、prompt distribution、hardware、precision、length、batch、concurrency 与 SLO 未完整披露，因此只证明该公开 evaluation snapshot。
- **Proves / does not prove / limitations / trade-offs:** 证明 05-06 存在可调用 preview 与官方宣称的行为变化；不证明通用 coding 优越、生产稳定性或内部机制。收益是更早可用，代价是 preview drift、可复现性和供应商依赖。
- **Evolution / owner / adjacent chapters / disposition / open question:** `previous preview → I/O preview → later stable release` 是版本演进而非新机制。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，Ch65/67 已核对；现有 Books 只需保留“版本行为不能替代机制证据”。`Weekly Only — Version/Product Fact / Mechanism Not Disclosed`；不改仓库其他文件。开放问题是稳定版是否提供可复现实验与 system card。

### Anthropic Web Search API — server tool contract for fresh evidence

- **Candidate / Week / Score; identity:** Anthropic Web Search API / W19 / 26；`anthropic-web-search-api-2025-05-07`，official announcement + event-time API docs，2025-05-07 first public；09-10 的 web-fetch update 是后续 node。
- **Direct / related sources; access / coverage:** 已读公告及 `web_search_20250305` 文档的 tool definition、request/response blocks、citations、domain policy、usage、errors 与 server-side loop；后来的 dynamic filtering 字段只作 revision 对照，不倒灌。
- **Problem / previous design / changed constraint:** 模型权重内知识稳定且低延迟，但遇到 freshness 或专门知识会过期；应用自建检索可控却要维护 crawler/index。新约束要求 API 内可审计地获取当下 evidence。
- **Mechanism / ownership / flow:** application 提交 tool policy；Claude 决定是否搜索并生成 query；Anthropic server tool 返回 result blocks；模型综合并生成带 source citation 的最终响应。应用拥有 allow/block domain 与 `max_uses`；服务拥有搜索执行；模型拥有 query/answer；原站拥有事实，citation 不转移事实所有权。
- **Implementation / evaluation / workload:** event-time type 为 `web_search_20250305`，支持 `max_uses`、domain allow/block、approximate location；错误作为 tool-result error，成功响应带 encrypted result/citation state。公告覆盖 Claude 3.7 Sonnet、upgraded 3.5 Sonnet、3.5 Haiku，价格为每千次搜索另计；hardware、precision、检索 backend、recall、latency/SLO 未披露。
- **Proves / does not prove / limitations:** 证明 server-side freshness/citation/control contract 已公开；不证明引用蕴含 claim、source 可靠、检索完整或生成无幻觉。引用正确性仍需 claim-evidence verifier。
- **Trade-offs / failure modes / coexistence:** 免自建 index，但引入搜索费用、网络/限流、source drift、prompt injection、domain-policy误配、max-use exhaustion 与不可见 ranking。稳定私有 corpus 仍更适合自管 RAG；开放 freshness 才使用 web search。
- **Evolution / owner / adjacent / disposition / open questions:** `closed-book → client-managed RAG → managed server search with citations`。Owner `AGENT-TOOL-CALLING` Ch78，handoff `AGENT-RAG` Ch76；Ch76/77/79 已读。Books Pending — `Refine — Existing Argument`；不改其他文件。待验证 event-time citation precision、latency tail 与失败重试语义。

### Voila — hierarchical voice tokens and full-duplex role separation

- **Candidate / Week / Score; identity:** Voila / W19 / 24；`voila-voice-language-foundation-2505.02707`，arXiv v1 2025-05-05，论文、项目/模型/benchmark 入口可访问。
- **Access / full-read coverage:** 已读 metadata、Introduction/Related Work、voice tokenizer、hierarchical transformer、alignment/autonomous interaction、implementation、ASR/TTS/interaction evaluation、ablation、Appendix 与 artifact说明。
- **Problem / previous / changed constraint:** cascade ASR→LLM→TTS 可分别优化、易审计，但丢失 prosody/speaker 状态并累加 latency；变化是单模型需同时理解与生成 voice，并允许用户与模型重叠发言。
- **Mechanism / state / flow:** 四层 RVQ 把首层作为 semantic、其余作为 acoustic token；backbone LLM 处理语义，audio transformer补声学细节；word-level text/audio interleave 对齐。autonomous 模式为用户/模型两路 audio stream，编码后平均融合；speaker embedding控制声音 identity。
- **Implementation / evaluation:** tokenizer 用约100K小时音频；作者报告约195ms response latency、预建/十秒定制 voice；ASR、TTS、spoken interaction 与 role-play 基准及相关 ablation。精确 GPU、precision、batch、并发和 production SLO `Not Disclosed`。
- **Proves / does not / limitations:** 证明分层 token 与显式双流在作者合同内兼顾语义、音质与交互；不证明百万 voice 的身份安全、真实噪声环境稳定或生产端到端尾延迟。
- **Trade-offs / coexistence / failure:** 减少 cascade 边界却增加 codec error propagation、speaker spoofing、两路串扰、连续监听 privacy 与 interruption arbitration；高可控企业流程仍可选择 cascade。
- **Evolution / owner / adjacent / disposition / open:** `speech cascade → shared semantic/acoustic token space → dual-stream autonomous interaction`。Owner `MULTIMODAL-REPRESENTATION` Ch23，Ch22/24 与 Ch26 已读。Books Pending — `Refine — Existing Argument`；不改其他文件。开放问题是 duplex overlap 下的 turn-taking 与 voice provenance。

### LLaMA-Omni 2 — gated speech/text state with causal-flow chunks

- **Candidate / Week / Score; identity:** LLaMA-Omni 2 / W19 / 22；`llama-omni-2-2505.02625`，arXiv v1 2025-05-05，event-time paper/artifact 已核验。
- **Access / coverage:** 全文覆盖 speech encoder/adapter、gate fusion、Read-R/Write-W stream、causal flow matching TTS、两阶段训练、SpokenQA/ASR/TTS evaluation、ablation 与 limitations。
- **Problem / previous / changed constraint:** 首代端到端 speech model 可同步输出，但只依赖 LLM hidden state 传声学条件会损失显式 lexical identity；实时场景又要求按 chunk 交错听/说。
- **Mechanism / state / flow:** gate 在 LLM hidden projection 与 text-token embedding 之间融合；TTS 用 causal flow matching 逐 chunk 生成；Read-R/Write-W 保存已读 speech 与已写 audio frontier。输入 speech→encoder/adapter→LLM text+semantic state→gate→TTS；文本与语音并发输出。
- **Implementation / evaluation:** 200K multi-turn S2S；stage I 分别训练 speech adapter/LLM 与 TTS，stage II 冻结 encoder/adapter/LLM 后训练 gate+TTS。评测 SpokenQA、instruction following、WER、UTMOS，与 LLaMA-Omni/GLM-4-Voice 比较；gate、embedding、TTS pretraining、R/W ratio、0.5B–14B ablation；单 NVIDIA L40 latency，7B R3/W10 约583ms。precision/batch/concurrency/SLO未披露。
- **Proves / does not / limitations:** 证明 gate 与 chunk policy 在该数据/模型上改善作者指标；不证明自然对话安全、任意语言/口音、持续 duplex 或通用低延迟。论文承认 emotion/rate 控制不足与 LLM hallucination。
- **Trade-offs / coexistence / owner:** chunk 提前输出降低等待，却使语义未完成时不可逆 audio commit；gate 增状态与训练阶段。高准确转写仍可用 cascade。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch42 streaming lifecycle；Ch22/24 已读。Books Pending — `Refine — Existing Argument`；开放问题是语音 rollback 与 commit boundary。

### RM-R1 — reasoning traces as a reward-model interface

- **Candidate / Week / Score; identity:** RM-R1 / W19 / 25；`rm-r1-2505.02387`，v1 2025-05-05；v2 05-15、v3 05-18、v4 2026-03-06 仅作 revision node。
- **Access / coverage:** 已读 v1 chain-of-rubrics method、distillation/GRPO、data cleaning、RewardBench/RM-Bench/RMB、baselines、ablation 与 failure analysis。
- **Problem / previous / changed constraint:** scalar reward head 快且便宜，但难解释为何偏好 A；直接让 LLM judge 可解释，却可能只生成流畅理由。新约束是 reward 不仅给分，还输出可检查 rubric reasoning。
- **Mechanism / ownership / flow:** teacher trace形成 cold start；generative RM 先产生 task-specific rubrics/analysis，再输出 preference；GRPO 用 correctness/preference reward 更新。training data owner 保存 response pair、rubric、label 与 provenance；reward policy 拥有 trace，trainer只消费最终 signal。
- **Implementation / evaluation:** Skywork Reward Preference 80K 中移除约30% `magpie_ultra` 以避免格式捷径，并加入约8K code preference；比较 scalar/generative RM，在三类 reward benchmark 上评估。hardware、precision、length、batch、concurrency/SLO `Not Disclosed`。
- **Proves / does not / limitations:** 证明在所列 benchmark 中 reasoning-style RM 可提升作者指标与表面可解释性；不证明 chain-of-rubrics faithful、无 preference leakage 或能替代 calibrated evaluator。
- **Trade-offs / coexistence / failure:** 增加 inference token/cost、rubric hallucination、position/style shortcut 与 reward hacking。高吞吐过滤仍适合 scalar RM；高风险样本可用 reasoning RM + external verifier。
- **Evolution / owner / adjacent / disposition / open:** `scalar score → generative judgment → rubric-conditioned judgment + RL`。Owner `TRAIN-RLHF` Ch31，handoff `PLATFORM-EVALUATION-SYSTEM` Ch66；Ch30/32 已读。Books Pending — `Refine — Existing Argument`；待验证 trace faithfulness 与 calibration。

### FormalMATH — executable proof as the evaluation contract

- **Candidate / Week / Score; identity:** FormalMATH / W19 / 26；`formalmath-lean4-2505.02735`，arXiv v1 2025-05-05，dataset/Lean artifact入口已核验。
- **Access / coverage:** 已读 autoformalization、negation disproof、人审、数据统计、theorem-prover protocols、budget sensitivity、domain/tactic analysis 与 Appendix。
- **Problem / previous / changed constraint:** natural-language math judge 容易把风格当正确性；Lean compilation 可执行、可复现，但 formalization 本身可能改题。新约束是同时验证 statement fidelity 与 proof correctness。
- **Mechanism / ownership / flow:** 多 LLM 生成 Lean statement→compiler验证语法/类型→negation-based disproof排除明显语义错误→12名 IMO-medalist level reviewers 核对原题与形式化→发布 statement；proof system 在固定 search budget 下产 proof，Lean kernel最终裁决。
- **Implementation / evaluation:** 5,560 statements，原始到有效约21.7%，最终 human preservation 72.09%，作者报告约$6.89/statement、22天。比较 BFS/single-pass provers；FormalMATH-Lite 扫到 Pass@3200，并分析 domain/tactic shortcut。hardware/precision/batch/concurrency/SLO未披露。
- **Proves / does not / limitations:** 证明可建立更强 executable contract；Lean 接受只证明形式化命题，不自动证明它忠实于原始自然语言，也不排除 contamination/library bias。
- **Trade-offs / coexistence / failure:** verification 强但构建贵，引入 formalizer error、library/version identity、tactic shortcut 与预算敏感性；开放式推导仍需人审/语义 judge。
- **Evolution / owner / adjacent / disposition / open:** `answer matching → model judge → formal statement + trusted kernel`。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff `TRAIN-GRPO`；Ch65/67 已读。Books Pending — `Integrate — New Mechanism`；待验证跨 Lean 版本可复现与 contamination audit。

### R1-Reward — stabilizing multimodal reward-model RL

- **Candidate / Week / Score; identity:** R1-Reward / W19 / 24；`r1-reward-stablereinforce-2505.02835`，v1 2025-05-05，v2 05-09 为同 family revision。
- **Access / coverage:** 已读 StableReinforce objective、reward decomposition、200K data construction、training/evaluation、voting、stability ablations 与 Appendix。
- **Problem / previous / changed constraint:** PPO/Reinforce++ 在 log-ratio exponent 与 near-uniform group reward 下会 overflow 或让 z-normalized advantage 放大噪声；视觉偏好还要求 reasoning 与最终 choice 一致。
- **Mechanism / state / flow:** 先把 probability ratio clip 到 `[1e-3,1e3]` 再 exponentiate；对 advantage 做 three-sigma filter。reward 由 format、result 与 Qwen2.5-VL-7B referee 的 reasoning consistency 组成，并采用乘法约束，只有结果正确时 consistency 才加分。
- **Implementation / evaluation:** 约200K multimodal preference，GPT-4o生成 reasoning cold start/难度；MM-RLHF Reward Bench、VL Reward-Bench、Multimodal Reward Bench，voting@5/15；比较 PPO/Reinforce++并做各稳定项、reward项 ablation。hardware、precision、length、batch、concurrency/SLO未披露。
- **Proves / does not / limitations:** 证明数值防护和 reward composition 在作者配置中减少 collapse、改善 benchmark；不证明 referee 公正、reasoning faithful 或稳定规则跨模型普适。
- **Trade-offs / coexistence / failure:** clip/filter牺牲极端样本 signal，乘法 reward 可能稀疏，referee 产生 correlated bias；低方差任务仍可用简单 preference loss。
- **Evolution / owner / adjacent / disposition / open:** `scalar preference → multimodal reasoning reward → numerically guarded online RL`。Owner `TRAIN-RLHF` Ch31，handoff `TRAIN-GRPO` Ch33；Ch30/32/33 已读。Books Pending — `Refine — Existing Argument`；开放问题是独立 human calibration。

### ReplaceMe — structural layer removal with learned replacement

- **Candidate / Week / Score; identity:** ReplaceMe / W19 / 25；`replaceme-layer-pruning-2505.02819`，v1 2025-05-05；v2 05-08、v3 06-20、v4 2026-02-19 为 revision。
- **Access / coverage:** 已读 block selection、least-squares/cosine fitting、merge rule、multi-LT、calibration、LLM/CLIP evaluation、regularization/mask/optimizer ablations。
- **Problem / previous / changed constraint:** unstructured pruning 保留函数细度，却依赖稀疏 kernel；直接删层结构简单，但误差大。目标是在普通 dense runtime 上获得真实 depth reduction。
- **Mechanism / ownership / flow:** 用 cosine distance 选影响小的连续 block；在 calibration activation 上拟合 linear transformation `T` 近似被删 block；把 `T` 合入前一 FFN 第二层权重，因此部署 artifact 只表现为少层模型，不新增 runtime op。multi-LT要求区间不重叠。
- **Implementation / evaluation:** training-free calibration（约1K/8K样本设置），Llama3-8B family 与 CLIP-L/14；比较直接 layer pruning、其他压缩方法，扫描 block位置、距离、正则、mask、optimizer 与压缩率，报告 perplexity/accuracy。hardware、precision、batch、concurrency/SLO未披露。
- **Proves / does not / limitations:** 证明在所测模型/校准集上 learned linear replacement 优于直接删除；不证明高压缩、分布漂移、量化后或任意 architecture 等价。
- **Trade-offs / coexistence / failure:** 结构执行简单但改变 artifact identity，可能出现 calibration overfit、长尾能力损失与 perplexity/任务指标背离；有高效 sparse hardware 时 unstructured branch 仍成立。
- **Evolution / owner / adjacent / disposition / open:** `unstructured sparsity → direct layer deletion → deletion + offline linear compensation`。Owner `INFER-TENSORRT-LLM` Ch49，handoff Model Transformer；Ch48/50 已读。Books Pending — `Integrate — New Mechanism`；待验证量化/编译融合与回归 gate。

### VITA-Audio — multi-token acoustic prediction over a preserved text backbone

- **Candidate / Week / Score; identity:** VITA-Audio / W19 / 25；`vita-audio-mctp-2505.03739`，v1 2025-05-06；v2 2025-10-21 是 revision。
- **Access / coverage:** 已读 interleaved representation、MCTP、四阶段训练、ASR/TTS/QA evaluation、Vanilla/Turbo与模块数量 ablation、implementation。
- **Problem / previous / changed constraint:** 单 audio-token 自回归保持依赖关系却太慢；独立 speech stack 快但破坏 LLM text knowledge。目标是在保留 backbone 行为下并行生成多枚声学 token。
- **Mechanism / state / flow:** interleaved audio-text 输入保留 text LM；每个 MCTP 读取 LLM hidden state 与 text embedding，逐级预测一组 audio token；单次 backbone forward 触发多个轻量 module，形成约10 token audio block。
- **Implementation / evaluation:** 10 个 MCTP，单 module 作者测约0.0024s、约backbone 11%；四阶段为 alignment→single MCTP→multiple MCTP→SFT。0.5B/7B/72B，较 Vanilla 作者报告 Turbo 4.56–6.46× token speed；ASR、TTS、spoken QA，1 GPU小模型/2 GPU 72B。GPU型号、precision、batch、并发/SLO未披露。
- **Proves / does not / limitations:** 证明多 token branch 可提高该实现生成速率并维持部分指标；不证明端到端低延迟或声学质量无损，Turbo WER存在退化。
- **Trade-offs / coexistence / failure:** 并行度换 token independence/error propagation，模块增显存与训练复杂度；高保真场景单 token branch 仍合理。
- **Evolution / owner / adjacent / disposition / open:** `single acoustic token → multi-token heads → staged parallel speech generation`。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff inference execution；Ch22/24 已读。Books Pending — `Refine — Existing Argument`；开放问题是 streaming commit 与错误恢复。

### OpenHelix — aligning slow semantic planning with fast embodied control

- **Candidate / Week / Score; identity:** OpenHelix / W19 / 23；`openhelix-dual-system-vla-2505.03912`，arXiv v1 2025-05-06，paper/code入口可访问。
- **Access / coverage:** 已读 dual-system taxonomy、latent interface、training/integration、CALVIN experiments、alignment/auxiliary-action ablations、async test 与 limitations。
- **Problem / previous / changed constraint:** 单 policy 的 perception-action loop 延迟低，但难承载语言规划；大 MLLM 语义强却无法高频闭环。变化是 high-level planning 与 low-level control 具有不同频率和 state schema。
- **Mechanism / ownership / flow:** LLaVA-7B high-level 通过 `<ACT>` latent 与 3D Diffuser Actor low-level连接；RGB-D/proprioception→高层语义/latent→projection→3D action diffusion→位置/旋转/gripper→环境反馈。MLLM冻结并 prompt tuning；先对齐 projection，再 fine-tune policy。
- **Implementation / evaluation:** CALVIN、CALVIN-E/D；比较 single-system RF 与3D Diffuser Actor、pretrained/scratch、freeze/fine-tune、CLIP alignment、auxiliary action prediction、sync/async。作者发现 `<ACT>` 易只含 instruction，辅助 action forcing 才注入视觉；测试中 async delay影响小但仅限该环境。hardware/precision/batch/SLO未披露。
- **Proves / does not / limitations:** 证明接口对齐是 dual-system 成败关键；不证明 real-robot、humanoid、安全或真实网络延迟，论文明确未做真机验证。
- **Trade-offs / coexistence / failure:** 分层复用强模型却增加 latent semantic mismatch、stale plan、控制频率错配与 emergency ownership；短任务可用单 policy。
- **Evolution / owner / adjacent / disposition / open:** `single policy → slow planner + fast controller → explicitly aligned latent contract`。Owner `MULTIMODAL-EMBODIED-VLA` Ch26，Ch25/27 已读。Books Pending — `Integrate — New Mechanism`；开放问题是真机安全 envelope 与 plan invalidation。

### OSUniverse — typed executable checks for desktop-agent tasks

- **Candidate / Week / Score; identity:** OSUniverse / W19 / 23；`osuniverse-desktop-agent-benchmark-2505.03570`，arXiv v1 2025-05-06，paper/environment artifacts可访问。
- **Access / coverage:** 已读 task construction、AgentDesk/Docker runner、TestCase schema、validator、人审、model configurations、cost/time结果与 Appendix。
- **Problem / previous / changed constraint:** final text judge 无法确认 GUI state；纯 screenshot judge 又可能忽略 hidden app state。需要把任务结果、执行轨迹与环境状态组合成 executable evidence。
- **Mechanism / ownership / flow:** YAML TestCase 声明 initial/desired state；runner执行 agent actions并保存 trajectory；checks 包括 ReturnedResult、FinalScreenshot、CommandOutput、ExpectedFlow；Gemini CoT validator聚合，Streamlit供人复核。环境拥有真实 state，test case拥有 contract，validator只拥有 judgment。
- **Implementation / evaluation:** 160任务，Paper/Wood/Bronze/Silver/Gold难度与加权分；8种 agent/config 多次运行，记录输入、成本、时长；作者称 automated validation平均 error低于2%。hardware、precision、屏幕延迟、并发/SLO未披露。
- **Proves / does not / limitations:** 证明 typed checks 比单一 final answer 提供更强 artifact；不证明 validator 无偏、task覆盖真实桌面分布或低错误率可迁移。
- **Trade-offs / coexistence / failure:** executable checks可审计，但 setup脆弱、GUI nondeterminism、validator correlated error 与环境版本漂移；简单 API task仍可用 deterministic assertion。
- **Evolution / owner / adjacent / disposition / open:** `final answer judge → screenshot judge → typed multi-artifact verifier`。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Agent workflow；Ch65/67 已读。Books Pending — `Refine — Existing Argument`；待验证 inter-rater agreement 与 environment reset。

### X-Reasoner — text reasoning as a constrained multimodal training branch

- **Candidate / Week / Score; identity:** X-Reasoner / W19 / 24；`x-reasoner-2505.03981`，arXiv v1 2025-05-06，event-time paper/code入口已核验。
- **Access / coverage:** 已读 long-CoT SFT、math RLVR、forced-exit、GRPO变化、training config、text/multimodal/domain evaluation 与 ablations。
- **Problem / previous / changed constraint:** domain-specific multimodal SFT最直接，但迁移窄；text-only reasoning数据便宜且可验证。问题是能否作为通用 reasoning anchor，又不让长 CoT 无限延伸。
- **Mechanism / state / flow:** OpenThoughts long-CoT SFT初始化；Orz 57K math RLVR；GRPO采用 clip-higher、token-level loss、弱/无 KL。rollout若达到 threshold则强制写 `</think>`，把 reasoning state切到 final answer。
- **Implementation / evaluation:** Qwen2.5-VL系模型；SFT 8×A100-40GB约8h，RLVR 32×A100-40GB约56h；3 epochs、LR `3e-6`、global batch128、8 rollouts、max 4096。覆盖 MMMU/MMMU-Pro/MathVista/MathVision及医学集，并剔除 text-solvable samples；比较 text、multimodal、domain branches。
- **Proves / does not / limitations:** 证明该模型/数据上 math RLVR可迁移部分视觉/领域 reasoning；不证明 text reasoning 普遍等价于视觉 grounding，domain data仍在域内更强。
- **Trade-offs / coexistence / failure:** 长 CoT增成本且约17% endless-thinking baseline需强制退出；forced exit可能截断正确推理，数学 reward可能偏置风格。视觉密集任务仍需 multimodal data。
- **Evolution / owner / adjacent / disposition / open:** `domain SFT → text reasoning anchor → bounded multimodal reasoning`。Owner `TRAIN-RLHF` Ch31，handoff `MULTIMODAL-REPRESENTATION`；Ch30/32 已读。Books Pending — `Refine — Existing Argument`；开放问题是 cross-modal gain 的因果来源。

### HunyuanCustom — decoupled identity, audio and motion conditioning

- **Candidate / Week / Score; identity:** HunyuanCustom / W19 / 24；`hunyuan-custom-video-2505.04512`，v1 2025-05-07、v2 05-08，同一 source family。
- **Access / coverage:** 已读 HunyuanVideo backbone、image/text fusion、ID enhancement、audio/video conditioning、data categories、evaluation与 ablations。
- **Problem / previous / changed constraint:** 单 text prompt不能稳定保持人物/主体 identity；把所有条件拼到同一 latent会互相覆盖。新约束是 identity、audio timing 与 motion reference需要独立控制。
- **Mechanism / state / flow:** LLaVA提取 image-text feature；ID image沿 temporal axis拼接增强身份；audio按 VAE temporal ratio对齐并以 frame-wise spatial cross-attention注入；reference video采用 addition而非 concat，保持 latent shape。各 conditioner拥有不同 identity/timestamp。
- **Implementation / evaluation:** 人/非人各约100 prompts；ArcFace、DINO、CLIP text-video、temporal consistency、dynamic degree与人评；比较开源/商业系统及 condition injection ablation。训练规模、GPU、precision、batch、并发/SLO未披露。
- **Proves / does not / limitations:** 证明解耦 conditioning在作者样本/代理指标中改善定制；不证明生物身份真实性、商业基线稳定或真实授权/隐私合规。
- **Trade-offs / coexistence / failure:** 控制更细却增加 condition冲突、身份泄漏、时间错位与指标 gaming；单主体文本生成仍可用 simpler text-only branch。
- **Evolution / owner / adjacent / disposition / open:** `text-only generation → reference concatenation → typed/decoupled conditioning`。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，Ch23/25 已读。Books Pending — `Refine — Existing Argument`；开放问题是 provenance/watermark 与 conflict arbitration。

### OpenVision — open vision-encoder scaling as a system contract

- **Candidate / Week / Score; identity:** OpenVision / W19 / 26；`openvision-encoder-family-2505.04601`，arXiv v1 2025-05-07，weights/data/recipes入口已核验。
- **Access / coverage:** 已读 family architecture、synthetic caption与 auxiliary decoder、resolution/data scaling、downstream LLaVA-style integration、classification/retrieval/VQA/OCR evaluation 与 ablation。
- **Problem / previous / changed constraint:** 闭源 encoder 强但训练 recipe 与 data provenance不可审计；单一 CLIP checkpoint又无法分离参数、数据、分辨率影响。需要开放 family 做受控 scaling。
- **Mechanism / state / flow:** 不同规模/分辨率 vision encoder产 patch representation，经 projector进入语言模型；synthetic caption与 auxiliary decoder提供训练信号；OpenVision-Smol把约150M LM与小encoder组合成低成本 branch。
- **Implementation / evaluation:** 最大 H/14约632.1M，含 B/S/Ti；扫描 Stage-2/3 data量、resolution与 learning rate；CLIP分类/检索及 TextVQA、ChartQA、OCR、MME、SEED、MMVet、SQA、GQA、POPE。hardware、precision、batch、并发/SLO未披露；高分辨率收益并非单调。
- **Proves / does not / limitations:** 证明开放 recipe支持较干净的 encoder/data/resolution比较；不证明任何规模最优、synthetic caption无偏或下游指标等价于通用视觉理解。
- **Trade-offs / coexistence / failure:** 更开放可审计但训练/存储昂贵，resolution增加 token与 serving成本；任务专用 encoder仍可能更优。
- **Evolution / owner / adjacent / disposition / open:** `single closed encoder → open scaling family → size/resolution/workload co-design`。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff `TRAIN-DATA` Ch27；Ch22/24/27 已读。Books Pending — `Integrate — New Mechanism`；待补各 recipe 的完整 carbon/hardware accounting。

### General-Level / General-Bench — breadth and synergy are different constructs

- **Candidate / Week / Score; identity:** General-Level / General-Bench / W19 / 24；`general-level-general-bench-2505.04620`，arXiv v1 2025-05-07，project/leaderboard/dataset repository已核验。
- **Access / coverage:** 已读 taxonomy、5-level definition、scoring relaxation、5-step construction、open/closed split、metric mapping、model evaluation、capability breakdown、Appendix task taxonomy与 limitations/discussion。
- **Problem / previous / changed constraint:** benchmark平均分奖励覆盖强项，不能区分“支持很多模态”与“跨任务知识产生协同”。真正反事实 synergy需分别训练 A、B、A+B，现成 foundation model无法廉价实现。
- **Mechanism / state / flow:** General-Level以 task→comprehension/generation→modality 三层聚合；无法测反事实时，放宽为“generalist zero-shot超过该任务 specialist threshold”作为 synergy proxy。General-Bench包含145 skills、702 tasks、325,876 instances，多模态原始格式，closed/open按2:3分离。
- **Implementation / evaluation:** 58类原始 metrics经 mapping标准化；测试172+102 systems，分 full/quick与更窄 scope。结果显示无模型 Level-5，且3D/生成覆盖弱。hardware、precision、prompt budget、并发/SLO跨闭源模型不可统一披露。
- **Proves / does not / limitations:** 证明广覆盖评测与层级 rubric可暴露 capability holes；“超过 specialist”并不因果证明知识迁移，可能来自预训练覆盖、metric mapping或旧 specialist。因此只能标为 synergy proxy。
- **Trade-offs / coexistence / failure:** 广度换来巨大运行成本、异质 metric不可比、leaderboard drift、contamination与closed-set维护压力；窄任务机制评测仍必需。
- **Evolution / owner / adjacent / disposition / open:** `single score → capability matrix → cross-task/paradigm/modality proxy`。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，Ch65/67 已读。`Emerging / Experimental`，Historical Books Gate关闭；不改其他文件。开放问题是如何用 intervention测真实 synergy 并校准 metric mapping。

### RL^V — reusing RL rollouts to train a unified verifier

- **Candidate / Week / Score; identity:** RL^V / W19 / 26；`rlv-unified-reasoner-verifier-2505.04842`，v1 2025-05-07；v2 2026-04-12 独立记录 revision。
- **Access / coverage:** 已读 value-free RL背景、generative verifier objective、joint loss、test-time selection、setup、generalization、head/objective ablations、Appendix与 limits。
- **Problem / previous / changed constraint:** GRPO/RLOO/VinePPO删 value network降低训练显存与计算，这是合理工程选择；但 test-time best-of-N又需 verifier，外置模型增加一份显存。
- **Mechanism / ownership / flow:** RL rollout自然产生 `(problem, solution, correctness)`；同一 LLM以 RL loss学 reasoner，以 SFT `Yes/No` next-token loss学 generative verifier，`J=J_RL+λJ_verify`。推理先采 N solutions，再取 `p(Yes|x,y,I)` 做 Best-of-N或按答案加权投票；policy/verifier共享参数但角色 prompt分离。
- **Implementation / evaluation:** Qwen2.5-Math 1.5B/7B、R1-Distill-Qwen-1.5B；MATH训练，MATH500/MATH2/GPQA Physics/AIME24；4×A100-80G约3h，short context1024、输出1024/2048；long-CoT每iteration 32题×5解、batch8、32 updates、40 epochs，SGLang inference。precision/production concurrency/SLO未披露。
- **Proves / does not / limitations:** 作者合同内显示 weighted voting/test-time compute更有效；`p(Yes)`只是模型条件概率，未证明 calibrated correctness，且 reasoner/verifier共享错误会相关。
- **Trade-offs / coexistence / failure:** 免额外模型显存但训练目标干扰、自证偏差、reward-label噪声与 sampling成本仍在；高风险场景仍需独立 verifier。
- **Evolution / owner / adjacent / disposition / open:** `PPO value head → value-free RL → shared generative verifier`。Owner `TRAIN-RLHF` Ch31，handoff `INFER-SPECULATIVE-DECODING`/Evaluation；Ch30/32/66 已读。Books Pending — `Integrate — New Mechanism`；开放问题是 verifier calibration 与 independence。

### Elastic Reasoning — reserve answer budget before scaling thought

- **Candidate / Week / Score; identity:** Elastic Reasoning / W19 / 26；`elastic-reasoning-budget-2505.05315`，v1 2025-05-08；v2 05-21 为 revision。
- **Access / coverage:** 已读 split-budget formulation、forced transition、budget-constrained GRPO、math/code setup、parallel/sequential baselines、budget ablations与 code availability声明。
- **Problem / previous / changed constraint:** 统一 max-token budget简单，却允许 reasoning耗尽所有 token，导致没有 final answer；固定短 CoT又损失难题能力。约束是有限总预算中必须保留提交空间。
- **Mechanism / state / flow:** 总预算 `c=t+s` 显式分 thinking与solution；thinking到 `t` 强制追加 `</think>`，solution保留 `s`；在固定 `(1K,1K)` rollout上用GRPO训练预算服从，推理接受未见 budget组合。
- **Implementation / evaluation:** DeepScaleR-1.5B、DeepCoder-14B；AIME、MATH500、LiveCodeBench、Codeforces、HumanEval+；比较 L1/budget baselines，扫描0.5/1/2/3K训练 budget与 thinking/solution贡献。event-time code under review；hardware、precision、batch、concurrency、wall-clock SLO未披露。
- **Proves / does not / limitations:** 证明显式 reserve在作者任务/预算下减少 answer truncation并改善 token efficiency；不证明强制边界能识别推理完成、跨模型普适或真实 latency收益。
- **Trade-offs / coexistence / failure:** 可控成本换截断正确思路、budget gaming与格式依赖；预算充足或自然短答任务无需复杂 controller。
- **Evolution / owner / adjacent / disposition / open:** `single token cap → fixed thought cap → two-account budget with forced handoff`。Owner `INFER-SCHEDULING` Ch56，handoff `TRAIN-GRPO`；Ch55与Platform入口已读。Books Pending — `Integrate — New Mechanism`；待验证以 wall-clock/energy而非 token计费。

### ICon — data value estimated through in-context contribution

- **Candidate / Week / Score; identity correction:** ICon: In-Context Contribution for Automatic Data Selection / W19 / 26；`icon-in-context-contribution-2505.05327`，v1 2025-05-08、v2 05-18。旧 ledger 的 `RICo` 是误名，本轮依据标题/ID纠正。
- **Access / coverage:** 已读 ICL contribution定义、assessment set、top-K labels、LoRA classifier、datasets/models、selection-scale curves、baselines、ablation与 limitations。
- **Problem / previous / changed constraint:** full fine-tuning逐样本估值准确但昂贵；perplexity/heuristic selector便宜却与目标能力脱节。需要低成本、target-aware proxy。
- **Mechanism / state / flow:** 在固定 assessment set 上，把 candidate 放入 context并测输出变化得到 contribution；以 top-K contribution构造 label，在 candidate representation上训练轻量 LoRA classifier；之后 O(m) 扫数据并选择训练集。assessment set拥有目标定义，selector拥有 score，trainer拥有最终 artifact。
- **Implementation / evaluation:** assessment 1,020（OpenOrca GPT-3.5/GPT-4与Dolly），候选 Alpaca/WizardLM；Llama3.1-8B、Qwen2.5-3B、Llama2-7B；3 epochs、Adam、LR `2e-5`、batch128；12 benchmark+5 pairwise；比较 full、PPL、Alpagasus、Deita、Superfilter，并扫1%–100%。hardware/precision/SLO未披露。
- **Proves / does not / limitations:** 证明 ICL proxy在所测 target/assessment/model上可选出较小有效子集；不证明 contribution是模型无关的内在数据价值，最佳比例随模型/数据变化。
- **Trade-offs / coexistence / failure:** 降低估值成本但高度依赖 assessment coverage，可能选到 prompt-format shortcut并放大目标偏差；无可靠 assessment时 diversity/quality heuristics仍必要。
- **Evolution / owner / adjacent / disposition / open:** `static quality score → gradient/influence estimate → ICL proxy + learned selector`。Owner `TRAIN-DATA` Ch27，Ch26/28 已读。Books Pending — `Integrate — New Mechanism`；开放问题是跨版本 selector drift与多目标覆盖。

### StreamBridge — streaming memory and response activation as separate state owners

- **Candidate / Week / Score; identity:** StreamBridge / W19 / 24；`streambridge-video-streaming-2505.05467`，v1 2025-05-08；v2 09-18 是 revision。
- **Access / coverage:** 已读 memory buffer、round-decayed compression、activation model、Stream-IT、settings/main results、in-depth analysis、implementation appendix、benchmarks、limitations与伪代码。
- **Problem / previous / changed constraint:** offline Video-LLM拥有整段视频，单次回答合理；直播输入无限增长，且系统必须决定“何时响应”，不能只解决“响应什么”。
- **Mechanism / state / flow:** frame encoder作为producer把 visual embedding与query/response append到 memory buffer；超过 MaxLen时从最早 round开始平均池化 visual token，保留近期高分辨率；并行0.5B activation model逐frame二分类，分数超过阈值才触发主LLM消费flattened buffer。memory owner与activation owner明确分离。
- **Implementation / evaluation:** 适配 LLaVA-OV、Oryx-1.5、Qwen2-VL；StreamingQA-120K来自约1.28M clips组合，平均>150s，含QA drop/interval shift；OVO-Bench、Streaming-Bench及离线视频基准，比较GPT-4o/Gemini等，并做buffer/compression/activation threshold分析。GPU、precision、batch、并发/端到端SLO未披露。
- **Proves / does not / limitations:** 证明插件式 memory+activation可在作者bench上把offline模型转为streaming；不证明真实无限流、严格实时或安全关键主动触发。论文承认数据合成、长时记忆损失与真实部署限制。
- **Trade-offs / coexistence / failure:** 避免重训 backbone，却引入旧帧信息损失、误触发/漏触发、buffer/response race与每帧activation成本；离线高精度任务仍应整段处理。
- **Evolution / owner / adjacent / disposition / open:** `offline full clip → causal buffer → decayed memory + decoupled activation`。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch25与 inference request lifecycle；Ch22/24/25 已读。Books Pending — `Integrate — New Mechanism`；开放问题是 event-time watermark、commit与rollback。

### Toxicity in LLaVA pretraining data — policy ensemble as a data gate

- **Candidate / Week / Score:** Understanding and Mitigating Toxicity in Image-Text Pretraining Datasets / W19 / 24；`llava-pretrain-toxicity-2505.06356`，arXiv v1 2025-05-09，后以 CVPR 2025 workshop paper公开。
- **Direct / related sources; access / coverage:** 已读 arXiv metadata、CVF正文的 dataset/method/results/future-work、filter pipeline与可取得 mitigated dataset说明；未发现 event-time commit可固定完整 artifact revision。
- **Problem / previous / changed constraint:** web-scale image-text数据覆盖广且便宜，但文本/图像分别可能含 hate、sexual content、harassment；只做关键词文本过滤看不到图像毒性。
- **Mechanism / ownership / flow:** 对约558K LLaVA pretrain pairs，Toxic-BERT以>80% threshold标记 caption；LlavaGuard产安全类别/理由，再用 Cohere Prompt Tuner优化给 Command R+的验证 prompt；取多路 unsafe IDs并集，删除对应 image-text pair。policy taxonomy与threshold属于 dataset release contract。
- **Implementation / evaluation:** Toxic-BERT标记892 captions，视觉链标记7,111 images，并集去重后删除7,531 pairs；论文展示类别/分布并发布 mitigated data。没有用重新预训练模型比较 downstream quality/safety，也未报告硬件、precision、batch、并发/SLO。
- **Proves / does not / limitations:** 证明该 ensemble在该数据上标记并移除这些pairs；不证明标记ground truth、下游模型毒性必然下降或无群体偏差。作者把 user evaluation/其他pipeline复核列为 future work。
- **Trade-offs / coexistence / failure:** safety gate减少已知policy违规，却可能 false-positive删除少数群体语境、false-negative漏检，并依赖闭源judge版本；保留原始数据需权限隔离与可逆 lineage。
- **Evolution / owner / adjacent / disposition / open:** `text keyword filter → modality-specific classifiers → policy ensemble + versioned quarantine`。Owner `TRAIN-DATA` Ch27，handoff `PLATFORM-SECURITY` Ch72；Ch26/28/72 已读。`Emerging / Experimental`，不进入Books直至有 downstream/cross-rater evidence；不改其他文件。待验证 inter-rater agreement、false-positive与artifact commit。

### Seed1.5-VL — model/data/parallelism co-design for heterogeneous tokens

- **Candidate / Week / Score; identity:** Seed1.5-VL Technical Report / W19 / 28；`seed1.5-vl-2505.07062`，arXiv v1 2025-05-11；官方网页/仓库在05-12/13发布属于W20 artifact node，不改变owner。
- **Access / coverage:** 已读technical report的 architecture、Seed-ViT、data construction、three-stage pretraining/post-training、multimodal reasoning/GUI/video evaluation、infrastructure、ablation与 limitations；官方 repo只公开cookbook/report，未发布可下载weights。
- **Problem / previous / changed constraint:** 固定分辨率视觉encoder浪费或丢失细节；VLM中532M视觉端与20B-active MoE语言端计算/并行不对称，统一parallel plan会负载失衡。
- **Mechanism / state / flow:** native-resolution Seed-ViT（532M）→MLP adapter→20B-active decoder-only MoE；图像/视频加入位置/时间 identity。ViT先MIM+2D RoPE，再native-resolution contrastive与omni-modal alignment；VLM stage0只训adapter，stage1全参3T multimodal tokens，stage2扩到131,072 context。
- **Implementation / evaluation:** stage预算16B/3T/240B，sequence 32,768/32,768/131,072，token-batch 8.4M/71M/71M；报告60个public benchmarks及GUI/game tasks、多项ablation。infra让ViT用ZeRO DP、LLM用4D parallel；visual token按约192 GPU group greedy rebalance，自定义loader减少pipeline组重复读与PCIe传输。GPU型号、precision、cluster总规模、serving concurrency/SLO未披露。
- **Proves / does not / limitations:** 证明在该内部数据/基础LLM/集群下，native representation、staged alignment和异构parallel可共同训练；作者benchmark不证明通用SOTA或因果归因，闭源weights/data限制复现。
- **Trade-offs / coexistence / failure:** 高分辨率与长context提高覆盖但放大token方差、MoE routing/通信与data-loader复杂度；group内greedy balance可能跨组不均。固定尺寸、小模型仍可用简单DP。
- **Evolution / owner / adjacent / disposition / open:** `fixed-resolution encoder + dense LLM → native-resolution encoder + adapter + MoE → modality-aware parallelism`。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff `TRAIN-PRETRAINING` Ch28与distributed training；Ch22/24/27/28/36 已读。Books Pending — `Integrate — New Mechanism`；开放问题是可复现artifact、完整hardware/precision与fleet cost。

## Low-score Closure

- **Anthropic AI for Science Program（14/30）**：官方日期与身份已核验；材料只描述 application/credit program，没有公开模型、训练、runtime 或 evaluation 机制。最终 disposition 为 `Weekly Only — Program Fact / No Long-term Mechanism`。

## Cross-Week Deduplication

- Spillback 至 W18：Llama-Nemotron `2505.00949`、Practical Efficiency of Muon `2505.02222` 与 `2505.01658`、`2505.01441`、`2505.00358`、`2504.21798`、`2505.00212`、`2505.01043` 已由 canonical W18 完成评分与相应全文/低分 closure；W19 只保留去重关系，不重复评分或重开 W18 Gate。
- W20 chronology correction：SweRank（2505.07849）v1 为 05-07，canonical owner 是 W19；W20 只保留后续读取关系，不重复评分。
- Forward 至 W20：HealthBench（05-12）、AlphaEvolve 与 Sufficient Context（05-14）。
- RM-R1 v2/v3、ZeroSearch v2、ICon v2 是后续 revision node，owner 仍为 W19；Elastic Reasoning v2（05-21）属于 W21 revision node。

## Knowledge Tree Position

- Training：`TRAIN-RLHF`、`TRAIN-GRPO`、`TRAIN-DATA`。
- Inference：`INFER-KV-CACHE`、`INFER-TENSORRT-LLM`、`INFER-SCHEDULING`。
- Multimodal：`MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`。
- Platform / Agent：`PLATFORM-EVALUATION-SYSTEM`、`AGENT-RAG`、`AGENT-TOOL-CALLING`。
- 映射只确定审计 owner；Historical Books Gate 关闭，不代表正文已经吸收。

## Gate Review

- **ISO / dates:** Python `date.fromisocalendar(2025, 19, 1/7)` 复算为 2025-05-05～2025-05-11；27 个 owner event 均落在窗口内，后续 revision 已分离。
- **Discovery / identity:** 固定机构、学术 metadata、项目/artifact 与 AI Infra release/tag replay 已闭合；27 个 primary identifier 唯一，spillback/forward/revision 均有 canonical owner。
- **Score / evidence:** 27/27 rows 六维字段齐全且 `TN+SI+PV+SR+PR+L = Total`；26 个 `20+` 对应26个唯一 Full Source Review，1个低分对应1个 closure。
- **Boundary / disposition:** 本周 `Review Pending = 0`、`Unverified / Blocked = 0`、`Disputed = 0`；Version Fact、Experimental 与 Books Pending 没有被误写为已进入长期正文。
- **Markdown / Git:** 标题无跳级、代码围栏成对（本文件无围栏）、URL shape与行尾空白检查通过；`git diff --check` 通过，W19 无 cached diff。

## Recommended Action

- W19 `Discovery Gate` 与 `Candidate Evidence Gate` 均通过：27/27 owner rows 已评分，26/26 retained reviews 与1/1低分 closure 完成，无本周 pending、blocked 或 disputed。
- 保留各 family 的 provisional Books disposition；仅当 2025 年度 Historical Evidence Gate 整体通过后，才由 Books Integration 流程逐项复核并写入正文。

## Event-Date Daily Decision

历史回填不创建 Daily；事件、revision 与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Books Frozen — Historical Gate Closed`。本周没有执行 Books Integration；旧文件中的“Books Gate 已完成”已撤销。单个 `Full Source Review Complete` 本身不等于整周完成；本周之所以通过 Candidate Evidence Gate，是因为26/26 retained reviews、1/1低分 closure、discovery/dedup与账目检查已同时闭合。

## Repository Changes

- 将 W19 从错误的空周重建为 27 个 scored owner Source Family 的闭合 ledger，并纠正 `2505.05327` 的名称为 ICon。
- 写入 26 个 strict Full Source Review、1 个低分闭合、固定来源 discovery 边界及跨周 owner/revision 关系。
- 仅修改本 Weekly；不修改年度索引、Learning State、Books、ROADMAP 或 DECISIONS。

## Open Questions

- General-Level 的 specialist-threshold proxy 能否被真正的 intervention / counterfactual synergy 测量替代？
- unified reasoner-verifier 如何校准并避免同源错误；streaming multimodal system 如何定义不可逆 output commit 与 rollback？
- W18 回拨项已在 canonical W18 闭合；W19 无需重复审计，后续只需保持 source-family alias 与 revision owner 可解析。

## Sources

- [Google — Gemini 2.5 Pro I/O Preview update](https://blog.google/products-and-platforms/products/gemini/gemini-2-5-pro-updates/)
- [Anthropic — Web Search API](https://www.anthropic.com/news/web-search-api)
- [Anthropic — AI for Science Program](https://www.anthropic.com/news/ai-for-science-program)
- [Voila — 2505.02707](https://arxiv.org/abs/2505.02707)
- [LLaMA-Omni 2 — 2505.02625](https://arxiv.org/abs/2505.02625)
- [RM-R1 — 2505.02387](https://arxiv.org/abs/2505.02387)
- [FormalMATH — 2505.02735](https://arxiv.org/abs/2505.02735)
- [R1-Reward — 2505.02835](https://arxiv.org/abs/2505.02835)
- [RetroInfer — 2505.02922](https://arxiv.org/abs/2505.02922)
- [ReplaceMe — 2505.02819](https://arxiv.org/abs/2505.02819)
- [Absolute Zero — 2505.03335](https://arxiv.org/abs/2505.03335)
- [VITA-Audio — 2505.03739](https://arxiv.org/abs/2505.03739)
- [OpenHelix — 2505.03912](https://arxiv.org/abs/2505.03912)
- [OSUniverse — 2505.03570](https://arxiv.org/abs/2505.03570)
- [X-Reasoner — 2505.03981](https://arxiv.org/abs/2505.03981)
- [ZeroSearch — 2505.04588](https://arxiv.org/abs/2505.04588)
- [HunyuanCustom — 2505.04512](https://arxiv.org/abs/2505.04512)
- [OpenVision — 2505.04601](https://arxiv.org/abs/2505.04601)
- [General-Level / General-Bench — 2505.04620](https://arxiv.org/abs/2505.04620)
- [RL^V — 2505.04842](https://arxiv.org/abs/2505.04842)
- [SweRank — 2505.07849](https://arxiv.org/abs/2505.07849)
- [Elastic Reasoning — 2505.05315](https://arxiv.org/abs/2505.05315)
- [ICon — 2505.05327](https://arxiv.org/abs/2505.05327)
- [StreamBridge — 2505.05467](https://arxiv.org/abs/2505.05467)
- [Flow-GRPO — 2505.05470](https://arxiv.org/abs/2505.05470)
- [Understanding and Mitigating Toxicity in Image-Text Pretraining Datasets — 2505.06356](https://arxiv.org/abs/2505.06356)
- [Seed1.5-VL — 2505.07062](https://arxiv.org/abs/2505.07062)
- [vLLM v0.8.5.post1 — W18 boundary](https://github.com/vllm-project/vllm/releases/tag/v0.8.5.post1)
- [SGLang v0.4.5 — W15 boundary](https://github.com/sgl-project/sglang/releases/tag/v0.4.5)
- [Transformers v4.52.0 — W20 boundary](https://github.com/huggingface/transformers/releases/tag/v4.52.0)
- [KServe v0.15.1 — W20 boundary](https://github.com/kserve/kserve/releases/tag/v0.15.1)
