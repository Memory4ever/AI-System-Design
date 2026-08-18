# AI Research Weekly — 2025-W26

> Coverage Window: 2025-06-23～2025-06-29
> Research Mode: Retrospective Primary-Source Backfill
> Re-audited: 2026-08-22
> Audit Status: Candidate Evidence Gate Passed — 40/40 Retained Strict
> Historical Books Gate: Closed

## Executive Summary

旧档案把本周写成空周，完整重放后该结论不成立。当前恢复44个scored owner：40项达到`20+`并全部完成strict Full Source Review，4项低分完成source/date/score/rejection closure；Review Pending、Blocked与Disputed均为0。revision、release和spillback按first-public date去重后，W26 Candidate Evidence Gate通过；Historical Books Gate仍关闭，本轮不修改Books。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。
- later revision只用于核验lineage，不作为新的W26事件，也不把后版结果倒写event-time packet。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- official owner包含Gemini Robotics On-Device、AlphaGenome、Gemma 3n full release、Qwen VLo preview、Hunyuan-A13B与Project Vend 1；产品事实与公开机制严格分开。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 当前论文owner按06-23～06-29 v1归档；40个retained family均回到event-time正文完成Method、evaluation、limitations与artifact审计。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- vLLM 0.9.1、Ray 2.47.0、DeepSpeed 0.17.1、Transformers 4.52.4、TensorRT-LLM 0.20.0、SGLang RFC/0.4.7均按真实release date回拨相邻周，不在W26重复评分。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Gemini Robotics On-Device | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| AlphaGenome | 4 | 3 | 3 | 5 | 3 | 4 | 22/30 | Full Source Review Complete — Domain Evidence |
| Gemma 3n full release | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Release Node |
| Qwen VLo preview | 3 | 3 | 3 | 3 | 4 | 3 | 19/30 | Low-score closure — Mechanism Not Disclosed |
| Hunyuan-A13B | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| Project Vend 1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Vision as a Dialect | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| ReasonFlux-PRM | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| CommVQ | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Source Review Complete |
| LongWriter-Zero | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| Adaptive Activation Steering / STU-PID | 3 | 3 | 3 | 5 | 3 | 3 | 20/30 | Full Source Review Complete — Experimental |
| Understanding Software Engineering Agents | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| Context-Aware CodeLLM Eviction | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| Chain-of-Experts | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| SlimMoE | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| AggTruth | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Full Source Review Complete — Experimental |
| HOLA | 4 | 4 | 5 | 5 | 4 | 4 | 26/30 | Full Source Review Complete — Experimental |
| PARALLELPROMPT | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| Radial Attention | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| HiMA-Ecom / JoyAgents-R1 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| KnowRL | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Why Do Open-Source LLMs Struggle with Data Analysis? | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Evaluation Evidence |
| SAGE query rewriting | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| SRFT | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| PLoP precise LoRA placement | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| Leaner Training, Lower Leakage | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Decrypto Benchmark | 3 | 3 | 3 | 5 | 2 | 3 | 19/30 | Low-score closure |
| π-CoT / Prolog-Initialized CoT | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| CoMind / MLE-Live | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| When Life Gives You Samples | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete |
| AIMeter | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| Model Editing as a Double-Edged Sword / BehaviorBench | 3 | 3 | 3 | 5 | 2 | 3 | 19/30 | Low-score closure |
| DiffuCoder | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Perry cyber deception framework | 3 | 3 | 3 | 5 | 2 | 2 | 18/30 | Low-score closure |
| Grokking in LLM Pretraining? | 3 | 3 | 3 | 5 | 4 | 3 | 21/30 | Full Source Review Complete — Interpretability Evidence |
| Potemkin Understanding | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| Mind2Web 2 | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Full Source Review Complete |
| Bridging Offline and Online RL for LLMs | 4 | 4 | 4 | 5 | 5 | 5 | 27/30 | Full Source Review Complete |
| Efficient and Reusable Cloud Configuration Search | 3 | 4 | 5 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| Automated LLM Speedrunning Benchmark | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| HyperCLOVA X THINK | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete |
| QuickSilver dynamic token halting | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review Complete — Experimental |
| OptScale | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| Sub-MoE | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |

账目：44 scored owners；40项20+且40/40 strict Full Source Review；4/4低分闭合；Review Pending 0、Blocked 0、Disputed 0。

## Full Source Review

### Gemini Robotics On-Device

- **Primary / date / owner:** DeepMind official announcement 2025-06-24 + Gemini Robotics family report，29/30；`MULTIMODAL-EMBODIED-VLA` Ch26。
- **Problem / mechanism / ownership:** cloud/large VLA能力强却不满足offline、latency与device constraints。on-device VLA把perception-language-action state与low-level execution迁到本地，并以50–100 demonstrations适配；device runtime拥有local observation/action state，controller/environment拥有physical commit。
- **Evidence boundary:** ALOHA/Franka/Apollo等event-time setup支持local deployment/adaptation，不证明universal real-time safety或未公开training mechanism。
- **Trade-off / coexistence / disposition:** device memory、thermal、model update与calibration；非实时、高compute planning仍可cloud。Books Pending — `Refine Existing Argument`。

### AlphaGenome

- **Primary / date / owner:** DeepMind official announcement/preprint 2025-06-25，22/30；`TRAIN-DATA`。
- **Problem / mechanism / ownership:** 窄assay下fixed-window predictor合理；million-base context与多output modalities需要shared sequence representation与multitask heads。DNA sequence+variant进入model，输出functional tracks/effects，biological evidence owner仍在外部实验。
- **Evidence boundary:** 支持genomic prediction utility，不证明causal truth或clinical validity；2026 Nature paper仅是forward publication。
- **Disposition:** `Weekly Only — Domain Evidence`；不把领域结果外推为通用AI System机制。

### Gemma 3n full release

- **Primary / date / owner:** Google Developers 2025-06-26 + model card/docs，26/30；`MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** May preview给出方向，full release才提供downloadable mobile-first multimodal weights/runtime contract及selective activation/memory features；artifact registry拥有version，device runtime拥有execution state。
- **Evidence boundary:** 证明version/artifact availability，不证明generic edge superiority；device、quantization与modality SLO均configuration-bound。
- **Disposition:** `Weekly Only — Version/Product Fact`，回链May family，不重复发明模型owner。

### Hunyuan-A13B

- **Primary / date / owner:** official report/model card/repo 2025-06-27，28/30；`MODEL-MOE` Ch21。
- **Problem / mechanism / ownership:** dense容量简单但昂贵。80B-total/13B-active fine-grained MoE、GQA、256K、fast/slow thinking与BF16/FP8/GPTQ artifacts共同改变active-state和deployment contract；router/expert placement由runtime管理。
- **Evidence boundary:** 只证明released family在披露benchmarks/recipes下的行为，不证明universal quality/cost。
- **Trade-off / coexistence / disposition:** routing imbalance、expert placement、quantization variance与long-context memory；portable/smaller workloads仍适合dense。Books Pending — `Refine Existing Argument`。

### Project Vend 1

- **Primary / date / owner:** Anthropic research 2025-06-27，26/30；`AGENT-WORKFLOW` Ch81。
- **Problem / mechanism / ownership:** 短benchmark隐藏long-running business state。Claude Sonnet3.7在真实office shop运行一个月，使用email/tools并维护inventory/pricing records；environment/human setup拥有真实机会与约束，Agent只在其workflow内决策。
- **Evidence boundary:** longitudinal evidence暴露planning、accounting、customer interaction failure，不证明economic autonomy或纯model capability。
- **Trade-off / coexistence / disposition:** state drift、bad pricing、identity confusion与弱escalation；scripted/human workflow仍是release gate。Books Pending — `Refine Existing Argument`。

### Vision as a Dialect

- **Primary / date / owner:** `2506.18898`，v1 2025-06-23，27/30；`MULTIMODAL-REPRESENTATION` Ch23。
- **Problem / mechanism / ownership:** continuous image encoder与text tokens的identity/scale不兼容。该工作学习text-aligned discrete visual units，使用scale-adaptive encoding/decoding，供AR understanding与diffusion reconstruction共享；tokenizer/codebook拥有representation identity。
- **Evidence boundary:** 作者tasks支持shared dialect可行，不证明lossless modality equivalence。
- **Trade-off / coexistence / disposition:** tokenizer bottleneck、codebook collapse、resolution/provenance identity；precision workload仍适合modality-specific representation。Books Pending — `Integrate New Mechanism Candidate`。

### ReasonFlux-PRM

- **Primary / date / owner:** `2506.18896`，v1 2025-06-23，26/30；`TRAIN-GRPO` Ch33。
- **Problem / mechanism / ownership:** outcome reward不能定位reasoning failure，independent step reward忽略trajectory dependence。trajectory-aware PRM在整条path内score step/state，并供offline rerank、online selection/RL与Best-of-N使用；verifier只提供derived reward evidence。
- **Evidence boundary:** 作者math/reasoning gains支持trajectory supervision，不证明latent reasoning faithful或verifier robust。
- **Trade-off / coexistence / disposition:** process data、reward hacking与long-context scoring；executable final answer仍适合outcome verifier。Books Pending — `Refine Existing Argument`。

### CommVQ

- **Primary / date / owner:** `2506.18879`，v1 2025-06-23，29/30；`INFER-KV-CACHE` Ch45。
- **Problem / mechanism / ownership:** full-precision KV精确但长上下文memory高，naive VQ可能破坏RoPE/identity。additive vector quantization用与rotary position transform可交换组合的codebooks压缩K/V；codebook/version成为cache identity一部分。
- **Evidence boundary:** 作者2-bit/1-bit结果支持named models中的memory-quality trade-off，不证明universal latency/accuracy或所有position encoding。
- **Trade-off / coexistence / disposition:** encode/decode、codebook state与quantization drift；敏感layers/SLO仍可uncompressed/selective KV。Books Pending — `Integrate New Mechanism Candidate`。

### LongWriter-Zero

- **Primary / date / owner:** `2506.18841`，v1 2025-06-23，25/30；`TRAIN-GRPO` Ch33。
- **Problem / mechanism / ownership:** finite-length SFT易教出early stop、drift与format collapse。该工作从base model直接RL，以length、quality、format rewards优化ultra-long trajectories；trainer拥有rollout/reward state。
- **Evidence boundary:** 支持该reward/data contract下long-writing behavior出现，不证明任意长度的事实连贯，judge/reward leakage仍在。
- **Trade-off / coexistence / disposition:** 巨量rollout tokens、sparse credit与verbosity gaming；结构已知时SFT/outline workflow仍更好。Books Pending — `Refine Existing Argument`。

### Adaptive Activation Steering / STU-PID

- **Primary / date / owner:** `2506.18831`，v1 2025-06-23，20/30；`MODEL-DECODER-ONLY`。
- **Mechanism / evidence:** static steering假设每个token/state同一强度；STU-PID从observed deviation形成error，经P/I/D controller调下一次activation intervention。小型DeepSeek-R1-Distill-Qwen-1.5B subset仅支持proof of concept，不证明broad controllability或safety。
- **Trade-off / disposition:** controller tuning、oscillation、integral wind-up与probe dependency；稳定任务仍可static/no steering。`Emerging / Experimental`。

### Understanding Software Engineering Agents

- **Primary / date / owner:** `2506.18824`，v1 2025-06-23，27/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / evidence:** 分析RepairAgent、AutoCodeRover、OpenHands的120 trajectories/2,822 LLM interactions，把navigation、patching、testing与recovery拆开，显示harness/tool use调节observed capability；只证明该样本taxonomy，不代表生产ranking或correctness。
- **Trade-off / disposition:** trace-label subjectivity与agent-sample限制；executable tests必要但不充分。Books Pending — `Refine Existing Argument`。

### Context-Aware CodeLLM Eviction

- **Primary / date / owner:** `2506.18796`，v1 2025-06-23，28/30；`INFER-SCHEDULING`。
- **Mechanism / evidence:** homogeneous workload下LRU/model-size合理；多CodeLLM的load cost、latency sensitivity、output length和demand不同。multifactor policy结合recent/future demand与service cost做eviction；trace/simulator只证明其setup收益，不是generic optimum。
- **Trade-off / disposition:** demand prediction、model identity/freshness和load-cost telemetry，错预测会thrash；telemetry稀疏仍可LRU。Books Pending — `Integrate New Mechanism Candidate`。

### Chain-of-Experts

- **Primary / date / owner:** `2506.18945`，v1 2025-06-23，27/30；`MODEL-MOE`。
- **Mechanism / evidence:** 标准MoE每layer一次并行top-k；CoE让token顺序通过iterative expert chain，后续route依赖先前output，新增per-token route depth state。作者models只证明feasibility，不证明universal scaling。
- **Trade-off / disposition:** latency、routing collapse与placement更难；吞吐优先仍可parallel top-k。Books Pending — `Integrate New Mechanism Candidate / Experimental`。

### SlimMoE

- **Primary / date / owner:** `2506.18349`，v1 2025-06-23，28/30；`MODEL-MOE`。
- **Mechanism / evaluation:** 保留expert count，按sensitivity在experts内部均匀prune neurons，geometric intermediate pruning与top-8-logit distillation交替。Phi-3.5-MoE 41.9B/6.6B-active经400B tokens压到7.6B/2.4B与3.8B/1.1B；stages、criterion、stopping、dense与inference cost均有ablation。
- **Boundary / disposition:** 证明该teacher/family可压缩，不证明所有MoE；付出teacher logits、多阶段training与uniform-width assumption。Books Pending — `Integrate New Mechanism Candidate`。

### AggTruth

- **Primary / date / owner:** `2506.18628`，v1 2025-06-23，24/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / evidence:** 聚合selected attention-head对supplied passage的scores，作为contextual hallucination detector feature；same/cross-task和head selection支持有限检测价值，不证明causal attribution或architecture portability。
- **Trade-off / disposition:** white-box access、head calibration与version coupling；高风险仍以external claim-evidence verifier为canonical。`Emerging / Experimental`。

### HOLA

- **Primary / date / owner:** `2506.18952`，v1 2025-06-23，26/30；`INFER-REQUEST-LIFECYCLE`。
- **Mechanism / evidence:** 把hierarchical speculative decoding、AdaComp-RAG与LoRA/pruning/quantization组合为edge prototype；Jetson Nano与task结果只支持其prototype，不证明production-ready或lossless。state跨retrieval decision、draft hierarchy、compressed weights与verifier commit。
- **Trade-off / disposition:** failure attribution困难；单一SLO下独立机制更简单。`Emerging / Experimental`。

### PARALLELPROMPT

- **Primary / date / owner:** `2506.18728`，v1 2025-06-23、v2 06-26，28/30；`INFER-SCHEDULING`。
- **Mechanism / evidence:** 对translation/comparison/list等含独立iterations的prompt，parser抽取template、shared context与dependency graph，并行执行后比较latency、structure与semantic fidelity。>37K prompts支持curated parsing及named tasks up-to 5×，不证明arbitrary prompt safety/cost。
- **Trade-off / disposition:** decomposition error、duplicated context/KV与aggregation order；coupled reasoning仍应monolithic。Books Pending — `Integrate New Mechanism Candidate`。

### Radial Attention

- **Primary / date / owner:** `2506.19852`，v1 2025-06-24，25/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Mechanism / evidence:** long-video diffusion full attention平方成本；Radial静态sparse mask按spatiotemporal energy decay构造近O(n log n) connectivity。作者video generation只支持tested models，不覆盖all motion/resolution。
- **Trade-off / disposition:** handcrafted decay/mask可能漏global events；短或全局耦合场景仍可dense。Books Pending — `Integrate New Mechanism Candidate / Experimental`。

### HiMA-Ecom / JoyAgents-R1

- **Primary / date / owner:** `2506.19846`，v1 2025-06-24，26/30；`AGENT-MULTI-AGENT`。
- **Mechanism / evidence:** hierarchical manager委派specialists，VR-GRPO训练verifiable steps，adaptive memory携带task state；e-commerce benchmarks只支持family-specific improvement，不证明enterprise autonomy。
- **Trade-off / disposition:** manager bottleneck、memory provenance、communication tax与correlated errors；decomposition/headroom弱时single agent更好。Books Pending — `Refine Existing Argument`。

### KnowRL

- **Primary / date / owner:** `2506.19807`，v1 2025-06-24，26/30；`TRAIN-GRPO`，handoff `PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** outcome-only RL在数学等可验证任务中合理，但事实型slow thinking可能在中间步骤编造知识仍获得终局奖励。KnowRL把外部knowledge verification形成的factuality reward并入RL；知识源/verifier拥有evidence state，model只学习policy，不获得runtime真值保证。
- **Evaluation boundary:** 三个hallucination与两个reasoning datasets支持该reward contract下降低幻觉并保持reasoning；不证明模型形成可靠“自知”、知识源无误或OOD事实安全。
- **Trade-off / coexistence / disposition:** verifier coverage、reward hacking、知识版本与训练成本；可执行答案仍可用outcome reward，高风险事实仍需runtime evidence。Books Pending — `Refine Existing Argument`。

### Why Do Open-Source LLMs Struggle with Data Analysis?

- **Primary / date / owner:** `2506.19794`，v1 2025-06-24，22/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** 单一最终答案分数不能区分data understanding、code generation和strategic planning。工作以seed scenarios拆成三维行为审计，再由failure taxonomy指导data synthesis；harness拥有data/interaction/judge contract，execution environment拥有代码结果。
- **Evaluation boundary:** 作者实验支持planning是主要瓶颈、data quality比diversity更关键；不证明open-source模型的普遍因果，也不能把harness差异归为model capability。
- **Trade-off / coexistence / disposition:** synthetic-data偏差、scenario coverage与judge leakage；静态benchmark仍适合窄能力回归。Books Pending — `Refine Existing Argument / Evaluation Evidence`。

### SAGE: Strategy-Adaptive Generation Engine for Query Rewriting

- **Primary / date / owner:** `2506.19783`，v1 2025-06-24，27/30；`AGENT-RAG`。
- **Problem / mechanism / ownership:** supervised rewriter依赖标注，unconstrained RL探索低效；SAGE以expert-crafted strategies构成action set，用Strategic Credit Shaping与Contrastive Reward Shaping给策略和检索结果credit。policy选择strategy/rewrite，retriever返回ranking，trainer拥有reward/update state。
- **Evaluation boundary:** HotpotQA、FEVER、NFCorpus、SciFact的NDCG@10及rewrite-cost结果支持strategy-guided RL；不证明任意retriever/domain稳定，也不保证rewrite忠实于用户意图。
- **Trade-off / coexistence / disposition:** strategy taxonomy维护、retriever coupling、reward gaming；简单query仍适合no rewrite或规则rewrite。Books Pending — `Integrate New Mechanism Candidate`。

### SRFT

- **Primary / date / owner:** `2506.19767`，v1 2025-06-24，26/30；`TRAIN-GRPO`，handoff `TRAIN-SFT`。
- **Problem / mechanism / ownership:** 两阶段SFT→RL边界清晰但可能stage mismatch/遗忘；SRFT在single-stage同时计算SFT与RL loss，以entropy-aware weighting调贡献。demonstration与rollout共享policy update，trainer拥有entropy/reward/optimizer state。
- **Evaluation boundary:** 五个数学与三个OOD benchmark、entropy dynamics支持该setup优于zero-RL baseline；不证明single-stage普遍优于sequential curriculum或跨模型稳定。
- **Trade-off / coexistence / disposition:** 双数据流、weight calibration、reward variance与objective interference；数据少或release需可解释阶段边界时two-stage仍合理。Books Pending — `Refine Existing Argument`。

### PLoP: Precise LoRA Placement

- **Primary / date / owner:** `2506.20629`，v1 2025-06-25，27/30；`TRAIN-LORA`。
- **Problem / mechanism / ownership:** 固定在Q/K/V或MLP放LoRA简单可移植，但不同model/task的有效更新位置不同。PLoP用task-conditioned lightweight criterion选择module types，再只为选中位置建立adapter；registry拥有placement/rank/base-version identity。
- **Evaluation boundary:** supervised FT与reasoning RL placement comparisons支持自动选择可匹配/优于常用规则；不证明criterion无需重测即可跨architecture/task迁移。
- **Trade-off / coexistence / disposition:** profiling、task overfit、module naming/version coupling；快速通用adaptation仍可uniform placement。Books Pending — `Integrate New Mechanism Candidate`。

### Leaner Training, Lower Leakage

- **Primary / date / owner:** `2506.20856`，v1 2025-06-25，26/30；`TRAIN-LORA`，handoff `PLATFORM-SECURITY`。
- **Problem / mechanism / ownership:** full FT的memorization规律不能直接外推LoRA。论文在同类fine-tuning tasks上比较full FT/LoRA，并以relaxed similarity extraction metric测泄漏；trainer拥有adapter update，auditor拥有prompt/response matching state。
- **Evaluation boundary:** 作者设置支持LoRA较full FT降低memorization并保持task quality；不证明LoRA具备隐私保证、抵抗所有extraction或消除pretraining leakage。
- **Trade-off / coexistence / disposition:** metric阈值、attack coverage与utility/privacy operating point；高capacity domain shift仍可能需要full FT和独立privacy controls。Books Pending — `Refine Existing Argument`。

### π-CoT / Prolog-Initialized CoT

- **Primary / date / owner:** `2506.20642`，v1 2025-06-25，26/30；`AGENT-PLANNING`，handoff `AGENT-RAG`。
- **Problem / mechanism / ownership:** free-form CoT灵活却在multi-hop RAG中易循环/漏依赖。π-CoT把问题编译为Prolog query和single-hop subqueries，形成intermediate artifacts再初始化CoT；logic engine拥有symbolic state，retriever提供evidence，LLM只拥有proposal。
- **Evaluation boundary:** multi-hop QA comparisons支持比standard RAG/in-context CoT更稳；不证明自然语言到Prolog编译总正确或开放域事实完备。
- **Trade-off / coexistence / disposition:** schema/parse failure、串行延迟与symbol grounding；无法形式化或短问题仍适合普通RAG/CoT。Books Pending — `Integrate New Mechanism Candidate`。

### CoMind / MLE-Live

- **Primary / date / owner:** `2506.20640`，v1 2025-06-25，28/30；`AGENT-MULTI-AGENT`，evaluation handoff `PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** 单agent固定offline任务易评测，却缺并行探索、知识交换与live deadline变化。CoMind维护多solution branches、共享外部知识并迭代selection；orchestrator拥有branch/budget/provenance，workers拥有local workspace，leader拥有submission commit。
- **Evaluation boundary:** 75个历史competition的36% medal rate及8个live competitions支持该scaffold机会；不证明基础模型独立能力、生产ML正确性或多agent普遍优于single-agent headroom。
- **Trade-off / coexistence / disposition:** communication tax、shared-error amplification、leader bottleneck与contamination；低可分解任务仍应single agent。Books Pending — `Refine Existing Argument`。

### When Life Gives You Samples

- **Primary / date / owner:** `2506.20544`，v1 2025-06-25，24/30；`MODEL-SAMPLING`。
- **Problem / mechanism / ownership:** fixed-temperature single sample成本低，但open-ended multilingual tasks缺统一verifier。方法按language/task调temperature生成parallel candidates，再以适配selector提交final response；sampler拥有candidate set，selector拥有score/calibration，runtime拥有budget。
- **Evaluation boundary:** 8B、Command-A与m-ArenaHard-v2.0等作者结果支持少量samples提升win-rate；不证明judge无偏、所有语言受益或总成本最优。
- **Trade-off / coexistence / disposition:** N倍decode、selector bias与candidate correlation；强SLO/低价值请求仍应single sample。Books Pending — `Refine Existing Argument`。

### AIMeter

- **Primary / date / owner:** `2506.20535`，v1 2025-06-25，29/30；`PLATFORM-MONITORING`，handoff `PLATFORM-COST`。
- **Problem / mechanism / ownership:** 框架零散energy/power counters不能形成可复算AI workload contract。AIMeter统一采集细粒度time series，把energy、power、hardware performance与time/location carbon factor关联；collector拥有raw telemetry，analysis拥有derived metrics，manifest拥有model/hardware/workload identity。
- **Evaluation boundary:** artifact与作者cases支持集成和报告复现；不证明carbon因果归属、跨硬件计量等价或default overhead可忽略。
- **Trade-off / coexistence / disposition:** sampling overhead、sensor calibration、regional factor freshness；粗粒度capacity accounting仍可用provider meter。Books Pending — `Integrate New Mechanism Candidate`。

### DiffuCoder

- **Primary / date / owner:** `2506.20639`，v1 2025-06-25，27/30；`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Problem / mechanism / ownership:** AR code generation有因果顺序和KV复用；masked diffusion能全局refine但RL likelihood估计不成熟。7B dLLM在130B code tokens训练，并用complementary mask noise构造coupled-GRPO降token likelihood variance；denoiser拥有mutable mask/state，sampler决定更新顺序，trainer拥有paired rollout/reward。
- **Evaluation boundary:** EvalPlus与温度/顺序分析支持该模型的diffusion-native RL；不证明dLLM替代AR、具有wall-clock优势或通用代码正确性。
- **Trade-off / coexistence / disposition:** iterative passes、mutable-state commit/rollback与cache困难；低延迟streaming仍适合AR。Books Pending — `Integrate New Mechanism Candidate / Experimental`。

### Grokking in LLM Pretraining?

- **Primary / date / owner:** `2506.21551`，v1 2025-06-26，21/30；`MODEL-WHAT-NEURAL-NETWORKS-LEARN`，handoff `TRAIN-PRETRAINING`。
- **Problem / mechanism / ownership:** global train loss不能显示不同data groups何时形成transferable structure。论文追踪样本跨层expert-choice pathways，以pathway similarity和相邻层aggregated-expert consistency作训练内generalization proxy；router trace只归trainer telemetry所有。
- **Evaluation boundary:** named MoE/pretraining setup中metrics随downstream improvement变化，支持local asynchronous grokking解释；不证明proxy具有因果性或跨architecture已校准。
- **Trade-off / coexistence / disposition:** 需router traces且易与load balancing混淆；dense model或release gate仍需held-out evaluation。Books Pending — `Refine Existing Argument / Interpretability Evidence`。

### Potemkin Understanding

- **Primary / date / owner:** `2506.21521`，v1 2025-06-26，29/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** 标准accuracy隐含模型错误结构与人类相似，可能被表面pattern满足。论文区分answer correctness与跨reformulations/implications的concept consistency，并以专门benchmark和lower-bound procedure测potemkin prevalence；evaluator拥有concept/rubric graph。
- **Evaluation boundary:** 多模型、task、domain支持内部不一致广泛存在；不证明模型完全不理解、内部representation机制或任意deployment failure rate。
- **Trade-off / coexistence / disposition:** counterfactual item construction与human-concept assumption；标准benchmark仍适合回归但不能单独承载capability claim。Books Pending — `Integrate New Evaluation Mechanism`。

### Mind2Web 2

- **Primary / date / owner:** `2506.21506`，v1 2025-06-26，29/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW`。
- **Problem / mechanism / ownership:** 静态短网页任务无法覆盖real-time browsing、长程综合与citation。130个长程tasks以tree-structured rubric生成task-specific judges，分别核answer correctness和source attribution；browser拥有live state，agent拥有trajectory，judge拥有rubric/evidence snapshot。
- **Evaluation boundary:** 十个frontier systems与human comparison/error analysis支持benchmark判别力；不证明judge等于ground truth、跨时间完全可复现或model-only capability。
- **Trade-off / coexistence / disposition:** web drift、judge cost/bias、source availability；稳定窄任务仍适合deterministic tests。Books Pending — `Refine Existing Argument`。

### Bridging Offline and Online RL for LLMs

- **Primary / date / owner:** `2506.21495`，v1 2025-06-26，27/30；`TRAIN-DPO`，handoff `TRAIN-GRPO`。
- **Problem / mechanism / ownership:** offline preference optimization便宜稳定，但policy变化后coverage不足；fully online新鲜却昂贵。论文比较offline、semi-online、online DPO/GRPO及多类reward；buffer拥有data freshness/provenance，policy生成on-policy samples，trainer管理reward/update。
- **Evaluation boundary:** 作者结果显示online/semi-online相近且优于offline、多任务reward有益；不证明任意reward/model相同，也不消除online sampling bias。
- **Trade-off / coexistence / disposition:** rollout成本、reward drift与replay provenance；静态高质量preference data和低预算仍适合offline DPO。Books Pending — `Refine Existing Argument`。

### Efficient and Reusable Cloud Configuration Search

- **Primary / date / owner:** `2506.21467`，v1 2025-06-26，25/30；`PLATFORM-GPU-SCHEDULER`，handoff `PLATFORM-COST`。
- **Problem / mechanism / ownership:** 每workload独立search在小空间合理，cloud+application参数形成百万级space后重复试验昂贵。Discovery Space显式建模parameter domain、constraints、objectives和observations，使optimizers共享/迁移execution evidence；controller拥有search state，executor拥有run state，catalog拥有provenance。
- **Evaluation boundary:** LLM inference与Big Data cases及作者>90% search speed-up支持reuse potential；不证明任意cloud topology最优、transfer无negative bias或production SLO安全。
- **Trade-off / coexistence / disposition:** schema matching、stale observations、exploration cost与constraint violations；小或一次性space仍可手工/独立optimizer。Books Pending — `Integrate New Mechanism Candidate`。

### Automated LLM Speedrunning Benchmark

- **Primary / date / owner:** `2506.22419`，v1 2025-06-27，26/30；`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** code score不测AI能否复现hardware-aware training innovation，完整research replication又难归因。benchmark从NanoGPT speedrun构造19个可执行tasks，给previous-record script和分级hints，以training result验证patch；harness拥有baseline/hardware/time contract，agent拥有patch，runner拥有commit/result。
- **Evaluation boundary:** recent reasoning LLM+scaffolds即使详细hint仍困难，支持benchmark未饱和；不证明autonomous science整体能力或未披露hardware公平性。
- **Trade-off / coexistence / disposition:** benchmark-specific optimization、GPU variance与hint leakage；普通SWE tests仍适合维护任务。Books Pending — `Integrate Evaluation Mechanism`。

### HyperCLOVA X THINK

- **Primary / date / owner:** `2506.22403`，v1 2025-06-27，25/30；`TRAIN-PRETRAINING`，handoff `TRAIN-GRPO`与`MULTIMODAL-REPRESENTATION`。
- **Problem / mechanism / ownership:** bilingual model需在Korean reasoning/long context上形成专门data/curriculum。报告使用Peri-LN+µP、约6T Korean/English及synthetic Korean、三阶段context curriculum至128K，后训练含SFT和verifiable-reward RL；artifact拥有version，trainer拥有curriculum/checkpoint state。
- **Evaluation boundary:** Korean/bilingual benchmarks支持该family capability；不证明recipe可独立复现、compute claim跨厂商可比或vision variant通用。
- **Trade-off / coexistence / disposition:** language mixture、synthetic bias、long-context memory与report-only mechanism；单语/短上下文模型仍可更小更高效。Books Pending — `Refine Existing Argument / Experimental Report`。

### QuickSilver

- **Primary / date / owner:** `2506.22396`，v1 2025-06-27，24/30；`INFER-DECODE`，handoff `INFER-KV-CACHE`。
- **Problem / mechanism / ownership:** frozen dense model逐token逐layer全算最易保持语义，但不同token表示收敛速度/KV价值不同。Dynamic Token Halting、KV Cache Skipping、Contextual Token Fusion与Adaptive Matryoshka Quantization协同；runtime维护token convergence、fusion lineage、KV write mask与precision state。
- **Evaluation boundary:** GPT-2/Llama-2、WikiText-103/C4作者结果支持FLOP reduction且perplexity近似；不证明wall-clock、现代serving并发收益或生成事实不变。
- **Trade-off / coexistence / disposition:** control overhead、token identity/fusion错误、cache incompatibility；短序列/strict exactness仍应full compute。`Emerging / Experimental`。

### OptScale

- **Primary / date / owner:** `2506.22376`，v1 2025-06-27，26/30；`MODEL-SAMPLING`。
- **Problem / mechanism / ownership:** fixed Best-of-N预算过度，heuristic early stop无概率保证。OptScale在i.i.d. samples和可估selection distribution假设下推导目标performance/confidence的sample lower bound，并以LM predictor动态决定最小N；sampler拥有candidate set，predictor拥有posterior，scheduler拥有budget/stop state。
- **Evaluation boundary:** MATH-500/GSM8K/AIME/AMC支持作者设置下降sampling overhead且保持performance；不证明i.i.d.假设、predictor calibration或开放域judge成立。
- **Trade-off / coexistence / disposition:** predictor cost、miscalibration与correlated samples；fixed N在高并发、稳定分布下更简单。Books Pending — `Integrate New Mechanism Candidate`。

### Sub-MoE

- **Primary / date / owner:** `2506.23266`，v1 2025-06-29，26/30；`MODEL-MOE`。
- **Problem / mechanism / ownership:** expert pruning省memory但丢capacity，直接merge受specialization冲突。Sub-MoE按expert output cosine similarity聚类，对组内weights joint SVD，抽shared subspace并按usage合并；compressor拥有cluster/SVD/usage state，runtime消费新expert identity。
- **Evaluation boundary:** Mixtral、DeepSeek、Qwen MoE作者实验支持受限压缩可行性；work-in-progress且不证明latency、router recalibration或所有MoE。
- **Trade-off / coexistence / disposition:** calibration data、SVD cost、rare expert loss与identity migration；memory充足/strong tail specialization仍应保留原experts。Books Pending — `Integrate New Mechanism Candidate / Experimental`。

### Low-score source/date/rejection closure

- **Qwen VLo preview（19/30）：** official preview 于 2025-06-25 公开，能核验产品定位与交互表面，但没有足够 technical report、training recipe、evaluation contract 或 artifact 来重建内部机制。`Weekly Only — Version Fact / Mechanism Not Disclosed`。
- **Decrypto Benchmark（19/30，`2506.20664`）：** v1 于 2025-06-25 公开，核验到 multi-agent reasoning / theory-of-mind evaluation identity；其系统影响和项目相关性不足以跨过 archive threshold，且 narrow benchmark 不应外推 general reasoning。`Weekly Only — Narrow Evaluation Case`。
- **BehaviorBench / Model Editing as a Double-Edged Sword（19/30，`2506.20606`）：** v1 于 2025-06-25 公开，核验到 model-editing behavior evaluation identity；当前是受限 evaluation case，没有形成新的长期 system owner。`Weekly Only — Narrow Evaluation Case`。
- **Perry cyber deception framework（18/30，`2506.20770`）：** v1 于 2025-06-25 公开，来源和日期可核验；deployment threat model、production evidence 与长期 owner 均不足。`Weekly Only — Domain-specific Security Case`。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- vLLM `v0.9.1`、Ray `2.47.0`、DeepSpeed `0.17.1` 与 SGLang `v0.4.7` 按 official release date 归属 W24；Transformers `4.52.4` 归属 W22；TensorRT-LLM `0.20.0` 与 SGLang structured-output RFC 归属 W25。
- later revision只更新同一 Source Family 的验证边界，不在W26重复评分；论文以arXiv v1归属，正式发表不制造第二个owner。
- Gemini Robotics、Gemma 3n、Hunyuan-A13B 与后续runtime集成分开保存“模型/版本事实”和“系统机制”证据角色，新版本不覆盖旧方案成立条件。

## Knowledge Tree Position

- Model/Multimodal：`MODEL-MOE`、`MODEL-DECODER-ONLY`、`MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`。
- Training：`TRAIN-SFT`、`TRAIN-RLHF`、`TRAIN-GRPO`、`TRAIN-LORA`、`TRAIN-DISTRIBUTED-TRAINING`。
- Inference/Platform：`INFER-KV-CACHE`、`INFER-REQUEST-LIFECYCLE`、`INFER-SCHEDULING`、`PLATFORM-EVALUATION-SYSTEM`。
- Agent：`AGENT-WORKFLOW`、`AGENT-MULTI-AGENT`；领域证据只作handoff，不建立孤立owner。

## Recommended Action

- W26 Candidate Evidence Gate已通过：40/40 retained packets完成，4/4低分来源/日期/拒绝闭合，ordinary pending、blocked、disputed均为0。
- Historical Books Gate保持关闭。这里的Books Pending只表示未来逐Source Family判断，不授权把Weekly摘要写入Books。
- 后续年度Archive/Discovery复核若发现owner遗漏，必须回到本周增加评分与Source Review，不能以当前40项宣称全年度召回闭合。

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。本周只完成Weekly证据门；没有修改Books，也不把`Books Pending`解释成已吸收。未来只有在年度Evidence Gate和逐Source Family owner/adjacent-chapter review通过后，才允许选择`Integrate`、`Refine`或`No Change`。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 重建 `papers/2025/weekly/2025-W26/README.md`：从错误的空周结论恢复44个scored owners、40个strict Source Review与4个低分闭合。
- 同步年度索引和Learning State的W26 checkpoint；本阶段不修改Books。

## Open Questions

- fixed-organization、cross-index与event-window discovery replay是否仍会发现新的W26 owner？
- CommVQ、context-aware model eviction、PARALLELPROMPT、ZeRO/RL与dynamic token-compute families能否在后续周形成独立复现或稳定演进链？
- Gemini Robotics On-Device、Hunyuan-A13B与Project Vend未披露的hardware/precision/concurrency/SLO或production failure data能否取得？

## Sources

- Gemini Robotics On-Device — https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/（2025-06-24）
- AlphaGenome — https://deepmind.google/blog/alphagenome-ai-for-better-understanding-the-genome/（2025-06-25）
- Gemma 3n full release — https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/（2025-06-26）
- Qwen VLo preview — https://qwenlm.github.io/blog/qwen-vlo/（2025-06-25）
- Hunyuan-A13B model card — https://huggingface.co/tencent/Hunyuan-A13B-Instruct（2025-06-27）
- Hunyuan-A13B technical report — https://github.com/Tencent-Hunyuan/Hunyuan-A13B/blob/main/report/Hunyuan_A13B_Technical_Report.pdf
- Project Vend 1 — https://www.anthropic.com/research/project-vend-1（2025-06-27）
- Vision as a Dialect — https://arxiv.org/abs/2506.18898
- ReasonFlux-PRM — https://arxiv.org/abs/2506.18896
- CommVQ — https://arxiv.org/abs/2506.18879
- LongWriter-Zero — https://arxiv.org/abs/2506.18841
- Adaptive Activation Steering / STU-PID — https://arxiv.org/abs/2506.18831
- Understanding Software Engineering Agents — https://arxiv.org/abs/2506.18824
- Context-Aware CodeLLM Eviction — https://arxiv.org/abs/2506.18796
- Chain-of-Experts — https://arxiv.org/abs/2506.18945
- SlimMoE — https://arxiv.org/abs/2506.18349
- AggTruth — https://arxiv.org/abs/2506.18628
- HOLA — https://arxiv.org/abs/2506.18952
- PARALLELPROMPT — https://arxiv.org/abs/2506.18728
- Radial Attention — https://arxiv.org/abs/2506.19852
- HiMA-Ecom / JoyAgents-R1 — https://arxiv.org/abs/2506.19846
- KnowRL — https://arxiv.org/abs/2506.19807
- Why Do Open-Source LLMs Struggle with Data Analysis? — https://arxiv.org/abs/2506.19794
- SAGE query rewriting — https://arxiv.org/abs/2506.19783
- SRFT — https://arxiv.org/abs/2506.19767
- PLoP precise LoRA placement — https://arxiv.org/abs/2506.20629
- Leaner Training, Lower Leakage — https://arxiv.org/abs/2506.20856
- Decrypto Benchmark — https://arxiv.org/abs/2506.20664
- π-CoT / Prolog-Initialized CoT — https://arxiv.org/abs/2506.20642
- CoMind / MLE-Live — https://arxiv.org/abs/2506.20640
- When Life Gives You Samples — https://arxiv.org/abs/2506.20544
- AIMeter — https://arxiv.org/abs/2506.20535
- BehaviorBench / Model Editing as a Double-Edged Sword — https://arxiv.org/abs/2506.20606
- DiffuCoder — https://arxiv.org/abs/2506.20639
- Perry cyber deception framework — https://arxiv.org/abs/2506.20770
- Grokking in LLM Pretraining? — https://arxiv.org/abs/2506.21551
- Potemkin Understanding — https://arxiv.org/abs/2506.21521
- Mind2Web 2 — https://arxiv.org/abs/2506.21506
- Bridging Offline and Online RL for LLMs — https://arxiv.org/abs/2506.21495
- Efficient and Reusable Cloud Configuration Search — https://arxiv.org/abs/2506.21467
- Automated LLM Speedrunning Benchmark — https://arxiv.org/abs/2506.22419
- HyperCLOVA X THINK — https://arxiv.org/abs/2506.22403
- QuickSilver dynamic token halting — https://arxiv.org/abs/2506.22396
- OptScale — https://arxiv.org/abs/2506.22376
- Sub-MoE — https://arxiv.org/abs/2506.23266
