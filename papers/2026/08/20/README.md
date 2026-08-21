# Daily Research — 2026-08-20

**Archive Date:** 2026-08-20（Asia/Shanghai）

**Coverage Window:** 2026-08-18 09:01 ～ 2026-08-20 09:01（Asia/Shanghai）

**Archive Clock:** Thursday；只生成 Daily，不生成当前周 provisional `2026-W34`。

**Status:** Daily Complete；3 Full Source Reviews Complete；Books Integration Complete

## Executive Summary

今天保留三项 first-public date 为 2026-08-17、但因 arXiv Wednesday listing 延迟到 8 月 19 日才进入稳定发现面的
论文。三者共同强化一个长期原则：**模型输出、内部信号与 Skill 只是 proposal；选择、事实与资源安全必须有独立、
可校准或可执行的 authority。**

CASE 说明多数投票在 correlated-error / modal-wrong regime 中会随采样数增加而更差；hidden-state selector 只有在
question-grouped、leakage-free decodability 已校准时才值得启用。Fool's Gold 构造性地说明，若输出分布被主动塑造成
一致而错误，self-consistency、semantic entropy 与重复采样不能在没有独立 ground truth 时恢复 truth。SkillEffect
则把资源敏感的 Agent program 从 Prompt/Skill 建议推进为 checked lowering：独立 checker 重建 bounded target，
capacity lease 与 postcondition 共同决定是否执行和发布。

三项均只有作者实验，不能外推为所有模型/任务的默认策略。模型机构与 AI Infra 官方入口没有确认到本窗口内同等级、
且具备稳定 event date 和 primary mechanism evidence 的独立事件。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google Research、Meta AI / FAIR、
Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、Qwen、DeepSeek、Kimi、
Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、StepFun、Xiaomi MiMo、
InclusionAI 与 Hugging Face Blog 的 Research、technical report、model/system card 与发布入口。

没有确认到本窗口内 first-public 且公开足够长期机制的新机构事件。OpenAI Research 与 Google DeepMind publication
index 的最新高信号条目早于窗口；产品页、旧内容重排和缺少机制的能力 headline 不计为候选。

### Candidate Scoring

本组没有 retained candidate。

## 2. arXiv / 学术来源

### Source Coverage

检查 arXiv `cs.AI → cs.CL → cs.LG → cs.DC → cs.IR → stat.ML` new/recent surface，并用 Google Scholar、
OpenAlex、DBLP、Semantic Scholar 与 Hugging Face 做 discovery/metadata/dedup；Crossref 留给 Weekly。Wednesday
list 中的 Aegis、GxP-Agent、Block-Layer VLA、Hallucination Snowball 与 FLOPs replication 等条目按 abs metadata
分别属于 4～6 月，不按展示日制造新事件。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence / Initial Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| CASE / Decodability | 2026-08-17 | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | E2；Refine candidate `MODEL-SAMPLING` |
| Fool's Gold | 2026-08-17 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | E2；Refine candidate `PLATFORM-EVALUATION-SYSTEM`；security recipe frozen |
| SkillEffect | 2026-08-17 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2；Refine candidate `AGENT-TOOL-CALLING` |

## Deep Analysis 1 — CASE：先证明 Correctness Signal 可读，再替换 Voting

### Why → Principle

Majority voting 假设正确答案在 samples 中形成 modal cluster；当模型在困难问题上稳定地产生同一个错误答案时，
增加 `N` 会把错误 mode 的票数估计得更精确。Hidden-state probe 可能读到输出文本没有表达的 correctness signal，
但普通 random split 会让同一 question 的 candidates 同时出现在 train/test，probe 只需识别 question identity 和该题
总体难度，就能得到虚假高分。

稳定原则是：**选择器必须在其实际 decision unit 内被校准。**要从同一 question 的 candidates 中挑一个答案，评估
就必须按 question 分组，并测量 correct candidate 是否在 incorrect candidates 之上，而不是跨题分类准确率。

### Mechanism

```text
question
→ sample N candidates
→ read answer-token hidden state at a selected late layer
→ linear correctness gate ranks candidates
→ CASE selects highest score

calibration set:
  question-grouped within-question AUC
  → decodability predicts CASE-vs-vote gain
  → below threshold: retain voting / verifier / abstain
```

论文将 modal-wrong、correct minority 且 gate AUC `>0.5` 的情形称为 Byzantine regime。在其 light-tailed score 假设下，
增加 candidates 会让 CASE 有更多 correct extremes 可选，而 voting 更稳定地收敛到错误 mode。Decodability 是选择器
是否可用的 measurement，不是 answer truth probability，也不具有固定跨任务阈值。

### Evaluation Contract

- Models：Qwen2.5 1.5B～14B、Qwen2.5-Math、Llama-3-8B 及多个 7B～70B medical specialists；FP16。
- Tasks：LogiQA、MedQA、MedMCQA、PubMedQA open/closed-book、MATH-500、GSM8K、GPQA。
- Sampling：每题 16～20 candidates，temperature 0.7、top-p 0.95、最多 512 new tokens。
- Hardware：NVIDIA A6000/A100；70B 使用 device-map sharding。
- Metrics：question-grouped within-question ranking AUC、CASE/voting accuracy、bootstrap CI、label permutation null。
- Main held-out relationship：calibration-half decodability 对 disjoint deployment-half gain 的 Pearson `r=0.75`，论文
  给出的约 `0.60` boundary 只属于其 difficulty distribution；production concurrency/SLO/cost 未披露。

### Trade-off / Connection / Evolution

```text
single sample
→ majority / semantic cluster voting
→ output-space self-confidence
→ leakage-free hidden-state competence readout
→ decodability-gated selector
→ external verifier / abstention when signal is absent
```

收益是 correlated-error regime 中不再把 popularity 当 correctness；代价是需要 labeled calibration、model/layer/task
绑定、hidden-state access 和 OOD revalidation。论文只研究 multiple-choice final answer token，free-form claim、intermediate
reasoning 与 model revision 仍是边界。Owner 初判 `MODEL-SAMPLING`（Ch20），handoff 到 Ch66 Evaluation。

## Deep Analysis 2 — Fool's Gold：一致性不是对抗性分布中的 Truth Signal

### Why → Principle

Self-consistency、semantic entropy 与 sampling-based self-check 假设错误在 samples 间有足够多样性；一旦模型分布被
训练成在关键元素上稳定地产生相同错误值，低 entropy 和高 consensus 反而成为错误的稳定性指标。论文用 safety-
removal threat model 构造这种分布，重要的长期证据不是 defense recipe，而是：**没有独立 ground truth 时，任何只观察
同一受控分布的 selector 都不能把 fluent decoy 与正确答案分开。**

### Mechanism and Evidence Boundary

作者在 open-weight checkpoint 中把 deception 绑定到 refusal 被移除后的 attacked state，同时用 refusal pin / benign
leash 约束 clean state；关键 procedure elements 被映射到注册的错误值。攻击者可白盒修改权重并采样最多 `K=64`，
但 threat model 明确假设没有领域专家、实验室、真实 reference 或 retrieval-verified ground truth。

实验覆盖 7 个、9B～122B、dense/MoE model families；6 个通过预注册 efficacy gate，1 个小模型作为失败边界。
公开结论使用 frozen split、registered critical-element registry、GPT-4.1 decomposed judge、154-row blinded expert audit 与
第二 judge family。作者报告的 decoy/fatal/consensus 数字只属于 chemical/biological procedural threat model；训练硬件、
完整 lifecycle cost 与部署 SLO 并非通用合同。

论文同时暴露自身限制：10～49% attacked draws 仍可能 escape；benign SFT erosion 未观察到 plateau；只覆盖 weight-space
safety removal，不覆盖 in-context jailbreak；内容 verdict 主要依赖一个 judge family，expert sample 也只有一名专家。
安全机制本身具有 deception、disclosure 与误伤风险，因此不把 recipe 写入 Books 的操作性正文。

### Trade-off / Connection / Evolution

对 Evaluation 的长期影响是：

```text
sample agreement / low semantic entropy
→ useful only under calibrated natural-error assumptions
→ source/model-family correlation audit
→ adversarial-distribution and shared-blind-spot test
→ independent evidence / executable verifier
→ otherwise abstain
```

它强化 Ch66 的 claim-confidence boundary：更多同源 samples 不能创造独立 evidence；partial verifier coverage 只能保护
被验证 elements，未覆盖 critical claim 仍决定整体风险。Owner 初判 `PLATFORM-EVALUATION-SYSTEM`（Ch66），Ch72 只保留
threat-model handoff，defensive-deception mechanism 保持 `Experimental / Security-sensitive`。

## Deep Analysis 3 — SkillEffect：Skill Program 必须经过可证明的 Resource Lowering

### Why → Principle

Prompt/Skill 可以正确描述“流式处理”或“分块读取”，但模型生成的具体程序仍可能 eager-load 整个输入，在单次 tool
call 的 memory cap 下 OOM。只做 cgroup reject 能 fail closed，却不能把原本正确的 computation 转成可运行版本；让模型
重试又无法证明语义等价或峰值上界。

稳定原则是：**优化建议不能获得执行 authority；bounded implementation 必须由独立 checker 从 source relation 与
immutable input facts 重新构造，并在资源租约和 postcondition 下提交。**

### Mechanism

```text
LLM-produced source program + immutable input
→ recognize one audited relation plugin
→ extract semantic parameters and input facts
→ checker rebuilds bounded IR / target
→ calculate platform-calibrated live-set bound
→ atomic capacity lease
→ bounded VM / cgroup execution
→ postcondition + no-limit-event publication gate
→ publish or abstain without partial output
```

每个 plugin 提供 source recognizer、fact extractor、bounded constructor、arena bound 与 postcondition；common runtime 只复用
dispatch、lease、execution 和 publication。它不自动验证任意 Python，也不从模型声明接受 memory bound。

### Evaluation Contract

- Workloads：6 tool families × 4 parameterizations = 24 task–Skill pairs；deterministic generator/verifier；3 input sizes。
- Inputs：最大包括 100K spreadsheet rows、2M events、150K×512 AnnData、65,536×1,024 Zarr、2M CSV rows、
  500K FASTA records。
- Caps：64～2048 MiB fixed sweep；每 physical cell 3 次；swap=0、cgroup v2、OOM/limit counters 与 verifier 联合判定。
- Tool testbed：Apple M5 / 16 GiB，Linux 6.8 aarch64 VM、4 vCPU；container 2 vCPU、CPython 3.11.15。
- Model generation：Qwen2.5-14B-AWQ 或 Mistral-7B，单 A800-80GB PCIe；GPU 不计入 tool cap。
- Results boundary：bounded references 在最大输入降低 peak，但 Prompt/retry/composition 不能稳定构造合法计划；只有注册
  lowering 在 24/24 tasks / 72 repeats 通过。数字不外推到 remote/stateful tools。

### Trade-off / Connection / Evolution

```text
Skill as instruction
→ model-generated concrete tool program
→ profile/reject-only cap gate
→ audited relation + independently rebuilt bounded target
→ capacity lease + staged publication
→ future transaction/compensation for remote effects
```

收益是把“可能省内存”升级为可执行 capacity invariant；代价是 closed grammar、逐 relation 审计、platform calibration、
checker TCB、保守 reserve 和 extension cost。当前只覆盖 deterministic local read-only programs；email、payment、mutable
services 仍需 idempotency、authorization 与 transaction/compensation。Owner 初判 `AGENT-TOOL-CALLING`（Ch78），handoff
到 Ch63/70/72/84。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、
Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与
OpenXLA 顺序检查官方 Release、RFC、PR 和文档入口。

未确认到本窗口内同时具备 immutable release date、机制说明、代码路径与完整 workload contract 的独立 retained
工程事件。搜索命中的 SGLang/vLLM release 页面包含更晚或更早版本聚合，不能按 crawler date 记为本日事件。

### Candidate Scoring

本组没有 retained candidate。

## Evidence Level and Fact Boundary

- **E2 / Primary paper:** 三项均阅读 metadata、method/algorithm、implementation、evaluation、baselines、ablation/
  sensitivity、limitations 与关键 Appendix/registry definitions；只有作者实验，无独立复现。
- **Official facts:** arXiv v1、论文披露的 artifacts/configs/results；作者数字只属于各自 workload contract。
- **Discovery/index:** Scholar、OpenAlex、DBLP、Semantic Scholar、Hugging Face 和 arXiv listing 只负责召回/去重。
- **Project inference:** Stable owner、演进与 Books decision 来自 primary source 和目标/相邻章节联读。
- 未披露的 hardware、precision、length、batch/concurrency、cost、latency/SLO 与 threat coverage 均为 `Not Disclosed`。

## Knowledge Tree Position

| Candidate | Stable Owner | Current / Legacy | Adjacent Chapters to Read | Initial Decision |
| --- | --- | --- | --- | --- |
| CASE / Decodability | `MODEL-SAMPLING` | Ch20 / Ch20 | Ch18～20、Ch66 | Refine — Existing Argument Candidate |
| Fool's Gold | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Ch20、Ch66、Ch72 | Refine evidence boundary；security recipe frozen |
| SkillEffect | `AGENT-TOOL-CALLING` | Ch78 / Ch74 | Ch77～79、Ch63/72/84 | Refine — Existing Argument Candidate |

## Recommended Action

- CASE：已 refine Ch20，只沉淀 decodability-gated selection 与 question-grouped leakage boundary；未保留论文阈值/
  headline gain。
- Fool's Gold：已 refine Ch66，只沉淀“同源一致性在 adversarially correlated distribution 下不是 truth evidence”；
  未写 defense recipe 或 hazardous examples。
- SkillEffect：已 refine Ch78，沉淀 proposal → checked lowering → capacity lease → postcondition publication；保留
  closed-relation 与 local/read-only 边界。

## Ignored Noise

- Aegis、GxP-Agent、Block-Layer VLA、Hallucination Snowball、FLOPs replication 等在 Wednesday listing 中重现，但
  first-public date 属于 4～6 月，不按展示日计为 W34 event。
- `The Price of Thinking` 的单一 API/model/task experiment 只保留为 discovery signal；没有形成跨模型机制结论。
- 旧 Release、产品 headline、leaderboard、无完整 workload contract 的倍率和社区转述。
- 其余同批论文留给 Sunday cross-source dedup；今天不在未完成同等全文审计时评分。

## Repository Changes

- 新建 `papers/2026/08/20/README.md`，记录三项 primary-source Full Review 与 Books 初判。
- Refine `MODEL-SAMPLING` Ch20：加入 question-grouped within-question decodability、selector admission 与 voting/
  verifier coexistence boundary。
- Refine `PLATFORM-EVALUATION-SYSTEM` Ch66：加入 adversarially correlated false mode、independent-ground-truth
  coverage 与同源一致性不能升级为 truth acceptance 的边界；security recipe 保持冻结。
- Refine `AGENT-TOOL-CALLING` Ch78：加入 audited relation、checker-rebuilt bounded target、capacity lease 与
  postcondition-gated staged publication。
- 更新 `docs/LEARNING_STATE.md`；ROADMAP、DECISIONS 与 7 Part / 84 章结构不变。
- 保持 2025 Weekly 暂停点，不恢复历史回填。

## Open Questions

1. CASE 的 decodability 在 free-form claims、intermediate steps、model revision 与 OOD task 上怎样重校准？
2. Fool's Gold 的构造是否意味着任何无外部 oracle 的 confidence estimator 都无法识别 correlated false mode；哪些
   partial-verifier coverage 才能形成可用下界？
3. SkillEffect 怎样扩展到 mutable/remote side effects，并把 relation checker、capacity lease 与 transaction commit
   放进同一 failure/recovery contract？
4. 8 月 19 日 listing 的 broader candidate queue 在 Sunday W34 是否形成新的 Source Family 或跨周 spillback？

## Sources

- arXiv cs.AI new（Wednesday 2026-08-19 listing；访问 2026-08-20）：https://arxiv.org/list/cs.AI/new
- arXiv cs.CL new（访问 2026-08-20）：https://arxiv.org/list/cs.CL/new
- arXiv cs.LG new（访问 2026-08-20）：https://arxiv.org/list/cs.LG/new
- arXiv cs.DC new（访问 2026-08-20）：https://arxiv.org/list/cs.DC/new
- CASE metadata（v1 first-public 2026-08-17；访问 2026-08-20）：https://arxiv.org/abs/2608.17124
- CASE v1 full text（访问 2026-08-20）：https://arxiv.org/html/2608.17124v1
- Fool's Gold metadata（v1 first-public 2026-08-17；访问 2026-08-20）：https://arxiv.org/abs/2608.17202
- Fool's Gold v1 full text（访问 2026-08-20）：https://arxiv.org/html/2608.17202v1
- SkillEffect metadata（v1 first-public 2026-08-17；访问 2026-08-20）：https://arxiv.org/abs/2608.17007
- SkillEffect v1 full text（访问 2026-08-20）：https://arxiv.org/html/2608.17007v1
- OpenAI Research（访问 2026-08-20）：https://openai.com/research/index/
- Google DeepMind publications（访问 2026-08-20）：https://deepmind.google/research/publications/
- Hugging Face Blog（访问 2026-08-20）：https://huggingface.co/blog
- vLLM releases（访问 2026-08-20）：https://github.com/vllm-project/vllm/releases
- SGLang releases（访问 2026-08-20）：https://github.com/sgl-project/sglang/releases
