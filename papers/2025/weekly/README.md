# 2025 Weekly Research Index

> Coverage: 2025-W01～2025-W52
> Calendar Window: 2024-12-30～2025-12-28
> Backfilled: 2026-07-31
> Weekly Rebuild Started: 2026-08-17
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Current Status: `2025 Weekly Discovery and Evidence Rebuild In Progress`
> Books Integration: `Deferred — existing decisions are legacy/provisional input`

## Archive Contract

- 使用 ISO week-year 和完整 Monday～Sunday。2025-W01 包含 2024-12-30～2025-01-05；
  2025-12-29～12-31 属于现有 2026-W01，不在本年度重复。
- 历史回填只生成 Weekly，不补造 Daily；事件日期、first-public date、来源和 evidence
  boundary 直接保留在对应周。
- 模型 release、paper v1、model card 与后续工程集成按不同证据角色记录；同一技术只形成一个
  Books source packet。
- Google Scholar、OpenAlex、DBLP 用于每日 discovery 和去重；Crossref 用于 Weekly
  metadata 交叉检查；机制结论回到 primary source。
- 当前 75 个评分条目只是旧版 discovery seed，不是年度候选召回已经闭合的证明。2026-08-17
  起按 2026 最后一轮历史 Weekly 标准重新扫描 W01～W52；候选总数、分数区间与 Full Source
  Review 分母只在逐周 replay 完成后重新计算。
- 本阶段只修复 Weekly evidence，不创建历史 Daily、不修改 Books，也不作新的 `Integrate / Refine /
  No Change` 判断。已完成 Weekly 证据的候选统一进入 `Books Pending — Integration Deferred`。

## Coverage Map

| Weeks | Calendar Window | Main Evidence Cluster |
| --- | --- | --- |
| W01～W05 | 2024-12-30～2025-02-02 | reasoning RL、hybrid/linear attention、test-time scaling、vLLM V1、research agents |
| W06～W13 | 2025-02-03～2025-03-30 | KV-constrained scheduling、native sparse attention、speculative decoding、Dynamo、interpretability/privacy |
| W14～W20 | 2025-03-31～2025-05-18 | multimodal/MoE model families、hybrid reasoning、compiler/runtime evolution、evaluator-driven agents、RAG sufficiency |
| W21～W26 | 2025-05-19～2025-06-29 | Kubernetes-native distributed inference、KServe/Gateway、user-level DP、long-reasoning co-design |
| W27～W33 | 2025-06-30～2025-08-17 | Kimi/GLM/Qwen agentic models、MTP/SpecForge、open-weight reasoning 与 safety |
| W34～W40 | 2025-08-18～2025-10-05 | hybrid model contracts、Kubernetes DRA、dual sparsity、NSA→DSA productization |
| W41～W46 | 2025-10-06～2025-11-16 | symmetric memory、policy-as-data safety、TPU backend portability、distributed DP runtime |
| W47～W52 | 2025-11-17～2025-12-28 | pipeline fusion、DeepSeek-V3.2、test-time memory、private telemetry、speculative artifact lifecycle |

## Cross-Week Evolution Routes

### Reasoning Training and Runtime Policy

```text
W04 DeepSeek-R1 / Kimi k1.5: outcome reward 与长 rollout
→ W05 s1: inference budget 也能成为能力杠杆
→ W09 Claude 3.7 / W18 Qwen3: thinking 与 non-thinking 合并为同一模型 contract
→ W16 o3/o4-mini: reasoning 中选择工具
→ W25 MiniMax-M1: attention architecture 与 RL rollout cost 联合设计
→ W34 DeepSeek-V3.1 / W49 V3.2: thinking state 进入 tool-use runtime
```

这条路线不是“RL 替代 SFT”。R1-Zero 暴露了纯 outcome optimization 的可读性边界，R1 的
cold start 与多阶段 pipeline 说明 SFT、筛选和偏好训练仍承担行为约束。后续 hybrid models
把训练收益转化为运行时 mode、reasoning budget、parser 与 capacity-planning 问题。

### Long Context and Memory

```text
W01 Titans: test-time neural memory
→ W03 MiniMax-01: hybrid linear/softmax attention
→ W07 Native Sparse Attention: trainable + hardware-aligned sparsity
→ W16 MIRAS: memory architecture / bias / retention / optimizer 设计空间
→ W25 MiniMax-M1: long context 与 long-reasoning RL co-design
→ W37 Qwen3-Next: hybrid attention + sparse MoE + MTP
→ W40 DeepSeek-V3.2-Exp: DSA 进入可服务模型
→ W49 DeepSeek-V3.2: sparse attention + tool reasoning
→ W49 Google Research synthesis: 对 W01/W16 的机构级解释与证据补强
```

这些分支解决不同问题：linear/recurrent state 控制随长度增长的成本，sparse attention 保留
选择性精确访问，test-time memory 允许在线更新参数化状态。它们分别引入压缩损失、稀疏
index/kernel 复杂度以及污染、遗忘、回滚和 session ownership。

### Speculative Decoding as an Artifact Lifecycle

```text
W10 EAGLE-3: draft architecture 与 training-time test
→ W29 SGLang MTP: draft/verify 进入 PD + EP runtime
→ W30 SpecForge: draft training 成为独立系统
→ W52 SpecBundle: target-specific draft weights 成为 versioned serving artifact
```

演进压力从“能否预测多个 token”转为 acceptance、verification cost、batch shape、训练数据、
target/draft compatibility、provenance 与持续重训。新工具链不改变 speculative decoding 在
高并发或低接受率场景可能失效的基本 trade-off。

### Distributed Inference Control Plane

```text
W05 vLLM V1: 单 engine 内统一 request/scheduler/execution state
→ W12 Dynamo: planner、router、KV transfer 与 telemetry
→ W21 llm-d: vLLM data plane + Kubernetes-native distributed stack
→ W22 KServe v0.15: multi-node/KV/autoscaling 进入声明式 API
→ W23 Gateway API Inference Extension: InferenceModel/Pool 与 endpoint selection
→ W35～W38 DRA: accelerator allocation、sharing 与 health 进入平台资源语义
```

单机 runtime、分布式 inference runtime、serving control plane、gateway 和 device scheduler
是分层依赖，不是互相替代。每上移一层都会获得更全局的决策信息，也会新增 freshness、
ownership、failure recovery、API lifecycle 与跨组件兼容性成本。

### Privacy from Algorithm to Operational Evidence

```text
W12 inference-time DP synthetic data
→ W21 user-level DP fine-tuning
→ W46 JAX-Privacy: clipping/noise/accounting/auditing 的 distributed runtime
→ W23 Urania paper / W50 Google Research follow-up: privacy-preserving usage telemetry
```

四个节点保护的 object 不同：query/record、user contribution、training pipeline、aggregate
usage insight。不能用“采用 DP”代替 privacy unit、threat model、epsilon/delta、accounting
和 utility boundary。

## 2025 Weekly Rebuild Gate

当前状态：`Discovery/Evidence Rebuild In Progress / Books Integration Deferred`。

当前只确认了以下结构事实：52 个 ISO Weekly 目录连续覆盖 2024-12-30～2025-12-28，旧版总账
包含 75 个评分条目。它们不能证明 fixed-source discovery、academic cross-index、revision、spillback
或所有 `20+` Full Source Review 已经闭合。W01～W52 将严格单向重放；每周只有完成来源召回、
日期归属、Source Family 去重、评分、全文或明确 blocked ledger 后，才通过该周 Candidate Evidence
Gate。存在 blocked 项可以继续 forward cursor，但年度 Archive Completion Gate 保持 Open。

Forward cursor checkpoint（2026-08-18）：`W01 Passed；W02 Passed；W03 Passed；W04 Passed；W05 Passed；W06 Passed；W07 Passed；W08 Passed；Next: W09；Paused by user`。W08 已完成
discovery / ownership ledger：恢复 61 个本周 arXiv family、AI co-scientist Blog family 与 3 个本周 engineering release family，
并把 arXiv:2502.09245、arXiv:2502.11271、MUDDFormer（arXiv:2502.12170）与 SGLang v0.4.3 按 first-public date 回拨 W07。
当前 65 个 W08 owner family 中，AI co-scientist、MLGym、Qwen2.5-VL、SigLIP 2、SuperGPQA、
LoRA Knowledge Capacity、Soundwave、Embedding Space Capacity、S*、Magma、RDLM、Logic-RL、SWE-Lancer、TrustGen、MMTEB、HumanUP、SongGen、Small Model Learnability Gap、Multimodal Mamba、RAD、Decomposed Reward Models、MoM、FLAG-Trader、SoFar、Craw4LLM、PC-Agent、S2R、Selective Question Answering、SafeRoute、RelaCtrl、YOLOv12、CLIPPER、Explorer、Template-Anchored Safety、NExT-Mol、video-SALMONN-o1、InfiR、LongPO、Temporal Heads、LongWriter-V、Intuitive Physics from Natural Videos、Autellix、Sailor2、Thinking Preference Optimization、HermesFlow、Atom of Thoughts、Dynamic Concepts Personalization、RealSyn、Diffusion-Sharpening、Revisiting Test-time Scaling、AlphaMaze、PAFT、CoSyn、LServe、From RAG to Memory / HippoRAG 2、LoRAM、Text2World、HeadInfer、AdaptiveStep、AIDE、Model-guidance、Transformers v4.49.0、Accelerate v1.4.0 与 vLLM v0.7.3 已完成完整 Source Review；HermesFlow、Diffusion-Sharpening、AlphaMaze、LoRAM、AdaptiveStep 与 Model-guidance 因 objective / result / executable / scope contract 冲突保持 `Disputed`；Quantum Error Correction with RL 已完成低分来源/日期/拒绝核验；MUDDFormer 已在 W07 完成 v1-locked Full Source Review。W08 65/65 owner family 均有最终 disposition：64/64 Full Source Review + 1/1 low-score verification；0 pending；Candidate Evidence Gate 通过，Books Gate 继续关闭。此前 look-ahead 发现 Hugging Face 推荐页混合更早
Source Family：`Jailbreaking to Jailbreak` 的 v1 为 2 月 9 日，回拨 W06；LLaDA、Overthinking、
Step-Video-T2V 等 v1 位于 2 月 10～16 日，回拨 W07；推荐日期从不替代事件日期。W02 replay
发现 2025-01-09 榜单中的 DPO Kernels v1 实际属于 2025-01-05；该 family 已回拨 W01 并完成第 37 份
Full Source Review。W01 在确认 01-10 与 01-13 连续两页无新增 owner 后，重新通过 37/37 scoring、
discovery、review、owner mapping 与 13/13 low-score checks。W02 已恢复 30 余项 discovery candidates，
并完成 rStar-Math、Search-o1、Cosmos、LLaVA-Mini、Meta-CoT、Agent Laboratory、URSA、
InfiGUIAgent 与原有 vLLM 共 9 份非模板化 Full Source Review；
随后完成 Sa2VA、MotionBench、PPTAgent 与 Diffusion as Shader，当前共 13 份；GeAR 作为 replay
遗漏候选补回 census。MotionBench 的 arXiv HTML 返回无关页面，已用同 ID v1 PDF、abs metadata 与
official repository 三方闭合并保留异常记录；随后完成 OpenOmni、Dolphin、Segmenting Text and
Learning Their Rewards 与 Modern GAN Baseline；再完成 GeAR、Toto、DriveBench 与 Centurio，纠正
GeAR 的名称和 owner；随后完成 SWE-Fixer、VideoRAG、SCRIT 与 LlamaV-o1。SWE-Fixer 的 HTML
错配已用 v1 PDF/abs/repository 闭合；LlamaV-o1 的 runtime/complexity 冲突保留为 `Disputed`；随后完成
OmniManip、OVO-Bench、Migician 与 Multiagent Finetuning，明确 physical feedback、streaming runtime、
multi-image identity 与 majority pseudo-label 的证据边界；再完成 ReFocus、ConceptMaster、Video Alchemist
与 FinDaP，纠正 FinDaP event date并保留 ReFocus数据量冲突。原论文/Research共 33 份，普通
`Review Pending = 0`；Transformers 4.48.0 已完成 20分 Release/PR Source Review，llama-cpp-python 0.3.6
已完成低分 version/changelog/rejection核验。最终复核确认35/35评分、34/34 `20+` Source Reviews、
1/1低分 disposition、日期、字段、owner和Markdown曾在原分母内闭合；W03 replay 随后发现
Transformer-Squared、Tensor Product Attention与ChemAgent的v1实际仍属于W02，均已回拨并完成全文、
revision/artifact、实验合同、limitations与owner审计。继续扫描01-14～15延迟发现页面，又回拨MinMo、
O1 Replication Journey Part 3、VideoAuteur、SPAM、Grad-Mimic、Padding Tone与3DIS-FLUX。前六项完成
非模板化30字段Full Source Review；3DIS-FLUX完成低分来源、日期和拒绝核验。W03后续页又找回
Beyond Sight / FuSe（v1 2025-01-08），已回拨并完成论文、项目页、代码和数据artifact联读。最终W02通过
46/46评分、44/44 `20+` Full Source Review、2/2低分disposition、评分合计、字段、owner与Markdown检查；Process
Reward Model lessons（arXiv:2501.07301，v1 01-13）确认归W03。W03 已完成 56 项 discovery census，
并完成 MiniMax-01、PRESERVE、Process Reward Model lessons、BIOMEDICA、WebWalker、FAST、Diffusion APT、
HALoGEN、Inference-Time Scaling for Diffusion 与 Scaling Visual Tokenizers，以及 Trusted Models for
Private Inference、Physics-IQ、The Heap、TA-TiTok / MaskGen，以及 Omni-RGPT、Output-Centric Feature
Descriptions、OpenCSG 与 MMDocIR，以及 RLHS、Tarsier2、Best Practices for Open Datasets 与 uCO3D，
再加 MatchAnything、PIIP、CityDreamer4D 与 RepVideo，以及 Ouroboros-Diffusion、OmniThink、
LLMs as Judges of Unstructured Text、Advanced Patient Simulators、PokerBench、Multimodal Aesthetics；
fixed-source replay 另补回 JAX 0.5.0，并纠正 device-polymorphic export 实际属于 JAX 0.4.38。
W03 一度通过 41/41 scoring、33/33 `20+` 非模板化 30 字段 Full Source Review 与 8/8 低分
identity/date/score/rejection disposition；但 W04 的 01-20～24 Hugging Face discovery 页面随后分批暴露
22 个 arXiv v1 实际属于 01-14～19 的延迟 owners。W03 因此按 first-public date 四次重开并完成回拨审计；
最终为 63/63 scoring、46/46 `20+` Full Source Review、17/17 low-score disposition，评分、30字段、owner、
revision 与 Markdown 检查通过，cursor 进入 W04。最后两批补回 Learn-by-interact、Step-KTO、Control LLM、
DiffuEraser、GauSTAR 与 EMO2；前三项完成全文审计，后三项完成可审计低分处置。
W04 已把旧 3 项 seed 扩展为 53 项候选 census：44 项 `20+`、9 项低分。DeepSeek-R1、Kimi k1.5、
Chain of Agents、Agent-R、Mobile-Agent-E、Demons in the Detail、MMVU、UI-TARS、Hunyuan3D 2.0、
InternLM-XComposer2.5-Reward、Video Depth Anything、MAGI、EmbodiedEval、Condor、VideoLLaMA 3、
FilmAgent、TPO、Autonomy-of-Experts 与 Pairwise RM 已完成非模板化 30 字段 Source Review；当前
44/44 high-score Full Source Review 与9/9低分identity/date/score/rejection disposition均已完成，W04 Gate Passed。EMO2 已按 v1 日期回拨 W03；
Video Depth Anything、MAGI、EmbodiedEval、Condor 与 TPO 的 HTML/PDF 访问异常均通过同 ID primary
source 或官方 artifact 闭合并保留 version boundary；Temporal Preference Optimization 已完成 PDF 审计。
W05 replay 新发现 Qwen2.5-VL 的官方 release 实际发表于 2025-01-26，已回拨 W04，并通过后续同 family
technical report/model card 完成 architecture、training、evaluation 与 evidence-boundary 复核。
Hugging Face 1月28日 discovery 另暴露 Qwen2.5-1M 的 arXiv v1 为1月26日；已一并回拨，完成 progressive
training、DCA/MInference、chunked Prefill、DCPP/TAG 与 batch-1 TTFT 边界的全文审计。
随后 1月27～28日 discovery replay 又回拨 HLE、CoRAG、ICRL、MLLM benchmark redundancy、RealCritic、
Baichuan-Omni-1.5、ARWKV、MoE sparsity scaling 与 CodeMonkeys；9项均完成30字段Source Review。DeepFlow
也因v1为1月24日回拨，补齐serverless request/job/task、FlowServe、RTC/DistFlow、PD/locality scheduling
与fast-scaling的生产系统边界；W05 fixed-source replay 又确认 Transformers 4.48.1 首发于1月20日，
作为低分 release fact 回拨。W06 replay 又发现 MatAnyone 的 v1 为1月24日；该窄域 video-matting
memory case 已回拨并完成低分核验，TracksTo4D 则因 first-public 为2024年未重复计分。因此 W04 最终
重新通过53/53 disposition、44/44高分全文审计和9/9低分拒绝核验。W06延迟发现的 Continuous 3D
Perception / CUT3R 也按1月21日v1回拨，补齐 recurrent persistent scene state、read/write separation、
online pointmap/pose evaluation 与 state compression failure modes。
Books Gate 仍关闭。
W05 已从旧 3 项 seed 扩展为55项候选 census：39项 `20+`、16项低分。除重新核验 vLLM V1、s1 与
OpenAI deep research 外，补齐 PyTorch 2.6、Streaming DiLoCo、Janus-Pro、Mixture-of-Mamba、
SFT-vs-RL、FP4 Training、Over-Tokenized Transformer、interpretability research agenda、TAID、Critique
Fine-Tuning、Atla、external o3-mini safety、Virus、Underthinking、GuardReasoner、SANA 1.5、WildChat-50M、
MedXpertQA 与 PhysBench。PhysBench 的 HTML、appendices、项目页和评测仓库已经恢复，明确区分
multiple-choice benchmark、tool/memory-assisted reasoning 与 embodied control evidence。W05 最终通过
55/55 disposition、39/39非模板化30字段 Full Source Review、16/16低分核验、评分/日期/revision/owner/
Markdown检查。W06 discovery spillback 额外恢复 Constitutional Classifiers、ChunkKV、Reward-Guided
Speculative Decoding、learning-rate scheduling、SafeRAG、adversarial inference-time compute、
Scalable-Softmax、PixelWorld、SAeUron、MM-IQ、Rethinking Mixture-of-Agents、Federated Sketching LoRA、
Activation Approximation Safety、Concept Steerers、RAG Interrogation Attack、HackerRank-ASTRA 与
Weak-to-Strong Diffusion；八项低分 domain candidates 也完成来源与拒绝核验。
Constitutional Classifiers 联读2月3日官方说明与2月13日 demo failure，避免只保留发布时正面结果；
未修改 Books，cursor 进入 W06。W06 旧版“无保留候选”已被推翻，当前恢复 63 项候选 census：38 项
达到 `20+`，25 项进入低分核验。OmniHuman-1、PRIME、DeepRAG、FastKV、vLLM 0.7.2、SmolLM2、
LIMO、recurrent-depth latent reasoning、Sliding Tile Attention、QuEST、BOLT、Satori 与 QLASS 已完成
30 字段 Full Source Review；On-device Sora随后通过arXiv metadata、CC BY v1全文副本与official repository
恢复正文。KVFundaBench/ShotKV、AlphaGeometry2、ScoreFlow、VideoRoPE、SCONE、InferenceGuard、
Transformer World Models、LongDPO、VideoJAM、Inverse Bridge Matching Distillation、Demystifying Long CoT
与 Teacher Hacking 又按事件时 arXiv v1 完成全文审计，其中 KV family 明确隔离 2026 v4 的改题与扩展结果，
World Model family 明确隔离后续摘要的69.66结果。Token Assorted、PyCapsule、ConceptAttention、UltraIF、
Goku 与 Self-Backtracking 随后完成事件时版本全文审计；UltraIF 的普通 HTML 返回错误，因此明确锁定
arXiv v1 PDF，未以当前 v2 或摘要替代。DuoGuard、Symbolic World Models、CMoE、CodeSteer、VectorQ
与 Gemini 2.0 GA 又完成非模板化30字段 Source Review；Gemini 仅保留 release/model-card 版本事实，
不从产品能力反推内部机制。随后对低分账目逐项校准，发现 Preference Leakage、MGA、HMA、particle
inference、Speak Easy、SliderSpace、MakeAnything、TwinMarket 等 22 项被低估了 Project Relevance / Longevity；
W06 因此首轮校正为 60 个 `20+` 和 3 个低分候选。60/60 high-score Full Source Review 完成；除 MGA、HMA、
particle inference、Speak Easy、verification scaling 与 Preference Leakage 外，又闭合 Direct Alignment、
AlignVLM、ZebraLogic、ACECODER、AStar、JUMP、ReasoningWeekly、RandLoRA、Improved Latent Consistency、
COCONut-PanCap、SynCD、AIM、3D point-regularized video generation、output-distribution capability decomposition、
fixed-grid procedural generation 与 multi-agent environment feedback。Transformers 4.48.3、MLX 0.22.1 与
LayerTracer 完成低分版本/identity/rejection核验。W07 discovery replay 随后暴露 The Curse of Depth、
Social-Deduction MARL、LM2、Hierarchical Drafting、Gemstones、CTRL 与 NoLiMa 的 arXiv v1 均落在
2月5～9日；七项按 first-public date 回拨 W06，并完成事件时版本 Method、evaluation、limitations、artifact、
30字段与 owner 审计。W06 首轮为 70/70 disposition、67/67 `20+` Full Source Review、3/3 low-score verification；
评分、日期、revision、Markdown 与 Books-closed boundary 检查通过后进入 W07。
W07 discovery replay 随后把旧版 3 项 seed 扩展为 31 项候选：13 项达到 `20+` 并完成非模板化
30 字段 Full Source Review，18 项完成 identity、v1/官方日期、评分与拒绝边界核验。新增高分证据包括
reward-aware test-time compute、OREAL、Matryoshka Quantization、Jakiro、InSTA、Hephaestus、
WebLI-100B VLM data scaling、prompt-cache timing audit、TransMLA、Distillation Scaling Laws 与 LASP-2；
旧版 W07 Books 完成声明和 changed Books paths 已撤回，Historical Books Gate 保持关闭。W07 的日期账本
同时确认 CODESIM、Competitive Programming、APE、Hypencoder、Éclair 与 CAD-Editor 的 v1
早于 2 月 10 日，不能留在 W07；arXiv:2502.05415 还暴露 revision-identity 风险：2 月 v1 实为
Show-o Turbo，5 月 v2 才改为 UniCMs，不能用当前 metadata 覆盖事件时内容。四个 `20+` family 已完成
全文、Method、evaluation、limitations/artifact与30字段审计，三个低分family完成拒绝核验。W06 最终
重新通过 77/77 disposition、71/71 Full Source Review、6/6 low-score verification；W08 look-ahead 后又把
`Jailbreaking to Jailbreak` 按 2 月 9 日 arXiv v1 回拨，最终通过 78/78 disposition、72/72 Full Source
Review 与 6/6 low-score verification。该 family 的 2 月 17 日 Hugging Face 推荐日期不再冒充 event date。
第三批明确保留 TCME 的概念性 trust boundary、Physics-IQ
的 heterogeneous model contract、The Heap 的 temporal contamination 边界与 TA-TiTok 的
text-conditioned reconstruction 风险；第四批进一步闭合 region-token temporal identity、
output-conditioned interpretability、中文语料版本边界与多模态文档检索的 storage/evaluation contract。
第五批进一步闭合 outcome-conditioned feedback、video data/SFT/DPO curriculum、open-data governance
与 real/synthetic 3D asset lineage；第六批闭合跨模态 correspondence supervision、resolution-capacity
allocation、生成式4D场景与 causal world model 的边界，以及跨层 feature cache 的执行代价；各项都保留
作者实验、未披露 workload 和 artifact access 的外推边界。第七批锁定 OmniThink v1、隔离当前 v5
revision bleed，并闭合 FIFO long-video memory、evidence-tree/derived-pool、human/model agreement 与
inquiry/diagnosis simulator 的状态、评测和 failure-mode 边界。最终批次进一步区分 PokerBench 的
single-spot solver proxy 与 adaptive gameplay、ArtCoT 的 rubric correlation 与 universal aesthetics，
以及 JAX deterministic PRNG 与跨版本 bitwise stability。新 spillback 包括 VideoWorld、Mind Evolution、
MSTS、PaSa、ComplexFuncBench、GameFactory、SEAL、Go-with-the-Flow、Geometry of Tokens、IntellAgent、
Learn-by-interact、Step-KTO、Control LLM 及 9 个低分窄域/校准候选；13 个 `20+` spillback 已完成非模板化
30 字段全文审计，8 个低分项完成可审计拒绝记录。
Books Gate 保持关闭。

W08 look-ahead 又发现 Hugging Face 2 月17～18日推荐页中有 42 个 Source Family 的 arXiv v1
实际落在 W07，另有 1 项回拨 W06。W07 完成逐项重评后，38/38 高分 spillback 形成非模板化 Full Source Review，
4/4 低分 spillback 完成 identity/date/score/rejection 核验；合并原有候选后最终通过 73/73 scoring、
51/51 `20+` Source Review 与 22/22 low-score disposition。后批次补齐 small-model adapter、TSP3D、
V2V-LLM、MRS、CLaMP3、MIKASA、Cuckoo、professional fact-checker evidence requirements 与
atomic data-alignment under budget；所有 Books disposition 仍为 Deferred，forward cursor 进入 W08。

W08 首轮重放已纠正旧版“论文与工程无候选”的结论。当前 ledger 包含 61 个本周 arXiv
identity、Transformers v4.49.0、Accelerate v1.4.0 与 vLLM v0.7.3；AI co-scientist Blog event
与 W09 paper v1 共享同一 Source Family。Soundwave 的普通 arXiv HTML 暂不可用，已通过对应
27-page v1 PDF 与官方 architecture/inference repository 完成全文核验；2025-05-03 权重发布只作
revision lineage，不倒写为 W08 event-time artifact。
Transformers v4.49.0 已锁定官方 tag `a22a437`，并完成完整 Release、compare、selected Cache/processor/quantizer/
parallel-plan/correctness PR 审计；其 315-commit integration surface 只支持 framework compatibility migration，
不支持 Release-wide 性能、全硬件可移植性或各集成模型质量结论。该 family 归 `PLATFORM-MODEL-REGISTRY`，
标记为 `Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate`。
Accelerate v1.4.0 已锁定官方 tag `b431d1f`，并完成 TP/DataLoader、torchao/DeepSpeed FP8、dtype estimator 与
GradientState/DataLoader weak-reference lifecycle 审计。它说明 thin wrapper 仍参与 process-group、sample identity、
precision 和 lifetime correctness，但不拥有 TP collective math 或平台调度；标记为 `Books Pending — No Change Candidate`。
vLLM v0.7.3 已锁定 signed tag `ed6e907`，完成完整 Release/compare 及 concurrent partial Prefill、KV hash owner、
n-gram/MTP speculation、msgpack、metrics 与 V1 pipeline paths 审计。它支持“调度对象扩展为带 KV/phase/proposal 的
token state”这一既有结论，但 constructed single-A100 TTFT 与各硬件 PR 数字不能合并为 Release-wide 性能结论；
标记为 `Books Pending — No Change Candidate`。按用户要求，W08 后暂停，W09 尚未开始。
随后完成 MLGym 与 Qwen2.5-VL 的 30 字段全文审计：前者只支持可执行、异构 artifact 的
Research-Agent evaluation contract，不支持“自治科学发现”；后者支持 native-resolution + absolute-time
representation contract，但缺少组件 ablation、完整 workload 和独立复现，不能从 benchmark 表外推生产效率。
SigLIP 2 的 30 字段审计进一步确认：其贡献是多目标训练配方、local/dense supervision 与 NaFlex
native-aspect-ratio artifact 的组合演进；缺少组件级因果 ablation，且 private WebLI、TPUv5e 训练规模和未披露
serving contract 阻止把作者 benchmark 外推为通用表示或生产效率结论。SuperGPQA 将长尾专业评测推进到
taxonomy/provenance/prompt-budget contract，
LoRA Knowledge Capacity 说明小 adapter 不代表小 behavioral blast radius；Soundwave 则把 speech-text
representation alignment 与 content-dependent sequence shrinking 拆成不同 owner，但 10k/520k 小时比较、
72 ms TTFT 与 2.5% sequence ratio 都只在作者披露的局部实验条件内成立。
Embedding Space Capacity 已严格回到 Transformer-only v1；6 月加入的 Mamba/entropy-coder/ACL evidence 未倒写。
其长期证据是 per-sample optimized input vector 的 uncertainty-reduction ceiling，而不是可部署的 1,568× compressor；
5,000-step encoding、teacher-forced threshold、未声明 precision 和 scattered/non-canonical latent geometry 保持为边界。
S* 进一步把 code test-time compute 拆成 parallel coverage、execution-grounded sequential repair 与 adaptive selection；
其长期价值是 Workflow ownership，而不是“小模型超越大模型”的榜单叙事。单次实验、competition-code scope、
未披露成本/SLO 与论文内部 headline 数字不一致均保留为证据边界。
SuperGPQA 的 v1 256-page source packet 与 artifact 复核确认：其长期价值是 taxonomy-aware EvalSpec、
human/LLM/rule quality pipeline 和 prompt/sampling sensitivity，而不是“61.82% 代表距离 AGI 的刻度”。STEM 集中、
Chinese-source translation、shared-model filtering、contamination 与未披露 compute contract 均保留为证据边界。
LoRA Knowledge Capacity 已回到 14-page v1，而没有把 v3 新增的 Mistral evidence 倒写到 W08。其证据支持
adapter promotion 必须同时检查 target recall、negative shifts、refusal 与 external slices；单模型、rank-1、
train/test overlap 和未披露 hardware 不能推出通用“可装入事实数量”或 LoRA capacity law。
TrustGen 已锁定 2025-02-20 的 v1，而没有把 ICLR 2026 的 39-model 版本或当前 toolkit 倒写到 W08。
其长期证据是 `metadata curator → test-case builder → contextual variator` 的动态评测流水线，以及
dataset、generator、variator、target 与 scorer 必须共同版本化；跨维度平均分不等于部署风险概率，
event-time code/data hashes、per-module ablation、judge calibration、成本和独立复现仍缺失。
MMTEB 已锁定 2025-02-19 v1 与论文指定的 results commit；它证明在所选公开模型/任务上，task-correlation
selection、retrieval pooling 与 embedding reuse 可以显著降低评测成本并大致保留相对排名，但不能证明对未来
model family 继续无损。v1 的 131/132、40/41 任务数冲突、mixed MTEB versions、pool-model blind spot 与
缺失的统一环境 manifest 已保留为 evidence boundary。
HumanUP 已锁定 2025-02-17 v1，并把 4 月后的 RSS revision 与 simulation code 仅作为 lineage。其两阶段机制
把 contact-rich sparse-reward motion discovery 与 full-mesh、posture/terrain randomization、strong control
regularization 下的 deployability refinement 分开；这支持 G1 受限环境中的 sim-to-real feasibility，但 event-time
artifact、真实试验完整分母、deadline/safety controller 与独立复现缺失，不能外推为开放世界自动恢复。
SongGen 已锁定 2025-02-18 v1；3～7 月的 checkpoints、test set 与 training code 只作 lineage。它把 mixed audio、
training-only vocal supervision、parallel dual-track 与 interleaved dual-track 还原为不同 state-layout 分支：统一 decoder
减少 cascade 边界，却没有消除 codec、condition encoder、data provenance 与 waveform decoder；interleaving 增强作者
workload 下的同步质量，也明确增加 sequence/KV 成本。16 kHz、English、30-second contract、非等成本 baseline 与缺失
serving evidence 阻止把结果外推为长音乐、跨语言或生产效率结论。
Small Model Learnability Gap 已锁定 W08 内最后修订的 2025-02-22 v2；11 月 v3、ACL publication 与当前 artifact
只作 lineage。它证明在作者数学、Qwen/Llama、SFT contract 中，teacher strength 和 trace length 不是脱离 student
capacity/domain prior 的总序；Mix Distillation 是 student-conditioned data policy，而不是“弱 teacher 永远更好”。
`<=3B`、1:4 mixture、distribution-shift 归因、judge-assisted scores 与缺少 seed/compute-matched ablation 均保留为边界。

Multimodal Mamba 已锁定 2025-02-18 v1；3 月 v2 与 2 月 19 日公开的代码/权重只作 lineage。它把
Transformer-to-SSM 替换重述为状态迁移问题：先继承可对应的 projection，再用逐层局部 MSE 对齐 recurrent
state 的行为，最后以 end-to-end KL 修复组合误差；纯 SSM 与 hybrid 因此是不同约束下的并存分支，而非线性
替代关系。20.6x headline 只绑定单张 RTX 4090、103K context、next-token latency 的作者测试；长上下文任务
质量、并发、SLO 与精度未披露，不能外推为通用 serving 吞吐结论。

RAD 已锁定 2025-02-18 v1；9 月核心代码、11 月 3DGS environment 与 NeurIPS 版本只作 lineage。它把 open-loop
IL 的 distribution gap 改写为可执行环境中的 policy-induced state problem：3DGS worker 产生闭环 rollout，PPO
探索安全关键偏差，dense directional objectives 改写完整 action distribution，IL 则约束 human alignment。
作者的 3x collision headline 只属于 337 个 held-out、non-reactive 3DGS dense-traffic scenes；actor log replay、
renderer boundary、未披露硬件与无 real-road denominator 阻止把它升级为真实道路安全或因果理解结论。

Decomposed Reward Models 已锁定 2025-02-18 v1；ACL publication 只作 lineage。它把单一 scalar reward 演进为
versioned latent basis：chosen/rejected embedding difference 经 PCA 形成 signed heads，再用少量 adaptation labels 组合
成当下 reward。关键边界是 PCA 只最大化 feature variance，论文与 Bradley-Terry 的联系依赖近似，component 的
benchmark correlation 不等于已命名或 causal 的人类价值；无代码、硬件、真实用户与跨版本稳定性证据也阻止把
“lightweight / interpretable”外推成生产 contract。

MoM 已锁定 2025-02-19 v1；5 月、10 月、11 月修订以及 9 月 varlen kernel 只作 lineage。它把线性序列模型的
单一 recurrent state 演进为 top-k routed local state bank 加 shared state：以固定但更大的 state capacity 和路由
复杂度，换取对不同 token 更新的隔离。作者两种规模与 2K recall contract 支持“优于所测单状态线性基线”，不支持
消除 interference、替代 KV、任意长度质量或 production throughput；single state、hybrid 与 dense KV 仍是条件分支。

FLAG-Trader 已锁定 W08 最后 revision v3（2025-02-19）。它把 prompt-only action generation 推进为外部环境
reward 驱动的 partially tuned LLM actor-critic，但复用的是 PPO/GAE 主线，不是新的 RL 算法。六个资产、单一历史
窗口、median-trajectory selection、无 fees/slippage/market impact、无 seed 与无 artifact，使其只支持机制可运行与
作者 backtest operating point，不支持盈利部署或“135M 普遍优于大模型”。

SoFar 已锁定 2025-02-18 v1 event，并把 2025-09-24 v2 的全文、appendix、artifact 与 NeurIPS 状态隔离为后续
lineage。其持久价值是 `position-only state → canonical pose → language-conditioned semantic direction → calibrated target
pose → controller/environment feedback`：语言可以选择任务相关的功能轴，但不能取消 camera/world/tool frame，也不能
取得 actuator authority。作者 ablation 与受限 sim/real experiments 支持该模块化机制在其 contract 中可行，不支持
开放世界 6-DoF、实时控制或 certified safety。

阶段边界：

- `Weekly Evidence Gate`：本轮唯一执行 Gate；所有可访问 `20+` 候选完成非模板化 Full Source
  Review，低分候选完成 identity/date/score/rejection 核验，ordinary `Review Pending = 0`。
- `Archive Completion Gate`：只有 W01～W52 discovery replay、spillback、revision 与 Materials Request
  Ledger 全部可复算后才能关闭。
- `Books Integration Gate`：本阶段不启动。Stable Node 只用于候选定位；相邻章节可以只读核对，但
  不修改 Books，不产生新的 integration disposition。

Claude Opus 4.5 保持用户已批准的 `Excluded / Unverified`；它不计 Full Source Review、不能支持机制
结论，也不阻止 forward cursor。若未来重新纳入，必须先取得并阅读全文，再重开候选级 Evidence Gate。

## Legacy Candidate and Books Ledger（Provisional Seed）

下表是 2026-07-31 旧轮次保存的 75 个候选与 Books 判断，只作为 discovery seed 和交叉检查入口。
表中的 `Complete`、`Refine`、`No Change` 或 `Weekly Only` 均不代表本轮 Weekly Gate 已通过；逐周
重放后，新候选、纠正日期、revision 和 evidence state 以对应 Weekly 的新记录为准。

| Week | Candidate | Score | Source Review | Current Disposition |
| --- | --- | ---: | --- | --- |
| 2025-W01 | Titans: Learning to Memorize at Test Time | 27 | Complete | Refine — Existing Argument |
| 2025-W02 | vLLM 2024 Retrospective and 2025 Vision | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W03 | MiniMax-01 | 25 | Complete | Refine — Existing Argument |
| 2025-W03 | PRESERVE | 21 | Complete | Weekly Only — Experimental Hardware-specific Case |
| 2025-W04 | DeepSeek-R1 | 29 | Complete | Refine — Existing Argument |
| 2025-W04 | Kimi k1.5 | 27 | Complete | Refine — Existing Argument |
| 2025-W04 | Chain of Agents | 21 | Complete | No Change — Already Covered |
| 2025-W05 | vLLM V1 Alpha | 28 | Complete | Refine — Existing Argument |
| 2025-W05 | s1: Simple test-time scaling | 24 | Complete | Refine — Existing Argument |
| 2025-W05 | OpenAI deep research | 23 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W07 | Online Scheduling for LLM Inference with KV Cache Constraints | 24 | Complete | Refine — Existing Argument |
| 2025-W07 | Building AI for the pluralistic society | 18 | Low-score verified | Weekly Only — Mechanism Not Disclosed |
| 2025-W07 | Native Sparse Attention | 27 | Complete | Refine — Existing Argument |
| 2025-W07 | MUDDFormer | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | AI co-scientist | 22 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | MLGym | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Qwen2.5-VL Technical Report | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SigLIP 2 | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SuperGPQA | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | LoRA Knowledge Capacity | 23 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Soundwave | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Embedding Space Capacity | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | S*: Test Time Scaling for Code Generation | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Magma | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Continuous Diffusion Model for Language Modeling | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Logic-RL | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SWE-Lancer | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | TrustGen | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | MMTEB | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | HumanUP | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SongGen | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Small Model Learnability Gap | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Multimodal Mamba | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | RAD: 3DGS-based Reinforcement Learning for End-to-End Driving | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Decomposed Reward Models / Preference PCA | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | MoM: Mixture-of-Memories | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | FLAG-Trader | 23 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SoFar | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Craw4LLM | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | PC-Agent | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | S2R: Self-verification and Self-correction via RL | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Selective Question Answering under Test-time Scaling | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SafeRoute | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | RelaCtrl | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | YOLOv12 | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | CLIPPER | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Explorer: Web Trajectory Synthesis | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Template-Anchored Safety | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | NExT-Mol | 25 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | video-SALMONN-o1 | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | InfiR | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | LongPO | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Temporal Heads | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | LongWriter-V | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Intuitive Physics from Natural Videos | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Autellix | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Sailor2 | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Thinking Preference Optimization | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | HermesFlow | 24 | Complete | Disputed — Books Frozen |
| 2025-W08 | Atom of Thoughts | 25 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Dynamic Concepts Personalization | 25 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | RealSyn | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Diffusion-Sharpening | 23 | Complete | Disputed — Books Frozen |
| 2025-W08 | Revisiting Test-time Scaling of o1-like Models | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | AlphaMaze / GRPO | 18 | Complete | Disputed — Weekly Only / Books Frozen |
| 2025-W08 | PAFT | 24 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | CoSyn / Scaling Text-Rich Image Understanding | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | LServe | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | From RAG to Memory / HippoRAG 2 | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Train Small, Infer Large / LoRAM | 24 | Complete | Disputed — Books Frozen |
| 2025-W08 | Text2World | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | HeadInfer | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | AdaptiveStep | 24 | Complete | Disputed — Books Frozen |
| 2025-W08 | AIDE | 27 | Complete | Books Pending — No Change Candidate |
| 2025-W08 | Diffusion Models without Classifier-free Guidance / Model-guidance | 26 | Complete | Disputed Scope Claim — Books Frozen |
| 2025-W08 | Transformers v4.49.0 | 22 | Complete | Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate |
| 2025-W08 | Accelerate v1.4.0 | 23 | Complete | Books Pending — No Change Candidate |
| 2025-W08 | vLLM v0.7.3 | 27 | Complete | Books Pending — No Change Candidate |
| 2025-W08 | Low-weight Quantum Error-Correcting Codes with RL | 18 | Low-score verified | Weekly Only — Outside Knowledge-tree Scope |
| 2025-W09 | Claude 3.7 Sonnet and Claude Code | 23 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W10 | EAGLE-3 | 26 | Complete | Refine — Existing Argument |
| 2025-W10 | Mistral OCR | 19 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W11 | Gemma 3 | 21 | Complete | No Change — Already Covered |
| 2025-W12 | Private prediction for large-scale synthetic text generation | 23 | Complete | Refine — Existing Argument |
| 2025-W12 | NVIDIA Dynamo | 27 | Complete | Refine — Existing Argument |
| 2025-W12 | SGLang joins PyTorch ecosystem | 20 | Complete | Weekly Only — Governance Fact |
| 2025-W13 | Gemini 2.5 Pro | 22 | Complete | Refine — Existing Argument |
| 2025-W13 | Tracing the thoughts of a large language model | 25 | Complete | Refine — Existing Argument |
| 2025-W14 | Llama 4 Scout and Maverick | 24 | Complete | No Change — Already Covered |
| 2025-W15 | Kimi-VL | 22 | Complete | Weekly Only — Experimental Model Case |
| 2025-W16 | OpenAI o3 and o4-mini | 24 | Complete | Weekly Only — Version/Product Fact |
| 2025-W16 | MIRAS — It’s All Connected | 26 | Complete | Refine — Existing Argument |
| 2025-W17 | PyTorch 2.7 | 23 | Complete | Weekly Only — Version/Product Fact |
| 2025-W17 | Kubernetes v1.33 | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W18 | Qwen3 | 26 | Complete | Refine — Existing Argument |
| 2025-W20 | AlphaEvolve | 25 | Complete | Refine — Existing Argument |
| 2025-W20 | Sufficient Context: A New Lens on RAG Systems | 25 | Complete | Refine — Existing Argument |
| 2025-W21 | llm-d community launch | 27 | Complete | No Change — Already Covered |
| 2025-W21 | Claude 4 | 22 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W21 | User-level differential privacy for LLM fine-tuning | 23 | Complete | Refine — Existing Argument |
| 2025-W22 | KServe v0.15 | 25 | Complete | No Change — Already Covered |
| 2025-W22 | DeepSeek-R1-0528 | 21 | Complete | Weekly Only — Version/Product Fact |
| 2025-W23 | Gateway API Inference Extension | 28 | Complete | No Change — Already Covered |
| 2025-W24 | Magistral | 21 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W25 | MiniMax-M1 | 26 | Complete | Refine — Existing Argument |
| 2025-W25 | Gemini 2.5 Pro/Flash GA | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W27 | GLM-4.1V-9B-Thinking | 21 | Complete | Weekly Only — Experimental Model Case |
| 2025-W28 | Kimi K2 release | 27 | Complete | Weekly Only — Version/Product Fact |
| 2025-W29 | SGLang Multiple Token Prediction integration | 25 | Complete | Refine — Existing Argument |
| 2025-W30 | Qwen3-Coder-480B-A35B-Instruct | 24 | Complete | Weekly Only — Version/Product Fact / Mechanism Partially Disclosed |
| 2025-W30 | SpecForge | 24 | Complete | Refine — Existing Argument |
| 2025-W31 | GLM-4.5 release | 25 | Complete | Weekly Only — Version/Product Fact |
| 2025-W31 | Kimi K2 technical report | 27 | Complete | No Change — Already Covered |
| 2025-W32 | gpt-oss-120b / gpt-oss-20b | 27 | Complete | Refine — Existing Argument |
| 2025-W32 | GPT-5 unified system | 24 | Complete | Refine — Existing Argument |
| 2025-W32 | GLM-4.5 technical report | 25 | Complete | No Change — Already Covered |
| 2025-W34 | DeepSeek-V3.1 | 25 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W35 | Kubernetes v1.34 DRA core GA | 26 | Complete | Refine — Existing Argument |
| 2025-W36 | Kubernetes DRA GA design details | 23 | Complete | Refine — Existing Argument |
| 2025-W37 | Qwen3-Next | 27 | Complete | Refine — Existing Argument |
| 2025-W38 | DRA resource health in Pod status | 22 | Complete | Refine — Existing Argument |
| 2025-W38 | DRA consumable capacity | 23 | Complete | Refine — Existing Argument |
| 2025-W39 | DeepSeek-V3.1-Terminus | 19 | Complete | Weekly Only — Version/Product Fact |
| 2025-W40 | DeepSeek-V3.2-Exp / DeepSeek Sparse Attention | 28 | Complete | Refine — Existing Argument |
| 2025-W42 | PyTorch 2.9 | 25 | Complete | Refine — Existing Argument |
| 2025-W44 | gpt-oss-safeguard | 24 | Complete | Refine — Existing Argument |
| 2025-W44 | SGLang-JAX | 25 | Complete | Refine — Existing Argument |
| 2025-W45 | Kimi K2 Thinking | 23 | Complete | No Change — Already Covered |
| 2025-W45 | SGLang Diffusion | 22 | Complete | No Change — Already Covered |
| 2025-W46 | JAX-Privacy 1.0 | 25 | Complete | Refine — Existing Argument |
| 2025-W47 | Gemini 3 | 22 | Complete | Weekly Only — Version/Product Fact |
| 2025-W47 | Real-time speech-to-speech translation | 23 | Complete | Refine — Existing Argument |
| 2025-W48 | Claude Opus 4.5 | 21 | Excluded / Unverified | User-approved exclusion / Unverified |
| 2025-W49 | DeepSeek-V3.2 | 29 | Complete | Refine — Existing Argument |
| 2025-W49 | Mistral 3 | 23 | Complete | Refine — Existing Argument |
| 2025-W49 | Google Research synthesis of Titans + MIRAS | 22 | Complete | No Change — Already Covered |
| 2025-W50 | Differentially private chatbot-use analytics | 25 | Complete | Refine — Existing Argument |
| 2025-W50 | GPT-5.2 | 22 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W51 | Gemini 3 Flash | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W52 | SpecBundle and SpecForge v0.2 | 24 | Complete | Refine — Existing Argument |

## Weekly Links

- [2025-W01](./2025-W01/README.md)
- [2025-W02](./2025-W02/README.md)
- [2025-W03](./2025-W03/README.md)
- [2025-W04](./2025-W04/README.md)
- [2025-W05](./2025-W05/README.md)
- [2025-W06](./2025-W06/README.md)
- [2025-W07](./2025-W07/README.md)
- [2025-W08](./2025-W08/README.md)
- [2025-W09](./2025-W09/README.md)
- [2025-W10](./2025-W10/README.md)
- [2025-W11](./2025-W11/README.md)
- [2025-W12](./2025-W12/README.md)
- [2025-W13](./2025-W13/README.md)
- [2025-W14](./2025-W14/README.md)
- [2025-W15](./2025-W15/README.md)
- [2025-W16](./2025-W16/README.md)
- [2025-W17](./2025-W17/README.md)
- [2025-W18](./2025-W18/README.md)
- [2025-W19](./2025-W19/README.md)
- [2025-W20](./2025-W20/README.md)
- [2025-W21](./2025-W21/README.md)
- [2025-W22](./2025-W22/README.md)
- [2025-W23](./2025-W23/README.md)
- [2025-W24](./2025-W24/README.md)
- [2025-W25](./2025-W25/README.md)
- [2025-W26](./2025-W26/README.md)
- [2025-W27](./2025-W27/README.md)
- [2025-W28](./2025-W28/README.md)
- [2025-W29](./2025-W29/README.md)
- [2025-W30](./2025-W30/README.md)
- [2025-W31](./2025-W31/README.md)
- [2025-W32](./2025-W32/README.md)
- [2025-W33](./2025-W33/README.md)
- [2025-W34](./2025-W34/README.md)
- [2025-W35](./2025-W35/README.md)
- [2025-W36](./2025-W36/README.md)
- [2025-W37](./2025-W37/README.md)
- [2025-W38](./2025-W38/README.md)
- [2025-W39](./2025-W39/README.md)
- [2025-W40](./2025-W40/README.md)
- [2025-W41](./2025-W41/README.md)
- [2025-W42](./2025-W42/README.md)
- [2025-W43](./2025-W43/README.md)
- [2025-W44](./2025-W44/README.md)
- [2025-W45](./2025-W45/README.md)
- [2025-W46](./2025-W46/README.md)
- [2025-W47](./2025-W47/README.md)
- [2025-W48](./2025-W48/README.md)
- [2025-W49](./2025-W49/README.md)
- [2025-W50](./2025-W50/README.md)
- [2025-W51](./2025-W51/README.md)
- [2025-W52](./2025-W52/README.md)

## Legacy Books Integration Summary（Not Revalidated in This Phase）

Status: `Frozen legacy snapshot / 2025 Weekly rebuild does not modify Books`。

本轮以 74 个已核验候选的 primary evidence 重新审查相邻章节；`Refine` 只表示候选补强或修正
了长期机制，不表示每个同族事件都重复生成一段正文。

| Evolution Route | Primary Weekly | Books Owner | Integrated Understanding |
| --- | --- | --- | --- |
| hybrid / sparse / test-time memory | W01、W03、W07、W16、W40、W49 | Ch22；Ch73 boundary | dense、linear/recurrent、hybrid、native sparse、DSA 与 neural memory 是不同约束下的分支；新增 selector、kernel、online state、隔离与恢复成本 |
| reasoning RL | W04 | Ch29 | pure RL 展示 emergence；cold start、筛选/SFT、第二阶段 RL 与 distillation 分别解决可读性、行为约束和部署成本，不互相覆盖 |
| speculative artifact lifecycle | W10、W29、W30、W52 | Ch44 | drafter 从独立小模型演进到 EAGLE-3、MTP、训练系统和 target-coupled bundle；收益受 acceptance、verification 与 workload 约束 |
| accelerator resource contract | W35、W36、W38 | Ch59 | DRA core GA、health alpha、consumable-capacity alpha 分层；driver、scheduler、admission 与 recovery 各有 owner |
| differential privacy stack | W12、W21、W46、W50 | Ch68 | privacy unit 从 record/query、user contribution 延伸到 distributed training runtime 与 production telemetry；DP 不是省略 threat model/accounting 的标签 |
| RAG control loop | W20 | Ch72 | relevance、context sufficiency、faithfulness 和 abstention 分开治理 |
| evaluator-driven search | W20 | Ch77 | evaluator、candidate lineage、evaluation cascade、diversity、held-out verification 与 human deployment authority 构成 Workflow，不等于模型自我改进 |
| interpretability evidence | W13 | Ch5 | probing→sparse replacement→attribution graph→原模型 intervention；更可读的图以 reconstruction、pruning 与 attention blind spot 为代价 |
| reasoning budget and rollout state | W04、W05、W18、W32 | Ch20、Ch29、Ch52 | stopping/effort、partial trajectory、route identity 与 serving capacity 是不同 owner 下的同一 compute contract |
| distributed runtime evolution | W05、W12、W42、W44 | Ch32、Ch45、Ch46、Ch48 | collective call、one-sided memory、backend portability、single-engine state 与 distributed paths 分层演进，不互相覆盖 |
| training resilience and distillation | W13、W49 | Ch24、Ch25 | elastic recovery 要保持 trajectory semantics；cascade distillation 用更多 lineage 换取更平滑的 teacher/student capacity gap |
| streaming pipeline fusion | W47 | Ch38 | cascade 的可替换/可诊断性与 end-to-end streaming 的 latency/voice continuity 共存；fusion 收紧 failure domain |

未写入的主要类别：

- Claude、Gemini、Gemma、Mistral、GPT、Qwen、Kimi、GLM 等产品/模型版本若没有公开的新机制，
  仅保留版本事实和 evidence boundary；
- llm-d、KServe 与 Gateway API 的长期分层原则已由 Ch48、Ch49、Ch58 覆盖；vLLM V1、Dynamo、
  PyTorch 2.9 与 SGLang-JAX 只把新的演进边界 refine 到 Ch46、Ch48、Ch32、Ch45；
- PRESERVE、Chain of Agents、AI co-scientist、Mistral OCR、pluralistic alignment 等候选仍受
  硬件、任务、评测或实现披露限制，保留为 Weekly evidence；
- 所有厂商 benchmark 与单篇论文实验均未升级为无条件生产结论。

Claude Opus 4.5 是唯一没有全文核验的候选，已按用户明确批准排除。除该 exclusion 外，
2025 的 74 个候选已完成 primary-source review、相邻章节复核和最终 disposition；没有把厂商
benchmark、后发报告或产品能力写成无条件事实。
