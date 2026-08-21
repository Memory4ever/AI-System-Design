# Daily Research — 2026-08-19

**Archive Date:** 2026-08-19（Asia/Shanghai）

**Coverage Window:** 2026-08-17 09:02 ～ 2026-08-19 09:02（Asia/Shanghai）

**Archive Clock:** Wednesday；只生成 Daily，不生成当前周 provisional `2026-W34`。

**Status:** Daily Complete；3 Full Source Reviews Complete；Books Integration Complete

## Executive Summary

今天保留三项 first-public date 为 2026-08-17、且能够形成长期 AI System 机制增量的论文。三者共同把
Agent 设计从“只看最终模型输出”推进到显式中间状态：ClawGym II 在 opaque harness 与训练器之间建立
token-faithful call capture 和 prefix-tree reconstruction；CAPO 把 Prompt optimization 从固定 scalar reward
推进到 constraint residual 驱动的 primal-dual control；RUPA 把单步 confidence 推进为沿 trajectory dependency
传播的风险状态。

这三项都只提供作者实验。它们没有证明任意 harness 都可无损重建、Prompt constraints 已成为确定性 enforcement，
或 graph score 等同真实失败概率。日报先完成 primary-source、实验条件与相邻章节审计；Books 是否写入由后续
Source-Family Gate 决定。模型公司与 AI Infra 官方来源没有确认到本窗口内同等级的新机制事件。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google Research、Meta AI / FAIR、
Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、Qwen、DeepSeek、Kimi、
Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、StepFun、Xiaomi MiMo、
InclusionAI 与 Hugging Face Blog 的 Research、technical report、model/system card 与官方发布入口。

没有确认到 first-public date 位于本窗口、同时公开足够机制与长期证据的新模型或机构 Research。产品入口、旧页面
重排、单独能力声明和缺少 technical report 的 benchmark 不进入候选。

### Candidate Scoring

本组没有 retained candidate。

## 2. arXiv / 学术来源

### Source Coverage

检查 arXiv `cs.AI → cs.CL → cs.LG → cs.DC → cs.IR → stat.ML` new/recent surface，并用 Google Scholar、
OpenAlex、DBLP、Semantic Scholar 与 Hugging Face 做 discovery 与去重；Crossref 留给 Weekly metadata 核验。
候选日期均回到 arXiv submission history。P-PAS、GraniKV、Harness the Memory 等 first-public date 为 8 月 15～16 日，
属于 W33；Block-Layer VLA、Hallucination Snowball、FLOPs vs Real Work 分别 first-public 于 6 月或 4 月，不按 8 月 18 日
展示日期重写为本日事件。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence / Initial Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| ClawGym II | 2026-08-17 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2；Refine candidate `TRAIN-GRPO` |
| CAPO / DCAPO | 2026-08-17 | 5 | 4 | 5 | 4 | 5 | 5 | 28/30 | E2；Refine candidate `AGENT-PROMPT` |
| RUPA | 2026-08-17 | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | E2；Refine candidate `AGENT-REFLECTION` |

## Deep Analysis 1 — ClawGym II：Opaque Harness 需要可训练的数据边界

### Why → Principle

White-box Agent loop 直接拥有 observation、action、tool result 与 trajectory，因此容易计算 token mask、reward 和
policy ratio。成熟 harness 会自行压缩 Context、重试无效 tool call、调用 subagent，并把模型输出重新序列化；训练器
若只收集最终 transcript，会丢失原始 sampling tokens、分支身份和被 supersede 的调用。

稳定原则是：**不必打开 harness 内部控制流，但必须在 model-serving boundary 捕获训练所需的不可变事实，并把
call graph 与 rollout-level reward 分开重建。**

### Mechanism

```text
task workspace + opaque harness in isolated sandbox
→ serving proxy captures exact input/output tokens + rollout logprobs
→ longest-prefix matching reconstructs call prefix tree
→ remove retry dead leaves / over-branching / auxiliary trajectories
→ preserve shared prefixes once
→ PPO or GRPO consumes rollout-level reward on retained tree
→ token-in-token-out + importance correction protect train/serve identity
```

Harness 继续拥有 tool、Context、retry 与 environment control；proxy 只拥有 model-call evidence；verifier 拥有最终
workspace reward；trainer 拥有 token mask、advantage 与 update。论文明确承认：PPO 对 sibling branches 不传播 advantage，
采用 `gamma=lambda=1` 的简化；subagent/compaction paths 因 credit ambiguity 被排除。这些不是已经解决的细节，而是
black-box RL 的剩余边界。

### Evaluation Contract

- Policy：Qwen3-8B 与 Qwen3-30A3B；PPO / GRPO；OpenClaw 与 Claude Code 两种 harness。
- Training data：ClawGym-SynData；扩展实验使用合成 JobBench / OfficeQA-style tasks。
- Evaluation：ClawGym-Bench、PinchBench、JobBench-Easy、OfficeQA-Full；Pass@1；code verifier 与 rubric 混合。
- Judge：rubric 部分使用 GPT-5.4；ClawGym 混合权重为 code 0.7 / rubric 0.3。
- Training：200～400 optimization steps；硬件、precision、并发 sandbox 数、token/cost、wall time 与 production SLO
  为 `Not Disclosed`。

作者结果支持两种 harness 下的受限提升和 mix-harness 可训练性，不证明任意 proprietary harness 都能无损 capture，
也不证明相同 terminal reward 对所有 tree branches 都是正确 credit。Sandbox 隔离、proxy schema、harness revision、
tokenizer、inference kernel 与 verifier 必须共同组成 rollout identity。

### Trade-off / Connection / Evolution

```text
white-box single trajectory
→ black-box transcript collection
→ model-boundary token capture
→ prefix-tree reconstruction and filtering
→ future branch-aware credit / auxiliary-agent attribution
```

收益是复用成熟 harness 并避免重复 shared prefixes；代价是 proxy 成为 critical evidence plane，新增 retry/dead-leaf
识别、tree corruption、harness drift、reward broadcast bias 与 train/serve probability mismatch。简单 loop、短 trajectory、
强 step verifier 或必须逐 action credit 时，white-box integration 仍更可靠。

Owner 初判为 `TRAIN-GRPO`（Ch33），handoff 到 `TRAIN-RLHF`、`AGENT-WORKFLOW`、`AGENT-PLATFORM` 与
`PLATFORM-EVALUATION-SYSTEM`。

## Deep Analysis 2 — CAPO：Prompt 优化从静态权重转向 Constraint Feedback

### Why → Principle

固定 scalar reward 把 accuracy、tool overuse、handoff、prompt length、安全和格式提前压成一组常数。不同 domain 或
optimization round 的 active constraint 会变化；一个固定 penalty 可能提高 accuracy 却越过 hard threshold，Pareto
frontier 也不会自动选出满足部署约束的 operating point。

稳定原则是：**soft program 的搜索目标应由 measured constraint residual 动态定价，但 hard enforcement 仍在模型外。**

### Mechanism

CAPO 保持 task agent 冻结，维护 prompt pool 与每个约束的 multiplier：候选 Prompt 在 held-out metrics 上评估，
rewriter 根据失败案例与当前 `lambda` 提出 discrete rewrites，pool 按 Lagrangian score 保留，dual update 根据
`cost-threshold` residual 增减相应权重。DCAPO 再用 pool-based GRPO 训练一个 feedback/dual-conditioned rewriter；
task agent 本身仍不更新。

```text
versioned prompt pool + explicit thresholds
→ evaluate objective and per-constraint residuals
→ residual-conditioned rewrite proposals
→ feasibility-aware selection
→ dual update
→ regression / canary / external enforcement
```

### Evaluation Contract

论文覆盖 tau2 Airline/Retail/Telecom、GSM8K、AdvBench、Over-Rejection、CharCount、PUPA/IFBench 与 SWE-bench Lite；
比较 APO、GEPA、MOPO、evolutionary search、StablePrompt 与 fixed-penalty Agent-GRPO。Task agents 包含 frontier API
models 与 Ministral/Qwen3 系列；CAPO 最多通常 6 rounds，coding 4、progressive chatbot 12。论文给出 constraint-set、
model/editor scale、task-cluster shift、noise、dual-rate/threshold、rewrite-depth 与 mechanism ablations。

硬件、完整 API snapshot/cost、每项 concurrency、tail latency 与 production SLO 为 `Not Disclosed`。理论部分依赖 surrogate
space 的 strong concavity、rewrite-gradient alignment、bounded noise/pool 等假设；作者只测到 alignment 均值为正，
没有估计关键常数。实验支持“adaptive residual 比固定权重更常找到 empirical feasible prompt”，不证明 Prompt 能执行
安全策略或跨模型保持语义。

### Trade-off / Connection / Evolution

```text
manual prompt
→ fixed scalar prompt search
→ Pareto candidate pool
→ residual-driven primal-dual search
→ learned constrained rewriter
```

新增成本包括大量 candidate evaluation、multiplier oscillation、threshold/judge noise、Prompt overfitting、API drift 与
constraint gaming。约束少、稳定且可直接写成 deterministic validator 时，人工 Prompt + regression 更简单；高风险
authorization 永远不能由 Prompt feasibility 取代。Owner 为 `AGENT-PROMPT`（Ch74），handoff 到 `PLATFORM-EVALUATION-SYSTEM`、
`PLATFORM-SECURITY` 与 `PLATFORM-PRODUCTION`。

## Deep Analysis 3 — RUPA：Confidence 必须沿 Dependency 传播，但不能成为 Truth

### Why → Principle

Token entropy、sequence probability 和 verbalized confidence 是局部信号。Agent 失败可能来自数步以前的错误 tool call、
timeout 或错误假设；后续输出语气稳定并不消除上游 state dependency。把 trajectory 只当时间序列，也会把平行尝试与
因果 continuation 混为同一相关性。

稳定原则是：**风险状态需要显式 dependency graph，但 graph construction、calibration 与 action authority 必须分层。**

### Mechanism

RUPA 将 reasoning、tool call 和 observation 转成 nodes，以 temporal、progression、parallel、feedback 和 goal-alignment
relations 建有向图；local uncertainty 沿 learned relation weights 传播，再与 behavioral feature 和 goal alignment 合并为
trajectory confidence。公开实现使用规则 cue、tool signature 与 bge-m3 embedding 构边，因此图是 derived telemetry，
不是环境的真实 causal graph。

### Evaluation Contract

- Benchmarks：tau2、Terminal-Bench-2、GAIA。
- Models：6 个 26B～230B open-source model families。
- Baselines：predictive entropy、sequence probability、SAUP、Tracer、UProp。
- Metrics：AUROC、AUPRC、best-F1；prefix early detection；uncertainty-guided multi-sample action selection。
- Artifact：official repository linked from paper；hardware、precision、candidate count、额外 latency/cost、concurrency 与 SLO
  为 `Not Disclosed`。

作者实验支持 graph feature 在其 frozen benchmarks 上补充 local/sequence proxy，并改善 lower-risk candidate selection；
不证明 score 已校准为 failure probability，也不证明 cue/embedding edges 是因果关系。Best-F1 使用最优 threshold，不能
直接作为 production operating point。

### Trade-off / Connection / Evolution

```text
token confidence
→ sequence / step aggregation
→ trajectory history features
→ relation-aware graph propagation
→ calibrated selective critic / verifier / human escalation
```

图方法能保留长程依赖，却新增 edge false positive/negative、embedding drift、graph growth、传播放大、threshold calibration
和额外 inference work。短任务、强 executable verifier 或高风险 action 仍应直接验证；uncertainty 只触发 review/replan，
不能授权副作用。Owner 为 `AGENT-REFLECTION`（Ch80），handoff 到 `PLATFORM-EVALUATION-SYSTEM`、`AGENT-WORKFLOW`
与 `PLATFORM-TRACE`。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、
Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与
OpenXLA 顺序检查官方 Release、RFC、PR 和文档入口。

没有确认到本窗口内同时满足 release identity、机制变更、相关代码路径与完整 workload contract 的独立 retained
release。搜索结果中的旧 release 和未来版本聚合不按抓取时间重写事件日期。

### Candidate Scoring

本组没有 retained candidate。

## Evidence Level and Fact Boundary

- **E2 / Primary paper:** 三项均阅读全文，包括 metadata、related work、method/公式、implementation、evaluation、
  baselines、ablation/sensitivity、limitations 或由正文重建的 threats、关键 Appendix 与公开 artifact 入口。
- **Official fact:** arXiv v1 日期、作者披露的算法、实验和仓库；作者 benchmark 只在其 workload contract 内成立。
- **Community/discovery:** Scholar、OpenAlex、DBLP、Semantic Scholar、Hugging Face 和搜索排序只用于召回与去重。
- **Project inference:** Stable owner、技术演进与 Books decision 来自论文和目标/相邻章节联读，不是作者声明。
- 未披露的 hardware、precision、tokens、batch/concurrency、cost、latency/SLO 或 verifier calibration 均写为
  `Not Disclosed`。

## Knowledge Tree Position

| Candidate | Stable Owner | Current / Legacy | Adjacent Chapters Read | Initial Decision |
| --- | --- | --- | --- | --- |
| ClawGym II | `TRAIN-GRPO` | Ch33 / Ch29 | Ch31、Ch33、Ch81、Ch84 | Refine — Existing Argument Candidate |
| CAPO / DCAPO | `AGENT-PROMPT` | Ch74 / Ch70 | Ch73、Ch74、Ch75、Ch66 | Refine — Existing Argument Candidate |
| RUPA | `AGENT-REFLECTION` | Ch80 / Ch76 | Ch66、Ch69、Ch79～81 | Refine — Existing Argument Candidate |

## Recommended Action

- ClawGym II：已 refine Ch33，补入 opaque harness call evidence → prefix-tree trajectory → policy update 的长期数据流；
  未复制 benchmark，也没有把 terminal reward 广播写成已解决 credit assignment。
- CAPO：已 refine Ch74，把 Prompt lifecycle 从 manual/fixed objective 推进到 threshold-residual feedback；Prompt
  仍不是 enforcement boundary。
- RUPA：已 refine Ch80，只补 relation-aware uncertainty sensor 与 calibrated escalation 的连接；graph score
  不等于 truth probability。

## Ignored Noise

- P-PAS、GraniKV、Harness the Memory 等 first-public 于 8 月 15～16 日，属于 W33 correction/discovery，不重复计为
  W34 Daily event。
- Block-Layer VLA、Hallucination Snowball、FLOPs vs Real Work 的真实 v1 日期为 6 月或 4 月，不能按 8 月 18 日列表
  展示时间重写。
- HyperSkill、QUMem、Skill2Query 等同批 memory/skill papers 留给 Sunday cross-source dedup；今天不为增加候选数
  在未完成同等全文审计时评分。
- 旧 Release、聚合新闻、产品 headline、社区 benchmark 与缺少 workload contract 的倍率。

## Repository Changes

- 新建 `papers/2026/08/19/README.md`，记录三项 primary-source Full Review 与 Books 候选判断。
- Refine `TRAIN-GRPO` Ch33：加入 opaque harness serving-boundary capture、prefix-tree reconstruction、dead/auxiliary
  branch filtering、token-faithful train/serve identity 与未解决 credit boundary。
- Refine `AGENT-PROMPT` Ch74：加入 fixed scalar / Pareto → constraint-residual primal-dual search 的演进，同时保留
  deterministic enforcement、regression、canary 与 rollback。
- Refine `AGENT-REFLECTION` Ch80：加入 local/sequence confidence → dependency-aware trajectory uncertainty → selective
  verifier/escalation 的演进，并明确 derived graph 不是 causal truth。
- 更新 `docs/LEARNING_STATE.md` 的 2026-08-19 checkpoint；ROADMAP、DECISIONS 与 7 Part / 84 章结构不变。
- 保持 2025 Weekly 暂停点 `W08 Passed；Next: W09；Paused by user`，不恢复历史回填。

## Open Questions

1. ClawGym II 怎样对 subagent、Context compaction 与 forked siblings 做非广播式 credit assignment，并证明 serving proxy
   在 harness/version failure 下不丢 token/logprob identity？
2. CAPO 在 threshold/judge drift、相互冲突 constraints 与在线流量改变时，怎样校准 dual control 并避免 Prompt gaming？
3. RUPA 的 derived edges 怎样用 executable/environment evidence 校准，并在 graph growth、domain shift 与高风险 action 下
   定义 abstain / verifier / human escalation operating point？
4. W33 correction queue 中的 P-PAS、GraniKV 与 Harness the Memory 应怎样按 8 月 15～16 日 owner date 回写，而不混入本日？

## Sources

- arXiv cs.AI new（展示 2026-08-18；访问 2026-08-19）：https://arxiv.org/list/cs.AI/new
- arXiv cs.CL new（展示 2026-08-18；访问 2026-08-19）：https://arxiv.org/list/cs.CL/new
- arXiv cs.LG new（展示 2026-08-18；访问 2026-08-19）：https://arxiv.org/list/cs.LG/new
- arXiv cs.DC new（展示 2026-08-18；访问 2026-08-19）：https://arxiv.org/list/cs.DC/new
- ClawGym II metadata（v1 first-public 2026-08-17；访问 2026-08-19）：https://arxiv.org/abs/2608.16798
- ClawGym II v1 full text（访问 2026-08-19）：https://arxiv.org/html/2608.16798v1
- CAPO metadata（v1 first-public 2026-08-17；访问 2026-08-19）：https://arxiv.org/abs/2608.16068
- CAPO v1 full text（访问 2026-08-19）：https://arxiv.org/html/2608.16068v1
- RUPA metadata（v1 first-public 2026-08-17；访问 2026-08-19）：https://arxiv.org/abs/2608.16002
- RUPA v1 full text（访问 2026-08-19）：https://arxiv.org/html/2608.16002v1
- RUPA official repository（访问 2026-08-19）：https://github.com/icip-cas/RUPA
- OpenAI Research（访问 2026-08-19）：https://openai.com/research/
- Anthropic Research（访问 2026-08-19）：https://www.anthropic.com/research
- Google DeepMind publications（访问 2026-08-19）：https://deepmind.google/research/publications/
- Hugging Face Blog（访问 2026-08-19）：https://huggingface.co/blog
- vLLM releases（访问 2026-08-19）：https://github.com/vllm-project/vllm/releases
- SGLang releases（访问 2026-08-19）：https://github.com/sgl-project/sglang/releases
- KServe releases（访问 2026-08-19）：https://github.com/kserve/kserve/releases
