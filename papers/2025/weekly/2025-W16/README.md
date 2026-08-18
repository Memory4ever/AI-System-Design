# AI Research Weekly — 2025-W16

> Coverage Window: 2025-04-14～2025-04-20 (ISO Monday–Sunday)
> Research Mode: Retrospective Primary-Source Backfill
> Reconciled: 2026-08-24
> Audit Status: Candidate Evidence Gate Conditional Open — 50 owners / 46 retained reviewed / 4 low closed / 1 Blocked / 1 Disputed
> Historical Books Gate: Closed

## Executive Result

W15 已批准的 13 个 spillback（Seaweed、GigaTok、MineWorld、VLM-R1、PixelFlow、Pangu Ultra、SpecReason、PRIMA.cpp、VL-Rethinker、AgentRewardBench、AI Scientist-v2、DUMP、MLRC-Bench）从未进入 W16 当前 39 行评分表，因此移出后 **W16 原始分母不变**：39 rows = 38 个 `20+` + 1 个低分。

本轮重放 04-18～20 与固定机构来源后，新增 8 个 `20+` owner 和 3 个低分 closure。最终 canonical ledger：

- **50 个唯一 Source Family**；
- **46 个 `20+` owner**：44 个 strict packet 已闭合，1 个 `Unverified / Blocked`，1 个 `Disputed`；
- **4 个低分候选**全部完成来源、日期、评分和拒绝理由闭合；
- **普通 `Review Pending = 0`**；
- Candidate Evidence Gate 为 `Conditional Open`：Codex CLI 缺事件时 artifact；ReZero 的 v1 metadata 与当前正文冲突；
- Discovery / Archive Gate 为 `Conditional Open`：固定机构、arXiv 关键词和 AI Infra replay 已完成，但 Scholar/OpenAlex 全量导出仍不可复算；
- Historical Books Gate 保持 Closed。

## Spillback Reconciliation

| Family | First Public | Owner Week | W16 Action |
| --- | --- | --- | --- |
| Seaweed / GigaTok / MineWorld | 2025-04-07 / 07 / 08 | W15 | Excluded; no W16 denominator change |
| VLM-R1 / PixelFlow | 2025-04-09 / 09 | W15 | Excluded; no W16 denominator change |
| Pangu Ultra / SpecReason / VL-Rethinker | 2025-04-10 | W15 | Excluded; no W16 denominator change |
| PRIMA.cpp | 2025-04-07 | W15 | Excluded; no W16 denominator change |
| AgentRewardBench | 2025-04-11 | W15 | Excluded; no W16 denominator change |
| The AI Scientist-v2 | 2025-04-10 | W15 | Excluded; no W16 denominator change |
| DUMP / MLRC-Bench | 2025-04-13 | W15 | Excluded; no W16 denominator change |

## Discovery Replay and Additions

- 固定机构顺序重放恢复 OpenAI Preparedness Framework v2（2025-04-15）；其余新增公告未形成可公开的独立机制 owner。
- arXiv 04-18～20 补回：From Large to Super-Tiny、Time Up!、High-Throughput LLM Inference on Heterogeneous Clusters、HPU、SlimPipe、Knowledge/Dataset Distillation Survey、Don't Retrieve, Generate。
- Self-Correction Makes LLMs Better Parsers、Multi-Agent Hazardous Object Detection、FAIRGAME 作为低分候选闭合。
- AI Infra 固定序列保留 vLLM v0.8.4；Transformers v4.51.3 低分闭合；未发现另一个独立的 20+ release owner。

| Added Candidate | N | I | P | R | K | L | Total | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OpenAI Preparedness Framework v2 | 4 | 5 | 5 | 5 | 4 | 4 | 27 | Strict Complete |
| From Large to Super-Tiny | 3 | 4 | 4 | 4 | 4 | 3 | 22 | Strict Complete |
| Time Up! | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Strict Complete |
| High-Throughput Heterogeneous Inference | 4 | 5 | 5 | 4 | 4 | 3 | 25 | Strict Complete |
| HPU | 5 | 5 | 4 | 4 | 5 | 3 | 26 | Strict Complete |
| SlimPipe | 5 | 5 | 5 | 4 | 5 | 4 | 28 | Strict Complete |
| Knowledge and Dataset Distillation Survey | 2 | 3 | 4 | 4 | 4 | 4 | 21 | Strict Complete — Secondary |
| Don't Retrieve, Generate | 4 | 3 | 4 | 4 | 4 | 3 | 22 | Strict Complete |
| Self-Correction Parsers | 3 | 2 | 3 | 4 | 3 | 3 | 18 | Low closure |
| Multi-Agent Hazardous Object Detection | 3 | 3 | 3 | 4 | 3 | 2 | 18 | Low closure |
| FAIRGAME | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Low closure |

## Canonical Candidate Scoring Ledger

评分维度固定为：`TN = Technical Novelty`、`SI = System Impact`、`PV = Practical Value`、`SR = Source Reliability`、`PR = Project Relevance`、`L = Longevity`。每行 Total 必须等于六维之和；状态是本轮证据审计后的最终 Weekly disposition，不以原先 provisional 状态代替。

| # | Candidate | Source Family ID | TN | SI | PV | SR | PR | L | Total | State |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | GPT-4.1 API family | `openai-gpt41-api-2025-04` | 3 | 4 | 5 | 5 | 4 | 2 | 23 | Weekly Only — Version Fact / Mechanism Not Disclosed |
| 2 | Claude Research | `anthropic-claude-research-2025-04` | 3 | 3 | 4 | 5 | 4 | 2 | 21 | Weekly Only — Product Workflow Fact |
| 3 | OpenAI o3 and o4-mini | `openai-o3-o4mini-2025-04` | 4 | 4 | 5 | 5 | 4 | 2 | 24 | Weekly Only — Version/Product Fact |
| 4 | Gemini 2.5 Flash preview | `google-gemini-25-flash-preview-2025-04` | 3 | 4 | 5 | 5 | 4 | 2 | 23 | Weekly Only — Version Fact / Mechanism Not Disclosed |
| 5 | OpenAI Codex CLI | `openai-codex-cli-launch-2025-04` | 4 | 4 | 5 | 4 | 5 | 3 | 25 | Unverified / Blocked — P2 Artifact |
| 6 | OpenAI Preparedness Framework v2 | `openai-preparedness-framework-v2` | 4 | 5 | 5 | 5 | 4 | 4 | 27 | Refine — Existing Argument Candidate |
| 7 | RealHarm | `realharm-real-world-agent-failures` | 3 | 4 | 4 | 5 | 4 | 3 | 23 | Refine — Existing Argument Candidate |
| 8 | AlayaDB | `alayadb-kv-attention-database` | 5 | 5 | 4 | 4 | 5 | 3 | 26 | Integrate — New Mechanism Candidate |
| 9 | Heimdall | `heimdall-long-cot-verifier` | 4 | 4 | 3 | 4 | 4 | 3 | 22 | Refine — Existing Argument Candidate |
| 10 | M1 | `m1-hybrid-mamba-reasoning` | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Emerging / Experimental |
| 11 | SAIL | `sail-native-pixel-language-model` | 4 | 4 | 4 | 4 | 5 | 3 | 24 | Refine — Existing Argument Candidate |
| 12 | InternVL3 | `internvl3-native-multimodal-pretraining` | 4 | 5 | 5 | 5 | 4 | 3 | 26 | Refine — Existing Argument Candidate |
| 13 | xVerify | `xverify-answer-equivalence-verifier` | 4 | 4 | 5 | 4 | 4 | 3 | 24 | Refine — Existing Argument Candidate |
| 14 | Layer-wise Gradients | `layerwise-gradients-data-quality` | 4 | 3 | 3 | 4 | 4 | 4 | 22 | Emerging / Experimental |
| 15 | Efficient Reasoning Models Survey | `efficient-reasoning-models-survey-2025` | 2 | 3 | 4 | 5 | 3 | 4 | 21 | No Change — Secondary Taxonomy |
| 16 | ReZero | `rezero-retry-search-rl` | 4 | 3 | 4 | 4 | 4 | 2 | 21 | Disputed — P3 Revision |
| 17 | Fluid-guided WAIT | `wait-fluid-llm-scheduling` | 5 | 5 | 5 | 4 | 5 | 3 | 27 | Integrate — New Mechanism Candidate |
| 18 | Minimalist Reasoning | `minimalist-reasoning-grpo-filtering` | 5 | 4 | 5 | 4 | 5 | 4 | 27 | Refine — Existing Argument Candidate |
| 19 | Seedream 3.0 | `seedream-3-native-image-generation` | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Refine — Existing Argument Candidate |
| 20 | DataDecide | `datadecide-small-scale-data-selection` | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Integrate — New Mechanism Candidate |
| 21 | TextArena | `textarena-game-agent-evaluation` | 3 | 4 | 4 | 4 | 4 | 3 | 22 | Refine — Existing Argument Candidate |
| 22 | SimpleAR | `simplear-visual-autoregressive-generation` | 4 | 4 | 4 | 4 | 4 | 2 | 22 | Emerging / Experimental |
| 23 | ReTool | `bytedance-retool-tool-integrated-rl` | 5 | 5 | 5 | 5 | 5 | 3 | 28 | Refine — Existing Argument Candidate |
| 24 | DFloat11 | `dfloat11-lossless-dynamic-float` | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Integrate — New Mechanism Candidate |
| 25 | BitNet b1.58 2B4T | `bitnet-b158-2b4t` | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Integrate — New Mechanism Candidate |
| 26 | WorldMem | `worldmem-long-term-video-world-memory` | 4 | 4 | 4 | 4 | 5 | 3 | 24 | Refine — Existing Argument Candidate |
| 27 | BrowseComp | `openai-browsecomp` | 3 | 4 | 5 | 5 | 4 | 4 | 25 | Refine — Existing Argument Candidate |
| 28 | FramePack | `framepack-next-frame-context-packing` | 5 | 4 | 5 | 4 | 5 | 3 | 26 | Integrate — New Mechanism Candidate |
| 29 | InstructRAG | `instructrag-planning-demonstration-generation` | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Emerging / Experimental |
| 30 | Conflicting RAG | `madam-rag-conflicting-documents` | 4 | 4 | 4 | 4 | 5 | 3 | 24 | Refine — Existing Argument Candidate |
| 31 | EEF | `eef-exploration-enhanced-finetuning` | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Emerging / Experimental |
| 32 | Antidistillation Sampling | `antidistillation-sampling` | 4 | 4 | 3 | 4 | 4 | 3 | 22 | Emerging / Experimental — Security-sensitive Alternative |
| 33 | Nemotron-CLIMB | `nvidia-nemotron-climb-data-mixture` | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Integrate — New Mechanism Candidate |
| 34 | Generate, but Verify | `reverse-retrospective-visual-verification` | 4 | 4 | 4 | 4 | 4 | 3 | 23 | Refine — Existing Argument Candidate |
| 35 | Sleep-time Compute | `berkeley-letta-sleep-time-compute` | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Refine — Existing Argument Candidate |
| 36 | MIRAS | `google-miras-titans-test-time-memory` | 5 | 5 | 4 | 5 | 5 | 2 | 26 | Refine — Existing Argument Candidate |
| 37 | PerceptionLM | `facebook-perceptionlm-open-video-language` | 4 | 5 | 5 | 5 | 5 | 4 | 28 | Integrate — New Mechanism Candidate |
| 38 | Perception Encoder | `facebook-perception-encoder` | 4 | 4 | 4 | 5 | 5 | 4 | 26 | Refine — Existing Argument Candidate |
| 39 | vLLM v0.8.4 | `vllm-v0.8.4` | 4 | 5 | 5 | 5 | 5 | 2 | 26 | Refine — Existing Argument Candidate |
| 40 | From Large to Super-Tiny | `large-to-super-tiny-task-llm` | 3 | 4 | 4 | 4 | 4 | 3 | 22 | Emerging / Experimental |
| 41 | Time Up! | `time-up-output-budget-model-selection` | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Refine — Existing Argument Candidate |
| 42 | High-Throughput LLM Inference on Heterogeneous Clusters | `heterogeneous-llm-inference-configuration-scheduling` | 4 | 5 | 5 | 4 | 4 | 3 | 25 | Integrate — New Mechanism Candidate |
| 43 | HPU | `hpu-attention-memory-coprocessor` | 5 | 5 | 4 | 4 | 5 | 3 | 26 | Emerging / Experimental |
| 44 | SlimPipe | `slimpipe-long-context-pipeline-parallelism` | 5 | 5 | 5 | 4 | 5 | 4 | 28 | Integrate — New Mechanism Candidate |
| 45 | Knowledge and Dataset Distillation Survey | `knowledge-dataset-distillation-survey-2025` | 2 | 3 | 4 | 4 | 4 | 4 | 21 | No Change — Secondary Taxonomy Already Covered |
| 46 | Don't Retrieve, Generate | `dont-retrieve-generate-hard-negatives` | 4 | 3 | 4 | 4 | 4 | 3 | 22 | Emerging / Experimental |
| 47 | Transformers v4.51.3 | `transformers-v4.51.3` | 2 | 2 | 3 | 5 | 2 | 2 | 16 | Weekly Only — Patch Fact |
| 48 | Self-Correction Makes LLMs Better Parsers | `self-correction-llm-parsers` | 3 | 2 | 3 | 4 | 3 | 3 | 18 | Weekly Only — Narrow Application Evidence |
| 49 | Multi-Agent Hazardous Object Detection | `multi-agent-hazardous-object-detection` | 3 | 3 | 3 | 4 | 3 | 2 | 18 | Weekly Only — Domain System Case |
| 50 | FAIRGAME | `fairgame-multi-agent-bias-simulator` | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — Evaluation Framework Case |

## Strict Full Source Reviews

每个 packet 均显式覆盖 identity/date/revision、primary source、正文范围、原问题与旧方案、变化约束、机制、state/control/data、implementation、evaluation contract、证明与未证明、trade-off/failure/coexistence、Stable Node、相邻章节和 disposition。`Not Disclosed` 不被推断补齐。

### GPT-4.1 API family — 23/30

- `openai-gpt41-api-2025-04`；官方发布页，First Public 2025-04-14。已核验 1M context、模型族、coding/long-context eval 及注释；无 technical report、weights/code。
- 旧 API 模型在 code editing、instruction following 和长上下文上暴露边界；公开变化是三档产品与 context contract，architecture/data/objective/router 未披露。runtime 拥有 request、tools、limits 与 billing。
- SWE-bench、OpenAI-MRCR、Graphwalks 均为 vendor evaluation；SWE-bench 有 23/500 omitted tasks，hardware/precision/batch/concurrency/SLO 未披露。不能外推通用性能。
- 长 context 换取更高 TTFT/cost/cache pressure；短任务旧模型仍合理。Owner `INFER-REQUEST-LIFECYCLE` Ch42，handoff Ch22/66。`Weekly Only — Version Fact / Mechanism Not Disclosed`。

### Claude Research — 21/30

- `anthropic-claude-research-2025-04`；官方公告，2025-04-15。已核验 web/Google Workspace multi-search、citation 与 beta scope；无 technical report 或 orchestrator code。
- 单次 retrieval 适合简单 lookup；复杂问题改为 query→多轮 search→synthesis→citations。planner、ranking、checkpoint、verifier 未披露，host 拥有权限和 execution state。
- 公告证明 product workflow，不证明 citation 覆盖全部 atomic claims，也不披露 latency/cost/recall/SLO。
- 深搜索增加权限面、citation laundering 和长尾 latency；普通 RAG 仍适合可控知识库。Owner `AGENT-WORKFLOW` Ch81，handoff Ch76/72。`Weekly Only — Product Workflow Fact`。

### OpenAI o3 and o4-mini — 24/30

- `openai-o3-o4mini-2025-04`；release + 33-page System Card，2025-04-16；全文覆盖 tools、vision、safety、Preparedness、benchmarks，后续 o3-pro 不反投影。
- hidden reasoning 无法执行环境动作；model 产生 tool intent，host 执行并回注 observation。授权、副作用、sandbox 和 durable state 不属于模型参数。
- AIME/SWE-bench/cyber/biological/autonomy 绑定官方 scaffold；hardware、precision、concurrency、SLO 与 tool-policy ablation 未披露。
- tools 带来可验证计算，也扩大 injection、数据外泄、副作用和 latency。Owner `AGENT-TOOL-CALLING` Ch78，handoff Ch66/72/81。`Weekly Only — Version/Product Fact`。

### Gemini 2.5 Flash preview — 23/30

- `google-gemini-25-flash-preview-2025-04`；官方公告，2025-04-17；已核验 thinking on/off、budget、preview/API scope；无完整 report。
- 固定 reasoning depth 不能同时满足简单 latency 与复杂 quality；公开的是 thinking budget contract，内部 allocation/objective/router/cache 为 `Not Disclosed`。
- 官方榜单未对齐 hardware/precision/length/batch/concurrency/SLO，只证明 knob 存在，不证明 correctness 随 budget 单调。
- 更高 budget 增加 cost、latency 与 overthinking；简单请求保留低预算 path。Owner Ch42，handoff Ch70/66。`Weekly Only — Version Fact`。

### OpenAI Codex CLI — 25/30 — Unverified / Blocked

- `openai-codex-cli-launch-2025-04`；官方同步公告确认 2025-04-16 launch，当前 GitHub history 可见 sandbox/shell/workdir/tracing 修复，但 current main 不能替代 launch tree。
- terminal agent 的 durable contract 应为 model proposal→host read/edit/execute→diff/result→next step；host 拥有 cwd、approval、sandbox 与 side effects。
- 缺 2025-04-16 tag/commit/source archive，无法验证 launch permission defaults、prompt、API 与 failure recovery；不以今日 code 反投影。
- Owner `AGENT-PLATFORM` Ch84，handoff Ch72/81。`Unverified / Blocked — P2 Artifact`；需 launch tag/commit/tree archive 或官方 source hash。

### OpenAI Preparedness Framework v2 — 27/30

- `openai-preparedness-framework-v2`；官方公告/PDF，Version 2，2025-04-15。已读 categories、thresholds、Capabilities/Safeguards Reports、SAG、defense-in-depth 与 adjustment clause。
- capability score 不能直接决定 deployment；框架把 threat model→threshold→safeguard claim→efficacy evidence→residual risk→SAG/leadership decision 串成 release gate。
- 这是 policy contract，不证明 safeguards 实际有效或执行一致；Research Category 不是成熟 threshold。
- 明确 gate 提升可审计性，也留下 internal judgment 和 exception discretion。Owner `PLATFORM-PRODUCTION` Ch73，handoff Ch72/66。`Refine — Existing Argument Candidate`。

### RealHarm — 23/30

- `realharm-real-world-agent-failures`；arXiv:2504.10277 v1 2025-04-14；论文、136-example dataset、taxonomy、guardrail replay、limitations 已核验。
- 68 个公开 incident 与 68 个 safe rewrite 形成 paired set，标 harms/hazards/causes，再重放 LlamaGuard/moderation；evaluator 拥有 provenance、rewrite lineage、taxonomy/guardrail version。
- 小样本、报道 selection bias、文本化 replay 丢失 tool/environment state；证明该 collection 的 coverage gap，不证明总体 incident prevalence 或 causal harm rate。
- 外部有效性换取可控性与完整 denominator。Owner `PLATFORM-SECURITY` Ch72，handoff Ch66/67。`Refine — Existing Argument Candidate`。

### AlayaDB — 26/30

- `alayadb-kv-attention-database`；arXiv:2504.10326 v1 2025-04-14；全文覆盖 DB/Session、DIPR、optimizer、storage、use cases 和 evaluation。
- 从 KV/cache 与 attention compute 同机演进为同时解耦 storage/compute；DB 拥有 KV identity，Session 拥有 context，DIPR 和 optimizer 决定相关 state 与移动方向。
- 对比 coupled、KV-disaggregated、sparse/retrieval；示例 495.5K-token、BF16 Llama-3-8B、2×A800 80GB、141.38GB。未证明多租户 isolation/recovery 或所有 workload 优势。
- 代价是 index freshness、approximation、network、invalidation 和 recovery。Owner `INFER-KV-CACHE` Ch45，handoff Ch55/56。`Integrate — New Mechanism Candidate`。

### Heimdall — 22/30

- `heimdall-long-cot-verifier`；arXiv:2504.10337 v1 2025-04-14；filtered PPO、Pessimistic Verification、AIME contract 与 limitations 已读。
- 32B solver 每题生成 16 解，过滤全对/全错 prompt 训练 verifier；推理融合 answer frequency 与 verifier lower-confidence bound。evaluator 拥有 candidates、judge version、sampling/aggregation。
- AIME24 validation/AIME25 test 共 60；作者报告 62.5→94.5，64-sample aggregation 97.5。小样本与 correlated errors 限制校准，不验证 reasoning faithfulness。
- 多样本提高可靠性但成本成倍、共同偏差会虚高信心。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch20。`Refine Candidate`。

### M1 — 23/30

- `m1-hybrid-mamba-reasoning`；arXiv:2504.10449 v1 2025-04-14；distillation、SFT/GRPO、architecture、throughput/ablation 已读。
- 28 层只保留 6 attention，其余 SSM；reverse-KL distill→math/reasoning SFT→带 entropy bonus、无 KL 的 GRPO。runtime 分别管理 SSM recurrent 与 KV state。
- Llama-3.2-3B family、<50B tokens；RL batch128、8 generations、32K；throughput 单 H100、prompt256/output4096、batch8–512，作者称大 batch 约 3×。
- 降低 state growth，却带 distillation loss、hybrid kernel/placement complexity。Owner `MODEL-LONG-CONTEXT` Ch22，handoff Ch44。`Emerging / Experimental`。

### SAIL — 24/30

- `sail-native-pixel-language-model`；arXiv:2504.10462 v1 2025-04-14；architecture、data/model scaling、tasks、ablation、artifact 已核验。
- 不冻结 ViT：单 transformer 处理 visual/text tokens；图像 token bidirectional、文本 causal，multimodal RoPE 统一位置。mask/tokenizer/modality identity 成为 contract。
- 多规模与 modular baselines 支持作者条件下 native pretraining 形成视觉 backbone；不证明无 tokenizer cost 或全任务更优，系统 SLO 未披露。
- end-to-end 表示减少 encoder ceiling，也增加训练成本、模态干扰和位置/mask 风险。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch28。`Refine Candidate`。

### InternVL3 — 26/30

- `internvl3-native-multimodal-pretraining`；arXiv:2504.10479 v1 2025-04-14；model family、data recipe、V2PE、MPO、benchmarks/ablation、artifact 已读。
- ViT–MLP–LLM 全参数联合；V2PE 用 fractional visual position，pixel-unshuffle 控制 token 数；MPO 组合 DPO+BCO+LM，VisualPRM 可做 best-of-N。
- 1B–78B；约 200B pretrain tokens、21.7M SFT、300K preference。v1 数据仍整理，vendor benchmark 与 test-time selection 不构成通用优势。
- joint training 换取跨模态协同，也引入 data-ratio、forgetting、position identity、artifact provenance。Owner Ch23，handoff Ch28/66。`Refine Candidate`。

### xVerify — 24/30

- `xverify-answer-equivalence-verifier`；arXiv:2504.10481 v1 2025-04-14；VAR、19 generators、24 benchmarks、annotation、0.5B–32B training、appendix 已读。
- 小 verifier 从长 reasoning 中抽取并判断最终答案等价性；evaluator 拥有 raw/canonical answer、equivalence ontology、judge version 与 disagreement。
- Qwen/Llama/Gemma；作者报告 accuracy/F1 多数 >95%，但只验证 final-answer equivalence，不验证 process、citation 或 executable effect。
- 低成本换取 ontology/parser/judge bias；可执行任务仍应优先规则 verifier。Owner Ch66。`Refine Candidate`。

### Layer-wise Gradients — 22/30

- `layerwise-gradients-data-quality`；arXiv:2504.10766 v1 2025-04-14；Q/K/V/O gradient SVD、datasets/models、correlations、limits 已读。
- 对每层计算 nuclear norm、effective rank、same/adjacent similarity，诊断 batch 如何更新网络；trainer 拥有 checkpoint、batch、layer/projection 和 statistics。
- Qwen2.5、Llama3.1/3.2、Gemma2 1.5B–14B，多 instruction/reasoning sets；quality 与 spectrum 相关，不证明因果或可替代 downstream eval。
- 细粒度信号增加计算/存储且受 optimizer/model/batch 影响。Owner `TRAIN-DATA` Ch27，handoff Ch28/66。`Emerging / Experimental`。

### Efficient Reasoning Models Survey — 21/30

- `efficient-reasoning-models-survey-2025`；arXiv:2504.10903 v1 2025-04-15；全文与 curated repository 已核验，secondary synthesis。
- taxonomy 为 shorter（少 token）、smaller（少每 token compute）、faster（更高执行效率）；三类不可互换。
- 无新 matched experiment；收录快速变化且 model/data/harness 不统一，不能据表跨论文排序。
- Owner Ch42，handoff Ch28/33/48。`No Change — Taxonomy Already Covered Candidate`。

### ReZero — 21/30 — Disputed

- `rezero-retry-search-rl`；arXiv:2504.11001 metadata v1 2025-04-15，但当前 HTML manuscript 显示 2026-08-11，事件时正文无法锁定。
- 当前页面声称以 retry reward 教 search failure 后再尝试；因 v1 body 冲突，机制/数字不纳入 W16 evidence。
- metadata 只证明 identifier/date，不能证明 2025 文件包含当前 method/eval；禁止 2026 content 反投影。
- provisional owner `AGENT-REFLECTION` Ch80。`Disputed — P3 Revision`；需 v1 PDF/TeX、SHA 或 2025 archive。

### Fluid-guided WAIT — 27/30

- `wait-fluid-llm-scheduling`；arXiv:2504.11320 v1 2025-04-15、v2 2026-01-05；事件时 PDF、algorithm、proof、eval、appendix 已读。
- 将 KV 随 decode 增长建模为多阶段队列；known length 用 WAIT threshold，unknown length 用 Nested WAIT。scheduler 拥有 age/stage/KV/length/capacity。
- Llama-7B、A100、synthetic+real arrivals，与 vLLM/Sarathi；heavy-traffic 结果不覆盖 model mix、priority、recovery 和 tail SLO。
- 理论策略依赖估计与 stationarity；低负载/强优先级场景 FCFS 仍合理。Owner `INFER-SCHEDULING` Ch56。`Integrate Candidate`。

### Minimalist Reasoning — 27/30

- `minimalist-reasoning-grpo-filtering`；arXiv:2504.11343 v1 2025-04-15；RAFT/REINFORCE/GRPO/DPO、filtering、entropy、ablation 已读。
- 结果显示 GRPO 部分收益来自过滤 group 内全对/全错 prompt；Reinforce-Rej 显式保留非零学习信号。trainer 拥有 samples/reward variance/provenance/entropy/policy version。
- Qwen/Llama math、verl；matched filtering/normalization 对比。RAFT 早收敛后 entropy collapse；不证明全 domain/长训练。
- 提高有效梯度密度但丢弃过易/过难 curriculum。Owner `TRAIN-GRPO` Ch33。`Refine Candidate`。

### Seedream 3.0 — 24/30

- `seedream-3-native-image-generation`；arXiv:2504.11346 v1 2025-04-15；data filter、resolution schedule、REPA、reward、eval/ablation 已读。
- 小 defect 图像保留但 mask latent gradient；dual-axis sampling、256→512–2048 curriculum、cross-modal RoPE、DINOv2-L REPA、resolution-aware timestep 与 VLM reward。
- 作者称额外保留 21.7% data、2K、4–8× sampling；完整 hardware/precision/concurrency/SLO 未披露，不能把产品质量归因于单组件。
- detector/judge bias 与 mixed-resolution batching 是新风险。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch27/66。`Refine Candidate`。

### DataDecide — 29/30

- `datadecide-small-scale-data-selection`；arXiv:2504.11393 v1 2025-04-15；25 recipes×14 scales×3 seeds、predictors、frontier、limitations 已读。
- 用小模型 rank 预测 1B target mixture；ledger 需绑定 recipe/tokenizer/scale/seed/checkpoint/metric。
- 1,050 models、4M–1B、最高100B tokens、30K checkpoints；target 1B 三复跑，小规模复跑到25% compute。约150M可做~80% decisions，但无 scaling law 统治 frontier。
- proxy 降低 search cost，也会 rank reversal/target shift。Owner `TRAIN-DATA` Ch27，handoff Ch28/66。`Integrate Candidate`。

### TextArena — 22/30

- `textarena-game-agent-evaluation`；arXiv:2504.11442 v1 2025-04-15；API、games、TrueSkill、model/human play、repo 已核验。
- turn-based environment 拥有 legal action/state transition/termination/transcript；rating service 拥有 opponent pool/model version/uncertainty。
- 论文 57+ games，后续 74；single/two/multi-player，TrueSkill μ25/σ25/3。live leaderboard 不是固定可复现 score。
- interactive eval 混合规则理解、format、对手池与能力。Owner Ch66，handoff `AGENT-MULTI-AGENT` Ch82。`Refine Candidate`。

### SimpleAR — 22/30

- `simplear-visual-autoregressive-generation`；arXiv:2504.11455 v1 2025-04-15；全文覆盖 tokenizer、AR、pretrain/SFT/GRPO、KV/vLLM/SJD、ablation/failures。
- Cosmos tokenizer→text+visual tokens→causal transformer；43M pretraining images，SFT 后 CLIP/HPS GRPO。runtime 拥有 4096 visual tokens、KV、CFG branches。
- 0.5B/1.5B，32×A100；单 A100+CFG 下 227.62→150.19→13.55 sec/img（baseline/KV/vLLM）。SJD 减 steps 但不能复用 KV，未降 latency。
- AR 简单统一却有长序列 latency、tokenizer ceiling、exposure bias。Owner Ch24，handoff Ch48/50。`Emerging / Experimental`。

### ReTool — 28/30

- `bytedance-retool-tool-integrated-rl`；arXiv:2504.11536 v1 2025-04-15、v2 typo；Method、PPO、sandbox、eval、appendix/code 已读。
- cold-start SFT 后在 code-interpreter feedback rollout 做 outcome-only PPO；policy 拥有 intent，sandbox 拥有 executable state，runtime 回注 result/KV。
- Qwen2.5-32B、AIME24/25、32 repeats、temperature1.0/top-p0.7；VeRL、lr1e-6、max seq16,384、mini-batch512。hardware/SLO 未披露。
- executable feedback 引入 sandbox cost、安全、timeout、reward equivalence。Owner `AGENT-TOOL-CALLING` Ch78，handoff Ch31。`Refine Candidate`。

### DFloat11 — 29/30

- `dfloat11-lossless-dynamic-float`；arXiv:2504.11651 v1 2025-04-15，v2/v3 后续；事件结论锁定 v1，method/kernel/model table/appendix 已读。
- BF16 symbol 低 entropy→dynamic-length coding；hierarchical LUT 入 SRAM、two-phase kernel 协调 offsets、block-level 在线解压，保持 bit-identical。runtime 拥有 stream/codebook/offset/kernel version。
- v1 Llama3.1/Qwen2.5/Gemma3，A5000/A100-40GB/RTX8000；约30% size、相对 CPU offload 1.9–38.8×、5.3–13.17× context。405B/8×80GB 是 capacity arithmetic 非吞吐实测。
- lossless 避免量化误差，但 variable-length decode 复杂；能 fit 时 BF16/FP8 更简单。Owner `INFER-GPU-MEMORY` Ch54，handoff Ch49。`Integrate Candidate`。

### BitNet b1.58 2B4T — 29/30

- `bitnet-b158-2b4t`；arXiv:2504.12285 v1 2025-04-16，v2 2025-04-25 属 W17 revision；已核验 v1 method、training recipe、kernel、evaluation、limitations 与官方 artifact。
- dense BF16 权重在内存带宽和矩阵乘上持续付高精度成本；BitNet 用原生 ternary `{-1,0,1}` 权重、per-token activation quantization 与专用 W1.58A8 kernels，把表示约束前移到训练，而不是事后压缩。
- 模型为 2B、训练 4T tokens；作者比较同规模 full-precision LLM、量化模型及 CPU/GPU inference。公开证据支持作者实现下的容量/能效收益，不证明所有硬件已有原生 ternary execution，也不证明相同 data/objective 下的普遍质量等价。
- weight code、scale、packing layout 与 kernel version 是 runtime identity；硬件缺少原生 W1.58A8 时会产生 unpack/dequant、算子覆盖和 compiler portability 风险。能装入显存且成熟 BF16/FP8 kernels 占优时旧路线仍合理。Owner `INFER-TENSORRT-LLM` Ch49，handoff Ch16/28/54。`Integrate — New Mechanism Candidate`。

### WorldMem — 24/30

- `worldmem-long-term-video-world-memory`；arXiv:2504.12369 v1 2025-04-16；已读 memory construction/retrieval、action-conditioned diffusion、pose prediction、long-horizon experiments、ablations、appendix 与项目 artifact。
- 短 sliding window 对局部 video prediction 合理，但长环境 traversal 会忘记已离开视野的几何与物体。WorldMem 建立带 frame、pose、timestamp 的 memory bank，按视域重叠与时间检索、去冗余，再通过 cross-attention 注入 action-conditioned DiT。
- memory service 拥有 observation/pose/time/provenance，world-model rollout 拥有 latent state 与 predicted pose；控制流为 observation/action→更新 bank→检索相关 frames→预测下一段与 pose→继续 rollout。memory context 8 在作者设置最好，扩到 16 反而退化，说明更多历史不是单调收益。
- 600-frame bank 压到约 100 retrieved frames 的实验只证明该模拟/数据 contract 下的长期一致性改善；不证明真实环境 causal fidelity、碰撞安全或无限期 persistence。新 failure 包括错误 pose、stale memory、retrieval omission 和 self-generated-state drift。Owner `MULTIMODAL-WORLD-MODELS` Ch25，handoff Ch26/77。`Refine — Existing Argument Candidate`。

### BrowseComp — 25/30

- `openai-browsecomp`；arXiv:2504.12516 v1 2025-04-16；已核验 1,266-question construction、adversarial filtering、encrypted test set、answer/reference grading、model/harness results 与 limitations。
- 静态 QA 不能测量在开放 web 中定位稀有且互相关联证据的能力；benchmark 让人类编写短、可验证但难搜索的问题，并保留来源/答案，使 browsing agent 必须迭代 query、阅读与综合。
- evaluator 拥有 encrypted item、reference answer、web snapshot/access policy、grader 和 agent trace；得分混合 base model、search/browser scaffold、机会性网页可达性与 judge 行为，不能称为纯模型能力。
- exact/reference/LLM grading 降低开放答案歧义，却受网页变化、source disappearance、contamination 与 judge error 影响；公开证据不证明现实 research correctness 或 citation completeness。Owner `PLATFORM-EVALUATION-SYSTEM` Ch66，handoff Ch76/81。`Refine — Existing Argument Candidate`。

### FramePack — 26/30

- `framepack-next-frame-context-packing`；arXiv:2504.12626 v1 2025-04-17，后续 v2 归 revision ledger；已读 context design、history compression、sampling、implementation、user study/metrics、ablations、limitations 与代码。
- video diffusion 的完整历史 token 随时长增长；固定窗口虽便宜却会漂移。FramePack 按离当前生成位置的距离压缩历史 frames，在固定 transformer context 中保留多尺度时间线，并用反向时间生成/endpoint conditioning 的 anti-drift sampling 维持早期约束。
- packer 拥有 frame/time/scale identity，diffusion runtime 拥有 latent/noise/sampling order；控制流从 endpoints 与压缩 history 构造 context，再逐段生成并把结果写回 history。它可在既有 video diffusion backbone 上 finetune，而非需要全新生成范式。
- 作者实验支持固定 context 下更长 video 和特定漂移改善；不证明物理 causal correctness、任意时长一致或生产 latency。压缩会丢细节，反向采样增加调度复杂度，短视频仍可用完整上下文。Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24，handoff Ch25/54。`Integrate — New Mechanism Candidate`。

### InstructRAG — 23/30

- `instructrag-planning-demonstration-generation`；arXiv:2504.13032 v1 2025-04-17；已核验 instruction graph、RL-Agent/ML-Agent、四个 planning datasets、baselines、ablation 与 limitations。
- 人工 demonstration 对固定 planner 合理，却昂贵且覆盖不了错误恢复。系统先由大模型执行任务生成正确 action paths，再让 RL-Agent 扩张成功轨迹覆盖、ML-Agent 从历史任务学习迁移，形成可用于 instruction tuning 的 graph。
- graph service 拥有 task/action/result/provenance，environment verifier 决定 path 是否正确，trainer 消费经验证轨迹；若 verifier 或 environment 不可靠，错误会被固化为 supervision。
- 作者报告在四个 planning 数据集上最高 19.2% 改善，但模型、harness 和任务分布绑定，不能证明通用 Agent planning。生成数据降低人工成本，也引入 teacher bias、coverage collapse 和 environment overfitting。Owner `AGENT-RAG` Ch76，handoff Ch79/27。`Emerging / Experimental`。

### Conflicting RAG — 24/30

- `madam-rag-conflicting-documents`；arXiv:2504.13079 v1 2025-04-17；已读 RAMDocs taxonomy、MADAM-RAG protocol、AmbigDocs/FaithEval、baselines、ablations 与 failure analysis。
- 把 top-k passages 拼入一次 prompt 在来源一致时简单有效；当 documents 互相矛盾时，位置/多数偏差会掩盖少数但可信证据。MADAM-RAG 让 document agents 独立提取观点，再多轮 debate，由 aggregator 综合。
- orchestrator 拥有 document identity、agent stance、round、message 与 aggregation trace；模型只生成观点。作者在 Llama-3.3-70B 设置报告 AmbigDocs +11.4 absolute、FaithEval +15.8，而 RAMDocs exact match 仍约 32.6，显示问题远未解决。
- debate 增加 token/latency、共享模型相关错误、虚假共识和 adversarial-document 放大；可信 metadata 完整时显式 source ranking 或单轮 structured comparison 更可控。Owner `AGENT-RAG` Ch76，handoff Ch66/72/82。`Refine — Existing Argument Candidate`。

### EEF — 23/30

- `eef-exploration-enhanced-finetuning`；arXiv:2504.13145 v1 2025-04-17；事件时 identity/body、method、WebShop/SciWorld setup、ablation 与 appendix 已核验；后续 revision 单独记录，不覆盖 v1。
- 纯行为克隆只学习 expert path，失败轨迹全部丢弃也会浪费已发现的有益 prefix/action。EEF 从失败 exploration 中识别 beneficial actions、排除 harmful branches，再与 expert demonstrations 合成训练数据。
- environment/evaluator 拥有 state、action、outcome 与 beneficial label，trainer 拥有 filtered trajectory provenance；若 credit assignment 错误，局部“有益”动作会制造长程偏差。
- WebShop 作者报告 62.0%（RFT 53.6%，其 GPT-4 scaffold 35.6%），SciWorld 超过 81%；仅支持指定 simulator/harness 下的数据利用，不能外推真实环境或复杂副作用。代价是额外 exploration 与 verifier，旧 expert-only FT 在安全、稀疏 feedback 场景仍合理。Owner `AGENT-REFLECTION` Ch80，handoff Ch29/79。`Emerging / Experimental`。

### Antidistillation Sampling — 22/30

- `antidistillation-sampling`；arXiv:2504.13146 v1 2025-04-17；已读 objective、proxy-student optimization、GSM8K/MATH/MMLU evaluation、sensitivity、limitations；v2 归后续 revision。
- 正常 sampling 追求 teacher utility，API owner 无法阻止消费者蒸馏输出。论文用 proxy student/downstream gradient 调整 next-token distribution，在保持 teacher task utility 的同时让被蒸馏 student 学得更差。
- serving policy 拥有 altered distribution 与 strength parameter，proxy learner 拥有 gradient/state；每 token 需额外 proxy forward/gradient signal，增加延迟、成本和实现耦合。
- DeepSeek-R1-7B teacher、Qwen/Llama students 与三类 benchmark 只证明作者 threat model 下可调 utility–sabotage trade-off；不证明对未知 student、adaptive attacker 或合法用户安全，也带 integrity/用户欺骗风险。Owner `MODEL-SAMPLING` Ch20，handoff Ch72。`Emerging / Experimental — Security-sensitive Alternative Branch`。

### Nemotron-CLIMB — 29/30

- `nvidia-nemotron-climb-data-mixture`；arXiv:2504.13161 v1 2025-04-17；已核验 clustering、iterative small-model proxy search、1.2T-token mixture、baselines、ablations、released dataset/recipe 与 limitations。
- 固定 web-data mixture 易被领域比例和质量噪声锁死；直接为大模型搜索配比又太贵。CLIMB 先把 Nemotron-CC 语义聚类，再以小模型迭代训练/评估候选 mixture，逐轮保留更有潜力的 cluster 权重，生成 ClimbMix。
- data platform 拥有 document/cluster/version/dedup lineage，experiment ledger 拥有 proxy model、seed、tokens、metric 与 selection history；target trainer 只消费冻结 mixture。
- 论文以 SmolLM family 等 proxy、约 1.2T-token final mix 做作者实验；证明该 corpus/target contract 下的 data selection 增益，不证明小模型 rank 对所有架构/规模稳定。搜索成本下降但会 proxy overfit、cluster leakage 与 target rank reversal。Owner `TRAIN-DATA` Ch27，handoff Ch28/66。`Integrate — New Mechanism Candidate`。

### Generate, but Verify — 23/30

- `reverse-retrospective-visual-verification`；arXiv:2504.13169 v1 2025-04-17；已读 1.3M semi-synthetic construction、hallucination-aware training、retrospective resampling、CHAIR/HaloQuest experiments、ablation 与 limitations。
- 一次性 VLM generation 无法知道自己的视觉 claim 是否受输入支持。REVERSE 先用 hallucination-aware data 训练，再让同一 VLM 回顾候选 response、重采样/自验证后输出。
- verifier 与 generator 共享模型先验；runtime 拥有 candidate set、verification prompt、sampling seed 与 chosen output。它不是外部 evidence verification，也未产生 calibrated probability。
- 作者在 MSCOCO CHAIR 与 HaloQuest 报告相对既有 best 的改善（约 12%/28% 表述需绑定其表格）；不证明 factuality 普遍解决、推理 faithfulness 或独立检测。额外 sampling 增 cost/latency，共同偏差可造成自洽幻觉。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch66。`Refine — Existing Argument Candidate`。

### Sleep-time Compute — 29/30

- `berkeley-letta-sleep-time-compute`；arXiv:2504.13171 v1 2025-04-17；Methods、Stateful GSM/AIME、Multi-Query、SWE case、limitations、appendix 与 released artifact 已核验。
- query 未知时将 compute 留在请求期最稳妥；当共享 context 先到且会服务多个 query，重复在线推理浪费 latency/cost。最多十次 `rethink_memory` 在离线期把 raw context 派生为自然语言 memory，在线读取该 state 后做 bounded reasoning。
- memory runtime 拥有 raw/derived context、version、provenance、invalidation 与 query-predictability；作者成本模型假设 online token 是 offline token 的 10 倍且每 context 有 10 queries。该假设下约 5× token、最高约 2.5× modeled cost 改善，不是通用生产测量。
- SWE 仅 33 PR 且以 modified-file F1 非 executable correctness；预计算还会浪费、陈旧与污染。单次查询或高频变化 context 仍应在线计算。Owner `AGENT-MEMORY` Ch77，handoff Ch56。`Refine — Existing Argument Candidate`。

### MIRAS — 26/30

- `google-miras-titans-test-time-memory`；arXiv:2504.13173 v1 2025-04-17；正文、公式、Moneta/Yaad/Memora、parallel training、LM/RULER、ablation、proof appendix 与 setup 已读；无公开 code/独立复现。
- 现有 recurrent memory 各自修改 write objective、retention 或 state shape，却缺统一设计坐标。MIRAS 将 associative memory 拆成 architecture、attentional bias、retention regularizer、online optimizer 四轴，并以三种实例展示组合。
- sequence model 拥有 test-time recurrent parameter state，outer trainer 拥有 frozen weights；这不是带 ACL/provenance/delete 的 Agent memory。120M–1.3B、15B–100B tokens、RULER 1K–8K 支持作者范围内的设计差异，不证明生产吞吐或大规模优势。
- 固定 state 减 KV 增长，却引入 sequential update、overwrite、漂移、数值稳定、isolation 和 checkpoint 问题；精确 token recall/成熟 serving 仍由 attention 更好承担。Owner `MODEL-LONG-CONTEXT` Ch22，handoff Ch77。`Refine — Existing Argument Candidate`。

### PerceptionLM — 28/30

- `facebook-perceptionlm-open-video-language`；arXiv:2504.13180 v1 2025-04-17；已核验 1B/3B/8B models、2.8M human-labeled video data、architecture/training、PLM-VideoBench、comparisons、ablations 与公开 weights/code/data。
- 依赖 proprietary teacher distillation 的 VLM 难以审计数据和错误来源；PerceptionLM 用公开 recipe、细粒度时空 captions/QA 与多尺度 video inputs 训练 open VLM family。
- data platform 拥有 clip/time/annotation/provenance，model runtime 拥有 frame sampling/token budget；2.8M 样本和 benchmark 证明公开条件下可复现的一条 video-language recipe，不证明所有 proprietary model 对比公平或实时 serving 成立。
- 人工标注提升可追溯性但昂贵、带 annotator bias；长视频 frame sampling 会漏事件，1B–8B scale 仍受视觉 encoder/token budget 限制。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch27/66。`Integrate — New Mechanism Candidate`。

### Perception Encoder — 26/30

- `facebook-perception-encoder`；arXiv:2504.13181 v1 2025-04-17；已读 contrastive pretraining、intermediate-layer analysis、PE_core/PE_lang/PE_spatial alignment、image/video tasks、ablations 与 artifact。
- 单一 final embedding 为 retrieval 优化时会丢 spatial/local details；论文先训练 general contrastive encoder，再从不同 intermediate layers/readouts 对齐 language 或 spatial tasks，保留 core representation 与 task adapter 的边界。
- encoder artifact 拥有 checkpoint/layer/preprocess identity，下游 adapter 拥有 language/spatial alignment；同一“视觉表示”不是可无条件互换的 tensor。
- classification/retrieval/QA/detection/depth/tracking 的作者结果支持层级表示有不同可迁移信息，不证明一个 checkpoint 对所有 modality/workload 最优，也未披露完整 serving SLO。多 readout 增版本与 feature-contract 风险。Owner `MULTIMODAL-REPRESENTATION` Ch23，handoff Ch57/66。`Refine — Existing Argument Candidate`。

### vLLM v0.8.4 — 26/30

- `vllm-v0.8.4`；official GitHub release/tag 2025-04-14，commit `dc1b4a6`；release notes、tag/compare 与 V1 execution、multi-input、tensor transfer、EAGLE/KV slots、structured output、metrics/model fixes 的相关 code/PR 已核验。
- V1 统一 engine/request/scheduler 是合理基础，但多输入、worker transfer、speculative state 与 observability 尚有 contract gaps。该 release 由多项修复组成，不是单一新架构。
- engine/scheduler 拥有 request state，worker 拥有 tensor/KV，draft/verify path 拥有 speculative slots；zero-copy 改变 lifetime/aliasing，EAGLE 改变 KV-slot identity，metrics 只观察而不拥有执行状态。
- tag 证明版本行为存在；单 PR 的性能数字缺 model/hardware/precision/length/batch/concurrency/SLO，不能外推 release-wide。旧 engine 对稳定 text-only workload 仍适用。Owner `INFER-VLLM` Ch50，handoff Ch45/48/67。`Refine — Existing Argument Candidate`。

### From Large to Super-Tiny — 22/30

- `large-to-super-tiny-task-llm`；arXiv:2504.13471 v1 2025-04-18；已读 prototype/data generation、rejection filtering、FT/RL/KD、compression、deployment case、baselines 与 limitations。
- 直接手写一个小模型的训练集难覆盖真实 function-call workflow；方案先用大模型和可执行 prototype 生成/验证高质量轨迹，再把行为经 rejection FT、RL/KD 迁移到约 0.5B，最后 quantization/pruning 到约 0.4B。
- prototype/runtime 拥有 tool schema、execution result 与 accept/reject evidence，trainer 拥有 teacher/student/versioned data；小模型不拥有外部 action authority。数据正确性依赖 executable verifier，而不是 teacher 自述。
- 论文展示特定在线任务中的成本/质量压缩路线，不证明任意 task 可蒸馏或 tiny model 保留 OOD 能力。新风险是 prototype leakage、teacher bias、压缩后的 rare-case collapse 和多阶段 provenance。Owner `TRAIN-SFT` Ch29，handoff `PLATFORM-COST` Ch70/`AGENT-TOOL-CALLING` Ch78。`Emerging / Experimental`。

### Time Up! — 24/30

- `time-up-output-budget-model-selection`；arXiv:2504.14350 v1 2025-04-19；已核验 25+ models、reasoning tasks、output-token budgets、device-latency mapping、selection results、sensitivity 与 limitations。
- 只按平均 accuracy 选 model/prompt 在无限 token 假设下合理；on-device workload 有严格 deadline，长 reasoning 可能在超时后等价于失败。论文把 output-token budget 映射到设备 latency，再比较不同 model/prompt 的 budget-conditioned utility。
- serving policy 拥有 device/profile/model/prompt/token budget 与 deadline，decoder 拥有 current token count；“更强模型”不是脱离 budget 的单一排序。
- 证据说明作者设备与 benchmark 下最优配置会随预算改变，不证明 token 是所有硬件的稳定 latency proxy，也不覆盖 queueing/concurrency/thermal throttling。紧预算保留短模型，宽预算才允许长 reasoning。Owner `INFER-REQUEST-LIFECYCLE` Ch42，handoff Ch56/70。`Refine — Existing Argument Candidate`。

### High-Throughput LLM Inference on Heterogeneous Clusters — 25/30

- `heterogeneous-llm-inference-configuration-scheduling`；arXiv:2504.15303 v1 2025-04-18；已读 performance model、configuration search、capacity-aware scheduler、two-cluster evaluation、baselines、sensitivity 与 limitations。
- 同构副本和 round-robin 在设备、memory 与 link 相同的 fleet 中合理；异构 cluster 会让同一 placement 的 prefill/decode capacity 不对称。系统先枚举/估计 deployment configurations，再以 remaining capacity 和 request demand 进行 routing。
- control plane 拥有 device/topology/model/config profile，scheduler 拥有 queue/request/SLO/capacity；worker 只执行被选计划。profile freshness 与 admission decision 必须进入 trace。
- 作者在两套 cluster 报告相对 baselines 的 throughput 改善（最高 122.5%/33.6%），但 workload、模型、拓扑、估计误差和 SLO 绑定，不构成通用数字。搜索/模型复杂度换取利用率，也会 stale profile、热点与 starvation。Owner `INFER-SCHEDULING` Ch56，handoff Ch49/60。`Integrate — New Mechanism Candidate`。

### HPU — 26/30

- `hpu-attention-memory-coprocessor`；arXiv:2504.16112 v1 2025-04-18；已核验 HPU architecture、attention offload flow、HBM bandwidth/capacity model、FPGA prototype、GPU-only comparison、sensitivity 与 limitations。
- GPU-only serving 把 compute-heavy GEMM 与 bandwidth/capacity-heavy attention/KV 放在同一 HBM，长 context 时 memory pressure 主导。HPU 将 attention/KV state 放到专用 high-bandwidth memory co-processor，GPU 保留其他 layers，通过 link 交换 activations。
- runtime 必须拥有 layer partition、KV location、transfer buffer、ordering 与 failure state；HPU 拥有 KV/attention execution，GPU 不能假设 KV 本地。论文的 HBM3e 4.9 TB/s、144 GB 是 design point，实际验证含 FPGA/PCIe 限制。
- 作者模型预测/原型报告最高约 4.1× performance、4.6× energy，但不是量产同条件 GPU matched deployment。新风险是 link bottleneck、split failure domain、kernel/compiler portability 与 recovery。短 context/compute-bound 时 GPU-only 更简单。Owner `INFER-TENSORRT-LLM` Ch49，handoff Ch54/56。`Emerging / Experimental`。

### SlimPipe — 28/30

- `slimpipe-long-context-pipeline-parallelism`；arXiv:2504.14519 v1 2025-04-20；已读 sequence slicing、causal-load model、1F1B integration、redistribution algorithm、distributed implementation、baselines/ablations 与 limitations。
- 标准 PP 按 microbatch 均分在短序列近似平衡；长 causal attention 随 token position 增长，使早/晚 sequence slices 工作量不同，简单 sequence parallel 或 uniform stage assignment 产生 bubble/straggler。
- SlimPipe 在 microbatch 内切分 sequence，保留 1F1B 依赖，再按 causal attention workload 重分 slice/stage。scheduler 拥有 microbatch/slice/dependency/work estimate，collective runtime 拥有 activation/gradient transfer。
- Llama-70B、512K/2048K context、最高 256 Hopper 80GB；作者报告 512K 最多 1.57× MFU、2048K >45% 而部分 baselines OOM/降级。结果不覆盖其他 topology、model mix、failure recovery。复杂 schedule 与通信换取负载平衡。Owner `TRAIN-PIPELINE-PARALLEL` Ch38，handoff Ch39/41。`Integrate — New Mechanism Candidate`。

### Knowledge and Dataset Distillation Survey — 21/30

- `knowledge-dataset-distillation-survey-2025`；arXiv:2504.14772 v1 2025-04-20；已读 taxonomy、task/rationale/multi-teacher KD、gradient matching/latent/generative DD、applications、challenges 与 references；它是 secondary source，无新 artifact/evaluation。
- survey 将“把 teacher 行为迁移给 student”的 knowledge distillation 与“把 dataset 压缩为少量 synthetic/optimized samples”的 dataset distillation 分开，并梳理二者在目标、state owner、成本和 privacy 上的差异。
- 它可作为 discovery map，不能提供 matched model/hardware/data/SLO 证据，跨论文表格也不能排序机制优劣。生成式 DD 还带 teacher leakage、synthetic bias 和可删除性问题。
- 原始数据充足、训练预算可承受时无需强行蒸馏；受限部署或重复训练才可能值得。Owner `TRAIN-SFT` Ch29，handoff Ch27/66。`No Change — Secondary Taxonomy Already Covered`。

### Don't Retrieve, Generate — 22/30

- `dont-retrieve-generate-hard-negatives`；arXiv:2504.21015 v1 metadata 2025-04-20；已读 query generation、LLM hard-negative generation、training/evaluation、BM25/cross-encoder baselines、BEIR metrics、sampling settings 与 limitations。
- 从 corpus 检索 hard negatives 能保留真实分布，但受 index/teacher 能力限制且可能只得到 lexical negatives。论文先从 passage 生成 query，再仅给 query 让 LLM 生成 plausible-but-wrong negative，以增加语义难度。
- data pipeline 拥有 source passage、generated query/negative、generator/version/seed 与 false-negative audit；trainer 不应把 synthetic negative 当作天然真实标签。公开 generation 设置含 temperature 0.6、top-p 0.95、top-k 20、max 1024。
- E5/GTE、BEIR 的 nDCG@10/P@10/R@100 支持作者设置下可接近检索 negatives；不证明 domain transfer、无 leakage 或更低端到端成本。生成带来 false negative、semantic artifacts 与 vendor dependence。Owner `AGENT-RAG` Ch76，handoff Ch27。`Emerging / Experimental`。

## Low-score Source / Date / Rejection Closure

#### Transformers v4.51.3 — 16/30

- Official Hugging Face release 2025-04-14；`transformers-v4.51.3`。评分 2/2/3/5/2/2；tag/release identity 已核验。
- patch 集合主要是 compatibility/bug/model support 更新，未形成独立长期机制或设计结论；不能把 release list 当作新 runtime architecture。`Weekly Only — Patch Fact`。

#### Self-Correction Makes LLMs Better Parsers — 18/30

- arXiv:2504.14165 v1 2025-04-19；`self-correction-llm-parsers`。评分 3/2/3/4/3/3；paper identity、method、parsing tasks 与 evaluation 已核验。
- 用 grammar-rule retrieval、hints/examples 让 LLM 修正 structured parsing，属于窄任务 workflow；没有跨 domain/runtime 的新 owner，也未证明通用 self-correction。`Weekly Only — Narrow Application Evidence`。

#### Multi-Agent Hazardous Object Detection — 18/30

- arXiv:2504.13399 v1 2025-04-18；`multi-agent-hazardous-object-detection`。评分 3/3/3/4/3/2；正文与扩展 COOOLer evaluation 已核验。
- VLM/LLM/CLIP agents 联合识别危险物体并用 cosine semantics 聚合，主要是 domain composition；未给出可迁移的 coordination/state mechanism 或生产 threat model。`Weekly Only — Domain System Case`。

#### FAIRGAME — 19/30

- arXiv:2504.14325 v1 2025-04-19；`fairgame-multi-agent-bias-simulator`。评分 3/3/3/4/3/3；framework、game scenarios、model comparisons、limitations 已核验。
- 标准化 game-theoretic simulator 可研究语言/personality bias，但结果强依赖 prompt、model 与 game rule；它是有用的窄 benchmark framework，不足以改变 Multi-Agent architecture。`Weekly Only — Evaluation Framework Case`。

## Final Gate Reconciliation

### Canonical Ledger

- Owner-week window：2025-04-14～2025-04-20，ISO 校验 Pass。
- W15 spillback：13 families，均未在原 W16 39-row table，故原分母仍为 38 个 `20+` + 1 low。
- Discovery replay additions：8 个 `20+` + 3 low。
- Final denominator：**50 unique Source Families = 46 个 `20+` + 4 low**。
- Strict Full Source Review：**46/46**；其中 44 Verified/closed，1 `Unverified / Blocked`，1 `Disputed`；普通 `Review Pending = 0`。
- Low-score source/date/score/rejection：**4/4**。
- Cross-week dedup：BitNet/FramePack/Antidistillation 后续 revision 仅作 family evolution；vLLM v0.8.4 留在 W16；W15 13 families 不重复计分。

### Evidence Boundary and Dispositions

- `Unverified / Blocked — P2 Artifact`：OpenAI Codex CLI。公开公告可锁定 2025-04-16 launch fact，但缺 event-time tag/commit/tree，当前 repository 不可反投影 launch defaults/implementation。
- `Disputed — P3 Revision`：ReZero。arXiv metadata 显示 v1 2025-04-15，但当前 HTML manuscript 显示 2026-08-11；在取得事件时正文前只保留 identity/date，不采用当前 mechanism/results。
- 官方产品页面均只沉淀 version/product fact；未公开 model/training/runtime mechanism 统一写 `Not Disclosed`。
- 作者 benchmark 均绑定本文披露的 model/data/hardware/precision/length/batch/concurrency/SLO；未披露字段不补推，作者结果不外推为通用事实。

### Discovery Replay Gate

- Fixed organizations：按 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI、Hugging Face 顺序重放；恢复 Preparedness Framework v2，其他公告无独立公开机制 owner。
- arXiv：按 2025-04-14～20、cs.AI/cs.CL/cs.LG/cs.DC/cs.SE/cs.CV 与 AI-system keywords 重放并进行 owner/date 去重；恢复 7 high 与 3 low families。
- Cross-index：DBLP/Crossref metadata 用于 identifier/date/venue 交叉；Scholar/OpenAlex 可用于发现，但本次无法取得可机器复算的完整查询导出。
- AI Infra：按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime、OpenXLA 重放；保留 vLLM v0.8.4，Transformers v4.51.3 低分闭合。

### Gate Status and Missing Materials

- Candidate Evidence Gate：**Conditional Open**。普通 reading backlog 已清零；只剩 1 blocked + 1 disputed，均有精确材料请求。
- Discovery / Archive Gate：**Conditional Open**。固定来源与关键词 replay 已闭合；若要求证明“全量召回可复算”，仍缺 Scholar/OpenAlex query/export snapshot。
- Historical Books Gate：**Closed**；本文件没有授权 Books Integration。
- P2 Artifact request：OpenAI Codex CLI 2025-04-16 launch tag、commit SHA、source tree archive 或官方 release source hash；可接受 GitHub archive、tarball、signed release notes 或 Internet Archive snapshot。
- P3 Revision request：ReZero arXiv:2504.11001 v1 PDF/TeX/source hash 或 2025-04-15 archive snapshot，用于比对 current 2026 manuscript 的 method/evaluation 变更。
- P4 Discovery Export request（仅 Archive Completion Gate 需要）：Scholar/OpenAlex 针对 2025-04-14～20 的查询字符串、过滤条件、结果导出与抓取时间；不影响已确认 46 个 high packet 的 evidence closure。

## Primary Sources

- OpenAI: https://openai.com/index/gpt-4-1/ ; https://openai.com/index/introducing-o3-and-o4-mini/ ; https://openai.com/index/updating-our-preparedness-framework/ ; https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
- Anthropic: https://www.anthropic.com/news/research
- Google: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-april-2025/
- W16 arXiv owner range: https://arxiv.org/abs/2504.10277 ; https://arxiv.org/abs/2504.10326 ; https://arxiv.org/abs/2504.10337 ; https://arxiv.org/abs/2504.10449 ; https://arxiv.org/abs/2504.10462 ; https://arxiv.org/abs/2504.10479 ; https://arxiv.org/abs/2504.10481 ; https://arxiv.org/abs/2504.10766 ; https://arxiv.org/abs/2504.10903 ; https://arxiv.org/abs/2504.11001 ; https://arxiv.org/abs/2504.11320 ; https://arxiv.org/abs/2504.11343 ; https://arxiv.org/abs/2504.11346 ; https://arxiv.org/abs/2504.11393 ; https://arxiv.org/abs/2504.11442 ; https://arxiv.org/abs/2504.11455 ; https://arxiv.org/abs/2504.11536 ; https://arxiv.org/abs/2504.11651 ; https://arxiv.org/abs/2504.12285 ; https://arxiv.org/abs/2504.12369 ; https://arxiv.org/abs/2504.12516 ; https://arxiv.org/abs/2504.12626 ; https://arxiv.org/abs/2504.13032 ; https://arxiv.org/abs/2504.13079 ; https://arxiv.org/abs/2504.13145 ; https://arxiv.org/abs/2504.13146 ; https://arxiv.org/abs/2504.13161 ; https://arxiv.org/abs/2504.13169 ; https://arxiv.org/abs/2504.13171 ; https://arxiv.org/abs/2504.13173 ; https://arxiv.org/abs/2504.13180 ; https://arxiv.org/abs/2504.13181
- Discovery additions: https://arxiv.org/abs/2504.13471 ; https://arxiv.org/abs/2504.14350 ; https://arxiv.org/abs/2504.15303 ; https://arxiv.org/abs/2504.16112 ; https://arxiv.org/abs/2504.14519 ; https://arxiv.org/abs/2504.14772 ; https://arxiv.org/abs/2504.21015 ; https://arxiv.org/abs/2504.14165 ; https://arxiv.org/abs/2504.13399 ; https://arxiv.org/abs/2504.14325
- vLLM v0.8.4: https://github.com/vllm-project/vllm/releases/tag/v0.8.4
- Transformers v4.51.3: https://github.com/huggingface/transformers/releases/tag/v4.51.3
