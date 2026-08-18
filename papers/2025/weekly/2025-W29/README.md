# AI Research Weekly — 2025-W29

> Coverage Window: 2025-07-14～2025-07-20
> Research Mode: Retrospective Backfill
> Accessed: 2026-08-24
> Backfilled: 2026-07-31
> Re-audited: 2026-08-24
> Audit Status: Candidate Evidence Gate Passed — 53/53 Scored Owners, 42/42 Retained Strict, 11/11 Low-score Closures
> Historical Books Gate: Closed

## Executive Summary

旧档案只保留SGLang Multiple Token Prediction integration；本轮重新执行固定机构、arXiv与AI Infra discovery，并对相邻周与年度spillback做owner复核，最终恢复53个scored owners：30项25～30分、12项20～24分、11项低分。42/42 retained均完成event-version strict Full Source Review，11/11低分完成source/date/rejection closure，`Review Pending = 0`、Blocked为0。新增恢复ElasticMM、CodeJudgeBench、LoRA-MCL、IFScale、Deep Hidden Cognition、SENTINEL、PhyWorldBench、ECP与Astrogator；166页Context Engineering survey已完成v1分节审计，但其“1400+ papers”是作者口径，正文未披露可复算systematic-search protocol。RedOne与Teach Old SAEs仍回拨W28；VisionThink、CSD-VAR、OpenBEATs等artifact/revision边界及ElasticMM数值等价、CodeJudgeBench judge替代execution等结论边界继续显式保留。Historical Books Gate关闭。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；本轮新增/复核来源Accessed统一为2026-08-24，既有source line保留原始2026-07-31访问记录。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。
- 本轮按2025-07-14～20逐日重放event-time identifiers，并用W28/W30、年度spillback与同family revision反查owner；命中revision不重复计分。Scholar/OpenAlex类索引只用于召回与metadata交叉，不作为论文机制证据。
- 固定机构面覆盖OpenAI、Anthropic、Google/DeepMind、Meta、Microsoft、Mistral、xAI、NVIDIA及主要国内模型机构的官方announcement/report/card；固定工程面覆盖PyTorch、JAX、CUDA/Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe/Kubeflow/Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime与OpenXLA的release/RFC/design history。没有机制披露或仅版本事实的项目不计入20+ owner。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 当前official/model owner包括EXAONE 4.0、Voxtral与ChatGPT agent；只公开产品行为的family不得反推内部runtime。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 已覆盖adaptive depth、multimodal representation/world model、post-training、evaluation/security、Agent context、code correctness与AI4Science。命中候选均以v1正文为owner证据；later revision仅作forward evidence。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 保留：SGLang Multiple Token Prediction integration（2025-07-17）与ElasticMM（2025-07-14）；其余固定工程release未形成独立20+机制owner，作为negative scan closure，不以版本功能凑数。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| (Almost) Free Modality Stitching of Foundation Models | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Mixture-of-Recursions | 5 | 5 | 4 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| Reasoning or Memorization? | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| REST stress testing reasoning models | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete |
| EmbRACE-3K | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Diffusion LM emergent safety vulnerability | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental Security Evidence |
| EXAONE 4.0 | 3 | 4 | 4 | 5 | 5 | 3 | 24/30 | Full Source Review Complete — Vendor Technical Evidence |
| Seq vs Seq / Ettin | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete |
| ElasticMM | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Source Review Complete — Experimental / Correctness Claim Disputed |
| CodeJudgeBench | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full Source Review Complete — Experimental Evaluation Evidence |
| Multiple Choice Learning of Low-Rank Adapters / LoRA-MCL | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental |
| How Many Instructions Can LLMs Follow at Once? / IFScale | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Source Review Complete — Experimental Evaluation Evidence |
| Deep Hidden Cognition | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental / Calibration Boundary |
| SENTINEL | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental |
| PhyWorldBench | 4 | 4 | 4 | 5 | 5 | 3 | 25/30 | Full Source Review Complete — Experimental Evaluation Evidence |
| ECP high-resolution MLLM framework | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Experimental |
| Astrogator formal verification for LLM-generated code | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Full Source Review Complete — Experimental / Language-specific |
| Einstein Fields | 3 | 2 | 2 | 5 | 3 | 4 | 19/30 | Low-score closure |
| RiemannLoRA | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| GitChameleon 2.0 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete |
| SWE-Perf | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Source Review Complete — Method Field Disputed |
| MMHU | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental Domain Benchmark |
| PhysX-3D | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| MindJourney | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| Mono-InternVL-1.5 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| FLEXITOKENS | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental |
| AnyCap Project | 3 | 3 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Experimental / Fields Disputed |
| FantasyPortrait | 3 | 2 | 2 | 5 | 3 | 3 | 18/30 | Low-score closure |
| Inverse RL Meets LLM Post-Training survey | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Full Source Review Complete — Survey Taxonomy / Fields Disputed |
| Automating Steering for Safe MLLMs | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental |
| Voxtral | 3 | 4 | 4 | 5 | 4 | 3 | 23/30 | Full Source Review Complete — Version/Technical Evidence |
| AbGen | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental Evaluation Evidence |
| Generative Energy Arena | 3 | 3 | 4 | 5 | 4 | 4 | 23/30 | Full Source Review Complete — Preliminary Human-preference Evidence |
| Turing Machine Imitator | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Full Source Review Complete — Experimental / Fields Disputed / Artifact Not Disclosed |
| Context Engineering survey | 3 | 4 | 5 | 5 | 5 | 5 | 27/30 | Full Source Review Complete — Narrative Survey / Search Protocol Not Disclosed |
| Diffuman4D | 3 | 3 | 3 | 5 | 4 | 3 | 21/30 | Full Source Review Complete — Experimental 4D Generation Evidence |
| π³ visual geometry learning | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental / Event-time Artifact Partially Available |
| VisionThink | 4 | 5 | 4 | 5 | 5 | 4 | 27/30 | Full Source Review Complete — Experimental / Event-time Artifact Revision Boundary |
| Russian speech data-centric framework / Balalaika v1 | 2 | 3 | 4 | 5 | 3 | 3 | 20/30 | Full Source Review Complete — Experimental |
| CSD-VAR | 3 | 3 | 3 | 5 | 4 | 3 | 21/30 | Full Source Review Complete — Experimental / Event-time Artifact Not Available |
| OpenBEATs | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Source Review Complete — Experimental / Event-time Training Artifact Boundary |
| Franca | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Full Source Review Complete — Experimental / Event-time Artifact Revision Boundary |
| SGLang Multiple Token Prediction integration | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full Source Review Complete — Version Evidence |
| Introducing ChatGPT agent | 2 | 4 | 4 | 5 | 4 | 3 | 22/30 | Full Source Review Complete — Mechanism Partially Disclosed |
| Logic-layer Prompt Control Injection | 3 | 4 | 3 | 3 | 4 | 2 | 19/30 | Low-score closure — Conceptual Security Taxonomy |
| Prompt Injection 2.0 | 2 | 4 | 3 | 3 | 4 | 2 | 18/30 | Low-score closure — Narrative Threat Synthesis |
| VLA Models in Robotic Manipulation survey | 2 | 3 | 3 | 4 | 4 | 3 | 19/30 | Low-score closure — Survey / No New Mechanism |
| DeepResearchEco | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Low-score closure — Domain Workflow Evidence |
| Enterprise structured-data RAG | 2 | 3 | 4 | 3 | 3 | 2 | 17/30 | Low-score closure — Artifact/Evaluation Contract Insufficient |
| Visual Input for Robotic Path Planning | 2 | 3 | 3 | 5 | 3 | 2 | 18/30 | Low-score closure — Simplified Benchmark |
| Probing for Arithmetic Errors | 3 | 3 | 3 | 5 | 3 | 2 | 19/30 | Low-score closure — Narrow Arithmetic Mechanism |
| Thought Purity | 3 | 4 | 3 | 4 | 3 | 2 | 19/30 | Low-score closure — Event-time Security Evidence Narrow |
| Cross-task Activation Steering / CAST | 3 | 3 | 3 | 4 | 4 | 2 | 19/30 | Low-score closure — Experimental Transfer Case |

账目：53 scored owners = 30 high + 12 medium + 11 low；42项达到20+且42项strict complete；11/11低分closure complete；`Review Pending = 0`，Blocked 0。SWE-Perf、AnyCap、Inverse RL survey、Turing Machine Imitator与ElasticMM部分correctness claim保留Disputed/Not Proven边界；π³、VisionThink、CSD-VAR、OpenBEATs与Franca保留artifact/revision/terminology boundary，AbGen保留revision-contract divergence。Identity/date/score/owner closure不等于archive-wide exhaustiveness，但本周固定source surface与cross-index replay已经闭合。

### Deep Analysis 1 — SGLang Multiple Token Prediction integration

- First Public: 2025-07-17
- Status: Official engineering blog; project benchmark
- Primary Source: https://www.lmsys.org/blog/2025-07-17-mtp/
- Evolution Relationship: Direct Evolution

#### Why

MTP 在低并发可能减少 decode iterations，但在高并发和 PD/EP 组合中，verification compute 与 batch shape 决定真实收益。

#### Principle and Mechanism

SGLang 将 MTP 与 expert parallelism、PD disaggregation 组合，并给出 draft/verify 的部署路径。

#### Trade-off and Evidence Boundary

plug-in 接口降低采用门槛，却不消除 acceptance、verification、CUDA Graph shape 与 workload sensitivity；项目最高吞吐数字不得外推。

#### Connection and Evolution

知识树位置：第 44、47、51、52 章。Must Read；与 EAGLE-3、SpecForge 合并审计。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### (Almost) Free Modality Stitching of Foundation Models / Hyma

- **Identity / date / coverage:** `2507.10015` v1 2025-07-14，v2/v3同周、later EMNLP venue与official repo作related evidence，26/30；`MULTIMODAL-REPRESENTATION`。全文覆盖method equations、VLM/MLLM experiments、rank/cost、AutoPair/equal-budget comparisons、Appendix A–G与limitations；event-time commit未锁定，未独立运行artifact。
- **Mechanism / ownership:** 为encoder pair和connector layer建立condition embedding，共享hypernetwork逐层生成connector参数；训练同时采样data batch与model-pair batch，最后materialize/rank connectors。model-zoo manifest拥有encoder digest/dimension/normalization，Hyma checkpoint拥有pair ID、generator与schema；opaque pair ID不能脱离具体artifact复用。
- **Evaluation boundary:** 9 image×3 text encoders、3 connector depths及小型MLLM appendix支持stitched compatibility不能由单模态质量/size推出，并在作者FLOP account下amortize pair search；不证明near-free、任意modality/model zoo稳定、causal MLLM ranking有效或end-to-end wall time/serving优势。3×3 MLLM已有ranking divergence，MaxViT被排除。
- **Trade-off / coexistence / disposition:** amortized search换来gradient interference、pair-ID brittleness、large generator、zoo drift、schema mismatch与uneven exposure；独立connector/grid search在最高质量、异质loss与审计隔离时仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Seq vs Seq / Ettin

- **Identity / date / coverage:** `2507.11412` v1 2025-07-15，v2/ICLR 2026只作forward evidence，official repo/checkpoints/data/eval family，27/30；`MODEL-DECODER-ONLY`。全文覆盖paired architecture/recipe、data stages、cross-objective continuation、encoder/decoder experiments、Tables 1–11、Appendix A–G与artifact docs；precision/seeds/SLO未披露。
- **Mechanism / ownership:** 六个matched scales在相同shape、tokenizer、data order和大体recipe下，比较bidirectional attention+MLM与causal attention+CLM；随后用50B decay tokens做reverse-objective continuation。checkpoint identity必须包含attention mask、objective、tokenizer、weights和trajectory；evaluation还需task adapter、fine-tune sweep与harness commit。
- **Evaluation boundary:** ≤1B、English-heavy open data、4×H100/node的paired contract支持native encoder在classification/retrieval、native decoder在generation更强，50B reverse continuation未消除历史偏置；但attention direction和objective同时变化，不能归因单一变量，也不证明universal dominance、adaptation永远失败、>1B/multilingual或production cost结论。
- **Trade-off / coexistence / disposition:** specialization提高task fit却拆分artifact/serving path；one decoder简化平台但可能浪费固定输出任务的质量/算力；reverse migration保留sunk compute却增加lineage和objective-switch shock。decoder-only仍适合generative/interactive，encoder-only仍适合高吞吐embedding/classification。Books Frozen；future `Refine — Existing Argument`。

### REST / Stress Testing Large Reasoning Models

- **Identity / date / coverage:** `2507.10541` v1 2025-07-14、v2 2025-07-15及official REST/OpenCompass artifact，26/30；`PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-CONTEXT`。全文覆盖cyclic reconstruction、stress aggregation、34-model/7-suite evaluation、position/order/error analyses、extractor comparison、32K→128K sensitivity、prompts、limitations与repo layout；event-time commit、hardware、precision与serving concurrency未锁定。
- **Problem / previous / changed constraint:** 单题frozen benchmark便宜、可比且便于atomic regression，但会遗漏一个bounded reasoning process同时处理多题时的context/output budget竞争与cross-question interference。REST不创建新题，而是在固定source items上引入multi-problem workload shape。
- **Mechanism / ownership / flow:** 对原题集按stress level `s`构造N个cyclic prompts，使每题出现`s`次并覆盖每个position；subject顺序回答，rule/LLM extractor解析每题，再聚合item、stress-level与cross-stress accuracy。benchmark owner拥有item order、composition、source revision、markers、extractor与aggregation；model run拥有model/provider revision、sampling与output cap；position是example identity的一部分。
- **Evaluation contract / proof boundary:** 34个1.5B～671B/API模型，GSM8K、MATH500、AMC23、AIME24/25、GPQA-Diamond、LiveCodeBench-v5，不同难度使用不同`s`集合，reasoning/non-reasoning output cap为32K/8K，三套小数据做8次sampling。结果证明该harness能暴露single-question ranking隐藏的omission、position与interference failure，并且selected 7B/32B runs把32K增至128K没有修复准确率；不证明存在可直接观测的“cognitive load”、Long2Short因果收益、production multi-ticket表现或通用ranking。
- **Trade-off / coexistence / disposition:** 每题被重复处理`s`次，增加token/cost与correlated samples，并引入parser、API drift、order与budget ownership；失败包括earlier-item capture、cross-answer contamination、truncation、repetition与extractor error。单题suite仍适合低成本回归与root-cause isolation。future `Refine — Existing Argument`，Historical Books Gate关闭。
- **Open Questions:** randomized order与uncertainty、cost-normalized goodput、shared-context interference与output budget的解耦、真实workflow queue验证、commit/provider pin与per-suite extractor disagreement。

### EmbRACE-3K

- **Identity / date / coverage:** `2507.10548` sole v1 2025-07-14及project page，26/30；`MULTIMODAL-EMBODIED-VLA`，handoff `TRAIN-DATA`与`PLATFORM-EVALUATION-SYSTEM`。全文覆盖Unreal collection/curation、SFT/GRPO equations、closed-loop protocol、metrics、all tables/ablations与conclusion；未找到可复现code/data repo、immutable manifest或environment digest。
- **Problem / previous / changed constraint:** passive image/video VLM benchmark适合recognition/QA，却没有action改变下一observation；作为controller后会暴露partial observability、goal forgetting、egocentric relation drift与short-horizon search。新约束是instruction-grounded policy必须在action→environment→observation loop中维护goal/spatial state。
- **Mechanism / ownership / flow:** 24个UnrealCV-Zoo maps采样6-DoF pose/RGB，Gemini 2.5 Pro基于image+nearby metadata起草任务，人类核验并执行demonstration，再由Gemini读取完整trajectory生成per-step rationale；数据经长度/格式过滤后训练Qwen2.5-VL-7B SFT，再用`G=6` GRPO与format/action reward。environment拥有authoritative transition/pose，capture pipeline拥有frame/action log，rationale是derived annotation而非sensor truth，policy只拥有proposal，evaluator拥有goal/optimal path/timeout。
- **Evaluation contract / proof boundary:** >3K tasks、约26K decision steps，SFT 2,344 trajectories/~10K actions；每步输入instruction、scene description、action history、current+5 recent+initial frames，输出rationale+one discrete action，最多约32步。训练各8张未披露型号GPU；precision、batch、seed、control rate、latency/SLO未披露。in/out-domain的Basic、Exploration、Dynamic Spatial-Semantic、Multi-stage、Open Door、Pick&Drop以SR/GDE/SSPL/steps/timeout比较proprietary VLM、Qwen origin、no-thinking SFT、SFT-only与SFT+RL。只证明该simulator/protocol下trajectory supervision改善作者报告的closed-loop success；不证明real-world VLA、安全、rationale faithfulness、RL因果generalization或跨map/action schema普适性。
- **Trade-off / coexistence / disposition:** retrospective rationale可使用online policy不可见的future trajectory，privileged object metadata与synthetic annotation带来leakage；7-frame bounded history控制latency却遗忘长期状态，simulator breadth换来较弱physical evidence。passive VLM、规则安全controller、短反应式policy与human demonstration仍各有成立条件。Ch26/Ch27已覆盖这一closed-loop与collection contract，故`No Change — Already Covered / Experimental`，Books Gate关闭。
- **Open Questions:** immutable dataset/repo、split/map disjointness、Gemini prompt/version、annotation agreement、training hyperparameters/seeds/CI、future leakage、reward/frame-history ablation、real-time intervention与sim-to-real evidence。

### SGLang Multiple Token Prediction integration

- **Candidate / Week / Score:** SGLang Multiple Token Prediction integration / 2025-W29 / 25/30。
- **Source Family ID:** `SGLANG-MTP-2025-07`。
- **Source Type:** official engineering blog、reproduction issue/commands、SGLang implementation documentation。
- **First-public Date / Revision History:** official blog 2025-07-17；reproduction issue opened 2025-07-13。当前 SGLang 已继续演进，review 只把 2025 当时列出的 compatibility matrix 和限制视作事件事实。
- **Direct Primary Sources:** LMSYS/SGLang MTP blog；`sgl-project/sglang#7998` reproduction instructions；2025-era SGLang speculative decoding code/config。
- **Related Primary Sources:** DeepSeek-V3 MTP architecture、DeepEP、Mooncake PD transfer 与 SGLang large-scale EP blog，用于解释依赖而不合并 benchmark。
- **Access and Verification Status:** Verified for documented algorithm, commands and author benchmark contract；exact commit/container、precision、network topology 与 independent reproduction Not Disclosed。
- **Full-read Coverage:** 已阅读 blog 全文的 draft/verify path、acceptance length、feature integration、两个 case study、best practices、future work；核对 reproduction issue 的 launch flags、batch/length、PD/EP topology 与当时“不支持 overlap scheduling”限制，并定位对应 runtime options。
- **Original Problem:** autoregressive decode 每轮只提交一个 token；当 target forward 的 GPU 并行资源未被充分利用时，serial dependency 限制 output throughput。
- **Why the Previous Design Was Reasonable:** single-token decode state最简单、无需 draft/verify state；continuous batching和overlap scheduling在高 batch时已能提升 utilization，且不依赖高 acceptance。
- **Changed Constraint:** DeepSeek-V3 自带轻量 MTP module，同时 production 需要与 DP Attention、large-scale EP、PD disaggregation、CUDA Graph 等机制组合；孤立实现 MTP 不足以上线。
- **Mechanism:** draft path 先给出若干候选 tokens，target model 在一次并行 verification 中接受最长匹配 prefix并从首个拒绝处 resample；收益由 average acceptance length 与 verification/draft overhead共同决定。
- **State Ownership:** request scheduler拥有sequence与batch placement；draft worker拥有candidate tree/window；target worker拥有 authoritative logits/accepted prefix；PD runtime拥有KV传输；acceptance telemetry只用于 tuning，不能改变模型语义。
- **Control Flow / Data Flow:** target extend 产生首 token → draft extend/decode 产生候选 → target parallel verify → commit longest accepted prefix/resample → 更新 KV/request state → next iteration；跨 PD/EP 时各 stage 还需一致的 expert/KV placement。
- **Implementation Details:** 2025 integration列出 DP Attention、EPLB、DeepEP、Two Batch Overlap、PD disaggregation、CUDA Graph 和多 attention backends；但 MTP 当时尚不能与 overlap scheduling 同时开启，issue 命令显式使用 `--disable-overlap-schedule`。
- **Evaluation Setup:** small case：DeepSeek-V3、2 decode nodes/16×H200、每 rank 2 concurrent、65,536 input/4,096 output；无 overlap/MTP baseline 51 tok/s/rank，overlap-only 60.4，3/4-token MTP 为81.5/82.0且 acceptance 2.18/2.44。large case：16 nodes/128×H200、4 prefill+12 decode、每 rank 128 concurrent、2,000/100、draft=2，报告相对同一无 overlap/MTP baseline +14.2%。
- **Baselines / Ablations / Sensitivity:** small case分开报告 baseline、overlap-only 与 MTP-only，但未报告 overlap+MTP；比较 3/4-token window。large case只给相对增益，缺绝对吞吐、tail latency及 draft/acceptance sweep。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** H200数量、model、input/output、concurrency与60.4 tok/s/rank应用阈值披露；precision/quantization、interconnect、TTFT/TPOT percentile、arrival process与exact software commit Not Disclosed。
- **What the Evidence Actually Proves:** 在作者两组特定 DeepSeek-V3/H200 配置中，MTP integration可运行于PD+EP并改善output throughput；acceptance length是可观测的主要收益信号。
- **What It Does Not Prove:** “最高60%”不是相对当时最佳 overlap baseline；它来自 MTP-only 对无 overlap baseline。也不证明任意 model、batch、sampling或SLO下保持同等收益与输出 bitwise deterministic。
- **Limitations / Threats to Validity:** vendor/author-only benchmark；MTP与overlap互斥使比较不完整；precision/network/version缺失；高 batch时draft增加的compute可抵消串行节省；sampling实现可能影响“identical output”表述。
- **Trade-offs / New Failure Modes:** 用额外 draft compute、KV/metadata、verify scheduling换取更少target iterations；新增acceptance collapse、candidate window过长、CUDA Graph shape膨胀、PD/EP state mismatch与公平性变化。
- **Where the Previous Design Still Applies:** 高并发已使 target充分利用、acceptance低、短 output、显存紧或需最简单确定性路径时，single-token decode + batching/overlap仍合理。
- **Evolution Relationship:** `Layering / Dependency`：autoregressive decode → speculative draft/verify → 与 batching/EP/PD 联合调度；MTP不是对continuous batching或overlap的替代。
- **ROADMAP Node:** Ch43～44、Ch47～48、Ch51～52。
- **Target and Adjacent Chapters Read:** 已阅读 Ch42～45、Ch46～48、Ch50～52；Ch44 已按本 packet 修正“60%”比较基线的证据边界。
- **Existing Coverage:** Ch44已解释lossless verification与acceptance/overhead模型，Ch52已覆盖token scheduling；真正新增证据是 MTP 与 PD/EP/overlap 的 compatibility contract，而非算法定义。
- **Integration Decision:** `Refine — Existing Argument`；owner `INFER-SPECULATIVE-DECODING`，作为 MTP 进入 PD/EP runtime 的 compatibility evidence。Historical Books Gate关闭，本轮不改Books。
- **Changed Files or Rejection Reason:** Weekly evidence only；旧记录中的Books-complete表述撤销。
- **Open Questions:** exact commit/precision/network、overlap+MTP后续公平对比、tail latency、non-greedy sampling contract与低 acceptance fallback。

### Mixture-of-Recursions

- **Identity / date / coverage:** `2507.10524` v1 2025-07-14（v2/v3只作revision evidence）及official code，28/30。全文覆盖method equations、expert/token-choice routing、recursion-wise/recursive KV、main/isoflop/throughput experiments、sharing/router/KV ablations、scaling、limitations与appendix；未独立运行artifact。
- **Problem / previous / changed constraint:** standard Transformer把unique parameter depth与每token execution depth绑定，便于训练、batch、PP与逐层KV；但parameter residency、attention FLOPs与KV traffic同时受限且token difficulty不同。fixed recursion增加effective depth却不减所有token执行，post-hoc early exit又缺deeper-layer KV。
- **Mechanism / ownership / flow:** 共享middle-cycle block并保留独立首尾层；router按recursion选择active token，active-set compaction后进入更深block，runtime维护recursion-local hidden/KV与depth-wise batch。expert-choice训练top-k依赖未来token统计，推理以aux router近似；checkpoint必须绑定router、recursion count与cache strategy，scheduler不得改变trained sharing semantics。
- **Evaluation contract / boundary:** 135M～1.7B、FineWeb-Edu、2K context、4×H100/A100；315M vanilla与167M MoR-2在16.5e18 FLOPs、IsoFLOP与single-GPU throughput比较。作者合同支持shared parameters+learned depth+selective cache形成compute/quality折衷，并显示depth-wise batching可转化部分结构稀疏；不证明>1.7B、production long-context/TP/PP/EP、semantic reasoning depth或任意SLO下2.06×。precision、arrival process与tail latency未披露。
- **Trade-off / coexistence / disposition:** router error、token starvation、depth-batch divergence、cache-map mismatch、kernel/graph complexity与OOD capacity drift；fixed stack/recursion/per-layer KV在predictable latency、backend不支持compaction或fidelity优先时仍合理。Owner `MODEL-TRANSFORMER-LAYER`，handoffMoE、model KV与inference scheduling；`Refine — Existing Argument / Books Frozen`。

### Reasoning or Memorization?

- **Primary / date / owner:** `2507.10532` v1 2025-07-14及author code，28/30；`PLATFORM-EVALUATION-SYSTEM`，handoffGRPO。全文覆盖partial-prompt probes、MATH/LiveMathBench、RandomCalculation、correct/random/inverted reward branches、Qwen/Llama controls、appendix configs与limitations。
- **Mechanism / evidence:** 冻结model/template/EvalSpec，以80/60/40% question prefix测tail reconstruction，再以发布后生成的RandomCalculation对相同GRPO分支施不同reward。旧公开MATH的reconstruction/answer recovery显著高于new task，clean task上reward fidelity决定稳定改进；支持benchmark accuracy会混淆memorization/template adaptation与learning，但不证明exact corpus、所有Qwen benchmark污染或所有random-reward结论无效。
- **Contract / trade-off / disposition:** 8×A800 80GB、16 rollouts/prompt、batch128；precision/max length/SLO未披露。fresh provenance提高因果解释力却降低生态真实性，synthetic generator也可能形成新模板泄漏。public benchmark仍可作comparability regression但应标潜在暴露。Books Frozen；future `Refine — Existing Argument`。

### SWE-Perf

- **Primary / date / owner:** `2507.12415` v1 2025-07-16及official project/repo/dataset，28/30；`PLATFORM-EVALUATION-SYSTEM`，handoffAgent platform。全文覆盖five-phase collection、timing/statistics、140-task evaluation、baseline configs、limitations与artifact schema。
- **Mechanism / evidence:** 从12个repos的PR构建base/head/Docker/test/runtime artifact，warm-up后重复20次、IQR filter与Mann–Whitney admission；Agent patch依次通过apply→correctness→performance。140个Python tasks显示patch可应用/正确远易于产生可测repo-level speedup，workflow Agent优于fixed pipeline但远低于expert aggregate；不证明通用human gap、跨语言/硬件或production SLO。
- **Disputed field / trade-off / disposition:** Phase3 prose的optimization-ratio公式与“below 0.3”方向冲突，必须核代码后复用；这是method field dispute，不否定其余runtime evidence。executable timing提高外部效度但增加环境成本、noise与target leakage；function-level/correctness-only suite仍适合便宜隔离测试。Books Frozen；future `Refine — Existing Argument`。

### GitChameleon 2.0

- **Primary / date / owner:** `2507.12367` v1 2025-07-16及official harness/dataset，28/30；`PLATFORM-EVALUATION-SYSTEM`，handoffRAG与Agent platform。全文覆盖328 tasks/26 Python libraries、version-pinned Docker、visible/hidden tests、RAG/agent/sandbox ablations、appendices与artifact。
- **Mechanism / evidence:** 每个task绑定library/version/dependencies/reference/docs/visible+hidden tests；model可检索docs或在sandbox调试，但installed environment+hidden execution才拥有version correctness。结果支持“知道API”不等于选择正确历史版本，visible repair、version docs与sandbox有条件改善；不证明全部dependency drift、语言/production build、安全或semantic completeness。
- **Trade-off / disposition:** pinned containers提高identity也昂贵脆弱；visible trace引入hidden overfit，internet/RAG可能混入邻近版本，sandbox扩权限。latest-version/migration benchmark与visible unit tests仍适合对应目标。Books Frozen；future `Refine — Existing Argument`。

### FLEXITOKENS

- **Identity / date / coverage:** `2507.12720` v1 2025-07-17；v2+只作forward revision，official repo为later artifact evidence，26/30；`MODEL-TOKENIZER`。全文覆盖hourglass architecture、boundary objective、119M/1B setup、BPE/fixed-binomial baselines、compression/task ablations、Appendix A–G、limitations与broader impacts；event-time commit未锁定。
- **Mechanism / ownership:** byte encoder→MLP boundary predictor→hard Gumbel-sigmoid segmentation→segment pooling→middle LM→upsampling/skip→byte output。把双向binomial target改为单边`max(k/N-β,0)`：只惩罚boundary过密，允许fine-tuning按task改变segmentation。checkpoint必须共同拥有predictor、language-conditioned target、normalization、sampling、pool alignment与LM weights；boundary不是可随意替换的独立tokenizer。
- **Evaluation boundary:** 119M/1B hourglass model、6种预训练语言/7类下游任务、3×/5×/10×与Urdu OOD实验支持adaptive boundary存在compression↔accuracy operating point；不证明普遍优于BPE、语义word boundary、large production decoder收益、任意code-mix适配或更高compression会等比例降低latency/KV/energy。无multi-seed CI和end-to-end serving measurement。
- **Trade-off / coexistence / disposition:** 减少碎片化却把token boundary变为input/model-revision dependent state，复杂化prefix/cache identity、span/tool offset、streaming和checkpoint compatibility；过少boundary丢信息，过多增加attention/KV，hard estimator增加优化噪声。stable ID/生态/容量规划优先时BPE/Unigram仍合理。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Automating Steering for Safe MLLMs / AutoSteer

- **Identity / date / coverage:** `2507.13255` v1 2025-07-17（v1标记work in progress；后续revision只作forward evidence），27/30；`PLATFORM-SECURITY`。全文覆盖SAS layer selection、64-unit ReLU prober、conditional refusal-head intervention、VLSafe/ToViLaG+/utility evaluation、layer/epsilon sensitivity、Appendix A–G与limitations；未发现公开artifact。
- **Mechanism / ownership:** safe/toxic controlled pairs在每层产生activation difference，以pairwise cosine mean选较可分离层；prober给出score并在`τ=0.5`二值触发，以`E'=(I+εαW)E`改变output-logit path。每个base model拥有layer identity、activation schema、prober、threshold、refusal head和epsilon calibration；score只是sensor，不拥有policy authority。
- **Evaluation boundary:** 两个7B MLLM、作者数据切片、GPT-4o binary judge与`ε=0.1`支持“model-specific probe + conditional intervention”可行；不证明universal safety layer、calibrated risk、OOD/adaptive attack robustness、production latency或real-world harm prevention。hardware、precision、length、batch、concurrency与SLO未披露。
- **Trade-off / coexistence / disposition:** conditional trigger减少benign drift，却新增false positive/negative、threshold/model drift、activation hook与output-head deployment coupling；epsilon与ASR非单调，个别case会使输出更toxic。无法访问hidden state时external classifier/gateway policy仍合理，高风险action仍需deterministic authorization。Books Frozen；future `Refine — Existing Argument / Experimental`。

### Voxtral

- **Identity / date / coverage:** Mistral official announcement 2025-07-15为first-public，technical report `2507.13264` v1 2025-07-17及official Mini/Small model cards为related evidence，23/30；`MULTIMODAL-REPRESENTATION`。全文覆盖modeling、pretraining/SFT/preference、evaluation、ablation、appendix与runtime card；paper无独立Limitations section。
- **Mechanism / ownership:** waveform→128-bin log-Mel→30-second independent Whisper-derived encoder chunks→MLP 4×downsample到12.5Hz→text decoder；`<repeat>`与`<next>`以1:1混合区分transcription与continuation。artifact identity必须绑定encoder、chunk/padding、feature config、adapter rate、task token、decoder/tokenizer/context；模型生成tool call仅是proposal。
- **Evaluation boundary:** ASR/translation/audio-QA、rate/padding/objective与post-training ablation证明在该artifact下encoder+adapter+decoder及dual objective可联合工作；不证明普遍优于ASR→LLM级联、12.5Hz/30s/1:1可迁移、synthetic speech等于真实acoustic robustness或40分钟上下文满足任何production SLO。训练hardware/data scale、latency/throughput与concurrency未披露。
- **Trade-off / coexistence / disposition:** downsample降低decoder成本却损失时序细节；独立chunk便于扩长却把跨chunk关系推给decoder；padding、pseudo-label、TTS与transcript-only reward带来浪费与偏差。纯ASR、streaming和可独立治理组件时级联仍合理。Books Frozen；future `Refine — Existing Argument / Version-bounded Technical Evidence`。

### Russian speech data-centric framework / Balalaika v1

- **Identity / date / coverage:** `2507.13563` v1 2025-07-17；v2/v3、5.1k-hour dataset与current repo仅作forward evidence，20/30；`TRAIN-DATA`。全文覆盖10-stage pipeline、2,161-hour v1 corpus、quality/speaker/transcript/prosody annotations、SEMamba/VITS experiments、four-arm ablation、limitations与结论；v1无appendix，event-time repo pin未找到。
- **Mechanism / ownership:** podcast admission→<15s segmentation→NISQA quality tiers/PyAnnote filtering→ASR→punctuation/stress/`е/ё`/G2P/alignment→speaker clustering→group-aware split。data owner必须保存source、segment、quality tier、speaker cluster、raw/derived transcript、phoneme duration和split membership；训练runtime只消费冻结manifest，license/consent/delete仍属governed owner。
- **Evaluation boundary:** Russian speech、固定step SEMamba/VITS、automatic/human MOS与stress/punctuation ablation支持“采集类型+quality tier+prosody annotation+speaker-group split”比单一hours更能说明training distribution；不证明跨语言阈值、自动标注ground truth、全部2.16k小时合法再分发、fixed-step等于收敛或当前v3 artifact在W29已存在。hardware/precision/SLO未披露。
- **Trade-off / coexistence / disposition:** 自动多级pipeline降低人工成本却串联ASR→punctuation→stress→G2P error，quality filtering可删方言/噪声长尾，speaker clustering会泄漏identity，podcast来源引入版权/voice privacy/delete lineage；单speaker朗读或授权清晰的小数据仍适合简单manifest+人工标注。Books Frozen；`No Change — Already Covered / Experimental`。

### Introducing ChatGPT agent

- **Identity / date / coverage:** OpenAI launch、full system card与release notes均first-public 2025-07-17，22/30；`AGENT-PLATFORM`，handoffsecurity/MCP/evaluation。联合阅读remote computer、visual/text browser、terminal、connectors、confirmation/watch-mode、policy monitor、capability/safety evaluations与limitations；内部planner、training与fleet runtime未公开。
- **Mechanism / ownership:** system把research、browser action、limited-network terminal和connectors置于统一task run；用户可interrupt/take over，consequential actions经过confirmation，policy monitor和site restrictions形成附加control layer，launch时memory关闭。task runtime拥有run/tool/virtual-computer state；credential、authorization与external side effect仍归user/policy/tool system。
- **Evidence boundary:** official materials只证明2025-07-17版本的公开能力、tool surface、product controls与author-evaluated safety/performance；不证明模型内部如何plan、工具选择为何正确、vendor benchmark可跨版本比较或deployment autonomy等于model capability。
- **Trade-off / coexistence / disposition:** unified run降低research→action handoff，却扩大prompt injection、credential exposure、irreversible action、long-run drift与monitoring surface；read-only deep research、单工具workflow或人工操作在低风险/高可控场景仍合理。`Weekly Only — Version/Product Fact / Mechanism Partially Disclosed`；Books Frozen。

### The Devil behind the mask / DIJA

- **Identity / date / coverage:** `2507.11097` v1 2025-07-15，v2 2026-02-10只作forward evidence，27/30；`PLATFORM-SECURITY`，handoff generative paradigms/evaluation。全文覆盖attack equations/algorithm、4 dLLM experiments、HarmBench/JailbreakBench/StrongREJECT、defenses、mask/length sensitivity、Appendix、Limitations与author repo；event-time commit未锁定且current repo仍有部分TODO。
- **Problem / changed boundary / mechanism:** AR guardrail假设append-only prefix，每个新token都可条件化检查；masked diffusion允许用户保留fixed harmful tokens并让模型并行补全mask span。DiJA用refinement LM重写harmful intent，把行动内容放在authoritative fixed tokens，穿插block/fine/progressive masks和benign separators；victim并行denoise后才形成完整输出。caller拥有fixed/masked partition，sampler只拥有provisional state，runtime/policy必须拥有validation与commit/abort。
- **Evaluation contract / proof boundary:** LLaDA-8B-Instruct/1.5、Dream-v0-Instruct-7B、MMaDA-8B-MixCoT，generation length512、block/steps32、temperature0.2；对比Zeroshot/AIM/PAIR/ReNeLLM并测Self-reminder/RPO。作者合同支持fixed/masked authority confusion是AR-style defenses未覆盖的attack surface，并显示mask count非单调；不证明所有dLLM、多模态diffusion或production policy脆弱，也不证明runtime不能逐block检查或gate final commit。hardware、precision、batch/concurrency、latency/SLO与false-positive均未披露。
- **Trade-off / coexistence:** commit-aware validation增加latency/compute和false refusal；post-filter可能已让provisional content进入stream/log/tool，逐step检查又损并行收益。append-only AR、server-owned trusted infill、低风险offline generation或已有strong sandbox场景仍适用旧防线。
- **Disposition / open:** future `Refine — Existing Argument / Experimental Security Evidence`，Books Gate关闭。Open：event-time commit、step/block/final三类guardrail的ASR-latency frontier、mask-source authentication、judge/human一致性和multimodal同构漏洞。

### EXAONE 4.0

- **Identity / date / coverage:** `2507.11407` v1-only 2025-07-15，24/30；official repository/model card与technical report联合核验。Owner `TRAIN-GRPO`，handoff `MODEL-LONG-CONTEXT`、`MODEL-MULTI-HEAD-ATTENTION`、`TRAIN-SFT`与`PLATFORM-EVALUATION-SYSTEM`。全文覆盖hybrid attention、QK-Reorder-LN、context extension、SFT/RL/preference stages、evaluation和limitations；公开材料未披露训练hardware、precision、batch、concurrency或SLO。
- **Problem / mechanism / ownership:** fixed global attention与单一post-training模式易解释，但128K、reasoning/non-reasoning双模式和训练稳定性同时出现时，成本与objective conflict上升。32B model采用3:1 local/global attention、4K local window、global layer无RoPE、QK-Reorder-LN和4K→32K→128K progressive extension；mixed SFT约1.5:1 reasoning/non-reasoning。AGAPO以leave-one-out group advantage保留all-incorrect group的小负反馈，做batch-global normalization、移除PPO clipping并保留sequence KL，之后再做preference learning。
- **State / flow:** model config拥有local/global schedule与position contract；trainer拥有context curriculum、mode mixture、group rollout/reward/normalization与checkpoint lineage；runtime只消费最终artifact，不拥有AGAPO训练state。数据流为mixed SFT→group rollouts/rewards→LOO advantage与global normalization→policy update+sequence KL→preference stage。
- **Evaluation boundary / trade-off:** broad benchmark table只构成vendor/self-report evidence；没有matched ablation隔离hybrid attention、QK-Reorder-LN和AGAPO，也未披露完整workload contract。材料不证明AGAPO普遍优于GRPO/PPO、128K有效推理或架构组件的独立因果。local/global交替降低部分长序列成本，却新增layer schedule、position extrapolation、dual-mode interference与复杂post-training failure surface。
- **Disposition:** `Refine — Existing Argument / Vendor Technical Evidence`；只作为future受限案例，Historical Books Gate关闭。

### RiemannLoRA

- **Identity / date / coverage:** `2507.12142` v1 2025-07-16；v2 2025-10-01改题为Muon/parameterization-independent framing，仅作forward revision，26/30。Owner `TRAIN-LORA`（Current Ch30 / Legacy Ch26）；相邻实读 `TRAIN-SFT` Ch29和`TRAIN-RLHF` Ch31。v1全文覆盖fixed-rank geometry、LOI/BackPropRSVD、language/diffusion experiments、ablations和limitations；未找到official artifact。
- **Problem / previous / constraint:** LoRA `ΔW=ABᵀ`可直接复用autograd/Adam且易merge，但对任意可逆`S`都有`ABᵀ=(AS)(BS⁻ᵀ)ᵀ`，factor coordinates不唯一；当收敛稳定性、初始化和coordinate scaling成为约束时，Euclidean optimizer会依赖任意gauge。
- **Mechanism / ownership:** 把`ΔW`视为fixed-rank manifold上的点：orthogonalize factors、将Euclidean gradient投影到tangent space、transport momentum、对rank≤2r候选做truncated-SVD retraction回rank r。LOI用BackPropRSVD近似full-gradient dominant subspace，并调整base使初始函数保持不变。base weight、adapter rank/gauge、tangent optimizer state与initialization batch/RNG必须分属不同owner。
- **Implementation / evaluation:** per-step几何开销作者给出`O((m+n)r²+r³)`；BackPropRSVD需`2(q+1)`次backward。Llama-3.2-1B rank16 commonsense/MetaMathQA与SD2 DreamBooth rank4/8/16，V100/A100，总计约2,000 GPU-hours；不同方法各自预选LR，precision与serving SLO未披露。收益在SGD+LOI最明显，Adam-like路径与LoRA-LOI差距小，且未测wall-clock/memory overhead。
- **Evidence boundary / trade-off:** 数学上证明coordinate ambiguity与invariant geometric update，实验只支持1B/SD2合同下的条件性增益；不证明大模型/分布式可行、full-FT parity、optimizer-only收益或v2 Muon framing。QR/SVD/retraction、rank-boundary degeneracy、tangent state、LOI额外backward与base correction增加实现和checkpoint复杂度；短训练或成熟AdamW/FSDP仍适合标准LoRA。
- **Disposition:** `Refine — Existing Argument / Experimental`；future只扩展Ch30的factor ambiguity和geometry branch，Historical Books Gate关闭。

### MMHU

- **Identity / date / coverage:** `2507.12463` sole v1 2025-07-16，24/30；project与current partial Hugging Face dataset只作later related evidence。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-DATA`与`MULTIMODAL-EMBODIED-VLA`。全文覆盖collection/annotation pipeline、motion/text/behavior/intention tasks、baselines、improvement experiments、appendices和limitations；事件时论文写明dataset“will be released”，当前HF 5,792 rows不等于论文宣称的完整57K immutable artifact。
- **Problem / mechanism / ownership:** 既有自动驾驶集常只拥有detection、trajectory或单一行为标签；MMHU试图让同一human instance绑定motion、trajectory、text、intention和13类安全相关behavior。视频经person detection/tracking、WHAM SMPL recovery/interpolation、trajectory与rule-based joint description，再由VLM提出caption/behavior；约10%人工标注用于训练annotation VLM，其余自动扩展。raw-source/license manifest、track/SMPL state、derived text/VLM labels、human reference和EvalSpec必须分别拥有provenance，derived annotation不是sensor fact。
- **Evaluation contract:** 1.73M frames/57K instances/48h motion；MMHU-V47K、H9.5K、T840。motion prediction、text-to-motion、binary behavior VQA和crossing-intention使用不同模型、指标与hardware；4–6 frame VQA要求direct/counter问题都正确并允许malformed retry。作者报告的VQA、MPJPE/ACCL、FID和JAAD结果属于不同task contract，不能合成单一能力分数。
- **Evidence boundary / trade-off:** 证明作者pipeline能构建统一多模态、多任务domain benchmark，额外MMHU data与若干受限task improvement相关；不证明全量label正确、因果安全提升、开放道路/VLA泛化、完整provenance或production action safety。VLM-assisted annotation降低成本，却耦合reconstruction/interpolation/annotation error、taxonomy lock-in、rare-class uncertainty、privacy/license和artifact incompleteness。
- **Disposition:** `No Change — Already Covered / Weekly-only Experimental Domain Benchmark`；Ch66已有dataset/environment/scorer identity和derived-evidence边界，Historical Books Gate关闭。

### PhysX-3D

- **Identity / coverage:** `2507.12465` v1 2025-07-16，same-week v2/v3；later v4和current repo/dataset只作forward evidence，26/30。Owner `MULTIMODAL-EMBODIED-VLA`，handoff generation/data/evaluation。v1全文覆盖PhysXNet typed annotation、PhysXGen dual latent、evaluation/ablations和limitations；event-time code/data/models尚未release。
- **Mechanism / ownership:** PartNet parts获得absolute scale、material/mechanical parameters、affordance priority、kinematic graph和descriptions；GPT-4o proposal经human refinement后形成typed manifest。PhysXGen以physical VAE和structural VAE分别编码property/geometry，再用dependent dual-branch conditional flow matching联合生成。mesh/license、annotation/units/rubric、human correction、physical latent和structural latent分属不同owner；generated property不是measured physics。
- **Evaluation boundary / trade-off:** 26K split、8×A100、geometry/appearance和normalized physical-property metrics支持joint latent相对tested post-hoc predictor的条件性改善；不证明simulator correctness、real material/contact/friction、robot success或6M procedural variants物理有效。统一typed asset降低下游接线成本，却耦合geometry/property error、taxonomy lock-in、false precision与annotation bias。
- **Disposition:** `Refine — Existing Argument / Experimental`；只作为Ch26 simulator/data boundary的受限案例，Books Gate关闭。

### MindJourney

- **Identity / coverage:** `2507.12508` v1 2025-07-16；later v2/NeurIPS与W49 contrary evidence只作forward nodes，26/30。Owner `MULTIMODAL-WORLD-MODELS`，handoff generation/embodied/evaluation。v1全文覆盖pose-conditioned video world model、bounded viewpoint tree search、SAT evaluation、depth/threshold ablations和limitations；event-time repo commit未锁定。
- **Mechanism / ownership:** controller把camera actions映射为SE(3)，world model生成imagined views，search VLM分别评exploration/helpfulness，beam保留top nodes和evidence buffer，最终QA VLM读original+imagined views回答。observed image是evidence，imagined frame是provisional model state，heuristic score不是confidence probability；search controller拥有budget/lineage，不能把synthetic pixels升级为environment fact。
- **Evaluation boundary / trade-off:** SAT-Real150与Synthetic random500、多个VLM/WM组合支持受限任务中bounded imagined-view search改善mean accuracy；depth在real set从2到3会下降，直接反证test-time scaling单调性。它不隔离额外VLM calls/context、不能证明physical correctness或production latency；每rollout约9秒、beam/state growth与world-model→scorer→buffer误差放大是新成本。
- **Disposition:** `Refine — Existing Argument / Experimental`；只作为Ch25 imagined-evidence search案例，Books Gate关闭。

### Mono-InternVL-1.5

- **Identity / coverage:** `2507.12566` sole v1 2025-07-16，26/30；predecessor `2410.08202`和current repo只作related evidence，事件时1.5 fused-kernel/model artifact未完整定位。Owner `MULTIMODAL-REPRESENTATION`，handoff MoE/pretraining/execution。全文覆盖EViP/EViP++、static modality experts、fused kernel、15-benchmark evaluation、ablations和latency tables。
- **Mechanism / ownership:** image经stride-28 patch embedding直接成为visual tokens；token modality已知，每层静态dispatch到modality-specific FFN与QKV，visual experts从language weights初始化。EViP/EViP++以concept→semantic→alignment→instruction stages逐步扩大trainable state；runtime按modality tag在fused CUDA branch中跳过不匹配expert。representation owner持token modality/patch contract，trainer持freeze mask/curriculum，runtime持kernel/backend identity。
- **Evaluation boundary / trade-off:** 1.8B base、256×A100和作者15-benchmark合同支持static modality subspaces加stage-wise unfreeze可降低部分data demand并保留更多language performance；headline 69.3% TTFT包含monolithic-vs-modular差异，不能全归因fused kernel，fused-vs-unfused在4096 input约19%。不证明monolithic普遍优于encoder+projector或1.5 artifact可独立复现。
- **Disposition:** `Refine — Existing Argument / Experimental`；显式modality identity可拥有static dispatch，但不推翻learned routing的语义不确定性，Books Gate关闭。

### AnyCap Project

- **Identity / coverage:** `2507.12841` v1 2025-07-17；later v2只作forward revision，22/30；official repo/event-near commit、weights和evaluation可定位，但完整training dataset仍未发布。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff multimodal/data。v1全文覆盖ACD triplets、ACM corrective model、AnyCapEval、public/downstream evaluation、ablations、human study和limitations。
- **Mechanism / ownership:** frozen base captioner先生成`y0` proposal；corrector重新编码原modality并读取instruction+`y0`，autoregressively产生`yc`。约40% `(q,c,c)` no-change cases教它在proposal已合规时不重写。base proposal、modality representation、correction policy、triplet provenance和content/style evaluator必须分属不同owner。
- **Evaluation boundary / dispute:** 作者dataset/benchmark支持residual correction与no-change mixture在其judge/human protocol下改善controllable caption，但不证明factuality、judge calibration、任意base/model泛化或production latency。paper对audio triplets写50K/75K冲突；正文global batch256与Appendix 32 GPUs×batch1×accum1不一致，均保留Disputed，不用推断补齐。
- **Trade-off / disposition:** modular corrector避免重训base，却增加双模型延迟、schema耦合、proposal-error amplification和judge gaming；generic/edge caption仍适合single pass。Ch66/23/27已有对应原则，故`No Change — Already Covered / Weekly-only Experimental Evaluation Case`，Books Gate关闭。

### Inverse Reinforcement Learning Meets Large Language Model Post-Training

- **Identity / coverage:** `2507.13158` sole v1 2025-07-17，21/30；narrative survey，无artifact、Appendix、独立Limitations或可审计search query/数据库/cutoff/纳排标准。全文覆盖MDP/IRL基础、BC/IL/RM、PPO/DPO/GRPO/Best-of-N、active preference、reward overoptimization与references。Owner `TRAIN-RLHF`，handoff PPO/GRPO/DPO/evaluation。
- **Problem / mechanism / ownership:** survey用`MDP\\R`统一描述缺少真实reward的post-training：prompt distribution给initial state，policy生成rollout occupancy，demonstration/preference/verifier提供不同feedback interface，系统训练explicit RM或形成implicit preference objective，再以PPO/DPO/GRPO/iterative update或test-time selection改变response distribution。dataset必须拥有generator/annotator/rubric/provenance，RM拥有score semantics与training distribution，reference/old policy拥有KL anchor与rollout identity，verifier/environment才可能拥有authoritative outcome；reward不是客观真值。
- **Evidence boundary / dispute:** 本source family没有原创experiment、model、dataset或统一重跑，不能跨被引论文比较性能。它支持demonstration和preference是不同接口、offline support会与current-policy occupancy漂移、learned reward可同时驱动训练和test-time selection；不证明所有post-training等价IRL、必须使用neural RM或任何算法普遍优越。alignment/post-training混用、pure-text MDP忽略tools/side effects、数学任务“没有oracle”、discount直接等同短回答、只有RM能test-time optimize等表述过宽；Fisher公式的`phi(x,y1)-phi(x,y1)`疑似typo，均保留Disputed。
- **Trade-off / disposition:** learned RM扩大可优化feedback，却引入calibration/OOD drift、Goodhart、policy-RM co-adaptation与serving cost；online data改善policy-current coverage但增加annotation latency/selection bias/privacy；rules/verifiers覆盖窄却可复算；Best-of-N不改权重却把成本移到inference。Ch31已更完整覆盖这些owner和分支，故`No Change — Already Covered / Survey-only Taxonomy`；Historical Books Gate关闭。

### The Generative Energy Arena

- **Identity / coverage:** `2507.13302` sole v1 2025-07-17，23/30；12页paper全文覆盖arena design、relative-energy presentation、impact metrics、implementation、694-question preliminary study、limitations与references。没有model/system card、独立energy measurement artifact或完整participant dataset。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `PLATFORM-COST`。
- **Problem / mechanism / ownership:** 普通human arena先比较blind response quality，无法回答能源信息是否改变可接受选择；绝对energy又依赖hardware、batch、quantization和verbosity，proprietary model通常不公开。GEA只比较同family不同size，先blind vote；仅当用户先选大模型时，再提示另一响应“consumes less energy”并询问是否愿在quality loss下改票。evaluation owner保存model/API revision、random pair、prompt、blind vote、提示文案与changed vote；runtime/measurement owner才应持hardware和joule evidence，用户偏好不拥有energy truth。
- **Evaluation boundary:** paper覆盖GPT-4o/mini、GPT-4.1/mini、Claude Sonnet/Haiku与Llama3 70B/8B，694 questions，其中295来自西语MOOC assignment，作者估计至少83%由MOOC students产生；报告41%～52%、平均约46%的eligible votes改变。它只证明该西语、self-selected/课程主导、pairwise提示合同中能源标签显著影响选择，不证明大模型通常不值得、size严格代表per-request energy、所有用户愿接受同等quality loss或结果可跨model family比较。论文没有绝对joules、matched output length、hardware、batch/concurrency、latency/SLO、confidence interval、participant count/demographics与prompt-category分层。
- **Trade-off / disposition:** 两阶段设计保留blind quality baseline，却只向先选大模型者提问，提示本身把“smaller”绑定“lower energy”且tie全部归入small-after-energy公式，可能产生framing/selection bias。绝对energy measurement更可审计但难覆盖closed APIs；relative label易理解却不适合resource accounting。Ch66已要求power/cost绑定workload、hardware与SLO，Ch70要求cost per good outcome，故`No Change — Already Covered / Preliminary Human-preference Evidence`；Historical Books Gate关闭。

### AbGen

- **Identity / revision boundary:** `2507.13300` sole arXiv v1 2025-07-17，26/30；event-time official repo initial commit 2025-07-14，dataset/code可定位。arXiv v1与artifact是1,500 examples/807 papers，later ACL formal metadata为2,000/677，视为same-family divergent revision evidence，不覆盖W29 workload。全文覆盖benchmark construction、three-criterion rubric、human/automated evaluation、AbGen-Eval、error analysis、user study、limitations与Appendix。Owner `PLATFORM-EVALUATION-SYSTEM`。
- **Mechanism / ownership:** 2024 cs.CL papers经LaTeX parsing、manual filtering和expert restructuring，移除原ablation后形成context/target module；模型生成objective+process，human按importance、faithfulness、soundness分别评分，可在查看reference后调整；meta-evaluator比较judge与human的system-level Kendall和instance-level Pearson。source snapshot、derived annotation、benchmark manifest、generation runtime、human judgment与automated judge必须分别拥有版本；真实experiment environment未执行，因而不提供scientific commit authority。
- **Evaluation boundary:** 18 models；1,000-example automated test由GPT-4.1-mini judge，100 testmini items做human model comparison，40 shared outputs测agreement，20 examples比较human/reference；AbGen-Eval为1,800 rows。instance-level best correlation仅约0.307，说明aggregate ranking好不等于单例可靠。它支持fluent design之外需要typed scientific rubric和judge meta-evaluation，不证明参考设计唯一正确、generated ablation可执行、跨科学领域泛化或部署价值。split是否paper-disjoint、seeds/hardware/CI/cost与ACL revision diff均未披露。
- **Trade-off / disposition:** explicit benchmark使开放任务可比，却冻结source-selection和rubric；human有效但昂贵主观，model judge便宜却可在单例失真，reference visibility又带anchoring。Ch66/27/81已覆盖subject/scorer identity、derived data provenance和executable scientific workflow，故`No Change — Already Covered / Experimental Evaluation Evidence`；Historical Books Gate关闭。

### Diffuman4D

- **Identity / coverage:** `2507.13344` sole v1 2025-07-17，21/30；official arXiv HTML/PDF覆盖metadata、related work、完整Method、Implementation、baselines、两组ablation、limitations与Appendix A～C。Owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff `MULTIMODAL-WORLD-MODELS`（Ch25）；project page只作related qualitative evidence，未把later artifact状态倒灌到event-time结论。
- **Problem / previous design / mechanism:** dense synchronized cameras或显式SMPL/depth reconstruction在观察充分时可复算且合理；sparse views使geometry ill-posed，直接用video diffusion补target views又因GPU窗口切分与stochastic denoising产生跨view/time跳变。方法把`M`个input与`N`个target、`T`个时间点编码成`(M+N)×T` latent grid，以双向sliding window交替做spatial/temporal denoising；每个窗口只推进`P`步、每样本总步数`D=2PW/S`，再由LongVolcap把input+generated views重建为4DGS。Sapiens 2D pose经triangulation成为3D skeleton、投影RGB latent与Plücker camera coordinates共同约束front/back、occlusion与pose ambiguity。
- **State / data / implementation:** observed videos、camera calibration和derived mask/skeleton拥有不同provenance；target latents是可修改proposal，diffusion sampler拥有更新schedule，4DGS只消费生成结果而不把它升级为observed fact。训练在spatial `M=4,N=12`与temporal `M=8,N=8`序列间各50%采样，10%全条件dropout；Stable Diffusion 2.1全参微调200K steps、batch32、lr `1e-5`、32×H20，首卷积4→15 channels。24-step DPM-Solver++、CFG3.0；length48单A100约2分钟并可并行到8×A100。4DGS阶段每7200-frame序列100K iterations、单RTX4090约1小时。
- **Evaluation / evidence boundary:** DNA-Rendering选择1000×48-view×225-frame约10M images，16 test sequences；ActorsHQ 12 sequences作zero-shot。作者与LongVolcap、GauHuman、GPS-Gaussian及自行复现CAT4D比较，并在3个motion sequences与6个complex-clothing sequences上消融sliding strategy和skeleton/Plücker。结果支持该数据、重建器与指标下的时空一致性和视觉质量改善；不证明生成视图是真实geometry、world-model causal dynamics、4K/novel-pose/复杂人-物交互、production goodput或跨domain action correctness。
- **Trade-off / disposition:** generative prior降低dense-camera需求，sliding iterative denoising以bounded memory扩大信息传播，却增加多GPU调度、可变latent state、derived-condition误差、数据清洗依赖和两阶段failure coupling；dense capture、精确simulator/geometry或安全关键measurement仍应优先使用observed/explicit state。Ch24已拥有mutable generation、window/state/commit与modality-specific workload contract，故`No Change — Already Covered / Experimental 4D Generation Case`；不能因“4D”名称归入causal World Model。Historical Books Gate关闭。

### Turing Machine Imitator / TAIL

- **Identity / coverage:** Source Family `ARXIV-2507.13332`，v1 2025-07-17、later v2/v3与ICLR 2026只作forward evidence，26/30。v1 HTML/PDF已覆盖metadata、Preliminaries、TAIL三组件、dataset synthesis、training/evaluation、sensitivity、ablation、discussion、limitations、Appendix A～G；event-time repository、dataset manifest、generator version与immutable commit均`Not Disclosed`，但不阻断paper全文审计。Owner `TRAIN-DATA`（Ch27），handoff `TRAIN-SFT`（Ch29）、`MODEL-LONG-CONTEXT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / ownership:** direct answer、普通CoT或task-specific Index Hint/Reversed Format在短输入和固定schema下成本低且合理，却会把control transition、operand retrieval和computation压在不可核验大步骤中。TAIL由authoritative program generator产生execution trace：Linear Transition按真实执行顺序展开loop/tree/graph，Atomic State限制每步只做retrieval/elementary operation/control transition，Memory Fetcher在operation前显式复制当前operand，把动态远距访问改成局部token interaction。generator/oracle拥有transition与answer，trace synthesizer拥有serialization schema，dataset应拥有task/length/split/dedup/version，trainer拥有Qwen2.5-7B checkpoint；模型只生成append-only imitation trace，并不拥有可变Turing tape。
- **Implementation / evaluation contract:** 覆盖Simulation、Recursion、Iteration、Greedy、Enumeration、DP、Divide & Conquer、Backtracking八类、可枚举Table A1为18 tasks；多数task声称100K train/500 eval。Qwen2.5-7B以global batch1024、lr `1e-5→7e-7`、weight decay0.1训练2～5+ epochs，hardware、precision、optimizer、packing、seed与cost未披露。greedy zero-shot pass@1先由1.5B extractor取答案，再由Qwen2.5-72B-Instruct作YES/NO judge；与Base/Instruct/DeepSeek-R1及addition上的Index Hint/Reversed Format比较。作者结果支持program-generated linear/atomic/fetch-explicit trace在这些synthetic deterministic tasks上改善部分train-short/test-long accuracy；不证明universal length generalization、真实Turing tape、open-ended reasoning、跨task/algorithm transfer、比symbolic executor更可靠或model judge无误。
- **Ablation / disputed fields / threats:** DP-long完整TAIL为71.8，低于`w/o Linear Transition=74.2`和`w/o Memory Fetcher=74.8`，不能写成每个组件都普遍必要。v1内部存在18/28 tasks、困难任务50K/20K train、`Qwen2.7-7B` typo、组件命名漂移、short-only与混入M/L support解释混杂等冲突；deterministic task本可用program oracle，却加入双模型extractor/judge且未审计scorer error。trace随algorithm complexity膨胀，增加token、KV、latency、exposure error、schema memorization与generator/oracle共错；缺artifact、seed、variance、hardware与serving evidence。
- **Evolution / coexistence / disposition:** `task-specific hint → structured CoT → executable linear atomic trace → explicit current-step operand materialization`是training-data specification分支，不是long-context architecture或external memory替代。短任务仍适合direct/ordinary CoT，单一算术schema可保留hint/reversed format，确定性correctness应优先external symbolic tool。Ch27已覆盖executable specification、trajectory/verifier lineage与synthetic-data blind spot，只需未来作为受限refine案例；当前`Refine — Existing Argument / Experimental / Books Frozen`，Historical Books Gate关闭。

### π³: Scalable Permutation-Equivariant Visual Geometry Learning

- **Identity / coverage:** Source Family `ARXIV-2507.13347`，official repo于2025-07-16公开inference/demo，paper v1 2025-07-17，均归W29，25/30；evaluation/training code、v2/v3、Pi3X与ICLR 2026只作forward evidence。v1全文覆盖Method、四类evaluation、robustness、ablation、scalability、Conclusion与Appendix A.1～A.5；event-time immutable tag/commit未定位。Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff Ch25/26与Ch66；它估计per-view geometry/pose，不拥有action-conditioned dynamics。
- **Problem / mechanism / state:** SfM/MVS或fixed-reference feed-forward model选择第一张/指定图像作为global anchor，在该frame有业务语义或需要incremental map时合理；unordered multi-view set中，偶然顺序会把模糊/遮挡view升级为world authority。π³删除frame-order positional embedding/reference token，以DINOv2 patches交替做view-wise和global attention；三个不共享权重的per-view decoders分别输出camera pose、local point map与confidence。每图拥有local coordinate frame，训练以shared scale的point/normal/confidence loss和所有ordered view pairs的relative pose loss实现`phi(P(S))=P(phi(S))`。downstream仍必须显式选择gauge/world frame；binary confidence只是按point-error threshold训练的validity proxy，不是calibrated uncertainty。
- **Implementation / evaluation:** backbone36 layers并从VGGT初始化，encoder冻结；两阶段224×224与100K～255K random-pixel training，每sample 2～24 images，各100 epochs×1000 iterations，Adam initial lr1e-4，16×A100→64×A100。camera pose在RealEstate10K/CO3Dv2/Sintel/TUM/ScanNet，point map在DTU/ETH3D/7-Scenes/NRGBD，depth在Sintel/Bonn/KITTI/NYU-v2；多处先做scale/shift、Sim(3)或ICP alignment。robustness只轮换first/reference frame共N次，不是穷举N! permutations。作者结果与component ablation支持per-view local geometry+relative supervision降低reference sensitivity；不证明metric/absolute frame、observed fact、temporal causality、World Model、physical control或production goodput。
- **Disputes / trade-off / limitations:** 作者称`Affine-Invariant Camera Pose`，正文实际为rigid+global scale的similarity gauge；`permutation equivariance`是architecture contract，而empirical test主要是first-frame rotation；large model892.37M与performance table959M scope未解释；event-time只有inference/demo，internal dynamic data不公开。取消arbitrary reference换来order robustness，却把gauge selection、local-map reconciliation、scale ambiguity与global-attention cost交给下游；unordered treatment还会丢失temporal-order prior。透明/反射、grid artifacts、aligned benchmark、seen training population、缺seed/CI/calibration均限制结论。
- **Evolution / coexistence / disposition:** `SfM/MVS+BA → first-camera feed-forward point maps → fixed-reference multi-view model → permutation-equivariant per-view local geometry + relative pose → downstream explicit gauge/alignment`。robot base或calibrated camera天然定义frame、高安全metric geometry、streaming/incremental mapping时旧方案仍合理。Ch23已有content/modality/coordinate/artifact identity，但缺少“arbitrary anchor→equivariance→explicit gauge”的演进段，故未来`Refine — Existing Argument / Experimental`；当前Books Frozen，Historical Books Gate关闭。

### VisionThink: Smart and Efficient Vision Language Model via Reinforcement Learning

- **Identity / revision / coverage:** Source Family `ARXIV-2507.13348`，sole arXiv v1 2025-07-17，27/30；data/models 7月17日、repo 7月18日，7月22日code note与后续evaluation/venue只作forward evidence。v1 Abstract、Introduction、Preliminary、Method、Experiments、Related Work、Conclusion、Limitations及Appendix A～E均已读；current repo没有event-time immutable tag/commit，不能倒灌后续实现。Canonical owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `TRAIN-GRPO`、`INFER-REQUEST-LIFECYCLE`、`INFER-SCHEDULING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / previous design / changed constraint:** Always-full resolution在细节、安全关键与tool不可用时最稳，fixed compression又便于capacity planning；但image-question pair的信息需求不同，OCR/chart/documents需要细节，普通VQA可接受较低visual-token operating point。静态策略无法同时优化平均成本与长尾fidelity。
- **Mechanism / state / control flow:** `question + downsampled image → direct answer or resize_image JSON call → original/high-resolution image → second response`。Multi-turn GRPO只对模型生成的action/answer tokens回传loss，user/tool-return text与image tokens被mask；reward由text-only judge accuracy、format reward与resolution-action penalty组成。Policy拥有direct/resize proposal，tool/environment拥有high-resolution observation，trainer拥有group/reward/mask，scheduler应拥有second-pass admission/deadline；requesting more pixels不是取得证据，也不是uncertainty truth。
- **Implementation / evaluation contract:** Qwen2.5-VL-7B-Instruct，veRL/GRPO，batch512、mini-batch32、FP16、LR `1e-6`、KL `0.001`、16 responses/prompt；inference用vLLM temperature0。九类multimodal benchmarks比较full/quarter resolution、fixed pruning与adaptive branches，并有penalty、threshold、prompt、RL-vs-SFT和cold-start ablations。论文报告平均约51.3% visual-token retention；easy slices可降低time，ChartQA hard slice反而更慢。GPU、seeds、main reward judge revision、concurrency、tail latency、memory与SLO未披露。
- **Evidence proves / does not prove:** 证据支持“low-resolution first + learned escalation”在该model/data/judge合同下可行，action-cost会改变call behavior，细节slice能抵消甚至反转收益。它不证明per-sample calibrated confidence、模型知道自己不知道什么、RL普遍优于SFT、51.3%可跨workload复用或two-pass tail latency可接受；resize-call ratio不是necessity accuracy，文中没有ECE、risk-coverage或abstention curve。
- **Trade-off / failure / coexistence:** Easy case少做visual-token work，hard case却支付low+high两次prefill，并引入tool timeout/stale asset、identity mismatch、always-high/low collapse、judge gaming、prompt/schema drift、batch fragmentation与cache invalidation。已知detail-heavy、hard real-time、安全关键或tool不可靠的workload仍宜always-high/fixed path；局部细节可能更适合bounded crop而非整图升级。
- **Evolution / disposition / questions:** `always-full → fixed compression → post-encoding content selection → low-resolution-first conditional escalation → bounded crop/zoom acquisition`，属于Direct Evolution + Layering。Ch23已有rate-distortion/token budget但缺sample-adaptive fidelity与hard-case double-pass边界，future `Refine — Existing Argument / Experimental`；当前Books Frozen。仍需event-time commit、reward aggregation scope、natural workload prevalence上的necessity calibration、p95/p99/goodput及stale-tool failure evidence。

### CSD-VAR: Content-Style Decomposition in Visual Autoregressive Models

- **Identity / revision / coverage:** Source Family `ARXIV-2507.13984`，v1 first-public 2025-07-18，21/30；v2 2026-03-15、ICCV paper与2025-11 CSD-100 upload只作forward evidence。v1 Abstract、Related Work、VAR equations、Method 4.1～4.3、dataset、main/ablation/user-study与Appendix A.1～A.5已读。Project Code链接当前404，v1没有CSD-VAR implementation/checkpoint/immutable config或event-time CSD-100 artifact。Canonical owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24），handoff Ch23、`TRAIN-LORA`与Ch66。
- **Problem / previous / changed constraint:** 单一textual-inversion embedding在只需整体concept时轻量且稳定；当单图的content与style需要独立组合，联合优化会纠缠两者，而next-scale VAR各scale对颜色、形状、纹理和细节贡献不同，使同一loss/单一state owner不再合适。
- **Mechanism / ownership / flow:** 作者在35-image validation上按scale-removal分析固定style scales `{1,2,3,10}`与content scales `{4…9}`，交替更新content/style embeddings；由LLM为content生成subconcepts、CLIP编码、SVD取top-10方向，从style embedding移除proxy content subspace；再在self-attention K/V前加入scale-specific residual memory（style scale1、content scale4，默认首block一对K/V）。Frozen backbone/VQ codebook、special embeddings、projection、KV memory和scale config必须分别绑定base/text encoder/codebook revision。
- **Implementation / evaluation contract:** Switti/Infinity，Adam、LR `1e-3`、200 steps、batch1、4 tokens、1 KV pair、single A100。CSD-100由Flux synthetic pool、人工与ChatGPT筛选成100 single-subject images；每concept 50 prompts×10 outputs，使用CSD/CLIP/DINO metrics并与DreamBooth/B-LoRA/Inspiration Tree比较。Ablations覆盖scale-aware loss、SVD、KV、rank、token/KV/block count；更多tokens/KV/blocks并非单调改善。A100型号、precision、seed、wall time、exact checkpoint、latency/memory/concurrency/SLO未披露。
- **Proof / non-proof / limitations:** 作者contract支持scale-aware alternating optimization、proxy subspace projection与small residual KV各自带来条件性增益，并说明factorization stage可成为optimization/state boundary；不证明content/style因果可识别、scale split跨backbone迁移、VAR优于diffusion/LoRA、CSD metrics等同human或event-time可复现。35-image scale analysis、synthetic curated 100-image dataset、CLIP/DINO-correlated scorers、notation ambiguity、无seed/CI与closest UnZipLoRA缺席限制结论。
- **Trade-off / coexistence / disposition:** 低trainable state换来embedding/KV/projection/scale config lineage、backbone-specific prior、prompt/KV mismatch与upgrade invalidation；更多prefix state还增加attention overhead和overfit。无需content/style拆分时single embedding更简单，成熟diffusion/LoRA在portable adapter和高fidelity上仍成立。Evolution为`single concept embedding → separate embeddings → scale-aware optimization → subspace rectification → scale-specific residual KV`，属于Experimental Alternative Branch。Ch24可future `Refine — Existing Argument`，当前Books Frozen。

### OpenBEATs: A Fully Open-Source General-Purpose Audio Encoder

- **Identity / coverage:** Source Family `ARXIV-2507.14129`，v1 first-public 2025-07-18 17:57:46 UTC，24/30；v2 2026-07-13与WASPAA/DOI只作forward evidence。v1 Abstract、Background、architecture/objectives/formulas、data/training、25-dataset evaluation、discussion与conclusion均已读；v1无Appendix或独立Limitations。作者项目与2025-07-16 Hugging Face checkpoint/config可核，current GitHub为later inference wrapper，不能冒充event-time full training pipeline。Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `TRAIN-DATA`、`TRAIN-PRETRAINING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / previous / changed constraint:** BEATs式audio SSL分散在environmental sound、bioacoustics与music，且pretraining pipeline并未全部开放。单域encoder在目标域、标签和SLO固定时易优化、验证与治理，AudioSet-only也降低mixture和lineage复杂度；但audio encoder成为audio-language/reasoning系统共享感知层后，需要跨域transfer、可复现训练和跨task evidence，YouTube-backed AudioSet availability drift也使dataset name不再足以定义实验。
- **Mechanism / state / data flow:** 16 kHz waveform经128-bin mel和`16×16` spectrogram patch进入ViT；masked positions预测acoustic tokenizer的1024-way离散ID。encoder与tokenizer最多交替三轮：上一轮encoder作teacher，tokenizer以nearest normalized codebook entry量化，用cosine alignment和双stop-gradient L2稳定，KMeans初始化、EMA更新codebook。dataset manifest拥有domain mixture/provenance，preprocess拥有16 kHz/mel/patch/约175 ms contract，每轮teacher snapshot与codebook revision拥有target语义，encoder checkpoint拥有representation state；`raw audio → patch/mask → encoder → discrete-target CE`与`teacher → tokenizer/codebook → next encoder iteration`形成版本化mutual-refinement lineage。
- **Implementation / evaluation contract:** Base 90M为12层、hidden768/FFN3072/12 heads，Large 300M为24层、hidden1024/FFN4096/16 heads；约20k小时/7.3M instances来自FMA、AudioSet、FreeSound、BBC、iNat等。两者batch约10.7k audio-seconds、400k updates、40k warmup、AdamW，LR分别`5e-4`与`1e-4`。HPC allocations可核，但GPU型号/数量、precision、wall time与energy未披露。6 task types、25 datasets横跨三域，分别用frozen linear probe、full fine-tune或frozen encoder+trained decoder；reasoning任务还引入BERT/CLAP text encoder，X-ARES把异构metrics归一化。比较BEATs iterations、AudioMAE/EAT/Data2Vec/Whisper-small、domain-specific encoders及272k小时Dasheng 600M/1.2B；iteration和capacity并非单调，OpenBEATs-Large aggregate `.552`仍低于Dasheng-1.2B `.570`。
- **Proof / non-proof / threats:** 证据支持在作者data/recipe/evaluator contract下，以开放multi-domain mixture和masked discrete-token pipeline训练共享audio representation，并说明general-purpose claim必须绑定domain slices、task recipes与codebook lineage；不证明universal encoder、mixture因果解释全部收益、masked objective普遍胜出、300M具有compute efficiency、encoder本身拥有reasoning、适合speech/fine temporal workload或具备production latency/SLO。缺matched-compute/data baseline、mixture ablation、seed/CI/significance；LP/FT/decoder-FT与normalized average混用，AudioSet漂移、heterogeneous scorer和175 ms patch共同限制结论。
- **Trade-off / coexistence / disposition:** multi-domain mixture增加negative transfer、duplicate/license/sampling-policy风险；iterative tokenizer↔encoder增加teacher/codebook/checkpoint三层lineage、stale target与mismatch failure；variable length降低padding假设却损伤batch regularity，coarse patch丢失短时信息。窄域、固定SLO仍可优先domain-specific encoder；speech可选更细stride，lineage成本过高时continuous reconstruction仍成立。Ch23已有representation/codebook identity，却尚未明确`encoder↔tokenizer iterative lineage + cross-domain audio evaluation contract`，future `Refine — Existing Argument / Experimental`；当前Books Frozen。
- **Open Questions:** event-time full training/eval repository immutable commit与logs、matched-compute mixture ablation、speech-compatible stride、per-domain sampling/negative transfer、AudioSet snapshot、LP/FT scorer weighting与variance仍待核验。

### Franca: Nested Matryoshka Clustering for Scalable Visual Representation Learning

- **Identity / revision / coverage:** Source Family `ARXIV-2507.14137`，v1 first-public 2025-07-18 17:59:55 UTC，25/30；v2/v3/v4只作forward revisions。v1 Abstract、Introduction、Related Work、Method与公式、Implementation、classification/robustness/dense/3D evaluations、component ablation与Conclusion均已读；v1没有独立Limitations或Appendix。official repo当前公开data-prep、training、RASA、models与checkpoints，但event-time immutable commit/tag未锁定，current artifact不能无条件回填v1。Owner `MULTIMODAL-REPRESENTATION`（Ch23），handoff `TRAIN-DATA`、`TRAIN-PRETRAINING`与`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / previous / changed constraint:** DINO/iBOT式单一大codebook和per-model proprietary data，在固定representation width与单一benchmark上实现简单且合理；但聚类语义本就存在多粒度歧义，naive multi-head MLP又会参数爆炸，dense patch clusters还可能编码绝对位置而非object semantics。新约束是同一open-data encoder要支持不同memory budget、coarse-to-fine semantics与dense transfer，同时保持可审计training lineage。
- **Mechanism / state / control flow:** student/EMA teacher共享ViT backbone，DINO/iBOT heads经Sinkhorn-Knopp产生balanced targets。Franca对encoder feature取嵌套subspaces `m_1<...<m_k=d`，每个slice用独立projection/clustering head和按dimension缩减的prototype数，loss等权求和；CyclicMask循环移动可见区域，避免inverse-block中心偏置。RASA在pretraining后训练2D patch-position regressor，将两行权重Gram-Schmidt正交化后，从每个patch embedding减去position-plane projection，迭代至position loss不再下降，并把最终线性变换折叠进末层。dataset/preprocess、teacher snapshot、nested-head/prototype schema、RASA transform与backbone checkpoint必须分开拥有版本；“去除可线性预测位置”不等于消除全部geometry或spurious correlation。
- **Implementation / evaluation contract:** ViT-B/L/G为86M/300M/1.1B，无register、从头训练500 epochs/625K iterations，五个nested heads维度`[d,d/2,...,d/16]`；batch 2048/3072，32/64/128张H100，LR `1e-3`或`3.5e-4`、80 epoch warmup。数据为ImageNet-21K和只使用image modality的LAION-600M。RASA在frozen backbone上用Pascal VOC、518² crops、batch128、AdamW和9轮position head；高分辨率适配仅Base、20K iterations。评测包括ImageNet linear/k-NN与OOD、fine-grained classification、Hummingbird in-context、linear segmentation、overclustering、SPair-71K/NYUv2和Feat2GS；作者有CyclicMask→Matryoshka→RASA→high-resolution逐项ablation，但未给seed/CI、training overhead分解或production latency/SLO。
- **Proof / non-proof / limitations:** 结果支持在作者open-data、ViT与probe contract下，nested multi-granular clustering、mask exposure balancing与linear positional projection能改善若干global/dense representation probes，也证明compression slice本身应进入representation contract；不证明cluster hierarchy具有因果/人类语义、RASA保留所有task-relevant geometry、Franca普遍优于DINOv2/SigLIPv2、开放数据是收益原因、3D probe等于world model或production更高效。DINOv2比较跨data/distillation/resolution且paper多处依赖作者reproduction；LAION mixture无独立ablation，RASA使用VOC后再评VOC相关dense tasks存在适用边界，v1无正式threats section。
- **Trade-off / coexistence / disposition:** nested heads和多loss提高训练状态/gradient coupling，压缩维度换下游memory却可能丢失domain-specific signals；RASA减少linear position bias，却可能删掉对detection、robotics或geometry重要的absolute coordinates，并增加transform/backbone兼容与upgrade invalidation；large open-data training仍有license、filter、dedup与cost压力。固定宽度single-head在目标任务明确时更简单，保留position的representation在坐标敏感任务仍成立。Ch23已覆盖continuous/discrete/codebook、rate-distortion与position/provenance identity，但尚未明确`single granularity → nested multi-granularity → downstream selectable slice`及`position bias probe → bounded projection removal`分支，future `Refine — Existing Argument / Experimental`；当前Books Frozen。
- **Open Questions:** event-time commit、nested-head parameter/compute overhead、RASA cross-dataset validation、seed/CI、matched-data/distillation baselines、position-removal对coordinate-sensitive tasks影响及各revision差异仍待核验。

### ElasticMM: Efficient Multimodal LLM Serving with Elastic Multimodal Parallelism

- **Identity / revision / coverage:** Source Family `ARXIV-2507.10069`，v1 first-public 2025-07-14，28/30；v2/v3与NeurIPS 2025 Oral仅作forward evidence。v1 Abstract、motivation、EMP算法、unified multimodal prefix cache、non-blocking encoding、implementation、evaluation、ablation、Appendix等价性讨论与limitations均已读。Owner `INFER-PD-DISAGGREGATION`，handoff `MULTIMODAL-REPRESENTATION`、`INFER-KV-CACHE`、`INFER-SCHEDULING`。
- **Problem / old design / changed constraint:** 静态tensor/pipeline parallel与单一request queue在text-only或稳定modality mix下简单、可预测；MLLM把vision encode、prefill、decode变成不同比例的stage，在线text/multimodal比例漂移会制造stage bubbles、head-of-line blocking与prefix复用断裂。
- **Mechanism / ownership / flow:** 系统拆分encoding/prefill/decode，按modality-aware proactive/reactive signal弹性迁移GPU partition；visual-token cache与KV-prefix tree统一prefix identity，encoding异步于decode。scheduler拥有request/stage placement，encoder拥有visual tokens，prefill/decode拥有authoritative KV，cache key必须绑定model/tokenizer/preprocessor/image digest与revision；NCCL/NVLink只搬运state，不改变owner。
- **Evaluation contract / proof boundary:** Llama-3.2-Vision-11B、Qwen2.5-VL-7B，VisualWebInstruct/ShareGPT-4o与Poisson/production traces，单机8×A800-80GB、2×Xeon 8358P、2TB RAM、NVLink 400GB/s，对比vLLM 0.6.6及作者decoupled baseline，SLO为light-load latency的10倍并扫1～5倍scale。作者报告最高4.2×TTFT、3.2～4.5×throughput，EMP ablation 1.8×/2.3×；只证明该单机workload下stage-aware elasticity有效，不证明多节点、其他vision encoder、通用SLO收益。Appendix关于parallel reconfiguration“exact equivalence”及FP16约`1e-7`误差不构成跨kernel/拓扑的bitwise theorem，标记`Disputed — Author-only numerical claim`。
- **Trade-off / coexistence / disposition:** elasticity增加迁移、warm-up、cache invalidation、control-loop oscillation与fault recovery state；unified cache提高reuse但扩大identity错误blast radius。modality mix稳定或迁移成本高时静态partition仍合理。future `Refine — Existing Argument / Experimental`；Historical Books Gate关闭。

### CodeJudgeBench: Benchmarking LLM-as-a-Judge for Coding Tasks

- **Identity / coverage:** Source Family `ARXIV-2507.10535`，v1 first-public 2025-07-14，27/30；v2只作forward evidence。v1 18页全文覆盖benchmark construction、CodeGen/Repair/TestGen task、26 judges、4,260 pair samples、prompts、position/generalization/preprocessing/point-vs-pair analyses、tables、limitations与appendix。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW`与`PLATFORM-SECURITY`。
- **Problem / mechanism / state:** executable tests提供强ground truth但测试构造/执行昂贵；直接用judge扩展性好，却可能按表面风格而非correctness判别。作者从HumanEval+/MBPP+生成10个responses，经unit tests分good/bad pool，构造pairwise code generation、repair与unit-test-generation样本；dataset owner保留problem/test/programmer model/error/output provenance，judge run保留prompt、candidate order、raw/full-code transform与model revision。
- **Evaluation contract:** 三个thinking programmer、temperature 1.0、max output、每题10 samples；26 general/reasoning/reward/judge-tuned/coder models，pair样本交换A/B各判一次。论文显示thinking judges整体更强但对programmer family和位置敏感，pairwise优于pointwise，保留完整response通常优于只抽code；这些是作者harness结果，不证明judge可替代execution verifier、跨语言/仓库任务泛化或生产成本更低。
- **Trade-off / failure / disposition:** pairwise增加两次调用和排序state，full response保留有用rationale也带来style/length leakage；unit-test ground truth自身可能不完备。可靠release gate应把judge当triage/排序信号，与execution、static analysis和human review分层。future `Refine — Existing Argument / Experimental Evaluation Evidence`，不把accuracy表写成通用事实。

### Multiple Choice Learning of Low-Rank Adapters / LoRA-MCL

- **Identity / coverage:** Source Family `ARXIV-2507.10419`，v1 first-public 2025-07-14，25/30；later revisions只作forward evidence。v1全文覆盖MLE/WTA推导、mixture/Markov-chain分析、batch-parallel implementation、audio/image captioning experiments、equal-parameter baselines、appendices与compute details。Owner `TRAIN-LORA`，handoff `MODEL-SAMPLING`与`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Problem / old design / mechanism:** 单一MLE adapter学习条件分布的平均/主模态，在target唯一或sampling足够时最简单；多种合理continuation同时存在时容易mode averaging。LoRA-MCL为同一frozen backbone挂K组LoRA hypotheses，以winner-takes-all/relaxed WTA把每个sample主要更新给最匹配adapter；把batch复制K次实现并行forward，并用`epsilon`给non-winners少量梯度避免collapse。
- **Ownership / evaluation boundary:** base checkpoint、K个adapter、winner assignment、epsilon/rank/alpha与decoding policy分别版本化；论文在Qwen2-Audio约8.4B与LLaVA-1.5-7B、Clotho-v2/AudioCaps/TextCaps上比较LoRA-MLE、beam/diverse beam与LoRA-MCL，并控制部分parameter/forward-pass budget。结果支持该captioning contract下quality-diversity分支，但不估计mixture weight `p(theta_k|c)`，不证明一般文本、RLHF、production latency或K增大可扩展；训练compute和serving memory随K增长。
- **Trade-off / coexistence / disposition:** specialization换来adapter routing/selection、collapse、uneven utilization、batch expansion与artifact explosion；单一LoRA在目标分布单峰、部署预算严或需要一个canonical answer时仍优。future `Refine — Existing Argument / Experimental`。

### How Many Instructions Can LLMs Follow at Once? / IFScale

- **Identity / coverage:** Source Family `ARXIV-2507.11538`，v1 first-public 2025-07-15，26/30。全文覆盖IFScale construction、retry/coherence filter、20-model setup、five seeds、accuracy/variance/position/latency/error/coherence analyses、prompts、keyword list与limitations。Owner `AGENT-CONTEXT`，handoff `PLATFORM-EVALUATION-SYSTEM`与`AGENT-WORKFLOW`。
- **Problem / mechanism:** 少量instruction benchmark在真实policy bundle较小时合理；当system、tool、tenant、safety与task constraints累积，单项正确不代表集合可同时满足。IFScale用business-report主任务叠加10～500个keyword inclusion constraints，regex给atomic adherence，另统计omission/modification、primacy、latency、variance与o4-mini coherence。
- **Evaluation contract / proof boundary:** 20个provider models经OpenRouter default generation、reasoning effort high，密度每10递增且5 seeds；作者观察多数模型在高密度出现performance cliff、omission上升和中段primacy peak。该结论仅适用于English/SEC vocabulary、简单positive keyword constraints与当时provider revisions；不证明真实互相冲突policy、tool permissions或语义约束遵循，也不能把“500 instructions”解释为认知容量常数。
- **Trade-off / disposition:** 可自动打分与密度扫描换来synthetic task、retry selection bias、regex false equivalence和provider drift；生产应把constraints结构化、分层验证并暴露unsatisfied set，而非继续堆prompt。future `Refine — Existing Argument / Experimental Evaluation Evidence`。

### Deep Hidden Cognition Facilitates Reliable Chain-of-Thought Reasoning

- **Identity / coverage:** Source Family `ARXIV-2507.10007`，v1 first-public 2025-07-14，26/30；v2/AAAI-26仅作forward evidence。v1全文覆盖dataset construction、head probes、confidence predictor、MSE/ECE、guided beam search、unimodal/multimodal tables、self-correction、LRM test、appendix calibration与ablations。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-REFLECTION`与`MODEL-MULTI-HEAD-ATTENTION`。
- **Mechanism / ownership:** 从每层attention head的最后token activation训练binary probes，按validation correlation选top-K heads，再拼接训练confidence predictor；decode时把generation probability与predictor confidence融合选择step-level beam。probe/checkpoint、selected-head coordinates、label generator、calibration split与base model revision共同定义confidence artifact，不能跨模型静默复用。
- **Evaluation boundary:** LLaMA2-7B/13B、LLaVA-7B/13B、Qwen2.5-VL-7B及R1 distilled case，WikiQA/TruthfulQA、GSM8K/SVAMP/StrategyQA/BoolQ/Boolean、ScienceQA/RealWorldQA/CLEVR-Math/MMStar；论文报告ECE/Brier/AUC与task accuracy improvements，但多模态表存在若干零/负增益，negative CoT steps由GPT-4o合成，未证明probe读取因果“truth”、跨domain calibration、long-horizon independence或无需external evidence。
- **Trade-off / disposition:** internal signal降低每步外部verification成本，却增加activation access、model-specific training、beam compute、label leakage与miscalibration risk；黑盒API、开放域事实和高风险claim仍需retrieval/execution verifier。future `Refine — Existing Argument / Experimental / Calibration Boundary`。

### SENTINEL: Sentence-level Early Intervention for Object Hallucination

- **Identity / coverage:** Source Family `ARXIV-2507.12455`，v1 first-public 2025-07-16，25/30；v2/v3只作forward evidence。v1全文覆盖candidate bootstrapping、dual-detector validation、iterative context、C-DPO objective、training config、hallucination/general benchmarks、ablation、appendix与repo link。Owner `TRAIN-DPO`，handoff `MULTIMODAL-REPRESENTATION`与`PLATFORM-EVALUATION-SYSTEM`。
- **Problem / mechanism / state:** inference-only contrastive decoding在无需训练时合理，但持续增加per-token compute；whole-response preference pairs又会把早期hallucination与后续style/context混在一起。SENTINEL逐句采样，抽取concrete entities，以两个open-vocabulary detectors交叉验证presence，选择context-coherent positive与hallucinated negative，递归把positive加入context，再用只覆盖当前句tokens的C-DPO训练LoRA。
- **Evaluation contract / proof boundary:** LLaVA-v1.5-7B/13B，LoRA rank128/alpha256、1 epoch、global batch64、max length2048；Object HalBench、AMBER、HallusionBench及VQAv2/TextVQA/ScienceQA/MM-Vet，对比VCD/OPERA/DoLa/EFUF/HA-DPO并做component ablation。只证明作者object-detector/data/model contract下降低object hallucination；检测器false positive/negative成为label truth，不能外推关系、计数、知识或长视频hallucination，亦不证明“90% reduction”为普遍率。
- **Trade-off / disposition:** 自动preference data省人审但继承detector ontology、entity parser与bootstrapped-context bias；训练改权重，可能损害未测capability。低延迟固定域可采用，开放域高风险回答仍需post-generation evidence verification。future `Refine — Existing Argument / Experimental`。

### PhyWorldBench

- **Identity / coverage:** Source Family `ARXIV-2507.13428`，v1 first-public 2025-07-17，25/30；later ICLR-2026 revision只作forward evidence。v1 35页覆盖taxonomy、1,050-prompt construction、human evaluation、CAP MLLM judge、12 video models、prompt variants、anti-physics、category tables、failure analysis与appendix。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-WORLD-MODELS`与`MULTIMODAL-GENERATIVE-PARADIGMS`。
- **Problem / mechanism:** perceptual/aesthetic video metrics在只关心visual fidelity时合理，却不能区分物理一致性；benchmark把object motion、conservation、rigid interactions、human/animal motion等分层，并加入故意违背物理的anti-physics prompts，区分“理解现实约束”与“遵循反事实创作指令”。CAP把prompt-specific standard与video交给MLLM，分别判semantic adherence与physical commonsense。
- **Evaluation boundary:** 1,050 curated prompts、event/physics-enhanced/detailed三种提示，12个open/proprietary T2V models，human labels与Qwen-VL/Gemini/GPT系列judge做ROC-AUC/ablation。作者自己观察judge aesthetic bias与overconfidence；这证明该harness揭示当时T2V physical failure，不证明video generator是action-conditioned world model、CAP等同物理simulator、anti-physics能识别causal understanding或model ranking随版本稳定。
- **Trade-off / disposition:** 细粒度standard提升诊断性但增加expert curation、judge drift与ambiguous-event disagreement；human review仍是高风险边界。future `Refine — Existing Argument / Experimental Evaluation Evidence`。

### ECP: Training-Free High-resolution MLLM Enhancement

- **Identity / coverage:** Source Family `ARXIV-2507.10202`，v1 first-public 2025-07-14，23/30。全文覆盖two-stage framework、region proposal/cropping、4K GUI grounding、4K/8K perception、random-region ablation、cross-model combinations、qualitative analysis与limitations。Owner `MULTIMODAL-REPRESENTATION`，handoff `AGENT-WORKFLOW`与`INFER-SCHEDULING`。
- **Problem / mechanism:** 全图downsample在普通分辨率成本低且保留global context；4K/8K small-object任务会丢细节，而直接扩大visual tokens增加quadratic attention与serving latency。ECP先让一个MLLM基于低分辨率全图做Explore/region proposal，再crop原图高分辨率region交给Perceive model完成grounding/QA；proposal/crop transform与原图坐标系共同拥有region identity。
- **Evidence boundary / trade-off:** 在ScreenSpot-Pro与HR-Bench 4K/8K、Qwen2-VL/OS-Atlas组合中作者报告相对single-stage增益，random crop显著下降；不证明proposal正确性、任意task/model泛化、端到端latency/cost优于native tiling，且失败可由首阶段漏检不可恢复。静态tiling适合coverage优先，single-stage适合低分辨率/低延迟。future `Refine — Existing Argument / Experimental`。

### Astrogator: Formal Verification of LLM-generated Ansible

- **Identity / coverage:** Source Family `ARXIV-2507.13290`，v1 first-public 2025-07-17，25/30。全文覆盖natural-language-like formal query、State Calculus、symbolic interpreter、module description language、underspecification questions、21-task benchmark、VM execution oracle、six-model/1,260-program evaluation、limitations与appendix query。Owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-TOOL`、`AGENT-WORKFLOW`与`PLATFORM-SECURITY`。
- **Problem / mechanism / ownership:** tests在observable I/O充分时合理，但无法证明所有state transitions或用户未表达的intent；直接相信LLM judge也无formal guarantee。Astrogator要求用户确认formal query，symbolically interprets Ansible against partial filesystem/package/service state，并在query underspecified时询问用户。用户拥有intent approval，query拥有spec state，module model拥有semantics，verifier拥有proof result，runtime VM只提供independent execution oracle。
- **Evaluation contract / proof boundary:** Debian 12.11、Ubuntu 24.04.2、RHEL 9.6 snapshots；21 Ansible tasks，6 LLMs×10 outputs=1,260 programs，execution tests判334 correct/926 incorrect；verifier接受277/334 correct并拒绝856/926 incorrect。证据支持该restricted Ansible/module subset的soundness-usefulness trade-off，不证明natural language intent已被形式化、shell/unsupported modules、general-purpose languages或verified program安全；false reject来自unsupported features和simplified models，少量incorrect accepted仍存在。
- **Trade-off / disposition:** formal query提升可审计性却把specification burden前移，并需要维护module semantics与state abstraction；test-only仍适合低风险fast feedback，formal verification适合高代价workflow的bounded action schema。future `Refine — Existing Argument / Experimental / Language-specific`。

### Context Engineering survey

- **Identity / coverage:** Source Family `ARXIV-2507.13334`，v1 first-public 2025-07-17，v2 2025-07-21为W30 forward revision，27/30。已按v1 166页HTML分节读取Introduction/Related Work、theoretical framework、Foundational Components、System Implementations、Evaluation、Future Directions、Conclusion与影响核心分类的references；作者bibliography repository只作related artifact。Owner `AGENT-CONTEXT`，handoff `AGENT-RAG`、`AGENT-MEMORY`、`AGENT-TOOL`、`AGENT-MULTI-AGENT`与`PLATFORM-EVALUATION-SYSTEM`。
- **Taxonomy / ownership:** survey把context engineering定义为对inference information payload的设计、生成、处理、管理：foundation层包括retrieval/generation、processing、management；system层包括RAG、memory、tool-integrated reasoning、multi-agent。该分类支持把prompt text、retrieved evidence、derived memory、tool observation和agent message分开拥有provenance/lifetime/authority，而非视作一个无限字符串。
- **Evidence boundary:** “over 1400 papers”与“first comprehensive”是作者声明；v1正文未披露database/query、时间边界、inclusion/exclusion、dual screening或可复算PRISMA式protocol，因此不能证明systematic completeness。该文没有新algorithm、original benchmark或production SLO；评估章节本身指出component-level与integrated system evaluation、memory generalization及standardized benchmark仍不足。
- **Trade-off / disposition:** unified vocabulary改善跨层handoff，但边界过宽会把prompt、RAG、memory、tool与multi-agent都重新命名而不产生新mechanism；应把它作为navigation taxonomy，不作为因果/性能证据。future `No Change — Already Covered / Survey Taxonomy`，Review Pending已清零，Historical Books Gate仍关闭。

### Low-score source/date/rejection closure

- **Einstein Fields（19/30，`2507.11589` v1 2025-07-15）：** 以field-equation style inductive bias处理特定AI4Science问题，来源与日期可核，但跨域系统机制、artifact/production contract和项目长期相关性不足。`Rejected — Below Threshold / Domain-specific AI4Science`。
- **FantasyPortrait（18/30，`2507.12956` v1 2025-07-17）：** domain-specific portrait generation方法，作者视觉质量实验不建立通用representation、generation runtime或evaluation owner的新结论。`Rejected — Below Threshold / Domain-specific Generation`。
- **Logic-layer Prompt Control Injection（19/30，`2507.10457` v1 2025-07-14，v2 2025-08-06）：** 提出encoded、delayed、conditional payload经memory/vector/tool output跨session触发的安全分类；event-time论文以taxonomy与scenario为主，缺少可复算attack corpus、baseline/ablation和artifact contract，不能作为新防御机制证据。`Rejected — Below Threshold / Conceptual Security Taxonomy`。
- **Prompt Injection 2.0（18/30，`2507.13169` sole v1 2025-07-17）：** 14KB短文综合prompt injection与XSS/CSRF/AI worm等hybrid threats，安全方向相关，但主要复述已有threat patterns与architectural advice，没有足够原始实验或机制对照。`Rejected — Below Threshold / Narrative Threat Synthesis`。
- **VLA Models in Robotic Manipulation survey（19/30，`2507.10672` sole v1 2025-07-14）：** 汇总102 models、26 datasets与12 simulators，并给出data/simulator taxonomy；其VLA闭环、sim-to-real与dataset gaps已由Ch26及更强primary studies承载，survey没有独立机制或可执行evaluation contract。`Rejected — Below Threshold / Survey Already Covered`。
- **DeepResearchEco（19/30，`2507.10522` sole v1 2025-07-14）：** recursive depth/breadth-controlled literature workflow与49个ecology questions能说明domain workflow形态，但“21× sources”主要衡量source count而非claim correctness、coverage calibration或expert adjudication，不能建立通用research-agent contract。`Rejected — Below Threshold / Domain Workflow Evidence`。
- **Enterprise structured-data RAG（17/30，`2507.12425` sole v1 2025-07-16）：** hybrid BM25/dense、metadata filter、rerank、semantic/table chunking属于已有RAG组合；single-author报告的企业数据与Likert改进缺dataset manifest、artifact release、independent evaluator及workload/SLO，不能形成新owner。`Rejected — Below Threshold / Insufficient Evaluation Contract`。
- **Visual Input for Robotic Path Planning（18/30，`2507.12391` sole v1 2025-07-16）：** 15 MLLMs在2D grid上比较text与text+vision，揭示large-grid退化；环境过度简化且无closed-loop embodiment、control frequency、dynamic obstacle或physical safety，作为Ch26 benchmark signal保留但不进入核心候选。`Rejected — Below Threshold / Simplified Benchmark`。
- **Probing for Arithmetic Errors（19/30，`2507.12379` sole v1 2025-07-16）：** hidden-state probes在3-digit addition及addition-only GSM8K检测错误并触发reprompt，机制与Deep Hidden Cognition同属model-specific probe family；任务范围、probe portability和causal truthfulness证据更窄，去重后作为related evidence。`Rejected — Below Threshold / Narrow Related Evidence`。
- **Thought Purity（19/30，`2507.12314` v1 2025-07-16；later v2/v3 forward evidence）：** dual-reward RL尝试从拒绝转向CoT recovery，但event-time evidence集中在作者构造攻击/模型组合，artifact、threat prevalence、adaptive attacker与deployment guardrail contract不足；不覆盖AutoSteer owner。`Rejected — Below Threshold / Narrow Security Experiment`。
- **CAST cross-task activation steering（19/30，`2507.13236` sole v1 2025-07-17）：** 从高资源task examples提取contrastive activation并注入低资源task，属于无需parameter update/input expansion的experimental transfer branch；与现有steering family去重后，cross-domain/cross-lingual author experiments不足以建立跨模型state portability或production safety owner。`Rejected — Below Threshold / Experimental Transfer Case`。

### Strict Full Source Review closure ledger

- **Retained（42/42）：** 42项20+候选均完成event-version正文、method/evaluation/limitations、owner/adjacent chapter与disposition审计；Context Engineering按166页v1分节审计，未把目录或“1400+”作者口径当作systematic-review证明。
- **Low closure（11/11）：** 11项均完成source identity、v1 date、revision与非模板化拒绝理由；没有用提高阈值来回避20+全文审计。
- **Pending / blocked:** `Review Pending = 0`，`Unverified / Blocked = 0`。缺event-time artifact的候选已作为evidence boundary记录，但其论文正文可访问，不冒充blocked。
- **Spillback:** 多个`2507.04*～2507.09*` family按v1日期归W27/W28；RedOne与Teach Old SAEs回拨W28；Context Engineering 2025-07-21 v2是W30 forward revision；FlowSpec `2507.02620`的2025-07-14 v2仍归W27 owner，均不重复计分。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。
- RedOne `2507.10605` v1 first-public为2025-07-13，canonical owner回拨W28；2025-10-12 v2只作forward revision，W29不重复计分。
- Teach Old SAEs source family的OpenReview forum `d4XXFVAlV7` first-public为2025-07-08，canonical owner回拨W28；arXiv `2507.12990` v1 2025-07-17只作forward revision。因未取得7月8日原始submission revision，W28保留P3 event-time revision pending。

## Knowledge Tree Position

- SGLang Multiple Token Prediction integration → 第 44、47、51、52 章（Direct Evolution）
- Hyma/FLEXITOKENS/Voxtral → `MULTIMODAL-REPRESENTATION`、`MODEL-TOKENIZER`；Balalaika → `TRAIN-DATA`。
- SWE-Perf/GitChameleon/RLVR contamination → `PLATFORM-EVALUATION-SYSTEM`；AutoSteer → `PLATFORM-SECURITY`；ChatGPT agent → `AGENT-PLATFORM`。
- ElasticMM → `INFER-PD-DISAGGREGATION`；CodeJudgeBench、Deep Hidden Cognition、PhyWorldBench、Astrogator → `PLATFORM-EVALUATION-SYSTEM`。
- LoRA-MCL、SENTINEL → `TRAIN-LORA`、`TRAIN-DPO`；IFScale/Context Engineering → `AGENT-CONTEXT`；ECP → `MULTIMODAL-REPRESENTATION`。

## Recommended Action

- 53个owner identity已写回；42/42 retained完成strict Full Source Review，11/11低分闭合，普通Review Pending与Blocked均为0。
- fixed-org、engineering release、arXiv event-date、相邻周spillback与cross-index replay已完成本周Gate；后续新发现仍按owner week幂等回补，但不保留泛化的“recall open”伪状态。
- Historical Books Gate保持关闭；所有`Refine`/`No Change`仅是future disposition，不授权本轮修改Books。

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

`Frozen — Historical Books Gate Closed`。本轮只重建Weekly evidence；Candidate Evidence Gate通过不等于Books Integration授权。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 将旧1项账本扩展并复核为53个scored owners；42/42 retained strict complete、11/11低分闭合、0 Pending/0 Blocked；RedOne与Teach Old SAEs按首次公开日期回拨W28，FlowSpec v2保持W27 owner。
- 本阶段未修改Books、ROADMAP或DECISIONS。

## Open Questions

- ElasticMM的多节点迁移成本、control-loop oscillation与跨kernel数值漂移能否被独立复现？CodeJudgeBench的judge signal在repository-level code、更多语言及hidden tests下能否保持calibration？
- Context Engineering缺少可复算search protocol，OpenBEATs缺event-time full training repository，Franca缺event-time commit；这些是明确evidence boundary，不是普通Review Pending。π³的892.37M/959M scope以及Turing Machine Imitator的18/28 tasks与50K/20K train冲突仍需event-time artifact或later revision解释。

## Sources

- SGLang Multiple Token Prediction integration — https://www.lmsys.org/blog/2025-07-17-mtp/（First Public: 2025-07-17；Accessed: 2026-07-31）
- SGLang reproduction issue #7998 — https://github.com/sgl-project/sglang/issues/7998（Opened: 2025-07-13；Accessed: 2026-07-31）
- Hyma — https://arxiv.org/abs/2507.10015
- Mixture-of-Recursions — https://arxiv.org/abs/2507.10524
- Reasoning or Memorization? — https://arxiv.org/abs/2507.10532
- GitChameleon 2.0 — https://arxiv.org/abs/2507.12367
- SWE-Perf — https://arxiv.org/abs/2507.12415
- FLEXITOKENS — https://arxiv.org/abs/2507.12720
- AutoSteer — https://arxiv.org/abs/2507.13255
- Voxtral — https://mistral.ai/news/voxtral/
- Voxtral technical report — https://arxiv.org/abs/2507.13264
- Balalaika v1 — https://arxiv.org/abs/2507.13563
- ChatGPT agent launch — https://openai.com/index/introducing-chatgpt-agent/
- ChatGPT agent system card — https://openai.com/index/chatgpt-agent-system-card/
- Seq vs Seq / Ettin — https://arxiv.org/abs/2507.11412
- ElasticMM v1 — https://arxiv.org/html/2507.10069v1
- CodeJudgeBench v1 — https://arxiv.org/pdf/2507.10535v1
- LoRA-MCL v1 — https://arxiv.org/html/2507.10419v1
- IFScale v1 — https://arxiv.org/html/2507.11538v1
- Deep Hidden Cognition v1 — https://arxiv.org/html/2507.10007v1
- SENTINEL v1 — https://arxiv.org/html/2507.12455v1
- PhyWorldBench v1 — https://arxiv.org/html/2507.13428v1
- ECP high-resolution MLLM v1 — https://arxiv.org/html/2507.10202v1
- Astrogator v1 — https://arxiv.org/html/2507.13290v1
- Context Engineering survey v1 — https://arxiv.org/html/2507.13334v1
- REST — https://arxiv.org/abs/2507.10541
- REST artifact — https://github.com/opendatalab/REST
- EmbRACE-3K — https://arxiv.org/abs/2507.10548
- EmbRACE-3K project — https://mxllc.github.io/EmbRACE-3K/
- DIJA — https://arxiv.org/abs/2507.11097
- DIJA artifact — https://github.com/ZichenWen1/DIJA
- EXAONE 4.0 — https://arxiv.org/abs/2507.11407
- EXAONE official repository — https://github.com/LG-AI-EXAONE/EXAONE-4.0
- RiemannLoRA — https://arxiv.org/abs/2507.12142
- MMHU — https://arxiv.org/abs/2507.12463
- MMHU project — https://mmhu-benchmark.github.io/
- PhysX-3D — https://arxiv.org/abs/2507.12465
- PhysX-3D project — https://physx-3d.github.io/
- MindJourney — https://arxiv.org/abs/2507.12508
- MindJourney project — https://umass-embodied-agi.github.io/MindJourney/
- Mono-InternVL-1.5 — https://arxiv.org/abs/2507.12566
- Mono-InternVL official repository — https://github.com/OpenGVLab/Mono-InternVL
- AnyCap — https://arxiv.org/abs/2507.12841
- AnyCap official repository — https://github.com/qishisuren123/AnyCap
- Inverse RL Meets LLM Post-Training — https://arxiv.org/abs/2507.13158
- Generative Energy Arena — https://arxiv.org/abs/2507.13302
- AbGen — https://arxiv.org/abs/2507.13300
- AbGen artifact — https://github.com/yale-nlp/AbGen
- Diffuman4D — https://arxiv.org/abs/2507.13344
- Diffuman4D project — https://diffuman4d.github.io/
- Turing Machine Imitator / TAIL — https://arxiv.org/abs/2507.13332
- π³ paper — https://arxiv.org/abs/2507.13347
- π³ official repository — https://github.com/yyfz/Pi3
- VisionThink — https://arxiv.org/abs/2507.13348
- VisionThink artifact — https://github.com/JIA-Lab-research/VisionThink
- CSD-VAR v1 — https://arxiv.org/abs/2507.13984
- CSD-VAR project — https://nqbinhcs.github.io/csd-var-page/
- CSD-100 later artifact — https://huggingface.co/datasets/qualcomm/csd100
- OpenBEATs v1 — https://arxiv.org/html/2507.14129v1
- OpenBEATs project — https://shikhar-s.github.io/OpenBEATs
- OpenBEATs event-time checkpoint — https://huggingface.co/shikhar7ssu/OpenBEATs-Large-i1/commits/main
- Franca v1 — https://arxiv.org/html/2507.14137v1
- Franca official repository — https://github.com/valeoai/Franca
- Logic-layer Prompt Control Injection — https://arxiv.org/abs/2507.10457
- Prompt Injection 2.0 — https://arxiv.org/abs/2507.13169
- VLA Models in Robotic Manipulation survey — https://arxiv.org/abs/2507.10672
- DeepResearchEco — https://arxiv.org/abs/2507.10522
- Enterprise structured-data RAG — https://arxiv.org/abs/2507.12425
- Visual Input for Robotic Path Planning — https://arxiv.org/abs/2507.12391
- Probing for Arithmetic Errors — https://arxiv.org/abs/2507.12379
- Thought Purity — https://arxiv.org/abs/2507.12314
- CAST activation steering — https://arxiv.org/abs/2507.13236
- Teach Old SAEs OpenReview — https://openreview.net/forum?id=d4XXFVAlV7（First Public: 2025-07-08；W28 owner）
- Teach Old SAEs arXiv v1 — https://arxiv.org/abs/2507.12990（First Public: 2025-07-17；W29 forward revision only）
