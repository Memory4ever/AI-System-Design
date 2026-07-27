# Daily Research — 2026-08-09

**Archive Date:** 2026-08-09（Asia/Shanghai）
**Recovery Date:** 2026-08-11；coverage repair 2026-08-12
**Research Mode:** Retrospective Daily Recovery
**Event Window:** 2026-08-09 natural day；cross-check lookback 2026-08-07～2026-08-10
**Status:** Daily Complete；10 scored candidates；9 Full Source Reviews + 1 low-score boundary；Books Integration Evaluated — 1 Refine

## Executive Summary

本次补全纠正了原恢复记录的 coverage false negative：8 月 9 日并非只有 **Beyond Routing / FDAA**。
重新按 submission date 检索后，识别出 10 个与本书相关的论文 source families。Tangent、
LLM Reasoning for Subjective Tasks、Beyond Routing、Business Arena、PIRL、pre-pretraining stability、
per-instance activation steering、carbon-aware fine-tuning 与 AquiLLM 均已完成全文 Source Review；
Theory-Guided Deception Detection 保留 18/30 低分边界。discovery 不再冒充全文审计。

三个最重要的长期信号分别位于不同 owner：

1. **Agent 测试不是 Benchmark 的同义词**。Tangent 的开源代码语料与 practitioner study 显示，
   现实测试往往停在孤立 unit、简单输入、heavy mocking 与浅断言；长期机制是把 test boundary、
   fixture、state transition、side effect、failure injection 与 adequacy 一起纳入 Evaluation contract。
2. **主观 rubric 不能沿用“更多推理必然更好”的假设**。主观任务论文观察到 outcome-only RLVR
   可能诱发短路式 reasoning collapse；但其 proprietary data、未公开模型身份和未实现的 persona-routing
   blueprint 限制了外推，因此只作 Experimental evidence。
3. **MoE dispatch 与 aggregation commitment 可被分开审计**。FDAA 固定执行集合后校准 commitment，
   提供受控的机制分解；短 sequence、窄 domain 和单一来源仍不足以建立新默认方案。

Tangent 补全了 Ch62 中 Benchmark / Evaluation / Testing 的层次关系，达到 `Refine — Existing
Argument` 门槛。其余两项不修改 Books。当天没有发现带公开技术材料的一线模型机构发布，也没有确认
改变稳定 runtime contract 的工程 Release。

## 1. 模型与研究机构

### Source Coverage

按固定来源顺序复核 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google Research、
Meta AI / FAIR、Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、
Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Seed、Baidu ERNIE、Tencent Hunyuan、Huawei Noah、
Shanghai AI Lab / InternLM、StepFun、Xiaomi MiMo、InclusionAI / Ant 与 Hugging Face Blog。

- 没有发现可把 first-public date 明确定位到 2026-08-09、并带 technical report、model/system card
  或 primary artifact 的新 Research event。
- OpenAI 与 Anthropic 的当前 Research index 最近可见高信号条目早于本日；Hugging Face 首页的
  community post、排行榜与旧文章重排不作为模型机构 Research。
- 国内外机构页面若缺精确 event date 或只有搜索摘要，本次不补猜。

### Candidate Scoring

本组没有达到评分门槛的可验证 2026-08-09 候选。

## 2. arXiv / 学术来源

### Source Coverage

复核 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`cs.CR`、`stat.ML` 的 recent/new
节奏，并用 Hugging Face Papers、OpenReview/TMLR、Google Scholar、OpenAlex、Semantic Scholar 与
DBLP 作 discovery / metadata cross-check。

- 8 月 9 日处于周末，没有常规批量 listing，但 arXiv submission metadata 显示当天仍有独立事件；
  “无 listing”不能推导为“无 paper”。原 Daily 只回写 `2608.08853v1`，属于 discovery coverage 不足。
- 本次以 `Submitted on 9 Aug 2026` 为 event-date contract，恢复 Tangent、Business Arena、
  pre-pretraining stability、carbon-aware fine-tuning、activation steering、multimodal RLVR、AquiLLM、
  theory-guided deception detection、subjective reasoning / RLVR 与 Beyond Routing 共 10 个 source families。
- 9 个 `20+` 候选均完成 primary paper 全文、实验/限制和章节邻接审计；Theory-Guided Deception
  Detection 维持低分边界。Business Arena 与 PIRL 不再是 Weekly pending。
- 8 月 11 日发现的 SwiftQK 与 QueryProof first-public date 为 8 月 10 日，继续归 W33；不因本次回填
  改写 event date。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence Level |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Tangent: testing practices for LLM Agent applications | 2026-08-09 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | E3 — ASE 2026 paper full text；artifact repository currently empty |
| LLM Reasoning for Subjective Tasks | 2026-08-09 | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | E3 — RecSys 2026 paper full text；private data / undisclosed API models |
| Business Arena | 2026-08-09 | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | E3 — full paper、appendices、mechanism ablations and reliability analysis |
| Improving Generalization Robustness of Multimodal RLVR / PIRL | 2026-08-09 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | E3 — full paper、proofs、3-seed experiments and compute contract |
| Beyond Routing / FDAA | 2026-08-09 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | E2 — arXiv v1 full text；单作者、无独立复现 |
| Instability of LLM Pre-Pretraining | 2026-08-09 | 4 | 3 | 4 | 4 | 4 | 5 | 24/30 | E3 — full paper、3-seed matrix and limitations；No Change |
| Deployable Per-Instance Multi-Layer Activation Steering | 2026-08-09 | 4 | 3 | 4 | 4 | 4 | 4 | 23/30 | E3 — full paper、oracle/deployable split、controls and limitations；Experimental |
| Performance–Carbon Break-Even Fine-Tuning | 2026-08-09 | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | E3 — full ongoing-work paper、calibration/log contract and limitations |
| AquiLLM | 2026-08-09 | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | E3 — full architecture/deployment paper；No Change case |
| Theory-Guided Deception Detection with RAG | 2026-08-09 | 3 | 2 | 3 | 4 | 3 | 3 | 18/30 | E1 — negative domain result；Ignored / Weekly boundary |

### Deep Analysis 1 — Tangent：从 Benchmark 走向可定位的 Agent Testing

**Why**

端到端 benchmark 能比较任务结果，却不能定位 tool、memory、planning、permission 或 side-effect
contract 的回归。传统 unit test 又容易 mock 掉 LLM、外部工具和环境，使“测试通过”只证明了一个
被大幅简化的 orchestration。

**Principle**

测试必须声明 subject boundary、fixture / initial state、stimulus、oracle / invariant、可观察状态变化
和 failure model。Benchmark、Evaluation 与 Testing 共享 evidence substrate，但回答的问题不同。

**Mechanism**

论文从 1,190 个 Python repositories 起步，以 11 类 Agent / tool frameworks 做静态识别，最终人工标注
240 个 modules 中的 2,572 个 test methods，并把 fixture、data、objective 与 assertion 归为 23 类
patterns；另访谈 10 名 IBM practitioners。它区分 unit、module、integration、API 与 end-to-end，
并观察到 interaction、multi-step、non-functional 与 environment-level assertions 覆盖较少。

**Trade-off and Evidence Boundary**

- repository mining 只能看到公开 Python 项目，`>=50 stars`、framework detection 与成熟度会造成选择偏差；
- practitioners 均来自 IBM，不能代表全部工业实践；
- LLM-assisted filtering 与人工 taxonomy 可能漏分类，论文只证明关联和实践倾向，不证明因果；
- 论文声称 artifact 可用，但 2026-08-12 访问 GitHub repository 时页面显示为空，当前不可独立复现数据处理；
- mock 能提供确定性和故障注入，不能因“真实度不足”被简单否定；它需要由少量真实 integration/failure
  tests 校准其 contract。

**Connection and Evolution**

主 owner 为 Ch62，Ch69 与 Ch77 是 handoff：

```text
snapshot benchmark
→ encoded unit / schema tests
→ stateful module and interaction tests
→ environment and failure-path tests
→ continuous release evidence
```

该演进是 `Layering / Dependency`，不是 end-to-end 对 unit test 的替代。

### Deep Analysis 2 — Subjective Reasoning：Reward 可验证不代表目标客观

**Why**

数学与代码任务常有明确 outcome verifier；内容质量、安全和推荐相关性则由主观 rubric 与人类标签定义。
把 math-centric CoT、更多 reasoning tokens 或 outcome-only RLVR 原样迁移过去，可能优化错误代理目标。

**Principle**

Reasoning 是 task-conditioned policy，不是默认单调增益。Reward contract 需要区分 final label、格式、
reasoning budget 与 rubric uncertainty；长度只能是受 correctness gate 约束的辅助信号，不能充当质量本身。

**Mechanism**

论文在四个 Netflix 二元 verification tasks 上比较 direct、implicit 与 explicit reasoning，并以 Mistral-7B、
Qwen2.5-7B 配合 GRPO、Dr.GRPO、GSPO 做 400-step post-training。作者观察到部分模型/任务中 reasoning
降低 macro-F1，且 outcome reward 会在约 70 steps 后伴随生成长度骤降；单纯奖励长度又产生 filler，
conditional length reward 只在答案正确时提供长度信号。1,500 personas 的实验用于说明 reasoning style
会改变 judge outcome，但完整 persona-routing 仍只是 blueprint。

**Trade-off and Evidence Boundary**

- 四个 rubric、训练数据和 proprietary model identity 不公开，绝对值不可独立复核；
- open-weight 实验只有两个 7B checkpoints，不能把“math reasoning 导致 collapse”提升为训练因果；
- best-validation checkpoint selection、human-label noise 与 macro-F1 无法证明 CoT faithfulness；
- persona-conditioned variation 可能来自 prompt framing、label prior 或 bias，不等于已经找到可部署 router；
- conditional length reward 阻止短路的同时增加 reward surface，仍可能被 verbosity 或 template exploit。

**Connection and Evolution**

Ch29 已说明 outcome reward、credit assignment 与 reward hacking，因此本项为 `No Change — Already
Covered / Experimental Case`；Ch62 接收 rubric uncertainty 与 human oversight handoff，不修改正文。

### Deep Analysis 3 — Beyond Routing：Dispatch 与 Commitment 是不同 Contract

**Why**

传统 sparse MoE router 的同一组 scores 同时决定 Top-K expert selection 和选中 outputs 的
aggregation weights。Top-K 排名足以决定实际 dispatch，却未必是对最终 language-model objective
最合适的相对 commitment。

**Principle**

离散资源决策与连续结果组合应分开审计：selection 决定候选 expert，dispatch / execution 决定
实际计算和通信路径，aggregation commitment 决定已计算结果如何进入 residual stream。

**Mechanism**

FDAA 固定 native Top-K expert IDs、执行集合与 selected router mass，只根据 token state、已计算
expert outputs、native weights、expert IDs 和 layer embedding 预测 residual commitment scores；重加权
后保持总 selected mass。head 的最后一层零初始化，使初始行为近似复现原模型。训练冻结 backbone、
router 与 experts，只优化约 30 万参数，目标为 next-token cross entropy、KL 与 residual regularization。

**Trade-off and Evidence Boundary**

- fixed-dispatch protocol 隔离了 aggregation 因果因素，但没有证明 joint routing 或改变 dispatch 更差；
- 主要实验使用短 sequence、batch 1 与少量 target layers，DeepSeek-V2-Lite 只有单 seed replication；
- WikiText policy 到 C4 的迁移失败，说明 token adaptivity 不等于 domain generality；
- 新 head 增加 checkpoint identity、version compatibility、inference fusion 与 rollback 状态。

**Connection and Evolution**

主 owner 为 Ch21，Ch29 / Ch36 / Ch40 为相邻章节。演进关系是：

```text
one router score owns selection + weighting
→ fixed-dispatch audit isolates aggregation mismatch
→ lightweight commitment calibration
→ future joint design must re-account dispatch cost and serving state
```

旧方案仍有联合训练自然、runtime 简单和 checkpoint 兼容性好的优势；只有 mismatch 稳定、跨域成立、
且新增状态成本可管理时，解耦 commitment 才可能成为长期设计。

## Full Source Review Addendum — Remaining Six `20+` Candidates

### Business Arena — 27/30

- **Problem / Previous Design / Changed Constraint**：短时、静态且有唯一答案的 benchmark 易复现，也便于
  exact scoring；但长期经营把 noisy evidence、延迟结果、变化市场、持续合规和 capital commitment 耦合在
  同一状态机中。单一 terminal profit 能比较结果，却无法说明 opportunity 是否存在、哪项 action 创造价值。
- **Mechanism / State and Flow**：Agent 在隔离 OpenClaw sandbox 内通过 60+ typed tools、backend API 与
  persistent workspace 经营跨境商店；arena/service 拥有隐藏市场状态，Agent 拥有可见 context/workspace，
  event loop 推进 buyers、NPC sellers、shipping、cost、tariff 与 compliance。评测把 terminal net worth、
  skill metrics、action-level economic attribution 分层，并用 save–fork–load 同时恢复 model-visible context、
  OS workspace 与 exact marketplace state，以同一历史做 controlled continuation。
- **Evaluation / Evidence Boundary**：15 个 proprietary/open-weight models，各 10 runs；另用 deterministic
  expert strategies 估计 available opportunity，以五组 intended/neglect/misuse mechanism ladders排除部分 shortcut，
  并用 ICC 分离 within/between-model variance。证据支持该 simulator 内的 stateful, delayed-credit evaluation，
  不证明 model 能安全操作真实 storefront、GUI、mailbox、支付或法规系统；real Alibaba listings 与 calibrated
  conditions 也不等于真实市场因果动态。
- **Trade-offs / Evolution / Decision**：更真实的 persistent world 提高 ecosystem validity，却放大 simulator
  policy、NPC、economic formula、model runtime 和 repeated-run 成本；snapshot/fork 还要求 environment、workspace、
  model context 与 evaluator 原子版本化。演进为 `static task -> long-horizon world -> outcome + diagnostic
  attribution -> exact-state counterfactual continuation -> production side-effect validation`。Ch62 已拥有 trajectory/
  stateful evaluation 与 subject-harness-evaluator identity，故为 `Refine candidate / No immediate Books change`；
  Ch77/75/69 handoff，避免重复 Tangent 当日已写入的 testing layer。

### PIRL: Improving Generalization Robustness of Multimodal RLVR — 26/30

- **Problem / Mechanism**：标准 GRPO 把 format failure、semantic failure 与 joint failure 压成同一 zero reward，
  且只在有限 prompt templates 上优化，可能让 policy 学到 prompt-dependent shortcut。PIRL 用 Dynamic Trinary
  Reward 分开 failure type、Decoupled Advantage Normalization 保留信号，再以 instruction-embedding adversary、
  consistency regularizer 和 hard-prompt sampling 约束 prompt invariance；policy update 仍是 clipped GRPO，
  inner adversary 不做 exact bilevel differentiation。
- **Evaluation Contract**：Qwen2.5-VL-7B 与 Qwen3-VL-8B，Exam/Medical/Legal VQA，standard、1～15-template
  stress 与 operator-based dynamic mutations，3 seeds；16×H100-80GB、ZeRO-3、BF16、vLLM rollout，10 RL
  iterations。adversary 每 4 policy updates 更新一次，作者测得约 25% wall-clock overhead。
- **Evidence Boundary / Trade-offs**：结果支持 PIRL 在该 contract 下缩小 prompt-template gap；MathVista 变成
  free-form 后所有方法都大幅下降，说明部分 dynamic mutation 已改变 task。ablation 中 full PIRL 与 MT+DTR
  常在 noise 内，不能证明 DTR 或 adversary 各自对 leading-order gain 独立必要。embedding adversary 新增四倍
  forward/backward-equivalent inner work、perturbation-policy identity 与训练复杂度；multi-template augmentation
  仍是较便宜 baseline。`Refine candidate (Ch29 owner; Ch62 handoff; Experimental)`，Books 暂不改，等待与
  reward robustness 演进链联合吸收。

### Instability of LLM Pre-Pretraining — 24/30

- **Mechanism / Contract**：在 natural-language training 前用 64/128-Dyck 或 shuffled-Dyck formal sequences
  做 500-step pre-pretraining，再对 Albanian、Czech、Danish、Dutch、English、Finnish 的 mC4 slice 做 10K
  steps。六个 Llama-3-based configurations（253M～884M total parameters）、Llama/Gemma tokenizers、每 setup
  三 seeds；token-efficiency gain 衡量达到 baseline validation loss 所需 token 差。
- **Evidence / Boundary**：相同设置只换 seed 即可能从 gain 变 loss；English 较稳定，其他语言、tokenizer、
  artificial grammar 和 pretraining length 的结果混合，20+ linguistic properties 几乎不能解释差异。实验只有
  655M natural-language tokens、有限 hyperparameter grid 和 web corpus，因此证明的是 pre-pretraining
  intervention 对 setup/seed 敏感，不是它普遍无效。
- **Evolution / Decision**：旧的 random initialization 与直接 pretraining 保持最少 prior bias；formal-language
  curriculum 以潜在 sample efficiency 换取 negative transfer、tokenizer interaction 与 extra stochasticity。
  `No Change — Already Covered (Ch24; Experimental replication case)`；长期原则是 curriculum intervention
  必须用 multi-seed distribution 而非 single-run headline 验收。

### Per-Instance Multi-Layer Activation Steering — 23/30

- **Mechanism**：固定 global layer set 实现简单，但同一 trait 的最佳 injection layers 会随 input 变化。
  gold-aware exhaustive/TKM oracle 先定义 ceiling；deployable W2S-Multi 从 prompt embedding PCA 预测 layer
  ranking，以 classifier 预测 steering direction，再由 adaptive-K gate 用短 steered passes 控制最多层数。
  model state 仍冻结；selector、direction classifier、gate config 与 steering vector 成为新的 artifact identity。
- **Evaluation / Boundary**：Llama-3-8B-Instruct、Aya-Expanse-8B，六个 binary persona traits，32 layers；
  exhaustive search 只在 K<=3 可验证，K=4/5 用 beam trend。主 metric 是 restricted Y/N probability lift，另看
  answer flip 与 PPL；2,400 test instances 中 direction error 有显式记录。没有 open-ended human preference、
  held-out trait、cross-model selector transfer 或 production latency，因此不能把 persona flip 当成通用 alignment。
- **Trade-offs / Decision**：per-instance routing 减少 oversteer，却新增 selector misclassification、multi-pass
  cost、configuration drift 和 cache/batch divergence。global layer 在 homogeneous task、low-latency 或缺少
  calibration data 时仍合理。`Emerging / Experimental; No Books change`，owner Ch5，Ch25/62 handoff。

### Performance–Carbon Break-Even Fine-Tuning — 22/30

- **Mechanism / Contract**：在 task loss 中加入 differentiable carbon surrogate 与 regularization。surrogate
  由 parameter norm、tensor-shape FLOP proxy、activation-memory proxy 构成，每模型只用三种 batch operating
  points 的 CodeCarbon/H100 measurement 做 non-negative fit；lambda 用 validation sweep 选择。实验覆盖
  Gemma-2-2B、Llama-3.1-8B、Qwen2.5-14B 的三个 MMLU subjects，另在 SQuAD v2/BoolQ 做 sensitivity。
- **Evidence Boundary / Trade-offs**：五个九个 model-task pairs 落入作者定义的 break-even region，但只有
  一个 strict Pareto case；absolute CO2 delta 很小，固定 H100 与单一 carbon intensity，三点 within-sample R2
  不是跨硬件/global predictor。该方法可能把 task-specific structural regularization 误读为 carbon mechanism，
  也新增 profiler、grid factor、lambda、hardware/runtime identity。`Emerging / Ongoing Work; No Books change`，
  Ch66 owner；待跨 hardware、region、workload 和 lifecycle accounting 再判断。

### AquiLLM — 21/30

- **Mechanism**：self-hosted research workspace 将 local vLLM-compatible chat、embedding/reranking/transcription/
  multimodal sidecars、document ingestion、semantic retrieval、episodic memory、project collections 与 skill packs
  组合。permission-filtered collection 先确定 corpus boundary，再加载 procedural prompts；episodic writes 异步，
  retrieval 尽量排除当前 conversation 以减少 self-echo，memory failure 回退到 local retrieval。
- **Engineering Boundary / Trade-offs**：per-service GPU memory/concurrency caps、serial startup、sidecar isolation、
  optional LMCache 与 short-lived exact caches 控制资源；但 hosted/local provider behavior 不一致，episodic state
  eventually consistent，feature flags 与 air-gap configuration 需要 deployment verification。论文是一个 UCLA
  astrophysics-group production-like case，没有 matched benchmark、ablation、multi-site replication 或通用 SLO。
- **Evolution / Decision**：`shared documents -> semantic retrieval -> user/project episodic memory -> collection-
  scoped procedural skills -> governed local research workspace`。Ch72/73/80 已分别覆盖 retrieval、memory 与
  Skill governance，故 `No Change — Already Covered (case architecture)`；不把 feature inventory写入 Books。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → NVIDIA Dynamo → TensorRT-LLM → Ray →
KServe → Kubeflow → Kubernetes → Transformers → Accelerate → DeepSpeed → Megatron-LM → Unsloth
→ MLX → llama.cpp → ONNX Runtime → OpenXLA 检查 official release index、tag、release notes 与公开文档。

- 没有确认到 released-at 为 2026-08-09、且改变稳定 runtime contract 的 release、RFC 或重要 PR。
- vLLM / SGLang 等索引当前显示的其他版本不能在缺少 tag date 与 release note 对齐时回填本日。
- 8 月 6 日的 KServe v0.20.0、Dynamo v1.3.1 与 DeepSpeed v0.19.4 已由 8 月 7～8 日 Daily 记录，
  不在本日重复计分。

### Candidate Scoring

本组没有达到评分门槛的可验证 2026-08-09 候选。

## Evidence Level and Fact Boundary

- **Official fact**：只记录官方 Research / Release index 与相邻 Daily 已保存的日期状态。
- **Full paper evidence**：9 个 `20+` candidates 已覆盖 metadata、
  problem、method、implementation / protocol、evaluation、limitations 与相关 appendix；作者实验仍是
  条件性证据。
- **Low-score boundary**：deception RAG 只保留 primary abstract / metadata 与负结果边界，不进入 Books。
- **Artifact boundary**：Tangent 正文声明 dataset / analysis artifact 公开，但引用 GitHub repository 在
  2026-08-12 访问时为空；论文阅读完成不等于 artifact 可复现。
- **Cross-day evidence**：8 月 8 日正向记录与 8 月 10 日 retrospective coverage 曾得到
  `No Verified Candidate`，本次 submission-date 检索证明该结论是假负例；相邻 Daily 只能约束已访问
  范围，不能替代 event-date recovery。
- **Community evidence**：Hugging Face community posts、排行榜与搜索摘要只作 discovery noise。
- **Performance numbers**：只保留与对应论文 model、task、run count、decoding / training protocol 绑定的
  数字；没有把宏观 benchmark、F1 或作者 speed / carbon 数字外推为 production SLO。

## Knowledge Tree Position

| Candidate | Primary owner | Adjacent chapters read | Books decision |
| --- | --- | --- | --- |
| Tangent | Ch62 Evaluation System | Ch63、Ch69；核对 Ch77 boundary | Refine — Existing Argument |
| Subjective reasoning / RLVR | Ch29 GRPO | Ch27～30、Ch62 | No Change — Already Covered；Experimental case |
| Beyond Routing / FDAA | Ch21 MoE | Ch29、Ch36、Ch40 | Emerging / Experimental；No Change |
| Business Arena | Ch62 Evaluation System | Ch63、Ch69、Ch75、Ch77 | Refine candidate；stateful counterfactual evaluation already broadly covered |
| PIRL | Ch29 GRPO | Ch27～30、Ch62 | Refine candidate；Experimental；defer joint evolution integration |
| Pre-pretraining instability | Ch24 Pretraining | Ch23～25 | No Change；multi-seed replication evidence |
| Activation steering | Ch5 Representation | Ch4～6、Ch25、Ch62 | Emerging / Experimental；No Change |
| Carbon-aware fine-tuning | Ch66 Cost | Ch24、Ch45、Ch69 | Emerging / Ongoing Work；No Change |
| AquiLLM | Ch72 RAG | Ch71～73、Ch80 | No Change — Already Covered；case architecture |

## Recommended Action

- `Refine — Existing Argument`：把 Tangent 支持的 Benchmark / Evaluation / Testing 分层、test boundary、
  mock contract 与 Agent-specific adequacy 融入 Ch62；不复制论文比例。
- `No Change / Emerging`：subjective reasoning / RLVR 与 Beyond Routing 都提供新案例，但没有足够公开、
  跨模型或跨来源证据改变 Ch29 / Ch21 的稳定结论。
- Business Arena、PIRL 与其余四个 `20+` candidates 已完成全文，不再进入 W32 pending。Business Arena
  的 stateful fork 与 PIRL 的 prompt-robustness reward 分解进入未来跨来源 Books 演进链候选；本日不再追加正文。
- W32 仍因既有 16 个 blocked source families 和 2 个 unscored discovery gaps保持 Evidence Gate Open。

## Books Integration

本日只 refine `books/part-05-ai-infrastructure/62-evaluation-system.md`：在既有四层 Evaluation 对象之后，
补入 Benchmark、Evaluation 与 Testing 的责任边界，以及 unit → module / interaction → environment /
failure → continuous release evidence 的层叠演进。没有新增章节，也没有把 Tangent 的样本比例写成通用事实。

Subjective reasoning / RLVR 与 Beyond Routing 不写入 Books；它们分别被既有 reward-contract 论点覆盖，
或仍缺第二来源与 production evidence。ROADMAP 与 DECISIONS 不变。

## Ignored Noise

- Automated Generation of Complexity-Validated Decision Scenarios：与 Eval 数据生成有关，但 throughput /
  schema 相关性只有 5 个模型且被单个高吞吐模型主导，暂不进入 20+ ledger；
- Theory-Guided Deception Detection with RAG：负结果有领域价值，但没有形成可泛化的 RAG / Security
  机制，保留 18/30 边界记录；
- 周末没有新 announcement 时对旧 arXiv 论文的重新排序与聚合推荐；
- Hugging Face community post、排行榜和未绑定 primary report 的 benchmark headline；
- 无法把 tag date、release notes、文档与代码路径共同核验的工程版本；
- 8 月 10 日 first-public 的 SwiftQK 与 QueryProof；它们属于 W33，不回填本日。

## Repository Changes

- 补全 `papers/2026/08/09/README.md`：从 1 个扩展为 10 个 scored source families，完成 9 项 `20+`
  Full Source Review，并保留 1 项 low-score boundary。
- refine `books/part-05-ai-infrastructure/62-evaluation-system.md`；ROADMAP、DECISIONS 与章节结构不变。
- W32 Weekly 在本 Daily 验收后重新聚合；未执行 stage、commit、push 或破坏性 Git。

## Open Questions

1. Tangent artifact repository 何时补齐 dataset 与 analysis pipeline，论文 taxonomy 能否被独立复现？
2. Business Arena 的 simulator/runtime、save–fork–load state identity 与 PIRL 的 reward decomposition 是否能由
   第二来源形成稳定演进链，而不是作为单篇论文直接写入 Books？
3. subjective rubric 的 label disagreement、annotator population 与 fairness slice 如何进入 reward /
   evaluation identity，而不被单一 macro-F1 隐藏？
4. FDAA 在长 context、更多 MoE backbones、多个 layers 同时启用和不同 Top-K 下是否保持收益？
5. aggregation head 怎样进入 checkpoint、kernel fusion、quantization 与 rollback identity，才不会把轻量
   training modification 变成隐式 serving fork？
6. arXiv 周末无常规 listing 时，怎样保存 submission / announcement / first-access 三种时间，避免
   Sunday event 被 Monday / Tuesday Daily 漏记？

## Sources

访问 / 恢复日期为 2026-08-11；coverage repair 与新增来源访问日期为 2026-08-12。相邻 Daily 是
retrospective boundary 的一手仓库记录。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/
- OpenAI Research Newsroom: https://openai.com/news/research/
- Anthropic Research: https://www.anthropic.com/research
- Google DeepMind: https://deepmind.google/blog/
- Google Research: https://research.google/blog/
- Meta AI: https://ai.meta.com/blog/
- Microsoft Research: https://www.microsoft.com/en-us/research/blog/
- Hugging Face Blog: https://huggingface.co/blog

### Academic and Discovery Sources

- Tangent metadata: https://arxiv.org/abs/2608.08413
- Tangent full HTML: https://arxiv.org/html/2608.08413
- Tangent artifact repository（2026-08-12 observed empty）:
  https://github.com/aster-test-generation/tangent-ase-2026
- LLM Reasoning for Subjective Tasks metadata: https://arxiv.org/abs/2608.08889
- LLM Reasoning for Subjective Tasks full HTML: https://arxiv.org/html/2608.08889
- Beyond Routing / FDAA metadata and v1: https://arxiv.org/abs/2608.08853
- Beyond Routing / FDAA full HTML: https://arxiv.org/html/2608.08853
- Business Arena: https://arxiv.org/abs/2608.08621 ; https://arxiv.org/html/2608.08621v1
- Improving Generalization Robustness of Multimodal RLVR: https://arxiv.org/abs/2608.08802 ; https://arxiv.org/html/2608.08802v1
- Instability of LLM Pre-Pretraining: https://arxiv.org/abs/2608.08800 ; https://arxiv.org/html/2608.08800v1
- Deployable Per-Instance Multi-Layer Activation Steering: https://arxiv.org/abs/2608.08829 ; https://arxiv.org/html/2608.08829v1
- Performance–Carbon Break-Even Fine-Tuning: https://arxiv.org/abs/2608.08744 ; https://arxiv.org/html/2608.08744v1
- AquiLLM: https://arxiv.org/abs/2608.08883 ; https://arxiv.org/html/2608.08883v1
- Theory-Guided Deception Detection with RAG: https://arxiv.org/abs/2608.08881
- Automated Generation of Complexity-Validated Decision Scenarios:
  https://arxiv.org/abs/2608.08822
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- Hugging Face Papers: https://huggingface.co/papers
- OpenReview: https://openreview.net/
- Google Scholar: https://scholar.google.com/
- OpenAlex: https://openalex.org/
- Semantic Scholar: https://www.semanticscholar.org/
- DBLP: https://dblp.org/

### Engineering Sources

- PyTorch releases: https://github.com/pytorch/pytorch/releases
- vLLM releases: https://github.com/vllm-project/vllm/releases
- SGLang releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo releases: https://github.com/ai-dynamo/dynamo/releases
- KServe releases: https://github.com/kserve/kserve/releases
- Kubernetes releases: https://github.com/kubernetes/kubernetes/releases

### Cross-day Archive Evidence

- 2026-08-08 Daily: `../08/README.md`
- 2026-08-10 Daily: `../10/README.md`
