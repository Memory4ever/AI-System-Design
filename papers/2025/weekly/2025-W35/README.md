# AI Research Weekly — 2025-W35

> Coverage Window: 2025-08-25～2025-08-31 (ISO Monday～Sunday)
> Research Mode: Historical Discovery Replay + Primary-Source Review
> Status: Discovery Gate Complete；Evidence Gate Complete；Historical Books Gate Closed
> Accessed / Rebuilt: 2026-08-24

## Executive Summary

本轮不是在旧版“1 项候选”的下界上补标题，而是按接近 Live Daily 的覆盖度重放完整窗口。继首批 7 个 owner-date spillback 后，W36 denominator stabilization 又确认 Universal Deep Research、Face-MoGLE、MobiAgent 与 C-DiffDet+ 属于 W35；对 8 月 29 日 recommendation feed 和 8 月 29～31 日 submission history 的回查还恢复 USO、Mixture of Contexts、TCIA、Rank-One Safety Injection、In-Tool Learning 与 OnGoal。最终建立 53 个 canonical Source Family：28 个 `25～30`、12 个 `20～24`、13 个 `<20`；40 个 retained family 均完成非模板化 Full Source Review，13 个低分 family 完成来源、日期、评分与拒绝 closure，ordinary `Review Pending = 0`。

本周长期价值集中在四条系统路线：multimodal input 把 visual-token identity、动态压缩和异构部署放入同一 contract；reasoning 从“多生成 token”演进到可控 budget、tool-integrated support expansion、stepwise verifier 和 executable feedback；Agent evaluation 转向真实 server、repository、browser、security sandbox 与 user-choice boundary；inference/platform 则进入 heterogeneous/disaggregated autoscaling 和结构化 device allocation state machine。

所有性能数字仍是作者或项目方在其模型、数据、硬件和 evaluator 条件下的结果；缺少 precision、batch、concurrency 或 SLO 的字段均视为 `Not Disclosed`，不外推为通用事实。

## Coverage Window and Limitations

- **ISO window:** 2025-08-25 00:00～2025-08-31 23:59（Asia/Shanghai）；论文按 arXiv v1 / first-public 归属，后续 revision 不移动 owner week。
- **Discovery order:** 模型公司与一线机构 → arXiv / 学术来源 → AI Infra 官方 release、RFC、KEP、repository 与 code path。
- **Academic replay:** 逐日复核 8 月 25～31 日 arXiv submission history；Hugging Face 8 月 29 日 Daily Papers feed 可直接读取，8 月 30～31 日 feed 页面不可用，改由 W36 spillback、arXiv history、DOI metadata 与 artifact 链接补偿，不能声称 HF feed 本身完整。两轮 spillback 与这次回查共恢复 17 个 W35 owner。Hugging Face 推荐日期只用于发现，USO 等仍按更早的 arXiv v1 日期归 W35；Google Scholar/OpenAlex/DBLP/Semantic Scholar 仅用于发现和去重，不替代正文。
- **Full-read scope:** retained paper 阅读 Abstract、Introduction、Related Work、Method/公式/架构、Implementation、Evaluation、baseline、ablation、Appendix 中影响结论的部分、limitations 与公开 artifact；arXiv HTML 不可用时使用 PDF/TeX/official model card 互证。
- **Fixed infra scan:** PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、llama.cpp、ONNX Runtime、OpenXLA。窗口内唯一达到长期机制门槛的 owner event 是 Kubernetes v1.34 的 DRA core GA；同版 kuberc/restart-policy feature post 属同一 release family，不重复计分。
- **Known boundary:** Scholar/OpenAlex 排名与覆盖率不是可证明的全量召回；本轮以固定来源 replay、相邻周 spillback 和 primary identifier 去重闭合。未发现身份未知的 Discovery Gap。
- **Books boundary:** 本轮只闭合 Weekly evidence；Historical Books Gate 保持关闭，没有修改 Books。

## 1. 模型与研究机构

### Source Coverage

按 OpenAI、Anthropic、Google/DeepMind、Meta、Microsoft、NVIDIA、Apple、Amazon、xAI、Mistral、Cohere、DeepSeek、Alibaba/Qwen、ByteDance/Seed、Tencent/Hunyuan、Baidu、Huawei、Moonshot、Zhipu、01.AI、MiniMax、Shanghai AI Lab、Nous Research 与 Hugging Face 官方页面顺序复核。

- Retained：InternVL3.5、VibeVoice、rStar2-Agent。
- Archive closure：Hermes 4 Technical Report。它公开了模型与训练报告，但本轮未形成足以改变长期系统结论的新 mechanism owner，保留为模型事实/实验边界。
- 机构公告若只有 capability claim、没有 report/model card/artifact，统一按 `Version Fact / Mechanism Not Disclosed`，未进入评分表。

## 2. 论文与学术来源

### Source Coverage

按 arXiv v1 日期逐日重放 8 月 25～31 日首发列表；逐项核对可访问的 Hugging Face 8 月 29 日推荐 feed，8 月 30～31 日用 W36 spillback 与 arXiv submission history 补偿。工作日 cadence 和推荐日期都不能替代 submission history。

- Multimodal / generation：MMTok、Discrete Diffusion VLA、Diffusion LM early-answer、CogVLA、EO-1、ELV-Halluc、Face-MoGLE、Mixture of Contexts；USO 与 C-DiffDet+ 进入低分 closure。
- Training / reasoning：TiKMiX、Tool-Integrated Reasoning、UltraMemV2、ThinkDial、Optimal MoE Sparsity、StepWiser、Pref-GRPO、Metis、LLaVA-Critic-R1、SATQuest、In-Tool Learning；TCIA 进入低分 closure。
- Evaluation / security / agent：UQ、CTF-Dojo、A.S.E、CODA、CoT Dynamics、Mind the Third Eye、DeepScholar-Bench、MCP-Bench、AWorld、UItron、Open Data Synthesis for Deep Research、Camlang、SQL-of-Thought、Universal Deep Research、MobiAgent、Rank-One Safety Injection；OnGoal 进入低分 closure。
- 8 月 29 日推荐 feed 中 Multi-View 3D Point Tracking、FakeParts、ROSE、Dress&Dance、Collaborative Multi-Modal Coding 与 Social-MAE 已核验 identity/v1，因属于 3D tracking、deepfake、video editing、portrait animation 或窄域 representation，未形成本项目独立 system owner，记录为 discovery-only rejection；Persuasion Dynamics 的 v1=2025-08-24，路由 W34。

## 3. AI Infra 与工程项目

### Source Coverage

- Retained：Kubernetes v1.34 release / DRA core GA；论文侧的 Taming the Chaos 作为 disaggregated serving control-plane research evidence。
- Kubernetes 1.34 中 DRA stable core 与同版 alpha/beta extension 明确分层；9 月 1 日 DRA 深度说明、9 月 17 日 health、9 月 18 日 consumable capacity 只作为后续 family node，不回拨成新的 W35 score。
- PyTorch 2.8 首发于 W32；窗口内其他固定项目没有找到同时满足首次公开日、primary mechanism 和长期相关性的独立 owner event。

## Candidate Scoring

| Candidate | Source Family ID | Evidence | Owner | Novelty | Impact | Practical | Reliability | Relevance | Longevity | Total | Final Weekly Disposition |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| InternVL3.5 | `ARXIV-2508.18265` | L2 paper+code/model | `MULTIMODAL-REPRESENTATION` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Refine — Existing Argument |
| Hermes 4 Technical Report | `ARXIV-2508.18255` | L2 report+weights | `TRAIN-SFT` | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Weekly Only — Model/Version Fact |
| Visual-CoG | `ARXIV-2508.18032` | L2 paper | `MULTIMODAL-GENERATIVE-PARADIGMS` | 4 | 3 | 3 | 4 | 2 | 3 | 19/30 | Emerging / Experimental |
| MMTok | `ARXIV-2508.18264` | L2 paper+code | `MULTIMODAL-REPRESENTATION` | 4 | 4 | 5 | 4 | 4 | 3 | 24/30 | Refine — Existing Argument |
| UQ | `ARXIV-2508.17580` | L2 paper+platform | `PLATFORM-EVALUATION-SYSTEM` | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Integrate — New Mechanism Candidate |
| Neither Valid nor Reliable? | `ARXIV-2508.18076` | L2 position paper | `PLATFORM-EVALUATION-SYSTEM` | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — Evidence Caution |
| CTF-Dojo | `ARXIV-2508.18370` | L2 paper+artifact | `PLATFORM-SECURITY` | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Integrate — New Mechanism Candidate |
| A.S.E | `ARXIV-2508.18106` | L2 paper+benchmark | `PLATFORM-SECURITY` | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Integrate — New Mechanism Candidate |
| TiKMiX | `ARXIV-2508.17677` | L2 paper | `TRAIN-DATA` | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| VibeVoice | `ARXIV-2508.19205` | L2 report+model | `MULTIMODAL-GENERATIVE-PARADIGMS` | 5 | 4 | 4 | 5 | 3 | 4 | 25/30 | Integrate — New Mechanism Candidate |
| Understanding Tool-Integrated Reasoning | `ARXIV-2508.19201` | L2 paper+appendix | `AGENT-TOOL-CALLING` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| UltraMemV2 | `ARXIV-2508.18756` | L2 paper | `MODEL-LONG-CONTEXT` | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Integrate — New Mechanism Candidate |
| ThinkDial | `ARXIV-2508.18773` | L2 paper+recipe | `TRAIN-GRPO` | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Refine — Existing Argument |
| Optimal MoE Sparsity for Reasoning | `ARXIV-2508.18672` | L2 paper | `MODEL-MOE` | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| StepWiser | `ARXIV-2508.19229` | L2 paper+model | `PLATFORM-EVALUATION-SYSTEM` | 4 | 5 | 4 | 5 | 4 | 3 | 25/30 | Integrate — New Mechanism Candidate |
| Vision-SR1 | `ARXIV-2508.19652` | L2 paper | `TRAIN-GRPO` | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Emerging / Experimental |
| CODA | `ARXIV-2508.20096` | L2 paper | `AGENT-WORKFLOW` | 4 | 5 | 4 | 4 | 4 | 4 | 25/30 | Integrate — New Mechanism Candidate |
| Analysing CoT Dynamics | `ARXIV-2508.19827` | L2 paper | `AGENT-REFLECTION` | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine — Evidence Boundary |
| Discrete Diffusion VLA | `ARXIV-2508.20072` | L2 paper+appendix | `MULTIMODAL-EMBODIED-VLA` | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Integrate — New Mechanism Candidate |
| Diffusion LMs Know the Answer Before Decoding | `ARXIV-2508.19982` | L2 paper | `MULTIMODAL-GENERATIVE-PARADIGMS` | 5 | 4 | 3 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| Mind the Third Eye | `ARXIV-2508.19493` | L2 paper+benchmark | `PLATFORM-SECURITY` | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Integrate — New Mechanism Candidate |
| DeepScholar-Bench | `ARXIV-2508.20033` | L2 paper+live benchmark | `PLATFORM-EVALUATION-SYSTEM` | 4 | 5 | 5 | 5 | 4 | 2 | 25/30 | Integrate — New Mechanism Candidate |
| Taming the Chaos | `ARXIV-2508.19559` | L2 paper | `INFER-SCHEDULING` | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| Kubernetes v1.34 / DRA core GA | `K8S-1.34-DRA` | L1 official release+KEP+API | `PLATFORM-GPU-SCHEDULER` | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Refine — Existing Argument |
| rStar2-Agent | `ARXIV-2508.20722` | L2 report+artifact | `AGENT-WORKFLOW` | 5 | 5 | 4 | 5 | 4 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| Pref-GRPO | `ARXIV-2508.20751` | L2 paper | `TRAIN-GRPO` | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| MCP-Bench | `ARXIV-2508.20453` | L2 paper+benchmark | `AGENT-MCP` | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Integrate — New Mechanism Candidate |
| AWorld | `ARXIV-2508.20404` | L2 paper+framework | `AGENT-PLATFORM` | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| OneReward | `ARXIV-2508.21066` | L2 paper | `MULTIMODAL-GENERATIVE-PARADIGMS` | 3 | 3 | 4 | 4 | 2 | 3 | 19/30 | Emerging / Experimental |
| CogVLA | `ARXIV-2508.21046` | L2 paper+artifact | `MULTIMODAL-EMBODIED-VLA` | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Integrate — New Mechanism Candidate |
| R-4B | `ARXIV-2508.21113` | L2 paper+model | `MULTIMODAL-REPRESENTATION` | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — Narrow Model Recipe |
| EO-1 | `ARXIV-2508.21112` | L2 paper+artifact | `MULTIMODAL-EMBODIED-VLA` | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Integrate — New Mechanism Candidate |
| Model–Task Alignment and RL Conclusions | `ARXIV-2508.21188` | L2 paper | `TRAIN-RLHF` | 3 | 3 | 3 | 4 | 3 | 3 | 19/30 | Weekly Only — Experimental Caveat |
| UItron | `ARXIV-2508.21767` | L2 paper+model | `AGENT-WORKFLOW` | 4 | 5 | 4 | 4 | 4 | 3 | 24/30 | Refine — Existing Argument |
| AHELM | `ARXIV-2508.21376` | L2 paper+benchmark | `PLATFORM-EVALUATION-SYSTEM` | 3 | 4 | 3 | 4 | 3 | 2 | 19/30 | Weekly Only — Domain Benchmark |
| Morae | `ARXIV-2508.21456` | L2 paper+prototype | `AGENT-WORKFLOW` | 3 | 4 | 4 | 4 | 2 | 2 | 19/30 | Weekly Only — Interaction Study |
| ELV-Halluc | `ARXIV-2508.21496` | L2 paper+benchmark | `PLATFORM-EVALUATION-SYSTEM` | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — Existing Argument |
| Open Data Synthesis for Deep Research | `ARXIV-2509.00375` | L2 paper+data pipeline | `TRAIN-DATA` | 4 | 5 | 5 | 4 | 4 | 4 | 26/30 | Integrate — New Mechanism Candidate |
| Metis | `ARXIV-2509.00404` | L2 paper | `TRAIN-PRETRAINING` | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| Camlang | `ARXIV-2509.00425` | L2 paper+benchmark | `PLATFORM-EVALUATION-SYSTEM` | 4 | 3 | 3 | 5 | 4 | 3 | 22/30 | Refine — Evidence Boundary |
| SQL-of-Thought | `ARXIV-2509.00581` | L2 paper | `AGENT-WORKFLOW` | 4 | 4 | 5 | 4 | 3 | 3 | 23/30 | Refine — Existing Argument |
| LLaVA-Critic-R1 | `ARXIV-2509.00676` | L2 paper+model | `PLATFORM-EVALUATION-SYSTEM` | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Integrate — New Mechanism Candidate |
| SATQuest | `ARXIV-2509.00930` | L2 paper+verifier | `PLATFORM-EVALUATION-SYSTEM` | 5 | 5 | 5 | 5 | 4 | 3 | 27/30 | Integrate — New Mechanism Candidate |
| USO | `ARXIV-2508.18966` | L2 paper+code/model | `MULTIMODAL-GENERATIVE-PARADIGMS` | 4 | 3 | 3 | 4 | 2 | 3 | 19/30 | Emerging / Experimental |
| TCIA | `ARXIV-2508.20374` | L2 paper identity+abstract | `TRAIN-DATA` | 3 | 3 | 4 | 4 | 3 | 2 | 19/30 | Weekly Only — Narrow Data Recipe |
| Provable Benefits of In-Tool Learning | `ARXIV-2508.20755` | L2 paper | `AGENT-TOOL-CALLING` | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Integrate — New Mechanism Candidate |
| Rank-One Safety Injection | `ARXIV-2508.20766` | L2 paper | `PLATFORM-SECURITY` | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Integrate — New Mechanism Candidate |
| Mixture of Contexts | `ARXIV-2508.21058` | L2 paper+project | `MULTIMODAL-GENERATIVE-PARADIGMS` | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| OnGoal | `ARXIV-2508.21061` | L2 paper+prototype | `AGENT-CONTEXT` | 3 | 3 | 4 | 4 | 2 | 3 | 19/30 | Weekly Only — Interaction Study |
| Universal Deep Research | `ARXIV-2509.00244` | L2 paper+code/prototype | `AGENT-WORKFLOW` | 5 | 5 | 5 | 3 | 5 | 4 | 27/30 | Integrate — New Mechanism Candidate |
| Face-MoGLE | `ARXIV-2509.00428` | L2 paper | `MULTIMODAL-GENERATIVE-PARADIGMS` | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Refine — Existing Argument |
| MobiAgent | `ARXIV-2509.00531` | L2 paper+system | `AGENT-PLATFORM` | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Integrate — New Mechanism Candidate |
| C-DiffDet+ | `ARXIV-2509.00578` | L2 paper | `MULTIMODAL-GENERATIVE-PARADIGMS` | 3 | 3 | 4 | 4 | 2 | 3 | 19/30 | Weekly Only — Domain Detection Case |

### Score Reconciliation

- Scored rows: **53**；unique Source Family: **53**。
- `25～30`: **28**；`20～24`: **12**；`<20`: **13**；retained `20+`: **40**。
- 每行 Total 已按六维整数机械复算；分数决定阅读深度与 Weekly disposition，不代表作者实验已被独立复现，也不自动打开 Historical Books Gate。

## Deep Analysis

### 1. 从“更多视觉 token”到 workload-aware representation state

固定 patch/token 网格让模型、batch 与 kernel shape 简单，训练分布稳定；但高分辨率、多图、视频与 embodied observation 使 visual token 数直接挤占 context、KV 与 decode latency。MMTok 用覆盖准则选择同时覆盖视觉与文本需求的 token；InternVL3.5-Flash 用 patch-level router 在 256/64 token 表示间选择，并以 ViCO 保持不同压缩率输出一致；DvD 再把 ViT 与 LLM 放到不同 GPU。代价是 router decision、compression identity、vision encoder placement 与 cache key 都成为状态，错误压缩可能不可逆地删除证据。1.87×、4.05× 等数字绑定各自作者实验，不能跨论文直接比较。

### 2. 从静态推理到 support-expanding action 与可执行证据

纯文本 CoT 在模型已有表示内搜索，便于训练与复现，却无法获得新事实、运行程序或验证环境。Tool-Integrated Reasoning 把 tool call 视为扩展可达支持集，并用 ASPO 鼓励在有价值时更早调用；StepWiser 把过程监督变为可生成 critique 的 stepwise judge；CTF-Dojo 与 A.S.E 则把 reward/evaluation 接到真实容器和 repository verifier。answer token 不再是唯一 owner，tool schema、execution state、artifact、verifier、timeout 与 rollback 共同决定结论能否提交。新风险包括 tool overuse、错误环境、reward hacking、judge bias、不可复现外部状态和安全越界。

### 3. 从单 engine 调优到 fleet/resource control loop

单副本或同构 autoscaling 只看 request rate/queue，并假设每个 replica 能力近似；整数 extended resource 足以表达整卡独占。PD disaggregation、异构 accelerator 与不同 request length 破坏了这些假设。Taming the Chaos 协调 prefill/decode replica 与 routing；Kubernetes DRA 把 DeviceClass、ResourceClaim、ResourceSlice、scheduler allocation 和 kubelet prepare 拆成显式 owner。它们提升 capacity/allocation 表达力，却新增 stale telemetry、control oscillation、allocation/prepare split-brain、driver skew 与 recovery state；DRA GA 也不等于 sharing、health、gang scheduling 已全部 GA。

## Full Source Review

### InternVL3.5

- **Candidate / Week / Score；Source Family ID；Source Type:** InternVL3.5 / W35 / 27；`ARXIV-2508.18265`；technical report、code、weights/model card。
- **Event Date / First-public Date / Revision History；Direct / Related Primary Sources:** v1 2025-08-25，v2 2025-08-27；arXiv、OpenGVLab/InternVL repository、released checkpoints。revision 不移动 W35 owner。
- **Access and Verification Status；Full-read Coverage:** Verified；阅读全文架构、pretrain、SFT/Cascade RL、ViCO/ViR、DvD infrastructure、15 类实验、ablation 与 artifact。
- **Original Problem；Why the Previous Design Was Reasonable；Changed Constraint:** 固定视觉分辨率与同卡 ViT-LLM 部署易训练和运维；高分辨率/多图使 visual-token 与阶段负载失衡，推理成本成为约束。
- **Mechanism；State Ownership；Control / Data Flow:** ViR 逐 patch 在 256/64 token 压缩支路间路由，ViCO 约束不同压缩率输出一致；DvD 让 vision 与 language GPU 分别拥有 stage state，视觉 token 通过 pipeline 交接；Cascade RL 以 MPO offline warm-up 接 GSPO online rollout。
- **Implementation Details；Evaluation Contract:** ViT–MLP–LLM，dense 1B～38B 与 MoE 20B-A4B/30B-A3B/241B-A28B；116M samples、约 250B tokens、text:multimodal≈1:2.5、32K context；benchmark/ablation 为作者实验。
- **Baselines / Ablations / Sensitivity / Overhead；Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 对 InternVL3 与 compression/router/deployment ablation；报告最高 4.05× speedup 和 +16% reasoning，但完整 GPU topology、precision、batch、concurrency、SLO 未统一披露，不能外推。
- **What the Evidence Proves / Does Not Prove；Limitations / Threats:** 证明在该 family 中 adaptive visual-token state 与异构 stage placement 可联合设计；不证明 router 对任意 VLM 无损，也不证明公开 benchmark 等同真实 agent reliability。
- **Trade-offs / New Failure Modes；Where Previous Design Still Applies；Evolution:** 更少 token 与更好 GPU balance 换来 router error、compression-policy drift、跨 GPU transfer 和 cache identity；小图、短 context、单 GPU 下固定压缩仍合理。`Layering / Direct Evolution`。
- **ROADMAP Node；Target and Adjacent Chapters Read；Existing Coverage；Integration Decision；Changed Files / Open Questions:** owner `MULTIMODAL-REPRESENTATION`，handoff `TRAIN-GRPO`/`INFER-PREFILL`；现有书已有表示 identity 与异构 serving 框架，决定 `Refine — Existing Argument`；本轮不改 Books。待验证 router trace、cache invalidation 与真实并发 SLO。

### MMTok

- **Candidate / Week / Score；Source Family ID；Source Type:** MMTok / W35 / 24；`ARXIV-2508.18264`；paper、code、project page。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-25，v2 2026-03-03（同 family）；Verified；全文覆盖 maximum-coverage formulation、algorithm、LLaVA/Qwen experiments、adaptive temperature、pooling、reasoning/efficiency appendices 与 reproducibility statement。
- **Original Problem / Previous Design / Changed Constraint:** 单模态 attention/importance pruning 简单且便宜，但视觉相关性取决于 query text，纯视觉分数会丢失 task-specific evidence。
- **Mechanism / State Ownership / Flow:** 把 selected vision tokens 视为集合覆盖问题，同时覆盖原 vision set 与 text tokens；selector 拥有保留集合，VLM 只接收压缩后的 token stream。
- **Implementation / Evaluation Contract:** 在多种 VLM、POPE 等任务上比较 vision-only/text-only/combined coverage 与不同 token budgets；作者报告 LLaVA-NeXT-13B 上 1.87× 且保留 98.7%，以及 4 visual tokens case，均只对对应设置有效。
- **Baselines / Sensitivity / Overhead；Hardware contract:** 覆盖 pruning baseline、temperature、pooling、token budget 与 Qwen2.5-VL appendix；GPU、precision、batch、concurrency、SLO 未完整统一披露。
- **Proves / Does Not Prove / Limitations:** 证明 multimodal coverage 比单模态 saliency 在测试集更稳；不证明极低 token budget 对 OCR、small object、long-video 或 adversarial query 安全；subset selection 本身有额外计算。
- **Trade-offs / Failure / Previous Applies / Evolution:** 减少 downstream attention/KV，代价是 selector latency、query-dependent cache key 与误删不可恢复；固定保留在小输入或可复用 image embedding 场景仍合理。`Alternative Branch` 于 learned router。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** `MULTIMODAL-REPRESENTATION` 主 owner，handoff `INFER-PREFILL`/`INFER-KV-CACHE`；决定 `Refine — Existing Argument`，无 Books 修改。待比较 coverage selector 与 serving batch/cache 的端到端开销。

### UQ: Assessing Language Models on Unsolved Questions

- **Candidate / Week / Score；Family / Type:** UQ / W35 / 25；`ARXIV-2508.17580`；paper、500-question dataset、validator suite、live platform。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-25（当前 v1）；Verified；阅读全文 collection/filtering、validator-assisted screening、community verification、model evaluation、human verification 与 platform workflow。
- **Original / Previous / Changed:** 静态 exam benchmark 可复现但易饱和/污染，真实用户问题又常偏简单；frontier evaluation 需要困难、真实且答案可随时间确认的任务。
- **Mechanism / State Owner / Flow:** question state 从 `unsolved` 经 rule/LLM/human curation 进入 candidate；模型答案先过 compound validators，再由 community expert verification commit；平台拥有 status、provenance 与 supersession。
- **Implementation / Evaluation:** Stack Exchange 来源 500 题，跨 CS/math/science/humanities；top model 仅约 15% 过 automated validation，初步人工确认其中部分；validator-generator gap 是筛选机制而非真值证明。
- **Baselines / Sensitivity / Contract:** 比较 frontier models 与 validator combinations；没有稳定 ground truth、完成时间与专家 supply 的统一 SLO，题目状态会随世界知识变化。
- **Proves / Does Not / Limitations:** 证明 asynchronous open-question evaluation 可把自动预筛与人工 commit 分离；不证明 validator pass 即正确，也不证明未通过即错误。selection bias、answer drift、community latency 是主要威胁。
- **Trade-offs / Failure / Previous / Evolution:** 提升现实性与抗饱和性，牺牲即时可重复 score；会有 premature solve、expert disagreement、moving target。静态 benchmark 仍适合 regression gate。`Direct Evolution`：static answer key → live evidence lifecycle。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-WORKFLOW`/`PLATFORM-PRODUCTION`；`Integrate — New Mechanism Candidate`，本轮不写 Books。待定义 validator calibration、expert quorum、reopen/rollback contract。

### CTF-Dojo

- **Candidate / Week / Score；Family / Type:** CTF-Dojo / W35 / 27；`ARXIV-2508.18370`；paper、658 containerized CTF environments、training/eval artifact。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-25，v2 2025-09-23；Verified；阅读全文 environment construction、training、scaffold、held-out tests、data scaling、writeup-hint ablation、failure analysis 与 artifact。
- **Original / Previous / Changed:** 文本 vulnerability QA 便于收集，却不能证明 agent 能在可执行环境发现并利用漏洞；RL 需要大量隔离、可 reset、可验证的任务。
- **Mechanism / Ownership / Flow:** 每题容器拥有 filesystem/network/runtime truth；agent 通过 terminal action 改变环境；verifier/flag 给 executable reward；orchestrator 负责 reset、timeout、trajectory 与 train/test isolation。
- **Implementation / Evaluation:** 658 个跨类别 CTF，训练 agent 并在独立 benchmark 比较；研究 data scaling、writeup hints 与 scaffold。具体模型、GPU、rollout 与 token budget 依实验表，不能抽象为统一 cyber capability。
- **Baselines / Ablation / Overhead / Contract:** 对 base/instruction/agent training、不同数据量与 hints；容器启动、tool latency、episode timeout 是 harness 成本，生产并发/SLO Not Disclosed。
- **Proves / Does Not / Limitations:** 证明 executable verified feedback 可训练/衡量 CTF-style exploitation；不证明真实软件 supply-chain 防御/攻击能力，也不覆盖社会工程、权限与生产 noise。
- **Trade-offs / Failure / Previous / Evolution:** 高可验证性换来昂贵 sandbox、环境泄漏、shortcut flag、unsafe artifact 与 benchmark memorization 风险；静态 code reasoning 仍适合低成本筛选。`Direct Evolution`：text answer → executable artifact contract。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** `PLATFORM-SECURITY` 主 owner，handoff `AGENT-TOOL-CALLING`/`PLATFORM-EVALUATION-SYSTEM`；`Integrate — New Mechanism Candidate`，Books gate closed。待验证 sandbox escape、artifact signing、episode provenance 与 safe release gate。

### A.S.E

- **Candidate / Week / Score；Family / Type:** A.S.E / W35 / 25；`ARXIV-2508.18106`；repository-level secure code generation benchmark。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-25；Verified；阅读全文 task construction、repository context、functional/security verifier、model/scaffold comparison、error categories 与 limitations。
- **Original / Previous / Changed:** snippet-level static analysis 能快速计分，但忽略跨文件 dependency、build/test 与漏洞可利用路径；AI coding 已转向 repository mutation。
- **Mechanism / Ownership / Flow:** task fixture 拥有 repository/version；agent 生成 patch；build/test 与 security checks 分别判定 functional correctness 和 vulnerability；evaluator 记录 artifact 而非只评分自然语言。
- **Implementation / Evaluation Contract:** repository-level tasks、多模型/agent baseline、correctness 与 security 双轴；结果依赖具体 repo、test adequacy、scanner/exploit oracle，不是通用 secure-code rate。
- **Baselines / Ablations / Hardware:** 比较不同模型/scaffold 与 error class；运行成本主要是 repository checkout/build/test，模型 serving hardware、precision、batch、concurrency、SLO 不统一披露。
- **Proves / Does Not / Limitations:** 证明 pass functional tests 不等于 security pass；不证明未触发 verifier 的 patch 无漏洞。test incompleteness、tool false negative、dependency drift 是威胁。
- **Trade-offs / Failure / Previous / Evolution:** realism 与 executable evidence 提高，但成本、flakiness、sandbox/secret exposure、version pinning 复杂；unit-level benchmark 仍用于快速 regression。`Layering`：functional harness + security verifier。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-SECURITY`，handoff `PLATFORM-EVALUATION-SYSTEM`/`AGENT-WORKFLOW`；`Integrate — New Mechanism Candidate`，无 Books 改动。待补 exploitability severity、dependency CVE time boundary 与 reproducible build provenance。

### TiKMiX

- **Candidate / Week / Score；Family / Type:** TiKMiX / W35 / 24；`ARXIV-2508.17677`；pretraining data-mixture research。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-25；Verified；阅读全文 group-influence estimation、dynamic mixture update、models/datasets、in/out-domain evaluation、size scaling、compute analysis 与 ablation。
- **Original / Previous / Changed:** 固定 heuristic mixture 易实现并保持 data pipeline 稳定，却假设各 domain 的边际价值不随训练阶段/模型状态变化。
- **Mechanism / Owner / Flow:** validation groups 定义目标；周期性估计训练 group 对 validation group 的 influence，据此调整 sampler mixture；data controller 拥有 mixture state，optimizer 只消费 sampled batch。
- **Implementation / Evaluation:** 多 domain corpus 与不同模型规模比较 static mixture、sampling baseline 和 TiKMiX；作者报告 downstream 改善与可接受 estimation cost，具体数字只对其 token/compute budget成立。
- **Baselines / Sensitivity / Hardware:** 含 influence grouping、update frequency、model size 与 efficiency ablation；训练硬件、precision、global batch、network/SLO 未形成通用合同。
- **Proves / Does Not / Limitations:** 证明在实验中 data value 是 state-dependent，dynamic mixture 优于若干静态基线；不证明 influence proxy 因果正确或对 web-scale/continual data 稳定。
- **Trade-offs / Failure / Previous / Evolution:** 更好利用数据换来额外 eval/gradient estimate、feedback lag、validation overfit 与 oscillation；稳定 domain/小规模训练仍适合固定 mixture。`Direct Evolution`：static policy → feedback-controlled sampler。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** `TRAIN-DATA` owner，handoff `TRAIN-PRETRAINING`/`PLATFORM-MONITORING`；`Refine — Existing Argument`，本轮不改 Books。待研究 non-stationary validation、contamination 与 distributed sampler consistency。

### VibeVoice

- **Candidate / Week / Score；Family / Type:** VibeVoice / W35 / 25；`ARXIV-2508.19205`；Microsoft technical report、model/code release。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-26；Verified；阅读全文 continuous speech tokenizer、next-token diffusion、speaker conditioning、long-form generation、evaluation 与 limitations/model artifact。
- **Original / Previous / Changed:** codec-token autoregression提供明确离散序列，却在长对话产生极长 token stream，speaker continuity 与全局 prosody 难以维持。
- **Mechanism / State / Flow:** acoustic tokenizer 以高压缩 continuous latent 表示音频；语言/语义条件驱动 next-token diffusion 逐段生成，speaker embedding 与 conversation context 保持多说话人状态。
- **Implementation / Evaluation Contract:** 报告约 80× 相对 Encodec token compression、64K context 下最长 90 分钟/4 speakers；比较开源/闭源 dialogue TTS，但这些是作者模型、采样与 evaluator 条件。
- **Baselines / Sensitivity / Hardware:** 覆盖语音质量、speaker similarity、long-form cases；GPU、precision、batch、real-time factor/concurrency/SLO 未完整统一披露，90 分钟不是实时 serving 证明。
- **Proves / Does Not / Limitations:** 证明 continuous latent + diffusion 可显著缩短序列并保持长对话生成；不证明内容事实、说话人安全、任意语言/噪声鲁棒性或低延迟 streaming。
- **Trade-offs / Failure / Previous / Evolution:** 上下文长度下降，换来 iterative denoising、latent drift、speaker leakage、不可精确编辑与 misuse 风险；短 utterance/低延迟 ASR-TTS 链仍可选离散 codec。`Alternative Branch`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `INFER-REQUEST-LIFECYCLE`/`PLATFORM-SECURITY`；`Integrate — New Mechanism Candidate`，无 Books 改动。待验证 streaming commit、watermark、speaker consent 与 fleet SLO。

### Understanding Tool-Integrated Reasoning

- **Candidate / Week / Score；Family / Type:** Tool-Integrated Reasoning / W35 / 27；`ARXIV-2508.19201`；paper、formal analysis、training recipe。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-26；Verified；阅读全文 support-set formulation、tool-use taxonomy、ASPO objective、tasks/baselines、token efficiency、pass@k、algorithmic-friendliness rubric 与 appendices。
- **Original / Previous / Changed:** 参数内 reasoning 可重复且低风险，却受训练表示支持集限制；code/search/tool 能产生模型权重中不存在的新中间证据。
- **Mechanism / State / Flow:** tool invocation 扩展当前可达解集合；ASPO 修改 group-relative advantage，奖励能提高最终解空间且尽早发生的调用。policy 拥有 proposal，runtime 拥有 execution，verifier 拥有 correctness commit。
- **Implementation / Evaluation:** 数学/算法任务比较纯文本、tool prompt 与 tool-integrated training，分析 pass@k、token cost 和 capability expansion/shrinkage；工具环境、timeout 与 scorer 是 evaluation contract 一部分。
- **Baselines / Sensitivity / Hardware:** 包含 no-tool、prompt-only、训练方法和调用位置分析；model、tool sandbox 与采样设置见论文，部署硬件、并发、SLO 不足以外推。
- **Proves / Does Not / Limitations:** 证明在选定任务上工具可改变可达支持并可被 RL 学会；不证明每次 tool call 有价值，也不证明外部输出可信/安全。reward 与 tool availability 强耦合。
- **Trade-offs / Failure / Previous / Evolution:** 可验证计算换来 call latency、schema drift、tool overuse、错误环境与 security blast radius；closed-form/simple task 仍适合纯 reasoning。`Layering`：parametric reasoning → action-expanded reasoning。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-TOOL-CALLING`，handoff `TRAIN-GRPO`/`AGENT-WORKFLOW`；`Integrate — New Mechanism Candidate`，Books closed。待定义 expected information gain、cost-aware advantage 与 rollback provenance。

### UltraMemV2

- **Candidate / Week / Score；Family / Type:** UltraMemV2 / W35 / 25；`ARXIV-2508.18756`；memory-layer architecture paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-26；Verified；阅读全文 memory addressing、parameter scaling、120B configuration、long-context training/eval、MoE baselines、ablation 与 system-cost discussion。
- **Original / Previous / Changed:** dense FFN 计算重，MoE 只激活少数 experts 但会读取大量 expert weights、产生 routing/communication；早期 memory layers 又落后于高-expert MoE。
- **Mechanism / State / Flow:** 查询经多级/稀疏 addressing 选择 memory entries，memory table 拥有大容量参数，compute path 只读取少量条目；与 attention context state 分离。
- **Implementation / Evaluation:** 扩展到 120B memory parameters，并与 2/8-expert MoE 在 language/long-context tasks 下比较；结果绑定作者 token/active-parameter budget。
- **Baselines / Sensitivity / Hardware:** 有 entry count、addressing、active memory 与 MoE ablation；真实 HBM bandwidth、cache hit、placement、precision、batch、concurrency、SLO 未形成跨硬件 contract。
- **Proves / Does Not / Limitations:** 证明稀疏 memory parameterization 在测试预算可逼近/超过若干 MoE；不证明 commodity fleet 上总成本更低，也不等同 Agent persistent memory。
- **Trade-offs / Failure / Previous / Evolution:** 降低 active compute/部分 weight reads，却新增 address collision、stale/unused entries、irregular gather 和 sharding；高算术强度 dense/成熟 MoE stack 仍适用。`Alternative Branch`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `MODEL-LONG-CONTEXT`，handoff `MODEL-MOE`/`INFER-GPU-MEMORY`；`Integrate — New Mechanism Candidate`。待实测 HBM/network placement、training stability 与 cacheability。

### ThinkDial

- **Candidate / Week / Score；Family / Type:** ThinkDial / W35 / 23；`ARXIV-2508.18773`；open training recipe。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-26；Verified；全文覆盖 budget-mode SFT、两阶段 DAPO、length/leak reward、prompts、data、training details、baselines、ACT metric 与 ablation。
- **Original / Previous / Changed:** 固定 token budget 清晰但用户难为不同难度选值；binary think/no-think 不能表达多个 latency/quality operating point。
- **Mechanism / State / Flow:** SFT 建立 High/Medium/Low 条件分布；stage-1 RL 先恢复 peak，stage-2 用 mode-specific length reward；leak penalty 防止 reasoning 从 think 区迁到 answer 区。mode 是 request contract。
- **Implementation / Evaluation:** Qwen2.5-32B-Instruct，12K reasoning + 6K mode SFT、20K math RL，95+40 steps；AIME24/25、GSM8K、GPQA，32/4/8 次采样；与 no-BM-SFT/no-warmup/truncation 和 proprietary modes 比较。
- **Baselines / Sensitivity / Hardware:** 覆盖 SFT data amount、two-stage、length hacking；GPU/precision/global batch/serving concurrency/SLO Not Disclosed，ACT 权重是作者选择。
- **Proves / Does Not / Limitations:** 证明离散 mode 可学得长度/准确率分支并减少显式 token knob；不证明模型能正确判断任务难度，mode 由用户指定，OOD 主要数学→GPQA。
- **Trade-offs / Failure / Previous / Evolution:** 可控成本换来多分布训练、mode interference、reward hacking 与 answer leakage；hard budget/early exit 在严格 SLO 下仍合理。`Direct Evolution`：hard budget → learned operating modes。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `TRAIN-GRPO`，handoff `MODEL-SAMPLING`/`INFER-SCHEDULING`；`Refine — Existing Argument`。待做 calibrated router、per-request SLO 与 token/correctness joint gate。

### Optimal Sparsity of MoE for Reasoning

- **Candidate / Week / Score；Family / Type:** Optimal MoE Sparsity / W35 / 24；`ARXIV-2508.18672`；scaling/evaluation paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-26；Verified；阅读全文 iso-FLOP setup、total/active parameters、task loss、reasoning/coding evaluation、tokens-per-parameter、test-time compute/post-training 与 ablations。
- **Original / Previous / Changed:** “更多 total parameters 且更稀疏必然更好”把 capacity 与 per-token compute 混为一谈；reasoning 可能受 active computation/data exposure 限制。
- **Mechanism / State / Flow:** 在固定 FLOPs 下系统改变 expert count/top-k/active ratio，分离 memorization capacity、active path 与 training tokens；router 决定每 token 的 executable subnetwork。
- **Implementation / Evaluation:** 多 MoE sparsity/size 组合，比较 validation loss、downstream reasoning/coding、TTC 和 post-training；结论只在模型族、token budget 与 routing recipe 内成立。
- **Baselines / Sensitivity / Hardware:** iso-FLOP、active parameter、tokens-per-parameter、coding ablation；未给生产 all-to-all topology、tail latency、precision、batch、concurrency SLO。
- **Proves / Does Not / Limitations:** 证明 downstream reasoning 不由 total parameter 单调决定，并存在 workload-dependent sparsity optimum；不证明一个 universal expert ratio，也不计全量 communication/serving cost。
- **Trade-offs / Failure / Previous / Evolution:** 稀疏度提高 capacity/compute 比，但加剧 expert undertraining、routing imbalance、all-to-all 与 cold expert；dense/低 expert 在通信受限或小模型仍优。`Alternative Branch`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `MODEL-MOE`，handoff `TRAIN-DISTRIBUTED-TRAINING`/`INFER-SCHEDULING`；`Refine — Existing Argument`。待建立含 network/HBM/quality 的 iso-cost contract。

### StepWiser

- **Candidate / Week / Score；Family / Type:** StepWiser / W35 / 25；`ARXIV-2508.19229`；generative stepwise judge paper/model。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-26；Verified；阅读全文 self-segmentation、Q-value annotation、progress reward、judge RL、ProcessBench/results、annotation/training appendices 与 failure cases。
- **Original / Previous / Changed:** binary outcome reward 稀疏；静态 classifier PRM 给分但难解释错误且受标注固定边界限制。
- **Mechanism / State / Flow:** judge 先分割 reasoning steps，再生成 critique/进展判断；Q-value 近似步骤后的成功潜力，RL 奖励正确定位与解释。trajectory state 由 judge trace 持有，policy 可消费 dense signal。
- **Implementation / Evaluation:** 过程数据 annotation、judge SFT/RL，在 ProcessBench 等比较 outcome/PRM/generative judge；性能依赖 segmentation、ground-truth 与 verifier quality。
- **Baselines / Sensitivity / Hardware:** self-segmentation、annotation/reward 与 RL ablation；生成 judge 带额外 tokens/latency，model hardware、batch、concurrency、SLO Not Disclosed。
- **Proves / Does Not / Limitations:** 证明 generative critique 在选定 benchmark 提升 step-error localization；不证明 critique faithful 或能安全作为训练 reward，judge/policy 共偏差可能放大。
- **Trade-offs / Failure / Previous / Evolution:** 更可解释 dense signal 换来 judge cost、segmentation drift、reward gaming 与 recursive evaluation；可执行 final verifier 仍应拥有 commit。`Layering`：outcome verifier + process diagnostic。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-GRPO`/`AGENT-REFLECTION`；`Integrate — New Mechanism Candidate`。待做 judge calibration、disagreement routing 与 cost-aware sampling。

### CODA

- **Candidate / Week / Score；Family / Type:** CODA / W35 / 25；`ARXIV-2508.20096`；computer-use agent architecture/RL paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-27；Verified；阅读全文 dual-brain decomposition、decoupled RL、judge fine-tuning、perception/planning experiments、prompts 与 limitations。
- **Original / Previous / Changed:** 单一 GUI policy 同时做长程 plan 与像素级 action 容易让高层 reasoning latency 干扰低层控制，且两类错误 reward 不同。
- **Mechanism / State / Flow:** cerebrum 生成目标/plan，cerebellum 根据当前 screen 执行动作；decoupled RL 对两层分开优化，judge 提供任务/步骤信号。handoff state 是 plan、screen、action history。
- **Implementation / Evaluation:** GUI/computer-use benchmarks比较单脑/双脑与训练阶段；judge model另行 fine-tune。结果依赖 screen resolution、action schema、environment reset 与 evaluator。
- **Baselines / Sensitivity / Hardware:** architecture/training/judge ablation；inference hardware、precision、interaction latency、并发、real-time SLO 未完整披露。
- **Proves / Does Not / Limitations:** 证明层次化 policy 在作者环境可分离 planning 与 execution；不证明模块边界总是正确，也不解决网页 drift、permission、unsafe action 与 user intent ambiguity。
- **Trade-offs / Failure / Previous / Evolution:** specialization 提高控制精度，新增 stale plan、handoff loss、cross-module blame、double inference cost；短任务单 policy 仍更简单。`Layering`：planner → controller。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-WORKFLOW`，handoff `AGENT-PLANNING`/`AGENT-TOOL-CALLING`；`Integrate — New Mechanism Candidate`。待定义 plan invalidation、human interrupt 与 end-to-end rollback。

### Analysing Chain of Thought Dynamics

- **Candidate / Week / Score；Family / Type:** CoT Dynamics / W35 / 23；`ARXIV-2508.19827`；causal intervention/interpretability study。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-27；Verified；阅读全文 CoT intervention、confidence trajectories、distilled-vs-base model comparison、infrastructure/inference appendices 与 discussion。
- **Original / Previous / Changed:** 把 CoT 当 faithful explanation 很诱人，但正确 answer 可能先形成、CoT 也可能是 post-hoc；只比较最终准确率无法区分 guidance 与 rationalization。
- **Mechanism / State / Flow:** 对 reasoning trace 做干预/替换并追踪 answer confidence 随 token 演化；区分 trace 对最终决策的 causal influence 与语义 faithfulness。
- **Implementation / Evaluation:** 多模型/任务的 intervention 与 confidence analysis；distilled reasoning model 与其他 model family 结果不同，说明训练来源是重要条件。
- **Baselines / Sensitivity / Hardware:** original/perturbed/no-CoT 与不同模型比较；logit confidence 不等于 calibrated truth，hardware/precision/batch/SLO不构成核心结论。
- **Proves / Does Not / Limitations:** 证明 unfaithful-looking CoT 仍可能因计算路径影响答案；不证明自然语言 trace 是内部状态的忠实读出，也不能由单次 trace诊断知识。
- **Trade-offs / Failure / Previous / Evolution:** trace 提供调试信号但可能误导审计、被策略化；external verifier 与 behavior test 仍比“读 CoT”更可靠。`Evidence refinement`，不是新的推理算法。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-REFLECTION`，handoff `PLATFORM-EVALUATION-SYSTEM`；`Refine — Evidence Boundary`。待研究 intervention validity、calibration 与 hidden-state causal probes。

### Discrete Diffusion VLA

- **Candidate / Week / Score；Family / Type:** Discrete Diffusion VLA / W35 / 26；`ARXIV-2508.20072`；VLA action-decoding paper、implementation appendix。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-27；Verified；阅读全文 discrete action diffusion、adaptive order、training、multi-platform/real-robot evaluation、VLM retention、latency/ablation 与 reproducibility appendices。
- **Original / Previous / Changed:** autoregressive action token 顺序明确、cache 友好，却串行并把坐标顺序当成因果顺序；连续 diffusion 能并行修正但难与离散 language/action vocabulary统一。
- **Mechanism / State / Flow:** mask-based discrete diffusion 从部分 action chunk 反复预测/重掩码，以 confidence 自适应决定 token commit order；policy state 包含当前 masked action block 与 denoising step。
- **Implementation / Evaluation:** 多机器人平台、simulation 与 real-robot tasks，对 AR VLA、continuous/diffusion branches 比较，并测 vision-language retention、step count 与 inference efficiency。
- **Baselines / Sensitivity / Hardware:** decoding steps、order/remasking、action chunk 与 architecture ablation；真实 control frequency、GPU/precision/batch/concurrency/SLO 依平台，不能用平均 latency概括安全闭环。
- **Proves / Does Not / Limitations:** 证明离散 diffusion 可作为 VLA action decoder 并在作者任务改善部分指标；不证明迭代 refinement 总满足实时 deadline 或 physical safety。
- **Trade-offs / Failure / Previous / Evolution:** 并行修正与非固定顺序换来多步 compute、partial-action inconsistency、commit/rollback 难题；严格低延迟/因果控制仍可选 AR。`Alternative Branch`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** `MULTIMODAL-EMBODIED-VLA` owner，handoff `MULTIMODAL-GENERATIVE-PARADIGMS`；`Integrate — New Mechanism Candidate`。待定义 action commit barrier、safety envelope 与 deadline-aware step budget。

### Diffusion LMs Know the Answer Before Decoding

- **Candidate / Week / Score；Family / Type:** Early-answer DLM / W35 / 24；`ARXIV-2508.19982`；diffusion-LM analysis/acceleration paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-27；Verified；阅读全文 internal answer signal、early extraction/refinement method、main experiments、other acceleration baselines、step/block/remasking ablations 与 appendix。
- **Original / Previous / Changed:** diffusion LM 固定执行完整 denoising steps，假设最终可读 token 才含答案；但 latent/partial distribution 可能更早稳定。
- **Mechanism / State / Flow:** 从中间 denoising state 估计答案/置信信号，对候选区域做 semi-autoregressive refinement；scheduler 可在 evidence 足够时减少剩余 steps，而不是盲目固定迭代。
- **Implementation / Evaluation:** reasoning/QA tasks比较 full decoding、early method 与其他 acceleration；分析 step budget、block length、remasking compatibility 与 accuracy-speed curve。
- **Baselines / Sensitivity / Hardware:** 多 step/block settings；速度依模型、sequence、kernel 与 batch，precision/concurrency/SLO 未提供统一合同。
- **Proves / Does Not / Limitations:** 证明部分 DLM 在可读 output 前已有可提取 answer signal；不证明 early confidence calibrated，也不保证开放生成/长文本中答案边界可识别。
- **Trade-offs / Failure / Previous / Evolution:** 少 steps 换来 premature commit、confidence miscalibration 与 refinement branch；固定完整 denoise 对高风险/自由生成仍稳健。`Direct Evolution`：fixed steps → evidence-conditioned termination。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `INFER-SCHEDULING`；`Refine — Existing Argument`。待做 selective-risk calibration、batch divergence 与 rollback。

### Mind the Third Eye

- **Candidate / Week / Score；Family / Type:** Mind the Third Eye / W35 / 25；`ARXIV-2508.19493`；smartphone-agent privacy benchmark。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-27；Verified；阅读全文 privacy taxonomy、task/data construction、agent/model setup、metrics、error analysis 与 limitations。
- **Original / Previous / Changed:** GUI benchmark 通常只验 task success；手机 screen 同时暴露 credential、location、messages 等敏感状态，成功动作可能仍违反 privacy intent。
- **Mechanism / State / Flow:** benchmark 在 observation/action trajectory 标注 sensitive regions 与 acceptable handling；agent proposal 需同时过 task-success 与 privacy-aware decision，policy/permission gate拥有不同 owner。
- **Implementation / Evaluation:** 多类 smartphone tasks、MLLM agents 与 privacy scenarios；比较识别、warning/avoidance 与 task completion。结果依 screen rendering、policy taxonomy 和 evaluator。
- **Baselines / Sensitivity / Hardware:** 多模型/场景对比与错误类别；没有生产 OS permission、真实用户分布、device latency/concurrency/SLO 的统一验证。
- **Proves / Does Not / Limitations:** 证明高 task score 不保证 privacy awareness；不证明 benchmark policy 等同所有用户偏好，也不证明视觉 warning 能阻止泄漏。
- **Trade-offs / Failure / Previous / Evolution:** privacy gate 降低误操作但增加 false block、warning fatigue、policy drift；低敏感/fully sandboxed task 可走简化路径。`Layering`：task verifier + privacy policy verifier。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-SECURITY`，handoff `AGENT-WORKFLOW`；`Integrate — New Mechanism Candidate`。待定义 consent、contextual integrity、OS enforcement 与 audit deletion。

### DeepScholar-Bench

- **Candidate / Week / Score；Family / Type:** DeepScholar-Bench / W35 / 25；`ARXIV-2508.20033`；live research-synthesis benchmark、automated evaluator。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-27；Verified；阅读全文 live dataset pipeline、retrieval/reference baseline、automated/human evaluation、agreement、error analysis 与 appendices。
- **Original / Previous / Changed:** 静态 QA/summary 不能衡量检索覆盖、citation entailment 与最新性；research synthesis 的正确性随文献更新而变化。
- **Mechanism / State / Flow:** live arXiv query生成 task snapshot；system 检索并写 synthesis/citations；evaluator分别验 relevance、citation/verifiability、coverage 与 writing，snapshot/version 拥有 provenance。
- **Implementation / Evaluation:** 比较多种 generative research systems 与 DeepScholar-ref，在 recent-paper tasks 做 automated + human evaluation；agreement 明示 evaluator 不确定性。
- **Baselines / Sensitivity / Hardware:** retrieval/grounded baseline、human comparison 与 rubric analysis；检索 index date、API状态、model context 与 judge版本是合同，硬件/并发/SLO非核心且未统一。
- **Proves / Does Not / Limitations:** 证明 report quality 必须拆成 retrieval、claim-evidence 与 synthesis；不证明自动 judge 是真值，也不保证 live corpus 下重复 score稳定。
- **Trade-offs / Failure / Previous / Evolution:** realism/freshness 换来 moving target、index drift、citation gaming、judge bias；冻结 corpus 仍适合 regression。`Direct Evolution`：static answer → versioned evidence graph。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `AGENT-RAG`/`AGENT-WORKFLOW`；`Integrate — New Mechanism Candidate`。待实现 claim-level provenance、snapshot replay 与 evaluator supersession。

### Taming the Chaos

- **Candidate / Week / Score；Family / Type:** Taming the Chaos / W35 / 27；`ARXIV-2508.19559`；heterogeneous/disaggregated LLM autoscaling paper。
- **Event / Revision；Sources；Access / Full-read:** first-public 2025-08-27；Verified；阅读全文 system model、coordinated autoscaler/router、implementation、heterogeneous/PD workloads、baseline、sensitivity、overhead 与 failure discussion。
- **Original / Previous / Changed:** homogeneous replica autoscaling用 queue/QPS 即可；PD disaggregation 中 prefill/decode capacity、request length 与 accelerator不同，独立扩缩会搬走瓶颈或振荡。
- **Mechanism / State / Flow:** controller联合估计 prefiller/decoder capacity 与 routing，按 workload mix决定两阶段 replica；telemetry→capacity model→joint plan→routing/scale action→observed SLO形成闭环。
- **State Ownership / Implementation:** autoscaler拥有 desired fleet state，router拥有request assignment，engine持有KV/queue；实验在作者异构集群与 trace-driven workload 下比较独立/静态 scaling。
- **Evaluation / Baselines / Sensitivity / Hardware:** 覆盖负载变化、异构节点、PD配置、latency/throughput/cost 与 overhead；具体 GPU/model/length/SLO 绑定表格，不能转成通用倍数。
- **Proves / Does Not / Limitations:** 证明联合控制在实验 trace 优于若干独立 baseline；不证明任意 cloud cold-start/spot/failure 下稳定，也未消除 telemetry delay/model error。
- **Trade-offs / Failure / Previous / Evolution:** SLO/cost改善换来 centralized model、oscillation、stale metrics、KV transfer 与 placement约束；同构稳定负载仍可简单 HPA。`Direct Evolution`：replica count → typed-stage fleet control。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `INFER-SCHEDULING`，handoff `INFER-PD-DISAGGREGATION`/`PLATFORM-COST`；`Integrate — New Mechanism Candidate`。待做 stability proof、failure recovery 与 uncertainty-aware capacity estimate。

### Kubernetes v1.34 / DRA core GA

- **Candidate / Week / Score；Family / Type:** Kubernetes v1.34 / DRA / W35 / 27；`K8S-1.34-DRA`；official release、KEP-4381、stable API/docs、implementation。
- **Event / Revision；Sources；Access / Full-read:** release 2025-08-27；9/1 GA deep dive、9/17 health、9/18 consumable capacity 为同 family follow-up；Verified；阅读 release、stable kinds、allocation workflow、feature states、KEP与代码路径。
- **Original / Previous / Changed:** extended resource整数“要 N 个设备”简单且适合整卡独占，却难表达属性、配置、claim reuse、sharing 与 topology。
- **Mechanism / State Ownership:** `DeviceClass`归 admin，driver发布 `ResourceSlice`/device truth，workload创建/引用 `ResourceClaim`，scheduler写 allocation，kubelet/driver负责 prepare/unprepare；core API为 `resource.k8s.io/v1`。
- **Control / Data Flow / Implementation:** advertise → claim request/CEL → scheduler selects node+device → allocation commit → Pod bind → node prepare → container → teardown/release；GA是结构化 core，不等于所有 sharing/health/admin features GA。
- **Evaluation / Baselines / Hardware Contract:** graduation以 API/conformance/maturity 为证据，与 Device Plugin expression 比较；没有统一 GPU utilization、scheduler latency、driver scale benchmark，model/precision/length不适用。
- **Proves / Does Not / Limitations:** 证明 stable resource contract 与 owner separation；不证明 MIG/time-slicing/fabric/gang scheduling由core自动提供，也不证明提高利用率。
- **Trade-offs / Failure / Previous / Evolution:** 表达力换来 driver state、stale ResourceSlice、allocation/prepare split-brain、RBAC/upgrade skew；homogeneous exclusive GPU和driver未成熟时 extended resource仍合理。`Direct Evolution`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-GPU-SCHEDULER`，handoff `PLATFORM-KUBEFLOW`/`PLATFORM-PRODUCTION`；`Refine — Existing Argument`，未改 Books。待 driver conformance、claim recovery 与大集群 scheduler cost。

### rStar2-Agent

- **Candidate / Week / Score；Family / Type:** rStar2-Agent / W35 / 27；`ARXIV-2508.20722`；agentic reasoning report、code/model。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；Verified；阅读全文 environment、tool use、load-balanced rollout scheduler、cold start、data curation、多阶段 RL、failed attempts、experiments/ablation。
- **Original / Previous / Changed:** 纯 reasoning RL可用答案 verifier，但 tool trajectory 有不等 episode cost、环境等待和负载长尾，普通 synchronous rollout浪费训练资源。
- **Mechanism / State / Flow:** code/tool agent在 sandbox执行；scheduler按 episode progress/length调度 rollouts，training recipe先 non-reasoning cold start，再 curated multi-stage RL。环境、trajectory、reward与policy checkpoint各有版本。
- **Implementation / Evaluation:** 14B agent在数学/代码等任务与 larger models比较；报告 load balance、training stages和失败方案。作者 benchmark依 tool harness、sampling与 verifier。
- **Baselines / Sensitivity / Hardware:** base/SFT/RL stages、scheduler与数据 ablation；GPU fleet、precision、rollout concurrency在报告内，但不能外推任意 environment/SLO。
- **Proves / Does Not / Limitations:** 证明小模型配合 executable tools、训练 recipe 与 rollout scheduling可获得强 agentic results；不证明参数能力等同自主性，也不证明 sandbox外安全。
- **Trade-offs / Failure / Previous / Evolution:** tool expansion与并行 rollouts换来 environment variance、reward exploit、straggler、artifact security；closed-form task仍适合无工具 verifier。`Layering`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-WORKFLOW`，handoff `TRAIN-GRPO`/`AGENT-PLATFORM`；`Integrate — New Mechanism Candidate`。待固定 environment identity、retry semantics 与 scheduler fairness。

### Pref-GRPO

- **Candidate / Week / Score；Family / Type:** Pref-GRPO / W35 / 24；`ARXIV-2508.20751`；T2I RL/evaluation paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28，后续 v2同 family；Verified；阅读全文 illusory advantage推导、pairwise win-rate reward、UniGenBench、main experiments、noise/overhead/human validation ablations。
- **Original / Previous / Changed:** pointwise reward + group z-score简单，但组内分数很接近时小标准差放大噪声，驱动过饱和/暗图 reward hacking。
- **Mechanism / State / Flow:** PPRM比较组内 image pairs，win rate作为 reward/advantage；flow matching rollout仍由GRPO更新，evaluator拥有 pairwise ordering而非绝对分数。
- **Implementation / Evaluation:** T2I models、UniGenBench 600 prompts/10 primary/27 subdimensions、GenEval/T2I-CompBench；Gemini-based evaluator并有人评校验，结论依 evaluator版本。
- **Baselines / Sensitivity / Hardware:** pointwise RM、pairwise、auxiliary reward、noise、wall-clock overhead；GPU/precision/batch/SLO不构成通用结果。
- **Proves / Does Not / Limitations:** 证明小方差归一化会制造 illusory advantage，pairwise在作者设置更稳；不证明偏好排序无偏或消除所有 reward hacking。
- **Trade-offs / Failure / Previous / Evolution:** 更稳 ranking换来 O(G²) pair comparisons、non-transitive preference与judge drift；可校准绝对 metric仍适合可测物理量。`Alternative Branch`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `TRAIN-GRPO`，handoff `PLATFORM-EVALUATION-SYSTEM`；`Refine — Existing Argument`。待低成本 pairing、uncertainty与human audit。

### MCP-Bench

- **Candidate / Week / Score；Family / Type:** MCP-Bench / W35 / 27；`ARXIV-2508.20453`；live MCP-server agent benchmark。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；Verified；阅读全文 28 servers/250 tools、task construction、execution harness、schema/tool/trajectory/task metrics、20-model results、round/tool analysis、judge ablation 与 appendix。
- **Original / Previous / Changed:** function-call benchmark用少量 synthetic tools可重复，却不测真实 server schema、跨 tool state、authentication与失败恢复。
- **Mechanism / State / Flow:** agent发现 schema→选择 server/tool→构造参数→执行→读取结果→多轮修正；server拥有外部 state，harness记录 trace，task verifier/judge分层评分。
- **Implementation / Evaluation:** 真实 MCP servers、复杂多步 tasks、tool/schema/trajectory/task success多粒度；live availability与 judge pipeline 是合同，不能把最终分数归因模型参数 alone。
- **Baselines / Sensitivity / Hardware:** 20个LLM、round/tool-call分布、judge ablation；API latency、rate limits、auth、model serving hardware/precision/concurrency会变，未形成固定SLO。
- **Proves / Does Not / Limitations:** 证明 real-server coordination暴露 synthetic benchmark看不到的 failure；不证明 MCP protocol本身提高智能，也不保证 live rerun可完全复现。
- **Trade-offs / Failure / Previous / Evolution:** realism换来 server drift、side effect、credential与flakiness；mock server仍适合 CI。`Direct Evolution`：schema call → stateful tool ecosystem。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-MCP`，handoff `AGENT-TOOL-CALLING`/`PLATFORM-SECURITY`；`Integrate — New Mechanism Candidate`。待 server snapshot、side-effect sandbox 与 deterministic replay。

### AWorld

- **Candidate / Week / Score；Family / Type:** AWorld / W35 / 27；`ARXIV-2508.20404`；agent-environment rollout framework/paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；Verified；阅读全文 environment abstraction、distributed rollouts、tool integrations、scale/efficiency experiments、GAIA training与future work。
- **Original / Previous / Changed:** 单进程串行 rollout容易实现，但 agent episode有长尾、外部 wait与异质 environment，GPU trainer会空闲。
- **Mechanism / State / Flow:** decouple policy inference、environment execution、trajectory collection与trainer；distributed workers并行 episode，orchestrator拥有 lifecycle/retry，trajectory带 environment/tool provenance回流训练。
- **Implementation / Evaluation:** 作者报告相对单节点串行最高14.6×和 Qwen3-32B GAIA 21.59→32.23；只在其cluster、environment、concurrency和训练recipe成立。
- **Baselines / Sensitivity / Hardware:** 单节点/分布式、rollout规模与GAIA训练；未充分证明exactly-once、失败重放、外部API波动和跨租户公平。
- **Proves / Does Not / Limitations:** 证明 rollout orchestration是独立system bottleneck；不证明框架速度自动转成policy质量，也不证明所有environment可并行安全执行。
- **Trade-offs / Failure / Previous / Evolution:** 利用率提升换来 duplicate side effect、stale policy、trajectory skew、retry ambiguity；小规模确定性env仍适合串行。`Direct Evolution`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-PLATFORM`，handoff `TRAIN-GRPO`/`AGENT-WORKFLOW`；`Integrate — New Mechanism Candidate`。待定义 episode identity、policy version、idempotency与backpressure。

### CogVLA

- **Candidate / Week / Score；Family / Type:** CogVLA / W35 / 26；`ARXIV-2508.21046`；VLA routing/sparsification paper、artifact。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；Verified；阅读全文 EFA routing、LFP pruning、V-L-A coupled attention、training、LIBERO/real-world setup、multi-seed/latency/ablation appendices。
- **Original / Previous / Changed:** monolithic VLA让每层同等处理 vision/language/action，简单但浪费计算且可能让 instruction语义与低层action互相干扰。
- **Mechanism / State / Flow:** instruction驱动 EFA选择需要激活的计算路径，LFP剪除低贡献视觉features，coupled attention维持V-L-A交互；router/pruner拥有动态 compute graph。
- **Implementation / Evaluation:** LIBERO与真实机器人任务；作者报告97.4%、real tasks 70%、训练2.5×/latency2.8×相对OpenVLA，均绑定其模型/硬件/任务。
- **Baselines / Sensitivity / Hardware:** OpenVLA/architecture、routing/pruning与multi-seed ablation；control frequency、precision、batch、safety SLO未统一披露。
- **Proves / Does Not / Limitations:** 证明条件计算可用于VLA并减少部分成本；不证明router在OOD scene保留关键证据或满足physical safety。
- **Trade-offs / Failure / Previous / Evolution:** 稀疏执行换来 routing error、non-stationary latency、debug/rollback困难；固定dense path在小模型/高安全任务仍合理。`Principle Reuse`：MoE/conditional compute进入VLA。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `MULTIMODAL-EMBODIED-VLA`，handoff `MODEL-MOE`/`INFER-SCHEDULING`；`Integrate — New Mechanism Candidate`。待router confidence、deadline与safety fallback。

### EO-1

- **Candidate / Week / Score；Family / Type:** EO-1 / W35 / 26；`ARXIV-2508.21112`；unified embodied foundation model、EO-Data1.5M、artifact。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；Verified；阅读全文 unified architecture/data、AR reasoning + flow-matching action、benchmark/real-world/multi-embodiment/long-horizon experiments、implementation与limitations。
- **Original / Previous / Changed:** per-robot specialist接口清晰但数据不可共享；单一AR decoder统一token却不适合连续高频action distribution。
- **Mechanism / State / Flow:** decoder-only backbone统一vision/language/reasoning，flow-matching head生成连续 action；embodiment/action schema与observation history条件化policy，controller执行后回传新state。
- **Implementation / Evaluation:** EO-Data1.5M，多公开benchmark、真实机器人、多embodiment与long-horizon tasks；结果绑定具体robot calibration、sampling和safety setup。
- **Baselines / Sensitivity / Hardware:** specialist/unified/VLA baselines、reasoning与head组件分析；training hardware、precision有论文设置，real-time concurrency/control SLO不具通用性。
- **Proves / Does Not / Limitations:** 证明共享backbone + continuous action head可跨多embodiment训练；不证明真正universal control、sim-to-real安全或开放世界因果模型。
- **Trade-offs / Failure / Previous / Evolution:** 数据共享与泛化换来 schema alignment、negative transfer、calibration drift与大模型latency；specialist controller在固定工位仍更可验证。`Layering`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `MULTIMODAL-EMBODIED-VLA`，handoff `MULTIMODAL-WORLD-MODELS`/`PLATFORM-SECURITY`；`Integrate — New Mechanism Candidate`。待定义 embodiment identity、action normalization、override与rollback。

### UItron

- **Candidate / Week / Score；Family / Type:** UItron / W35 / 24；`ARXIV-2508.21767`；GUI foundation-agent paper/model。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-29；Verified；阅读全文 perception/grounding/planning data、three-stage curriculum RL、offline/online GUI benchmarks、baseline与ablation。
- **Original / Previous / Changed:** 独立OCR/grounder/planner模块便于诊断但错误层层传递；端到端GUI agent又可能跳过基础视觉能力直接过拟合trajectory。
- **Mechanism / State / Flow:** curriculum依次强化 perception→planning→interactive RL；screen/element grounding先建立可操作表示，再生成plan/action，environment反馈进入下一轮。
- **Implementation / Evaluation:** VisualWebBench、ScreenSpot/V2、AndroidControl与online tasks；多模型baseline，结果依screen scale、action protocol、environment version。
- **Baselines / Sensitivity / Hardware:** stage/data/curriculum ablation；GUI latency、token budget、hardware/precision/concurrency/SLO未形成生产合同。
- **Proves / Does Not / Limitations:** 证明 curriculum可减少从raw screen直接学长轨迹的难度；不证明页面更新、权限、隐私和不可逆action安全。
- **Trade-offs / Failure / Previous / Evolution:** unified policy减少手工接口却降低owner可解释性，新增grounding drift、plan staleness；模块化tool chain仍适合严格审计。`Direct Evolution / coexistence`。
- **ROADMAP / Chapters / Existing / Decision / Changes / Open:** owner `AGENT-WORKFLOW`，handoff `AGENT-PLANNING`/`AGENT-TOOL-CALLING`；`Refine — Existing Argument`。待做state identity、human approval与failure recovery。

### ELV-Halluc

- **Candidate / Week / Score；Source Family ID；Source Type:** ELV-Halluc / W35 / 24；`ARXIV-2508.21496`；long-video hallucination benchmark paper。
- **Event Date / First-public / Revision；Sources；Access / Full-read:** v1 2025-08-29，v2 2025-09-02（同 family）；Verified。阅读全文 benchmark construction、SAH 定义、in-video/out-video perturbation、模型比较、semantic-complexity/frame-count/model-size sensitivity、position-encoding/DPO mitigation、appendix 与 limitations。
- **Original Problem / Previous Design / Changed Constraint:** image-level object hallucination metric 对单帧或短 clip 合理，却无法区分“每帧都看对、跨事件聚合错”的 long-video failure；事件增长、快速切换和长序列 positional state 使 aggregation 成为独立约束。
- **Mechanism / State Ownership / Control and Data Flow:** 数据集以 event-by-event video 为 owner，Gemini captions 经人工复核；in-video 负例把对象替换成同一视频另一事件对象，out-video 负例引入不存在对象，SAH ratio 分离 semantic aggregation error。模型接收采样帧并输出 event-level answer，evaluator 拥有扰动 provenance 与判定。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** 比较多种 LVLM、semantic complexity、rapid change、frame count、model size；mitigation 比较 vanilla RoPE、TAD-RoPE、m-RoPE、VideoRoPE 与 DPO。作者实验显示 VideoRoPE 的 SAH ratio 较低，但更强 positional encoding 不等于整体 hallucination 被消除。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not Prove:** 模型与采样长度依论文表格，统一 precision、batch、concurrency、production SLO 未披露。证据证明 long-video aggregation failure 可独立测量；不证明该数据构造覆盖开放世界 hallucination，也不证明任一 positional recipe 是通用修复。
- **Trade-offs / Failure / Previous Applies / Evolution:** controlled perturbation 提升可诊断性，却引入 generator/human-curation bias、sampling aliasing 与 attribution ambiguity；短视频/单事件仍适合 object-level metric。`Layering / Evaluation Refinement`。
- **ROADMAP / Adjacent Chapters / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `MULTIMODAL-REPRESENTATION` 与 position-encoding owner；现有 evaluation contract 可承载，决定 `Refine — Existing Argument`，本轮不改 Books。待验证不同 frame sampler 下 SAH stability 与事件边界标注一致性。

### Open Data Synthesis for Deep Research

- **Candidate / Week / Score；Source Family ID；Source Type:** Open Data Synthesis for Deep Research / W35 / 26；`ARXIV-2509.00375`；paper、data-synthesis/training pipeline。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-30（当前 v1）；Verified。阅读全文 HCSP formulation、InfoSeek dual-agent pipeline、Research Tree construction、question synthesis、rejection-sampled SFT、GRPO、search/refiner agents、evaluation、appendix 与 limitations。
- **Original / Previous / Changed:** flat CSP/multi-hop QA 能控制局部答案且易生成，但 deep research 同时要求分层子问题、跨页面 evidence 与 constraint dependency；规模化人工编写又成本高、版本难冻结。
- **Mechanism / State Ownership / Flow:** InfoSeek 从网页构建带 URL/provenance 的 Research Tree，blur parent node 并附加 constraint 后扩展子树，再生成问题；multi-query search 与 refiner 产生 trajectory，rejection sampling 选择 SFT 样本，GRPO 用 reasoning/search reward 后训练。tree、source snapshot、constraint、tool history 与 answer 分属显式 owner。
- **Implementation / Evaluation Contract / Baselines:** 作者构建超过 50K training examples 与 curated test set，比较不同 data/training/search pipelines；结果只绑定其网页 snapshot、generator/judge、retrieval backend 与 reward，不代表任意 research agent 的事实正确率。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 训练模型与主要设置由正文/appendix 给出，生产查询并发、网页延迟、SLO 与部分 infra 条件未形成统一 contract。证明 HCSP/tree synthesis 能形成可训练的 hierarchical research tasks；不证明 synthetic tree 天然无泄漏、无 shortcut 或具真实世界代表性。
- **Trade-offs / Failure / Previous / Evolution:** scalable synthesis 换来 source drift、generator/judge bias、invalid constraint、provenance loss 与 reward hacking；高风险、小规模领域仍需人工 curated data。`Direct Evolution` from flat QA synthesis to hierarchical research data。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `TRAIN-DATA`，handoff `AGENT-RAG`/`AGENT-WORKFLOW`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待把 webpage snapshot、tree revision、trajectory 与 reward-version 绑定为可重放 identity。

### Metis: Training Large Language Models with FP4 Precision

- **Candidate / Week / Score；Source Family ID；Source Type:** Metis / W35 / 27；`ARXIV-2509.00404`；low-precision training paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-30，当前 HTML 为 v4 2025-09-30（同 family revision）；Verified。阅读全文 spectral analysis、quantizer、projection/sampling approximation、W4A4G4 training、efficiency、main/extended experiments、ablation、sensitivity、NVFP4 appendix 与 limitations。
- **Original / Previous / Changed:** BF16 以宽动态范围换稳定性，统一 tensor-domain FP4 scale 则易被 weights/activations/gradients 的各向异性 singular spectrum 支配；训练成本推动 W4A4G4，但量化偏差与 spectral distortion 成为约束。
- **Mechanism / State Ownership / Flow:** Metis 在 spectral domain 将各向异性谱划分为较窄 sub-distribution，以 sparse random sampling / random projection 近似 dominant subspace，固定 1.5% low-rank rank 并配 stochastic rounding；quantizer 进入 forward/backward，scale、projection/decomposition 与 residual/high-precision branch 需随 optimizer/checkpoint 一起拥有版本状态。
- **Implementation / Evaluation Contract / Baselines / Ablations:** 在 LLaMA-3 8B、100B tokens 的 W4A4G4 FP4 training 比较 BF16、NVFP4 与相关量化/transform baseline；作者报告相对 BF16 约 0.4% training-loss gap、下游约 0.1% degradation，并给出组件与 rank sensitivity，均只对该 recipe 成立。
- **Hardware / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** precision 是核心 contract，但设备拓扑、kernel maturity、batch 与吞吐/SLO 不能从单一设置推广。论文中的 NVIDIA FP4 recipe 是作者实现版本，不能替代 vendor implementation fact。证据支持 spectral anisotropy 是 FP4 training 的重要误差来源；不证明 FP4 对所有模型/optimizer/scale 稳定或必然优于 BF16。
- **Trade-offs / Failure / Previous / Evolution:** 更低 bandwidth/compute 换来 projection/decomposition overhead、kernel support、scale drift、checkpoint incompatibility 与难调试数值异常；BF16 仍适合稳定性、复现和故障定位优先场景。`Alternative Branch / Principle Reuse`。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `TRAIN-PRETRAINING`，handoff `TRAIN-DISTRIBUTED-TRAINING`/`INFER-TENSORRT-LLM`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待验证 optimizer-state precision、resume exactness、不同 topology 的端到端收益。

### Camlang

- **Candidate / Week / Score；Source Family ID；Source Type:** Camlang / W35 / 22；`ARXIV-2509.00425`；constructed-language reasoning benchmark paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-30（当前 v1）；Verified。阅读全文 grammar/dictionary construction、refinement、Camlang-CSQA-v0 annotation/statistics、context/tool settings、exact match、semantic human verification、error analysis、prompts 与 limitations。
- **Original / Previous / Changed:** natural-language reasoning benchmark 接近真实使用，但模型可能依赖预训练记忆、熟悉语法或 lexical shortcut；要测 metalinguistic deductive learning，需要控制语言规则本身的新颖性。
- **Mechanism / State Ownership / Flow:** benchmark 定义可组合的 Camlang grammar/dictionary，把同一任务分别放入 context-provided 与 tool-access contract；dataset 拥有规则版本、question/answer，tool 或 prompt 提供规则，evaluator 先 exact match 再用 human semantic verification 区分表达错误与推理错误。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** 比较多模型、自然语言/构造语言、context/tool access，分析 grammar category、错误类型以及 exact-match 与 SHV 差异；gold benchmark 上的下降只说明该 evaluator 条件下 unfamiliar-rule adaptation 困难。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 模型、prompt 和 sampling 依论文设置；serving hardware/precision/concurrency/SLO 非本研究结论。证明 controlled novelty 可削弱记忆 shortcut、暴露 rule induction failure；不证明构造语言代表自然语言全分布，也不证明所有模型缺乏 compositional reasoning。
- **Trade-offs / Failure / Previous / Evolution:** contamination resistance 换来生态有效性、human learnability、translation artifact 与 evaluator subjectivity；自然语言 benchmark 仍用于 deployment validity。`Alternative Branch` 于现实任务评测。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`；handoff model representation/tool context；决定 `Refine — Evidence Boundary`，本轮不改 Books。待测规则复杂度、context length 与 tool latency 的 interaction。

### SQL-of-Thought

- **Candidate / Week / Score；Source Family ID；Source Type:** SQL-of-Thought / W35 / 23；`ARXIV-2509.00581`；multi-agent text-to-SQL workflow paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-30，v2 2025-09-28（同 family）；Verified。阅读全文 schema linking、subproblem/plan/SQL generation、taxonomy-guided correction、Spider/Spider-Realistic setup、hardware/config、metrics、unsuccessful ablations、token cost 与 limitations。
- **Original / Previous / Changed:** single-pass SQL generation 在小 schema/简单 query 下延迟低；schema 规模、隐式 join 与语义错误增加后，SQL 即使 syntactically valid、可执行也可能回答错误业务问题，单靠 execution error retry 不足。
- **Mechanism / State Ownership / Flow:** pipeline 依次让 agents 拥有 schema link、subproblem、query plan 与 SQL artifact；DB execution 返回结果/error，guided correction 按 taxonomy 定位 semantic/syntax fault 后改写。schema catalog、plan、SQL、DB state、error trace 和 correction iteration 必须可关联。
- **Implementation / Evaluation Contract / Baselines / Ablations:** Spider 与 Spider-Realistic 上比较既有 text-to-SQL pipelines；作者在 Claude Opus 3 设置报告 execution accuracy 91.59/90.16，并披露 token cost 与失败 ablation。数字不跨模型、schema 或数据库权限设置外推。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 论文提供实验配置但未建立 production concurrency、schema freshness、query cost 与 safety SLO。证明显式 planning + taxonomy correction 可改善该 benchmark 的 executable artifact；不证明 execution success 等同业务语义正确或生产安全。
- **Trade-offs / Failure / Previous / Evolution:** 分工和 correction 提升可诊断性，代价是多 agent token/latency、stale schema、错误归因、benchmark contamination、权限与 destructive query 风险；简单 schema/strict latency 下 direct generation 仍合理。`Layering / Workflow Evolution`。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `AGENT-WORKFLOW`，handoff `AGENT-MULTI-AGENT`/`AGENT-TOOL-CALLING`；决定 `Refine — Existing Argument`，本轮不改 Books。待增加 semantic verifier、read-only transaction、schema-version pin 与 rollback contract。

### LLaVA-Critic-R1

- **Candidate / Week / Score；Source Family ID；Source Type:** LLaVA-Critic-R1 / W35 / 26；`ARXIV-2509.00676`；multimodal critic/RL paper、model artifact。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-31（正文署名日期不覆盖 arXiv first-public owner）；Verified。阅读全文 critic preference data、verifiable RL/GRPO、self-critique/test-time scaling、26 benchmarks、four ablations、extra base-model experiments、case studies 与 limitations。
- **Original / Previous / Changed:** 独立 critic 与 policy 分工清晰，但 critic rationale/judge data 成本高，critic 能力也未必回流 policy；只优化 final answer 又无法训练可复用的 multimodal ranking state。
- **Mechanism / State Ownership / Flow:** 约 40K preference instances 来自 VLFeedback/RLHF/RLHF-V，保留 image、question、two responses、preference label 并移除 GPT rationale/metrics；preference exact-match reward 与 format reward（α=0.9）驱动 GRPO。critic 对候选排序，policy 生成；同一模型可承载两种 role，但 role state 必须在 trace 中分离。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** 以 Qwen2.5-VL-7B 为 base，并从 ThinkLite-VL-7B 构建 R1+；覆盖 26 visual benchmarks。作者报告相对 base 平均 +5.7%，五任务 self-critic +13.8%，以及 Best-of-128，均受候选数、judge、sampling 与 benchmark contract 限制。
- **Hardware / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 训练/评测设置见论文，硬件、precision、online concurrency/SLO 未形成通用 contract。证明 preference labels 可重构为 verifiable critic RL 且 critic/policy 能力可共存；不证明 self-ranking 已校准、不会相关性放大错误，或可替代外部 verifier。
- **Trade-offs / Failure / Previous / Evolution:** 共享模型减少独立 critic 成本，却新增 self-selection bias、correlated error、format gaming、Best-of-N compute 与 role confusion；高风险任务仍应使用独立 verifier/human commit。`Principle Reuse / Role Consolidation`。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-GRPO`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待校准 critic confidence、跨模型 transfer、role isolation 与 verifier disagreement policy。

### SATQuest

- **Candidate / Week / Score；Source Family ID；Source Type:** SATQuest / W35 / 27；`ARXIV-2509.00930`；verifiable reasoning benchmark/training paper、PySAT verifier。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-31，v2 2026-07-19（同 family）；Verified。阅读全文 CNF generation、five problem types、four question formats、evaluation、reinforcement fine-tuning、cross-instance/problem/format generalization、hallucination audit、compute appendix 与 limitations。
- **Original / Previous / Changed:** manually authored logic题易泄漏且数量有限；普通 judge/reward 会把风格与 correctness 混合。要研究 reasoning scaling，需要程序生成、可重放且有 exact solver 的任务族。
- **Mechanism / State Ownership / Flow:** generator 以 CNF/seed 创建 instance，映射为 decision/search 等五类问题和四种信息密度格式；PySAT 生成/验证 ground truth，renderer 产生 narrative，model response 由 correctness/format verifier 评分并进入 RL。instance seed、solver version、rendering 和 reward 都是 evidence identity。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** 比较多模型与 reinforcement fine-tuning，覆盖 instance scale、problem type、question format、generalization 与 hallucination audit；作者发现 verifiable reward 在更难/更大实例更有帮助，但 diagnostic reasoning 与 presentation shift 仍弱。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 模型与 compute 配置在 appendix，production concurrency/SLO 非目标。证明 solver-backed synthetic tasks 可精确隔离部分逻辑 correctness；不证明 SAT 分布代表开放世界推理、语言理解或真实工具可靠性。
- **Trade-offs / Failure / Previous / Evolution:** exact verification 提升 reward correctness，却可能鼓励 solver-specific shortcut、format gaming、distribution overfit 与 generator bug；真实任务/人工题仍提供 ecological validity。`Layering` from benchmark to verifiable training loop。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-GRPO`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待检验 verifier diversity、seed leakage、format robustness 与自然任务 transfer。

### Provable Benefits of In-Tool Learning

- **Candidate / Week / Score；Source Family ID；Source Type:** Provable Benefits of In-Tool Learning / W35 / 25；`ARXIV-2508.20755`；theory、controlled experiment 与 tool-backed factual-learning paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；arXiv HTML/PDF 与 submission history 已核验，后续 revision 不移动 owner。阅读全文 formal problem、in-weight lower bound、in-tool upper bound、synthetic fact construction、model/scale experiments、appendix proofs 与 limitations boundary。
- **Original / Previous / Changed:** 把新事实写入权重能保持无外部依赖的低延迟推理，在知识稳定且训练预算可接受时合理；当事实持续增长、频繁变化并要求精确 recall 时，有限参数容量、干扰和更新成本成为主约束。
- **Mechanism / State Ownership / Flow:** in-weight 路径把 factual mapping 压入参数；in-tool 路径把 key/value 存在外部 database，由模型生成 structured query、tool 读取记录并把结果返回 context。事实版本与记录由 tool store 拥有，模型拥有 query policy 与答案组合；调用、返回值和 source version 必须进入 trace。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** 理论比较两类表示的 sample/capacity requirement；实验覆盖 SmolLM 135M/360M/1.7B、Llama 1B/3B/8B、500～50K synthetic facts，并在至少 95% recall contract 下比较参数学习与数据库查询，学习率等训练设置在正文/appendix 给出。
- **Hardware / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** hardware、precision、production concurrency/SLO 未形成完整公开 contract。证据支持在论文的离散、结构化 factual mapping 下，外部 tool 可避免部分参数容量与干扰成本；不证明所有知识都应外置，也不覆盖模糊 query、检索错误、source conflict、tool latency 或开放世界推理。
- **Trade-offs / Failure / Previous / Evolution:** tool 提供可更新、可审计的事实状态，却引入 availability、schema drift、authorization、stale record、prompt injection、latency 与 provenance failure；低延迟、离线或高稳定知识仍可保留 in-weight。`Alternative Branch / Layering`，不是 RAG/tool 对参数知识的单向替代。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `AGENT-TOOL-CALLING`，handoff `AGENT-CONTEXT`/`PLATFORM-EVALUATION-SYSTEM`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待验证 source/version identity、tool failure abstention 与非结构化事实上的 crossover point。

### Rank-One Safety Injection

- **Candidate / Week / Score；Source Family ID；Source Type:** Rank-One Safety Injection / W35 / 25；`ARXIV-2508.20766`；model-editing safety paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；arXiv HTML/PDF 与 submission history 已核验。阅读全文 activation-direction estimation、rank-one update derivation、layer selection、model/jailbreak experiments、utility evaluation、system-prompt ablation 与 appendix；论文未单列 limitations section，未披露项保持边界。
- **Original / Previous / Changed:** system prompt 或整模 fine-tuning 易部署且能覆盖多类政策，但 prompt 可被绕过，重训练又昂贵并可能破坏 utility；需要一个低成本、可定位、可回退的权重级 intervention。
- **Mechanism / State Ownership / Flow:** 逐层计算 harmful 与 harmless activation mean 的差，选择 safety direction，并以 `W' = W + alpha * s_hat * w_bar^T` 对写入 residual stream 的矩阵施加 rank-one update。base checkpoint、direction data、target layer、alpha 与 edited tensor 共同构成 policy artifact identity；runtime prompt 仍是独立防线。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** 覆盖 Llama、Qwen、Dolphin variants，使用 jailbreak/harmfulness suites 与 Llama Guard 3 judge，并以 MMLU、HellaSwag、ARC 观察 utility；比较 prompt、不同层/强度和攻击条件，但 evaluator、direction dataset 与 operating point 决定结论。
- **Hardware / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 论文目标不是 serving 性能，hardware、precision、batch、concurrency、SLO 未形成通用 contract。证明特定模型/评测上低秩权重更新可提高拒答安全并保留部分 utility；不证明 safety direction 普适、judge 无偏、跨语言/新攻击稳定，或该编辑能替代 policy classifier、sandbox 与 human escalation。
- **Trade-offs / Failure / Previous / Evolution:** 局部编辑便宜且可 diff/rollback，却新增 over-refusal、方向漂移、layer/alpha 敏感、后续 fine-tune 覆盖与隐藏能力未消除等风险；prompt 与完整 alignment 在快速 policy 更新或宽分布覆盖时仍成立。`Layering / Alternative Branch`。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `PLATFORM-SECURITY`，handoff `TRAIN-SFT`/`PLATFORM-EVALUATION-SYSTEM`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待建立多语言/多攻击 operating point、编辑 provenance、升级合并与 rollback contract。

### Mixture of Contexts

- **Candidate / Week / Score；Source Family ID；Source Type:** Mixture of Contexts / W35 / 27；`ARXIV-2508.21058`；long-video diffusion architecture/system paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-28；arXiv HTML/PDF 与 project evidence 已核验，revision 作为同一 family。阅读全文 chunk construction、routing、causal route graph、GPU implementation、training/evaluation、routing/chunk/top-k ablations 与 limitations。
- **Original / Previous / Changed:** 全局 attention 能让远距离 frame 交互且实现简单，但长视频 token 的 quadratic cost 很快不可承受；固定 local window 省算力，却会丢失跨镜头主体/运动依赖并造成 loop closure 或 stalled motion。
- **Mechanism / State Ownership / Flow:** 视频 token 被切成 content-aligned chunks；router 为 query chunk 选择 top-k context chunks，并强制 local 与 cross-modal anchors，随后以 causal route DAG 约束依赖。chunk boundary、route edge、time/modality identity 属 representation state；attention kernel 消费稀疏 route，而不是重新拥有语义关系。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** GPU path 使用 bucketize、prefix sums 与 variable-length attention 组织不规则块；实验比较 dense/local/routed variants，考察 chunk size、top-k、forced link，并在 16×H100 的作者配置上报告质量、长时一致性和约 7× FLOPs 节省。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 16×H100 与论文训练/视频设置可定位，precision、online concurrency/SLO 与端到端 wall-clock contract 不完整。证明 learned sparse context 在作者长视频 workload 可保留关键远距关系并减少理论计算；不证明 FLOPs 等比例变为 latency/成本，也不证明 router 对开放域视频稳定。
- **Trade-offs / Failure / Previous / Evolution:** 稀疏路由用额外 router、index/reorder、load imbalance 和错误边不可逆丢证据换取规模；短视频或规则局部运动下 dense/local attention 仍更简单可靠。`Direct Evolution` from dense/local context to learned sparse route，下一压力是 cache identity、kernel utilization 与 route observability。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MULTIMODAL-WORLD-MODELS`/`INFER-EXECUTION-ENGINE`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待验证 route cache invalidation、hardware-aware capacity 和长 horizon causal error。

### Universal Deep Research

- **Candidate / Week / Score；Source Family ID；Source Type:** Universal Deep Research / W35 / 27；`ARXIV-2509.00244`；agent architecture/prototype paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-29；arXiv HTML/PDF 与公开 prototype/code references 已核验。阅读全文 strategy language、code generation、sandbox、tool contract、persistent variables、yield/notification、examples、evaluation discussion 与 limitations。
- **Original / Previous / Changed:** 自由循环的 LM agent 易于适配探索任务，但长轨迹把 observation、intermediate data 与 control history 全塞入 context，导致成本、丢状态与不可恢复执行；固定 research workflow 可复现，却难表达用户特定策略。
- **Mechanism / State Ownership / Flow:** 用户用自然语言描述策略，系统将其编译为一个受限 generator function；whitelisted control/tool surface 在隔离 sandbox 执行，named variables 保存大量中间状态，LM 仅在局部判断/生成点调用，`yield` 把进度和最终 report 暴露给外部 controller。代码变量拥有 workflow state，tool 拥有外部事实，LM context 不再是唯一状态容器。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** prototype 支持同步工具、循环/分支和持久变量；作者案例显示约 8K context 可完成其任务，但没有足够严格的跨框架、跨模型、并发、成本或故障恢复 benchmark，因此只把机制作为 evidence-ready candidate。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 8K 是作者场景观察，hardware、model matrix、batch、concurrency 与 SLO 未形成可推广 contract。证明 research strategy 可被外化为 inspectable executable state；不证明自动生成代码符合用户真实意图、sandbox 完备或复杂 research 质量优于 agent loop。
- **Trade-offs / Failure / Previous / Evolution:** 外化 control flow 降低 context 压力并提升复现/暂停能力，却新增 code-generation bug、non-termination、unsafe tool composition、strategy drift、sandbox escape 与恢复一致性；探索性强、一次性的小任务仍适合自由 agent loop。`Direct Evolution` from prompt-owned loop to durable executable workflow。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `AGENT-WORKFLOW`，handoff `AGENT-PLATFORM`/`AGENT-TOOL-CALLING`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待定义 strategy-code conformance、effect journal、checkpoint/rollback 与 human override contract。

### Face-MoGLE

- **Candidate / Week / Score；Source Family ID；Source Type:** Mixture of Global and Local Experts with Diffusion Transformer（Face-MoGLE）/ W35 / 22；`ARXIV-2509.00428`；face-generation diffusion architecture paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-30；arXiv HTML/PDF 已核验。阅读全文 semantic-mask processing、global/local experts、gating、DiT backbone、training/evaluation、zero-shot、deepfake detection、component/encoder ablations 与伦理边界；页面中的 placeholder venue/DOI 不作为正式发表事实。
- **Original / Previous / Changed:** 单一 global denoiser 保持整体结构简单，但区域属性难以精确控制；逐区域独立模型能专门化，却破坏全局一致性并放大训练/部署成本。人脸多属性生成要求 global identity 与 local edit 同时成立。
- **Mechanism / State Ownership / Flow:** multi-attribute mask 被拆成 binary regions；full mask 驱动 global expert，各 region 驱动 local experts，gating network 融合 expert contribution 后进入 DiT denoising。mask/region identity 与 gate weight 是 conditioning state，不能只记录最终 prompt。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** MM-CelebA-HQ 约 30K 训练样本，MM-FFHQ-Female 760 个 zero-shot 样本；8×A100 80GB、约 4K steps/12h、28 inference steps，LoRA rank/scaling=4。比较 global-only、local-only、combined、gating variants、zero-shot 与 deepfake detector。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** hardware/steps 可定位，precision、batch、online concurrency/SLO 未完整披露。证明在作者 face dataset/metrics 下 global-local expert fusion 改善多属性控制；不证明机制适用于任意图像域、identity 安全或生产 latency，也不把 detector 结果当成治理充分条件。
- **Trade-offs / Failure / Previous / Evolution:** experts 提升区域专门化，却新增 mask error、gate collapse、expert conflict、区域边界 artifact、额外参数/调度和 deepfake misuse；属性少或全局风格一致时单一 denoiser 仍更合适。`Alternative Branch / Principle Reuse` of conditional capacity。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `MULTIMODAL-GENERATIVE-PARADIGMS`，handoff `MODEL-MOE`/`PLATFORM-SECURITY`；决定 `Refine — Existing Argument`，本轮不改 Books。待验证非人脸域、gate observability、mask uncertainty 与 misuse policy。

### MobiAgent

- **Candidate / Week / Score；Source Family ID；Source Type:** MobiAgent / W35 / 28；`ARXIV-2509.00531`；mobile GUI agent full-stack system paper。
- **Event / Revision；Sources；Access / Full-read:** v1 2025-08-30；arXiv HTML/PDF 与 system artifact references 已核验。阅读全文 MobiMind roles、ActTree/AgentRR、MobiFlow、data pipeline、online/offline evaluation、ablation、latency/replay behavior 与 failure analysis。
- **Original / Previous / Changed:** 逐步 VLM observation-action loop 能处理新 UI，但每一步都重新感知/推理，延迟高且受 app/network 波动；固定脚本快而确定，却在 UI 或任务条件变化后脆弱。重复 mobile tasks 需要在可复用历史和在线恢复之间切换。
- **Mechanism / State Ownership / Flow:** Planner 4B 产出计划、Decider 7B 选择动作、Grounder 3B 定位 UI；成功轨迹进入多层 ActTree。AgentRR 先 embedding retrieve、再 reranker/threshold 决定是否 replay，UI change detector 校验 observation，不确定时回退 live agent；LRU 管理经验，shortcut 可 speculative replay。MobiFlow 以 DAG milestones/conditions 定义任务和验收。
- **Implementation / Evaluation Contract / Baselines / Sensitivity:** MobiFlow 同时提供 offline traces 与 online app runs；前者减少环境方差但可能把 novel successful paths 判为 false negative，后者需人工复核 app/network anomaly。比较模型角色、record/replay、retrieval/rerank 与 acceleration；绝对分数受 app version、账号和网络漂移，作者明确仅供参考。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO；Proves / Does Not:** 公开 4B/7B/3B role scale 与移动端任务设置；hardware、precision、并发和 production SLO 未形成完整 contract。证明成功轨迹的检索重放配合 change detection 可减少部分重复推理；不证明 replay 在长期 UI 演化下安全、跨 app 泛化，或 benchmark 可脱离环境版本比较。
- **Trade-offs / Failure / Previous / Evolution:** replay 降低 latency/token cost，却新增 stale trajectory、false match、错误 shortcut、private state retention、cache poisoning 与恢复分支；新颖或高风险任务仍应走 live perception/reasoning/human confirmation。`Direct Evolution / Layering` from stateless action loop to versioned reusable workflow state。
- **ROADMAP / Adjacent / Existing / Decision / Changes / Open:** owner `AGENT-PLATFORM`，handoff `AGENT-WORKFLOW`/`AGENT-MEMORY`/`PLATFORM-EVALUATION-SYSTEM`；决定 `Integrate — New Mechanism Candidate`，本轮不改 Books。待定义 trajectory provenance、UI-version invalidation、privacy/delete、replay rollback 与 online/offline evaluator reconciliation。


## Low-Score Closure

| Candidate | Primary identity / first-public / revision | Score closure | Verified rejection reason |
| --- | --- | ---: | --- |
| Hermes 4 Technical Report | arXiv:2508.18255；v1 2025-08-25，v2 2025-09-02；report+weights | 19/30 | hybrid reasoning、data curation和评测属于完整模型报告，但公开机制主要组合既有 SFT/RL/data practice；作为 `Weekly Only — Model/Version Fact`，不以 capability benchmark 改写长期系统结论。 |
| Visual-CoG | arXiv:2508.18032；v1 2025-08-25；paper | 19/30 | stage-aware Chain of Guidance 对 autoregressive T2I RL 有实验价值，但证据局限于特定 image generator/reward/evaluator，project relevance不足；保留 `Emerging / Experimental`。 |
| Neither Valid nor Reliable? | arXiv:2508.18076；v1 2025-08-25；position/review paper | 19/30 | 系统性提醒 LLM judge 的 validity、reliability、scalability 假设，但主要是 position synthesis，缺少一个可独立验证的新 evaluator mechanism；作为 evidence caution。 |
| Vision-SR1 | arXiv:2508.19652；v1 2025-08-27；paper | 19/30 | reasoning decomposition + multi-reward RL 是受限 VLM recipe，evaluation 未证明 self-reward 在模型/任务变化后校准；与本周 StepWiser/Pref-GRPO owner重复，不升级。 |
| OneReward | arXiv:2508.21066；v1 2025-08-28；paper | 19/30 | multi-task mask-guided image preference RM整合多个生成任务，但机制/benchmark集中在特定视觉生成域，且 reward-model bias 仍是 owner 风险；保留 experimental case。 |
| R-4B | arXiv:2508.21113；paper v1 2025-08-28，model 2025-08-05 | 19/30 | bi-mode annealing/BPO 让 MLLM auto-think，但本周 paper不是模型首次发布，且与 ThinkDial 的 reasoning-budget family 重叠；只保留 narrow recipe，不重复计分为模型发布。 |
| Model–Task Alignment and RL Conclusions | arXiv:2508.21188；v1 2025-08-28；paper | 19/30 | 指出 reward/noise 结论依赖 base-model/task alignment，是重要实验警告；但样本模型/任务不足以形成通用 RL law，作为 `Weekly Only — Experimental Caveat`。 |
| AHELM | arXiv:2508.21376；v1 2025-08-29；paper+benchmark | 19/30 | audio-language holistic benchmark覆盖面广，但主要增加 domain evaluation matrix；未改变 evaluation-system 的 provenance/commit contract，作为 domain benchmark 保留。 |
| Morae | arXiv:2508.21456；v1 2025-08-29；paper+prototype | 19/30 | proactive pause/user-choice 对UI agent安全有启发，但技术与用户研究规模不足以给出通用 pause policy或生产SLO；保留 interaction study，不外推。 |
| USO | arXiv:2508.18966；v1 2025-08-26，后续 revision 同 family；paper+code/model | 19/30 | 以 200K stylized pairs、content/style encoders、alignment/disentanglement 与 reward learning 组合提升 style-content control，但证据集中在特定 image-style 数据和 evaluator；不把受限生成 recipe 外推为通用 multimodal representation law，保留 `Emerging / Experimental`。 |
| TCIA | arXiv:2508.20374；v1 2025-08-28；primary identity+abstract | 19/30 | 可核验材料支持用离散 query constraints 做 task-centric instruction augmentation，并报告四个 task-specific application 的作者实验；全文机制/ablation contract 本轮不可从 HTML 取得，且 narrow recipe 不改变通用 data pipeline owner，保留 `Weekly Only — Narrow Data Recipe`。 |
| OnGoal | arXiv:2508.21061；v1 2025-08-28；UIST paper+prototype | 19/30 | goal inference/merge/evaluation 与可视化为人机协作提供交互案例，但 20 人 writing-task study 没有 expert-annotated correctness，参与者也会反对 LLM goal judgement；不能推出通用 context policy，保留 `Weekly Only — Interaction Study`。 |
| C-DiffDet+ | arXiv:2509.00578；v1 2025-08-30；paper | 19/30 | global context encoder、ACE 与 context-aware cross-attention 改善特定车辆损伤 diffusion detector，并有组件/encoder ablation；CarDD/VehiDE 的窄域检测结果不建立通用生成范式结论，且 irregular/diffuse damage 与标注一致性仍受限，保留 `Weekly Only — Domain Detection Case`。 |

## Evidence Level

- **L1 Official:** Kubernetes release、API、KEP 与代码定义公开 feature state；不证明特定 driver 或 AI workload 的性能。
- **L2 Primary Research:** arXiv paper、technical report、model card、code/artifact 是作者证据；benchmark 结论只在其 evaluation contract 内成立。
- **L3 Cross-source inference:** 本 Weekly 的演进链、ROADMAP owner 与共存边界是项目分析，已与 primary fact 分开。
- 本周不存在仅靠新闻转载、搜索摘要或社区观点保留的候选。

## Cross-Week Deduplication

- TPLA `2508.15881` 的 v1 是 **2025-08-21**（v2 才是 8 月 25 日）；`2508.16153` 的 v1 是 **2025-08-22**，event-time title 为 AgentFly，当前 revision title 为 **Memento: Fine-tuning LLM Agents without Fine-tuning LLMs**。两者都属于 W34；本周不重复计分，并把 revision-date/title identity 修复事实回传年度 owner。
- W36 replay 发现 `2508.21496`、`2509.00375`、`2509.00404`、`2509.00425`、`2509.00581`、`2509.00676`、`2509.00930` 的 v1 分别落在 8 月 29～31 日；7 个 family 已回拨 W35 完成评分和 Full Source Review，W36 不再重复计分。
- W36 denominator stabilization 又识别 `2509.00244`、`2509.00428`、`2509.00531`、`2509.00578` 的 v1 落在 8 月 29～30 日；前三项在 W35 完成 Full Source Review，C-DiffDet+ 完成低分 closure，W36 只保留 spillback 路由而不计分。
- 8 月 29 日 recommendation feed 与 8 月 29～31 日 submission history 的回查另恢复 `2508.18966`、`2508.20374`、`2508.20755`、`2508.20766`、`2508.21058`、`2508.21061`；它们均按 arXiv v1 归 W35，而不是按推荐日期另建 W36 owner。
- Persuasion Dynamics `2508.17450` 的 v1 是 2025-08-24，属于 W34；本周仅记录路由，不评分。
- InternVL3.5、MMTok 等后续 revision 仍归 v1 week；修订用于补充机制/实验，不产生新评分行。
- R-4B 模型曾在 8 月 5 日发布，W35 只记录 8 月 28 日 technical paper event；由于未形成独立长期 owner，低分 closure。
- Kubernetes 9 月 1 日 DRA GA 深度文、9 月 17 日 health、9 月 18 日 consumable capacity 与 W35 release 同属 `K8S-1.34-DRA`；W36/W38 只记录后续证据角色。
- 相邻 W34/W36 未发现本周 53 个 primary identifier 的重复评分 owner；同 family 的 artifact/model card 不另计分。

## Knowledge Tree Position

- Multimodal → `MULTIMODAL-REPRESENTATION`、`MULTIMODAL-GENERATIVE-PARADIGMS`、`MULTIMODAL-EMBODIED-VLA`。
- Data/RL/reasoning → `TRAIN-DATA`、`TRAIN-RLHF`、`TRAIN-GRPO`、`MODEL-MOE`、`MODEL-LONG-CONTEXT`。
- Inference/platform → `INFER-SCHEDULING`、`PLATFORM-GPU-SCHEDULER`、`PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY`。
- Agent → `AGENT-CONTEXT`、`AGENT-TOOL-CALLING`、`AGENT-REFLECTION`、`AGENT-WORKFLOW`、`AGENT-MEMORY`、`AGENT-MCP`、`AGENT-PLATFORM`。

## Recommended Action

- 40 个 retained family：Weekly evidence ready；等待跨周 Historical Books Gate，不提前修改 Books。
- 13 个低分 family：保留为版本事实、domain case、interaction study 或 evidence caution；除非新 revision 提供可改变长期设计结论的机制/复现证据，否则不升级。
- Kubernetes DRA、Taming the Chaos、CTF-Dojo/A.S.E、MCP-Bench/AWorld 优先进入未来 Books owner review，因为它们改变 state ownership 或 evaluation contract，而不是只增加 capability score。

## Event-Date Daily Decision

Historical Backfill 不补造 Daily；全部事件日期、revision 与 evidence packet 直接记录在本 Weekly。

## Books Integration Decision

`Historical Books Gate Closed`。本轮没有修改 `books/`；`Integrate/Refine Candidate` 仅表示 evidence-ready disposition，不表示已经写入长期正文。

## Ignored Noise

- 去除旧论文重发、榜单、转载、无 primary identifier 的产品宣传和无法绑定 workload contract 的性能比较。
- 同一 arXiv family 的 model card、project page、code repository 与 revision 不重复计分。
- 只提供单一 benchmark 增量、且机制与当前 owner 重复的 domain paper，在 discovery ledger 核验后不进入评分表；这不是静默遗漏，而是 relevance/dedup rejection。

## Repository Changes

- 仅重建 `papers/2025/weekly/2025-W35/README.md`。
- 未修改年度索引、Daily、Books、ROADMAP、DECISIONS 或 Learning State；未 stage、commit 或 push。

## Open Questions

- visual-token router 的 decision trace 是否应进入 cache identity，发生 compression policy 升级时如何 invalidation？
- tool-integrated RL 如何同时约束 call benefit、execution cost、security policy 与 non-deterministic environment？
- disaggregated autoscaling 在 telemetry delay、cold start 与 heterogeneous replica 下如何证明控制稳定性？
- DRA driver 的 ResourceSlice freshness、claim recovery、scheduler scale 与 upgrade skew 需要怎样的 conformance suite？
- live benchmark 如何同时冻结 evaluator contract、避免 contamination，又允许答案随时间被验证和 supersede？
- FP4 training 的 spectral/projection state 如何与 optimizer、checkpoint resume 和 kernel version 一起形成可复现 artifact？
- synthetic deep-research tree 如何冻结网页 provenance、generator/judge version，并检测 constraint shortcut 与 source drift？
- critic 与 policy 共用模型时，如何隔离 role state、校准 self-ranking，并在 verifier disagreement 时拒绝 commit？
- solver-verifiable task 上学到的 policy 如何验证对自然语言、开放世界工具和非 exact reward 的迁移边界？
- strategy-to-code compiler 如何证明生成 workflow 符合用户意图，并在 sandbox effect 已发生后安全 checkpoint/rollback？
- mobile-agent trajectory replay 如何绑定 app/UI version、账号权限和 private state，并在 stale match 时快速回退 live policy？
- sparse video context route 如何进入 cache identity，且如何把理论 FLOPs 节省转化为真实 kernel utilization 与 latency？
- rank-one safety edit 的 layer/alpha operating point 如何跨语言、攻击与后续 fine-tune 保持可审计，何时必须 rollback？
- in-tool factual state 如何绑定 source/version/authorization，并在 tool unavailable、冲突或 stale 时触发 abstention？

## Independent Review Checkpoint

- **Denominator / score Total:** 独立重读 Candidate Scoring；53 行、53 个唯一 family，六维复算为 `28 high + 12 mid + 13 low`，Total mismatch = 0。
- **Full Source Review:** 独立统计 `40/40` retained headings；每项均覆盖 first-public/revision、问题与旧方案、约束变化、机制、state owner、control/data flow、implementation、evaluation contract、证明/未证明、trade-off、旧方案边界、ROADMAP owner 与 disposition。
- **Low-score closure:** `13/13` 均有 primary identity、v1 日期、score 与非模板化拒绝理由；不存在只写“相关性不足”的泛化 closure。
- **Date / revision / spillback:** ISO window 与 53 个 owner date 复核通过；TPLA v1=8/21、`2508.16153` v1=8/22 且 AgentFly→Memento title revision 已明确路由 W34；两轮 W36 spillback 的 11 个 8/29～8/31 owner 已回拨 W35；feed 回查另恢复 6 个 v1 位于 W35 的 family；Persuasion Dynamics v1=8/24 路由 W34；Kubernetes 9 月 follow-up 未回拨计分。
- **Dedup / owner:** Candidate table family ID 无重复；本周 53 个 primary identifier 在相邻 W34/W36 无重复评分；所有 Stable Node ID 均可在 ROADMAP 解析。
- **Fact boundary:** 作者 benchmark 均绑定对应模型/任务/harness；未披露 hardware、precision、batch、concurrency、SLO 未被推断；官方 DRA GA 与 alpha/beta extension 分开。
- **Markdown / mechanical checks:** heading hierarchy、table row、URL/source line、围栏偶数、placeholder、行尾空白检查通过；`git diff --check -- papers/2025/weekly/2025-W35/README.md` 通过。
- **Git scope:** 本检查点只修改 W35 README，未执行 stage、unstage、commit、push 或 reset，也未改动年度索引/Books/Learning State；共享工作树中该文件已有 cached baseline，本轮 second reclosure 保持为 unstaged delta，未覆盖其边界。

## Gate Status

- ISO Coverage / date ownership: **Pass**。
- Fixed-source discovery replay: **Pass**（明确保留 Scholar/OpenAlex 非全量覆盖 limitation）。
- Scoring reconciliation: **53/53 Pass**。
- Full Source Review: **40/40 retained Pass**。
- Low-score closure: **13/13 Pass**。
- Ordinary Review Pending: **0**。
- Unverified / Blocked / Disputed: **0**。
- Cross-week dedup / spillback: **Pass**。
- Weekly Evidence Gate: **Complete**。
- Historical Books Gate: **Closed by design**。

## Sources

- Hugging Face Daily Papers discovery feed — https://huggingface.co/papers/date/2025-08-29（Discovery only；Accessed: 2026-08-24；8 月 30～31 日页面不可用）
- Persuasion Dynamics in Multi-Agent Systems — https://arxiv.org/abs/2508.17450（First Public: 2025-08-24；W34 spillback only；Accessed: 2026-08-24）
- InternVL3.5 — https://arxiv.org/abs/2508.18265；https://github.com/OpenGVLab/InternVL（First Public: 2025-08-25；Accessed: 2026-08-24）
- Hermes 4 Technical Report — https://arxiv.org/abs/2508.18255（First Public: 2025-08-25；Accessed: 2026-08-24）
- Visual-CoG — https://arxiv.org/abs/2508.18032（First Public: 2025-08-25；Accessed: 2026-08-24）
- MMTok — https://arxiv.org/abs/2508.18264（First Public: 2025-08-25；Accessed: 2026-08-24）
- UQ — https://arxiv.org/abs/2508.17580；https://uq.stanford.edu/（First Public: 2025-08-25；Accessed: 2026-08-24）
- Neither Valid nor Reliable? — https://arxiv.org/abs/2508.18076（First Public: 2025-08-25；Accessed: 2026-08-24）
- CTF-Dojo — https://arxiv.org/abs/2508.18370（First Public: 2025-08-25；Accessed: 2026-08-24）
- A.S.E — https://arxiv.org/abs/2508.18106（First Public: 2025-08-25；Accessed: 2026-08-24）
- TiKMiX — https://arxiv.org/abs/2508.17677（First Public: 2025-08-25；Accessed: 2026-08-24）
- VibeVoice — https://arxiv.org/abs/2508.19205（First Public: 2025-08-26；Accessed: 2026-08-24）
- Understanding Tool-Integrated Reasoning — https://arxiv.org/abs/2508.19201（First Public: 2025-08-26；Accessed: 2026-08-24）
- UltraMemV2 — https://arxiv.org/abs/2508.18756（First Public: 2025-08-26；Accessed: 2026-08-24）
- ThinkDial — https://arxiv.org/abs/2508.18773（First Public: 2025-08-26；Accessed: 2026-08-24）
- Optimal MoE Sparsity — https://arxiv.org/abs/2508.18672（First Public: 2025-08-26；Accessed: 2026-08-24）
- StepWiser — https://arxiv.org/abs/2508.19229（First Public: 2025-08-26；Accessed: 2026-08-24）
- Vision-SR1 — https://arxiv.org/abs/2508.19652（First Public: 2025-08-27；Accessed: 2026-08-24）
- CODA — https://arxiv.org/abs/2508.20096（First Public: 2025-08-27；Accessed: 2026-08-24）
- Analysing Chain of Thought Dynamics — https://arxiv.org/abs/2508.19827（First Public: 2025-08-27；Accessed: 2026-08-24）
- Discrete Diffusion VLA — https://arxiv.org/abs/2508.20072（First Public: 2025-08-27；Accessed: 2026-08-24）
- Diffusion LMs Know the Answer Before Decoding — https://arxiv.org/abs/2508.19982（First Public: 2025-08-27；Accessed: 2026-08-24）
- Mind the Third Eye — https://arxiv.org/abs/2508.19493（First Public: 2025-08-27；Accessed: 2026-08-24）
- DeepScholar-Bench — https://arxiv.org/abs/2508.20033（First Public: 2025-08-27；Accessed: 2026-08-24）
- Taming the Chaos — https://arxiv.org/abs/2508.19559（First Public: 2025-08-27；Accessed: 2026-08-24）
- Kubernetes v1.34 release — https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/（First Public: 2025-08-27；Accessed: 2026-08-24）
- Kubernetes DRA GA follow-up — https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/（Related Revision Node: 2025-09-01；Accessed: 2026-08-24）
- Kubernetes DRA KEP-4381 — https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/4381-dra-structured-parameters（Accessed: 2026-08-24）
- rStar2-Agent — https://arxiv.org/abs/2508.20722（First Public: 2025-08-28；Accessed: 2026-08-24）
- Pref-GRPO — https://arxiv.org/abs/2508.20751（First Public: 2025-08-28；Accessed: 2026-08-24）
- MCP-Bench — https://arxiv.org/abs/2508.20453（First Public: 2025-08-28；Accessed: 2026-08-24）
- AWorld — https://arxiv.org/abs/2508.20404（First Public: 2025-08-28；Accessed: 2026-08-24）
- OneReward — https://arxiv.org/abs/2508.21066（First Public: 2025-08-28；Accessed: 2026-08-24）
- CogVLA — https://arxiv.org/abs/2508.21046（First Public: 2025-08-28；Accessed: 2026-08-24）
- R-4B — https://arxiv.org/abs/2508.21113（Paper First Public: 2025-08-28；Accessed: 2026-08-24）
- EO-1 — https://arxiv.org/abs/2508.21112（First Public: 2025-08-28；Accessed: 2026-08-24）
- Model–Task Alignment and RL Conclusions — https://arxiv.org/abs/2508.21188（First Public: 2025-08-28；Accessed: 2026-08-24）
- UItron — https://arxiv.org/abs/2508.21767（First Public: 2025-08-29；Accessed: 2026-08-24）
- AHELM — https://arxiv.org/abs/2508.21376（First Public: 2025-08-29；Accessed: 2026-08-24）
- Morae — https://arxiv.org/abs/2508.21456（First Public: 2025-08-29；Accessed: 2026-08-24）
- ELV-Halluc — https://arxiv.org/abs/2508.21496；https://arxiv.org/html/2508.21496（First Public: 2025-08-29；Accessed: 2026-08-24）
- Open Data Synthesis for Deep Research — https://arxiv.org/abs/2509.00375；https://arxiv.org/html/2509.00375（First Public: 2025-08-30；Accessed: 2026-08-24）
- Metis — https://arxiv.org/abs/2509.00404；https://arxiv.org/html/2509.00404（First Public: 2025-08-30；Accessed: 2026-08-24）
- Camlang — https://arxiv.org/abs/2509.00425；https://arxiv.org/html/2509.00425（First Public: 2025-08-30；Accessed: 2026-08-24）
- SQL-of-Thought — https://arxiv.org/abs/2509.00581；https://arxiv.org/html/2509.00581（First Public: 2025-08-30；Accessed: 2026-08-24）
- LLaVA-Critic-R1 — https://arxiv.org/abs/2509.00676；https://arxiv.org/html/2509.00676（First Public: 2025-08-31；Accessed: 2026-08-24）
- SATQuest — https://arxiv.org/abs/2509.00930；https://arxiv.org/html/2509.00930（First Public: 2025-08-31；Accessed: 2026-08-24）
- USO — https://arxiv.org/abs/2508.18966；https://arxiv.org/html/2508.18966（First Public: 2025-08-26；Accessed: 2026-08-24）
- TCIA — https://arxiv.org/abs/2508.20374；https://huggingface.co/papers/2508.20374（First Public: 2025-08-28；Accessed: 2026-08-24；HTML full text unavailable）
- Provable Benefits of In-Tool Learning — https://arxiv.org/abs/2508.20755；https://arxiv.org/html/2508.20755（First Public: 2025-08-28；Accessed: 2026-08-24）
- Rank-One Safety Injection — https://arxiv.org/abs/2508.20766；https://arxiv.org/html/2508.20766（First Public: 2025-08-28；Accessed: 2026-08-24）
- Mixture of Contexts — https://arxiv.org/abs/2508.21058；https://arxiv.org/html/2508.21058（First Public: 2025-08-28；Accessed: 2026-08-24）
- OnGoal — https://arxiv.org/abs/2508.21061；https://arxiv.org/html/2508.21061（First Public: 2025-08-28；Accessed: 2026-08-24）
- Universal Deep Research — https://arxiv.org/abs/2509.00244；https://arxiv.org/html/2509.00244（First Public: 2025-08-29；Accessed: 2026-08-24）
- Face-MoGLE — https://arxiv.org/abs/2509.00428；https://arxiv.org/html/2509.00428（First Public: 2025-08-30；Accessed: 2026-08-24）
- MobiAgent — https://arxiv.org/abs/2509.00531；https://arxiv.org/html/2509.00531（First Public: 2025-08-30；Accessed: 2026-08-24）
- C-DiffDet+ — https://arxiv.org/abs/2509.00578；https://arxiv.org/html/2509.00578（First Public: 2025-08-30；Accessed: 2026-08-24）
