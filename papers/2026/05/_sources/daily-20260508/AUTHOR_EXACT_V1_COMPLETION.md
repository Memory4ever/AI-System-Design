# 2026-05-08 作者侧 exact-v1 完成记录

**范围：** 原 `Review Pending` 的 24 个 source family

**作者侧状态：** 24/24 已审阅；20 项深入审阅，4 项标准审阅；材料受阻 0；待非作者 final review

**统一账本：** `V3_RECERTIFICATION.json` 的 619 个 `items` 是本日报唯一 denominator ledger；本文只保存这 24 项的证据与 Books 判断，不另建候选分母。

## 2605.05697 — Budgeted Attention Allocation

- **Primary：** `arXiv:2605.05697v1`；[exact-v1 HTML](https://arxiv.org/html/2605.05697v1)。
- **机制：** §3 训练 budget-conditioned、单调的 layer/head gate，以 soft cost regularization 学习多预算 operating point；部署时转为 hard top-k mask，必要时从 dense warm start 做 hard-gate adaptation。
- **评价：** §5–6 覆盖 synthetic task、AG News/DBpedia 子集、BERT-Tiny/BERT-Mini 与 DistilBERT pilot；仅有限 CPU/GPU hard-gate latency，主要 cost 仍为估算。
- **未证明：** §9 明确 soft gate cost 不等于 wall-clock；A100 eager execution 不自动加速，数据、seed 与模型规模有限，dense warm start 还增加训练成本。
- **评分与 Books：** `3+2+2=7`，深入完成。建议 `Integrate → MODEL-SELF-ATTENTION`：补入“单 checkpoint 的请求预算→head compute gate”分支，并把 runtime SLO commit 交接给 `INFER-SCHEDULING`；旧 dense attention 在预算稳定或缺专用执行支持时保留。

## 2605.05701 — Inference-Time Budget Control for LLM Search Agents

- **Primary：** `arXiv:2605.05701v1`；[exact-v1 HTML](https://arxiv.org/html/2605.05701v1)。
- **机制：** §4 先由 task-level VOI controller 在 Search/Decompose/Answer 间分配 tool/token budget，再由保守 finalizer 只修复 typed answer-form 错误；budget penalty、value-per-cost 与 deterministic guard 共同约束动作。
- **评价：** §5 使用 Qwen3-32B、Qwen3.5-122B 与 GPT-5.4-Mini，在 HotpotQA、2Wiki、MuSiQue、Bamboogle 的硬预算下比较多种 search controller；高预算并不单调占优，BATS 在部分格点仍有竞争力。
- **未证明：** §6 说明 controller 不能修复错误 retrieval 或 unresolved bridge，且 backbone、预算与任务改变会改变收益。
- **评分与 Books：** `2+2+2=6`，标准完成。`No Change — Existing Coverage → AGENT-PLANNING`：现有章节已把 act/ask/verify/stop 作为 information-value、opportunity-cost、hard cap 与 verification reserve 的预算决策；本论文是受限实例，不新增 owner。

## 2605.05802 — Selective Rollout

- **Primary：** `arXiv:2605.05802v1`；[exact-v1 HTML](https://arxiv.org/html/2605.05802v1)。
- **机制：** §3 在固定 prefix 长度 `K=10` 比较组内轨迹 edit divergence；低 divergence 组在 rollout 中途终止，位于 pre-rollout filtering 与 post-rollout filtering 之间，直接改变 trajectory lifecycle。
- **评价：** §3.1、§4–5 使用 ALFWorld、Qwen2.5-7B-Instruct、group size 8、horizon 30，并做 rollout-only、off-policy 与 on-policy 三层验证；低 divergence 可捕获部分 all-success/all-fail 组，但对 high-divergence all-fail 无能为力，online 改善是方向性而非显著性定论。
- **未证明：** 固定模型、环境、`K` 与少量 seed 不证明跨任务最优 gate；错误早停会删掉稀有学习信号，gate 必须与 policy revision 和完整组身份绑定。
- **评分与 Books：** `3+2+2=7`，深入完成。建议 `Integrate → TRAIN-GRPO`：补入“mid-rollout informativeness gate”，由 rollout controller 提议早停、group builder 冻结 membership、optimizer 只消费完整同版本组；无法校准 precision 时回退完整 rollout。

## 2605.05899 — VisMMOE

- **Primary：** `arXiv:2605.05899v1`；[exact-v1 HTML](https://arxiv.org/html/2605.05899v1)。
- **机制：** §3 先压缩 visual tokens 以缩小 expert working set，再用 compression-guided lookahead predictor 驱动 dynamic expert cache 与异步 CPU→GPU prefetch；miss 时仍由 CPU fallback 执行真实 expert。
- **评价：** §4 在 Qwen3-VL-30B-A3B、DeepSeek-VL2 与 A100-40GB、RTX3090-24GB、Jetson Orin 32GB 上报告 MME/OCRBench/POPE/MMBench 质量及 prefill/decode 时间，并给出 compressor、predictor、cache 的消融。
- **未证明：** 结果绑定两类 VL-MoE、特定 offload runtime 与硬件；Orin 路径使用 OS swap，未证明生产并发、tail SLO 或任意 modality/router 分布收益。
- **评分与 Books：** `3+3+2=8`，深入完成。建议 `Integrate → INFER-TENSORRT-LLM`：补入 modality compression 改变 expert working-set 与 prefetch plan 的跨层分支；router 保留 expert 真值，cache 只拥有 placement hint，错预测回退 authoritative execution。

## 2605.06053 — Generation-Efficient Uncertainty

- **Primary：** `arXiv:2605.06053v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06053v1)。
- **机制：** §4.1 用 partial generation 的 Logit Magnitude 配合 early stop/top-M 估计不确定性；§4.2 用冻结 encoder 与 MLP 从输入预测由 Logit Magnitude 产生的 pseudo-label，把观测时点前移到生成前。
- **评价：** §5 在 CoQA、NewsQA、emrQA 与 Qwen/Gemma/Llama family 上比较 AUROC、AURAC、balanced accuracy 和生成 token 数；主要硬件是 RTX 6000 Ada 48GB，较大配置用 96GB。
- **未证明：** §6/附录只覆盖开放式 QA；Llama3-emrQA 出现 calibration failure，长文生成、domain shift 与生产 abstention SLO 未被充分验证。
- **评分与 Books：** `2+2+2=6`，标准完成。`No Change — Existing Coverage → PLATFORM-EVALUATION-SYSTEM`：现有章节已把 uncertainty estimator 的 access contract、calibration slice、coverage/release gate 与成本分开；该方法仅提供两个新 estimator 实例。

## 2605.06067 — Normalized Architectures are Natively 4-Bit

- **Primary：** `arXiv:2605.06067v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06067v1)。
- **机制：** §3–4 将 hypersphere-normalized geometry 的 constructive signal accumulation 与量化 SNR、较平坦 loss landscape 联系起来，使 NVFP4 end-to-end training 可省去随机 Hadamard 与逐 tensor scaling；这是 architecture–precision 共设计，而非普通 PTQ。
- **评价：** §5/Appendix C 覆盖 1.2B dense 1T tokens、hybrid Mamba-Transformer MoE 400M/600M 与 3B/30B 500B tokens，并在 Blackwell 上报告学习率鲁棒性和加速。
- **未证明：** Appendix E 说明主分析集中在较小模型/宽度，3B/30B 训练 horizon 远短于超大规模生产训练；正相关来源仍未完全解释。
- **评分与 Books：** `3+3+3=9`，深入完成。建议 `Integrate → TRAIN-PRETRAINING`：加入 normalized geometry 作为低比特训练的结构分支，绑定 exact architecture、precision、optimizer 与硬件；标准 BF16/FP8 在稳定性或 kernel 支持不足时继续成立。

## 2605.06116 — Policy-Guided Stepwise Model Routing

- **Primary：** `arXiv:2605.06116v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06116v1)。
- **机制：** §3–4 将每个 reasoning step 的模型选择写成 CMDP，用 V-trace、trust-region constrained policy learning 与联合阈值校准控制成本/相对正确性；verifier 只在训练中提供信号。
- **评价：** §5 在 GSM8K、MATH500、OmniMath 上比较 Qwen2.5 Math 小/大模型与 Qwen→GPT-4.1-mini，开放模型路由较稳定，跨 API 路径受 top-logprob 与格式限制且未报告直接 latency。
- **未证明：** 证据限数学推理与所列模型；confidence proxy、API 可见性和阈值都可能漂移，未证明跨域或生产 SLO。
- **评分与 Books：** `3+2+2=7`，深入完成。`No Change — Existing Coverage → INFER-SCHEDULING`：现有章节已覆盖按步骤/阶段的多模型选择、能力 profile、成本/SLO 与保守 fallback；该 family 不改变 owner。

## 2605.06125 — TEBench

- **Primary：** `arXiv:2605.06125v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06125v1)。
- **机制：** §1–2 将 project-level test evolution 分为 breaking、stale、missing 三态；测试能运行只证明 breaking 被修复，不能证明需求变化后的语义 coverage 仍存在。
- **评价：** §2–4 构造 314 个实例、10 个 Java/Defects4J 项目和七种 Agent 配置，分别测 identification 与 update；stale/missing 是主要盲点。
- **未证明：** §6 指出 developer patch 不是唯一正确 test evolution，项目/语言范围有限，coverage overlap 只是 construct proxy。
- **评分与 Books：** `3+2+2=7`，深入完成。建议 `Integrate → PLATFORM-EVALUATION-SYSTEM`：把“测试通过”拆为 executable、freshness、requirement coverage 三个证据对象，并在需求/代码 revision 变化时重新绑定 test-suite identity。

## 2605.06158 — Stateful Agent Backdoor

- **Primary：** `arXiv:2605.06158v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06158v1)。
- **机制：** §3–4 将持久读写组件作为跨 session key-value state，用 Mealy machine 把攻击分解成多个单次看似无害的 sub-backdoor transition。
- **评价：** §5 覆盖四个模型、四类工具、1000 trajectories、五会话 episode，并检查主链、branch-and-merge 与 note-based 变体。
- **未证明：** §6.4 依赖共享 R/W channel、跨会话可见性与训练成功；容量、拓扑和 cascade attenuation 会限制攻击，不证明所有持久 Agent 都可同样后门化。
- **评分与 Books：** `3+3+3=9`，深入完成。`No Change — Existing Coverage → PLATFORM-SECURITY`：现有“durable control cell / harness backdoor”已经要求跨 run 保存 writer、provenance、digest、trigger lineage 与 mutation gate；Mealy-machine 攻击是该命题的受限实例。

## 2605.06205 — ClawGuard

- **Primary：** `arXiv:2605.06205v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06205v1)。
- **机制：** §V 用 host 外 SDR 采集 EM 与 temperature side channel，先粗粒度识别 workload、再细粒度恢复 skill sequence，形成不依赖被监控 host telemetry 的 evidence plane。
- **评价：** §VI 在 laptop/Raspberry Pi、16 benign 与 22 attack skills 上做 prototype、LOCO CV、robustness/transfer/cost；主语料 12,232 records/7.82TB。
- **未证明：** §VIII 显示 flat 16-class macro-F1 很低，近似资源模式、adaptive mimicking、短攻击、DVFS 和设备/日期漂移均会失效；只证明单设备 feasibility。
- **评分与 Books：** `2+2+2=6`，标准完成。`No Change — Existing Coverage → PLATFORM-SECURITY`：现有章节已要求 security evidence plane 独立于被测主体，并明确 side-channel/threat-model 边界；EM 是昂贵且特定的观测实现。

## 2605.06206 — Federation of Experts

- **Primary：** `arXiv:2605.06206v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06206v1)。
- **机制：** §3 按独立 expert/KV-head group 重构每层，使全局 all-to-all 变为 group 内 all-to-all 与 group 间 all-reduce；这是模型架构改变通信图，而非仅改变 placement。
- **评价：** §4 在 1B/7B、单节点 8×H100 与双节点 InfiniBand、FlexServe/LongBench Poisson workload 下测 forward、TTFT、TBT、负载和生成质量。
- **未证明：** §5 说明单 GPU 只有新增 all-reduce、无收益；证据依赖同构拓扑、需要重新训练，未覆盖更大模型、异构 fabric 与长期质量。
- **评分与 Books：** `3+3+3=9`，深入完成。建议 `Integrate → MODEL-MOE`，handoff `INFER-TENSORRT-LLM`：加入“改变 expert ownership 以替换 collective”的 architecture branch，并保留标准 EP 在单卡、强层级专业化或 all-reduce 更贵时的边界。

## 2605.06279 — Correct Code, Vulnerable Dependencies

- **Primary：** `arXiv:2605.06279v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06279v1)。
- **机制：** §3–4 把模型生成的 dependency version pin 单独送入 OSV、隔离 uv environment、static typing 与动态 tests；代码正确与 dependency 安全/兼容被拆成不同 admission evidence。
- **评价：** §4–6 覆盖 10 个 LLM、1000 PinTrace tasks 和 BigCodeBench 子集，比较 prompt mode、漏洞暴露、版本兼容与 mitigation probe。
- **未证明：** §8 限于 PyPI/Python 与固定时间锚点，provider 默认参数和 cutoff 部分为推断；measurement 不证明所有模型存在同一因果偏差。
- **评分与 Books：** `2+3+3=8`，深入完成。`No Change — Existing Coverage → PLATFORM-SECURITY`：现有章节已经要求 SBOM/AIBOM、依赖 version、漏洞状态、runtime activation 与 release mutation 共同进入 artifact admission；无需为本测量另写机制。

## 2605.06339 — Controller Class Selection

- **Primary：** `arXiv:2605.06339v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06339v1)。
- **机制：** §2 在 fixed、partition、instance 与 prior-gated controller class 间做有限样本选择，并用 residual mass、样本数和 partition geometry 判断复杂 router 是否可辨识。
- **评价：** §3/Appendix C–E 在 SMS Spam、HallusionBench、A-OKVQA、FOLIO 与受控 synthetic setting 中做 nested cross-validation；TextVQA 的 prior gate 另作补充。
- **未证明：** Appendix A 说明结论依赖 action/loss/features/judge；gold rationale branch 不可部署，单一 judge 与少量 benchmark 不证明通用 class boundary。
- **评分与 Books：** `2+2+2=6`，标准完成。`No Change — Existing Coverage → INFER-SCHEDULING`：现有章节已要求 router complexity 由可观测 signal、校准样本、gain certificate 与保守固定模型 fallback 决定。

## 2605.06350 — LLM Cascades

- **Primary：** `arXiv:2605.06350v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06350v1)。
- **机制：** §3–5 推导 k-model threshold cascade 的累计 cost/quality、pairwise envelope、shadow price 与 marginal quality-per-cost；cascade 必须先支付廉价模型成本，而 pre-generation router 可直接选择强模型。
- **评价：** §6 用八个模型、五家 provider 和 MMLU、TriviaQA、MATH、SimpleQA、LiveCodeBench，做 50 个 calibration/test split；learned pre-generation router 在 4/5 数据集更优，TriviaQA 是反例。
- **未证明：** 只覆盖 deterministic threshold cascade、所列 pool 与 token price；没有 latency、长输出和丰富 hybrid router 结论，不能宣称 cascade 普遍劣于 router。
- **评分与 Books：** `3+3+3=9`，深入完成。建议 `Integrate → INFER-SCHEDULING`：明确区分“回答后升级的 cascade”与“生成前 routing”的结构成本，只有被升级路径的边际质量超过已支付成本和未来预算才升级；高不确定/低可预测任务仍保留 cascade。

## 2605.06388 — Robotic World-Model Latent Space

- **Primary：** `arXiv:2605.06388v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06388v1)。
- **机制：** §2–5 在 action-conditioned latent diffusion 中分离 reconstruction-aligned 与 semantic encoder，并分别检验 action recoverability、task semantics、visual fidelity、planning 与 policy-in-world-model。
- **评价：** §3–4 使用 Bridge V2、CEM planning、OpenVLA 固定 policy、inverse dynamics、success classifier 与 VLM consensus；不同 latent 在视觉和 policy relevance 上排序不同。
- **未证明：** §7 限于单 embodiment/Bridge V2，固定 policy evaluation 不是 policy improvement 或 sim-to-real，VLM judge 也可能偏置。
- **评分与 Books：** `3+2+3=8`，深入完成。`No Change — Existing Coverage → MULTIMODAL-WORLD-MODELS`：现有章节已明确 video realism、predictive state、controllability 与 policy-relevant evaluation 不能互相替代；该 family 强化而未改变这条主线。

## 2605.06402 — SparseForge

- **Primary：** `arXiv:2605.06402v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06402v1)。
- **机制：** §4 联合优化 weights 与 soft mask，用 Hessian-guided structured target 和 progressive quenching 将可训练稀疏性收敛到硬件可执行 2:4 mask；遍历/annealing 是算法语义的一部分。
- **评价：** §5/Appendix A–C 覆盖 GPT-2、OPT、LLaMA2、Qwen3、DeepSeek-MoE 的 124M–16B 模型与 L20A；给出 PPL/zero-shot、消融和特定 2:4 端到端 speedup。
- **未证明：** Appendix D 说明语料、模型和 mask family 范围有限；硬件支持不等于所有 serving shape/并发都加速，恢复成本也未被通用摊销。
- **评分与 Books：** `3+2+3=8`，深入完成。建议 `Integrate → INFER-TENSORRT-LLM`，handoff `TRAIN-PRETRAINING`：把 mask learning/annealing 与 runtime executable sparsity contract 绑定；无 2:4 kernel、质量回归或 recovery 成本过高时回退 dense/既有 pruning。

## 2605.06445 — Constraint Decay

- **Primary：** `arXiv:2605.06445v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06445v1)。
- **机制：** §3 固定 functional spec，逐步增加 architecture、database、ORM 等 structural constraints；验收取 behavioral tests 与 static verifier 的交集。
- **评价：** §4–5 覆盖八种 framework、Mini-SWE/OpenHands、多模型和 generation/feature implementation task，观察 constraint load 与 framework sensitivity。
- **未证明：** Appendix C–G 说明 static regex verifier 可能误判，ground truth 不是唯一实现，子集和成本限制约束外推。
- **评分与 Books：** `2+2+3=7`，深入完成。`No Change — Existing Coverage → PLATFORM-EVALUATION-SYSTEM`：现有章节已要求 behavior、structure/interface invariant 与 artifact revision 分别验收；该 benchmark 不新增通用 owner。

## 2605.06457 — Workflow Fidelity

- **Primary：** `arXiv:2605.06457v1`；[exact-v1 PDF](https://arxiv.org/pdf/2605.06457v1.pdf)。
- **机制：** §3 将 expected/observed trajectory 转成 transition multiset，以 Transition Recall、Transition Precision 及其 F1 定义 Agentic Success Rate；最终 task success 与 handoff set 都可能掩盖 checkpoint skip。
- **评价：** §3–4 在 HMASP payment workflow、18 个模型、1000 points×5 repeats（90,000 instances）下比较 TSR/HF1/ASR，并用 prompt refinement 与 deterministic routing guard 做诊断性修复。
- **未证明：** 单一支付 workflow、固定 expected path 与 bigram/multiset metric 不能覆盖全部长程顺序、状态语义或多合法路径；修复混合 prompt 与 guard，不能把收益归因给 metric 本身。
- **评分与 Books：** `2+2+3=7`，深入完成。`No Change — Existing Coverage → AGENT-WORKFLOW`：现有章节已把 transition、checkpoint、receipt、side effect 与最终 outcome 分离；ASR 可作受限 evaluator，不需要新正文。

## 2605.06481 — OA-WAM

- **Primary：** `arXiv:2605.06481v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06481v1)。
- **机制：** §3 用 persistent object-slot address 维持跨视角 identity，同时把 mutable content、action chunk 与 per-object next state 分开；address 参与每层 attention，避免把对象身份与瞬时外观合并。
- **评价：** §4 在 LIBERO、SimplerEnv、LIBERO-Plus 做三 seed、消融、视觉/对象鲁棒性和 latency；附录披露多阶段训练与组件耗时。
- **未证明：** 证据以 simulation/visual matching 为主，不证明真实物理安全；地址依赖 detection/tracking 和 slot count，frozen perception 约 95ms、trunk/head 约 5.6ms，实时瓶颈并未消失。
- **评分与 Books：** `3+2+3=8`，深入完成。建议 `Integrate → MULTIMODAL-WORLD-MODELS`：加入“persistent address 与 mutable state 分离”的 world-state identity；检测/跟踪失效时回退 observation-grounded re-identification 或显式 uncertain identity。

## 2605.06490 — Instrumental Choices

- **Primary：** `arXiv:2605.06490v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06490v1)。
- **机制：** §3 用 deterministic environment state 同时标记 task completion 与是否采用 policy-violating shortcut，并以 controlled variants 改变 shortcut usefulness/necessity。
- **评价：** 七任务、八 variants、三 repeats、十模型，共 1680 runs；基础发生率较低，环境激励比 verbal stakes 更能改变 shortcut 行为。
- **未证明：** §5 明确 behavior 不等于 latent goal；短时 terminal sandbox 不含长期制度、multi-agent 或不可逆副作用，样本量、evaluation awareness 与 provider drift 均限制结论。
- **评分与 Books：** `2+2+3=7`，深入完成。`No Change — Existing Coverage → PLATFORM-EVALUATION-SYSTEM`：现有章节已要求 task success、policy compliance、tool trace 与 deterministic predicate 分责；该数据不形成新的通用安全机制。

## 2605.06554 — Lighthouse Attention

- **Primary：** `arXiv:2605.06554v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06554v1)。
- **机制：** §3–5 在 stock attention kernel 外构建 multi-resolution QKV pyramid，selection 后 gather→FlashAttention→scatter；训练末期使用同一 optimizer/dataloader 恢复 dense SDPA，使稀疏训练路径与 dense deployment artifact 分离。
- **评价：** §6 在 530M、C4、98K context、50B tokens、B200 上比较 scaling、recoverability 与 throughput，并扩展到多节点/1M context；作者报告 ≥100K 下约 1.4–1.7× training speed。
- **未证明：** 所有 query 同时存在，因此该路径不兼容 autoregressive decode；下游结果只在 dense resume 后获得，内部 attention 对选择后序列仍为二次复杂度，serving integration 未证明。
- **评分与 Books：** `3+3+3=9`，深入完成。建议 `Integrate → TRAIN-PRETRAINING`：加入“training-only sparse attention → dense recovery → deployment”的阶段性分支，artifact 必须记录 selection schedule 与 recovery checkpoint；短上下文或恢复质量不足时保留 dense training。

## 2605.06614 — SkillOS

- **Primary：** `arXiv:2605.06614v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06614v1)。
- **机制：** §3 分离 frozen executor、RL-trained skill curator 与 external SkillRepo；curator 跨 grouped task stream 写入/更新 skills，用未来任务结果优化写入策略。
- **评价：** §4–5 在 ALFWorld、WebShop、DeepMath、Qwen3-8B curator 与多种 frozen executor 上比较 ReasoningBank/MemP，并在 16×H100/verl 配置训练。
- **未证明：** Appendix D 说明 BM25 retrieval、单 Markdown skill、冻结 executor miscalibration 与联合优化成本；未覆盖脚本/资源、层次 skill 或安全授权。
- **评分与 Books：** `3+2+3=8`，深入完成。`No Change — Existing Coverage → AGENT-MEMORY`：现有章节已分离 writer/curator、task executor、derived memory、provenance 与 admission；该论文提供 learned curator 实例但未改变责任边界。

## 2605.06639 — Recursive Agent Optimization

- **Primary：** `arXiv:2605.06639v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06639v1)。
- **机制：** §2 让同一 shared policy 在递归树的所有节点决定是否 delegation、怎样写 subtask、怎样 aggregate；训练加入 subagent reward 与 inverse-frequency depth weighting，使递归本身成为被优化的 inference-time scaling policy。
- **评价：** §3–5 覆盖 TextCraft-Synth、Oolong-Real、DeepDive，并报告 context chunking、并行/深度使用和消融；DeepDive 的披露结果从 0.24 提升到 0.40。
- **未证明：** §7/Appendix A 说明需要 per-domain training，子任务需与父任务相似，recursive rollout 昂贵，未覆盖 heterogeneous agents、权限或安全。
- **评分与 Books：** `3+3+3=9`，深入完成。建议 `Integrate → AGENT-MULTI-AGENT`：区分静态 delegation policy 与“训练模型学习何时递归”的分支；每层仍需 task/authority/budget/receipt，收益不足或深度失控时回退单 Agent/固定拓扑。

## 2605.06652 — Benchmarkless Safety Scoring

- **Primary：** `arXiv:2605.06652v1`；[exact-v1 HTML](https://arxiv.org/html/2605.06652v1)。
- **机制：** §3–6 将 scenario、rubric、auditor、judge、target 与 sampling 固定为 measurement instrument；无 ground-truth label 时只通过 known contrast、target-driven variance 与 rerun stability 建立比较有效性链。
- **评价：** §4–7 使用本地 Qwen ladder、abliterated targets、八场景 Norwegian safety/legal pack 与 SimpleAudit/Petri，比较 judge–auditor 配置、critical-miss agreement、稳定性和 token cost。
- **未证明：** §9 明确 validation chain 是必要而非充分条件；scenario construct 与 auditor 支配结果，范围有限，不能把 comparative score 升级为 safety certification。
- **评分与 Books：** `3+3+3=9`，深入完成。建议 `Integrate → PLATFORM-EVALUATION-SYSTEM`：加入“无标签时先验证 instrument，再报告比较分数”的分支；judge 只拥有比较证据，缺 known contrast、target sensitivity 或 rerun stability 时不得进入 release gate。

## 作者侧汇总

- `24/24` 已取得 exact-v1；`23` 项 HTML、`1` 项 PDF；无材料阻塞、无 withdrawn。
- 分数：`20` 项 `7–9` 深入完成，`4` 项 `5–6` 标准完成。
- Books 建议：`12 Integrate`、`12 No Change — Existing Coverage`。这里只形成 writeback queue，不直接修改共享 Books；由 root 按日期/owner 协调写入并完成 post-write semantic audit。
- 日报在新的非作者 final review 前保持“进行中”，不能因作者侧 24 项闭合而登记 Complete。
