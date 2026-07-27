# AI Research Daily — 2026-08-14

- **Research date:** 2026-08-14（Asia/Shanghai）
- **Coverage window:** 2026-08-12 00:00 ～ 2026-08-14 08:50（Asia/Shanghai）
- **Access date:** 2026-08-14
- **Status:** Daily primary-source review completed；4 个 `20+` 学术候选完成全文核验；4 个既有章节 refined

## Executive Summary

今天没有确认到窗口内足以形成长期机制的模型机构公告或 AI Infra release。高价值证据集中在 8 月 12 日
首次公开的四篇论文，它们共同补全四条已经存在、但仍缺少中间机制的演进路线：

```text
explicit future video → joint WAM → direct policy + latent predictive interface
generic gist compression → typed preservation contract → per-slice loss evidence
stored candidate → exact-predecessor activation → authoritative workflow head
skill catalog → paired utility gate → trajectory-level failure and cost attribution
```

四篇均为 arXiv v1。作者实验分别来自 LIBERO/LIBERO-Plus、LoCoMo、有限状态空间模型与两个 Skill
benchmark；它们支持受控条件下的 mechanism，不证明真实机器人、开放会话、物理存储或任意 Agent Skill
生态中的通用生产结论。完成章节及相邻章节去重后，本日 refine Ch26、Ch75、Ch81、Ch84；没有改变
ROADMAP、Part、章节号或旧方案仍成立的边界。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple Machine Learning Research、Google DeepMind、Google Research、
Meta AI / FAIR、Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、
Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、
StepFun、Xiaomi MiMo、InclusionAI 与 Hugging Face Blog 的可访问 official Research/News/Publications、
model/system card、organization repository 和 technical-report surface。

没有确认到 first-public date 位于本次窗口、同时公开足够 mechanism 且达到 `20/30` 的机构候选。此结论
仅表示本次可访问面的实际覆盖；搜索索引未返回结果不能证明机构没有更新，旧公告和被重新索引的论文也
没有被移动到今天。

### Candidate Scoring

本组没有新增评分候选。

## 2. 论文与学术来源

### Source Coverage

按 `cs.AI → cs.CL → cs.LG → cs.DC → cs.IR → stat.ML` 检查 arXiv recent，并以 cs.CV、cs.RO、
cs.SE、cs.CR、cs.AR、cs.PF、cs.OS、cs.PL 与 cs.MA 主题交叉筛选。arXiv 8 月 13 日 recent list
显示 211 条 cs.AI entries；这里只保留与 AI System 知识树相关且达到阈值的四项。Hugging Face Daily
Papers、Semantic Scholar、Google Scholar、OpenAlex 与 DBLP 仅用于发现、身份和去重；所有日期、方法、
实验和限制均回到 arXiv v1 HTML 正文核验。

四个 retained candidates 的 first-public date 均为 `2026-08-12`；8 月 13 日出现在 recent list 是展示日，
不是新的事件日期。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence Level |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Agent Skills Can Be Harmful | 2026-08-12 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、paired executable runs 与人工归因；两组 benchmark、单篇预印本 |
| Beyond Memory: A Transactional Continuity Kernel | 2026-08-12 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2 — arXiv v1 全文、bounded executable model；未验证真实 storage/side effects |
| Foresight Without Seeing / ForeWAM | 2026-08-12 | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | E2 — arXiv v1 全文、LIBERO/LIBERO-Plus 与 component ablation；无 real-world robot evidence |
| The Sleeping Agent | 2026-08-12 | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | E2 — arXiv v1 全文、LoCoMo matched evaluation 与 preservation ablation；单一 summarizer pipeline |

### Deep Analysis 1 — Skill：从“是否有帮助”到差分归因

#### Why

Skill 的 topic 与任务相关，不代表其 operational path 合适。它可能把示例当成任务要求、修改 dependency/cwd
后在错误环境验证、把可选 checklist 变成 mandatory workflow，或让长 skill body 在每轮重复占用 Context。
只观察最终失败或平均 pass rate 无法把问题归因到 Skill、模型方差、环境或 verifier。

#### Principle

Skill admission 需要 paired marginal evidence：固定 task、model、agent framework、repository/environment 与
verifier，只改变 skill setup；再把 correctness difference 与 cost difference 定位到具体 instruction、trajectory
step、artifact 或 environment mutation。Reference run 是 contrastive evidence，不是完整 ground truth。

#### Mechanism

论文在 SkillsBench 的 84 tasks / 11 domains 与 SWE-Skills-Bench 的 490 repository tasks 上增加 matched public
skills，比较 no-skill、target skill 与 alternative skill runs。最终审计集包含 125 个 functional failures 和 182 个
efficiency regressions。功能失效拆为 instruction-requirement、environment-state 与 task-implementation surface；
成本拆为 context bloat、excessive procedure 与 dependency resolution。SkillTriage 再从 paired trajectories 提取
差异 evidence，而不是只输出一个标签。

#### Trade-off / Evidence Boundary

- 307 cases 是经过人工排除 ambiguous、verifier-narrow 与 duplicate cases 后的归因集，不是总体 failure rate。
- 两个 benchmark 与所选 skill ecosystem 不能代表所有模型、harness 或 domain。
- 自动归因在相邻 taxonomy 上仍有 boundary error；应暴露证据，不应让分类器直接禁用 Skill。
- 更严格 paired run、trajectory capture 与 canary 会增加评估成本，但换来可定位的 rollback evidence。

#### Connection / Evolution / Recommended Action

主 owner 为 `AGENT-PLATFORM`（Current Ch84，Legacy Ch80），Ch75/81 只接收 Context cost 与 Workflow budget
handoff。关系为 `Direct Evolution`：catalog/activation metadata → paired utility Gate → trajectory-level attribution。
`Refine — Existing Argument`，不保留论文 failure frequency 作为生产先验。

### Deep Analysis 2 — Workflow：从 retention 到 authoritative activation

#### Why

Agent 的 model、tool、compactor 与 recovery worker 都可能写 candidate state。对象已写入 storage 只证明它存在，
不证明它是当前事实；stale retry、自授权 proposal、重复 effect 与 writer handoff race 都可能推进错误状态。

#### Principle

Authority 是从当前 branch head 的可达性。慢而不可靠的 proposal/evaluation 在 transaction 外完成，只有短小、
确定的 activation step 可以对 exact predecessor、pre-state authority、freshness、effect identity 与 lifecycle 做
最终复核。候选内容不能给自身授予写入它所需的权限。

#### Mechanism

Continuity Kernel 将 proposal 绑定到 exact head 或 typed absence，并产生 `Commit / Reject / Quarantine / Defer`
之一；只有 Commit 原子安装 state、authority、lineage、effects、outcome 与 receipt。bounded Python model 在深度 7
探索 2,808,230 reachable states，并对 exact succession、pre-state authorization、effect identity、writer fencing、
handoff 与 restoration 等已编码 invariants 检查到零 violation。

#### Trade-off / Evidence Boundary

- bounded exploration 证明有限抽象内部的一致性，不证明 PostgreSQL/FoundationDB/Raft 的物理实现。
- WAL crash、network partition、storage engine bug、signature durability 与外部 side-effect atomicity 未被覆盖。
- 17 stage checks、double freshness 与 multi-key serialization 增加 commit latency 和 contention。
- single-writer、短生命周期、无副作用任务仍可使用 version/CAS；完整 kernel 不是所有 Agent 的默认答案。

#### Connection / Evolution / Recommended Action

主 owner 为 `AGENT-WORKFLOW`（Current Ch81，Legacy Ch77），Ch77 仍拥有事实/经验 Memory，Ch84 拥有平台
policy。关系为 `Layering / Dependency`：durable storage → typed candidate → authoritative activation。
`Refine — Existing Argument`，只吸收 activation contract 与 realization boundary。

### Deep Analysis 3 — Embodied：预测未来不等于必须生成未来画面

#### Why

显式 future-video WAM 把 predictive dynamics 暴露给 action path，却把 iterative video denoising 放入 control
critical path；直接 VLA 更快，但移除未来生成时也可能失去 action-facing predictive interface。

#### Principle

“是否建模未来”与“是否在部署时 materialize pixels”是两个正交选择。可以在训练期用 future observation 和
teacher 塑造 latent predictive state，部署时只把 versioned latent interface 交给 action policy。

#### Mechanism

ForeWAM 在 current visual latent 与 stochastic future slots 上执行一次 Video DiT prefill，将逐层 Future-KV 复用到
action denoising；16 个 dynamics registers 由 frozen latent-action teacher 监督。训练使用 future video/action flow
matching，deployment 不需要真实 future frames 或 teacher。实验使用 2B policy、32-step action horizon、双视角
`224×224`、8D proprioception、7D action；standard 为 10 denoising steps，Flash variant 为 2 steps。

#### Trade-off / Evidence Boundary

- 标准 LIBERO 每 task 50 rollouts；LIBERO-Plus 只覆盖作者 observed subset，不能证明 real-world 或跨 embodiment。
- single A800-80GB 的 568/220ms 是 standalone action-generation latency，不是 task-completion time 或 control SLO。
- component ablation 支持 Future-KV 与 LA supervision 的组合，但不能证明 registers causal 或 control-sufficient。
- explicit future visualization 在 human audit 需要时仍有价值；纯 direct policy 在 deadline 极紧时仍可能更合适。

#### Connection / Evolution / Recommended Action

主 owner 为 `MULTIMODAL-EMBODIED-VLA`（Current Ch26），Ch25 继续拥有 World Model semantics。关系为
`Direct Evolution`：explicit future rollout → joint WAM → direct policy + latent predictive interface。
`Refine — Existing Argument`，性能数字只留在本 Daily 的 workload contract 中。

## Full Source Review Addendum — Four `20+` Candidates

### The Sleeping Agent — 27/30

- **Problem / Previous Design / Changed Constraint:** truncation 简单且 recency-preserving；generic gist 能在固定 token
  budget 保留更多关系。长会话开始承担 temporal query 后，aggregate compression quality 无法保证 dates/order。
- **Mechanism / State / Flow:** SWC 先按 salience 分层，再对 mid-priority history 做 gist abstraction；temporal variant
  在 prompt 中显式保护 temporal anchors。compressed view 是 derived Context，raw conversation 仍是 evidence owner。
- **Evaluation Contract:** LoCoMo 10 conversations；1,935 matched text-only questions，主 aggregate 使用 categories 1–4
  的 1,501 questions；Claude Sonnet 4.6 answer、Haiku compression/judge、temperature 0、2,000 bootstrap resamples。
- **Evidence Proves / Does Not Prove:** 单句 temporal protection 在该 pipeline 中把 temporal-expression preservation 从
  3.05% 提到 62.39%，并改善 matched temporal slice；不证明其他 summarizer、language 或 Memory pipeline 同样有效。
- **Trade-off / Previous Design / Owner:** temporal fields 增加 tokens 与 schema burden；非 temporal task 仍可使用普通 gist。
  Owner `AGENT-CONTEXT`（Ch75）；`Refine — Existing Argument / Experimental`。

### Agent Skills Can Be Harmful — 29/30

- **Problem / Mechanism:** paired executable runs 固定 task/model/framework/environment/verifier，比较 no-skill 或 matched
  alternative，使用 trajectory/artifact/cost difference 归因 Skill-induced functional failure 与 efficiency regression。
- **State Ownership:** registry 拥有 immutable Skill；run trace 拥有 observed behavior；attribution 是 review evidence，
  不能自动获得 rollout authority。
- **Evaluation:** SkillsBench 84 tasks/11 domains + SWE-Skills-Bench 490 repository tasks；665 labeled candidates 经审计形成
  307 cases。无公开 hardware/concurrency/SLO；这些字段为 `Not Disclosed`。
- **Limits:** curated cases 不是 prevalence，manual taxonomy 与 automatic triage 都有 boundary error。
- **Owner / Decision:** `AGENT-PLATFORM`（Ch84）；`Refine — Existing Argument / Experimental`。

### Beyond Memory — 29/30

- **Problem / Mechanism:** candidate preparation 与 authoritative activation 分离；exact predecessor、pre-state authorization、
  double freshness、effect identity、writer epoch 与 typed disposition 在一个 activation contract 中绑定。
- **State Ownership:** proposer/evaluator 不推进 head；kernel control plane 独占 activation；storage 只提供物理 transaction。
- **Evaluation:** bounded model 2,808,230 reachable states；8,880,248 transition attempts；单线程 Python transition timing 不是
  production storage benchmark，hardware `Not Disclosed`。
- **Limits:** physical crash/partition/signature/side-effect atomicity 与 availability 不在证明范围。
- **Owner / Decision:** `AGENT-WORKFLOW`（Ch81）；`Refine — Existing Argument / Experimental`。

### ForeWAM — 28/30

- **Problem / Mechanism:** direct-policy WAM 用 single Future-KV prefill + teacher-supervised dynamics registers，把 predictive
  context 交给 Action DiT，而不在 deployment 生成 future video。
- **State Ownership:** environment/observation 是事实；Future-KV/registers 是 policy-local derived state；controller 仍拥有
  action authority。
- **Evaluation:** 2B policy、single A800-80GB latency；LIBERO 50 rollouts/task；LIBERO-Plus matched component subset；
  10-step/2-step action denoising。没有 real-world、multi-robot、concurrency 或 SLO evidence。
- **Limits:** teacher/future targets 只在 training；latent causal sufficiency 未证明；cross-method comparisons 非完全 matched。
- **Owner / Decision:** `MULTIMODAL-EMBODIED-VLA`（Ch26）；`Refine — Existing Argument / Experimental`。

## 3. AI Infra 与工程项目

### Source Coverage

检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、
Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与
OpenXLA 的 official release surfaces。没有确认到本窗口内达到长期门槛的新 release/RFC。

vLLM `v0.27.0` 与 `v0.27.1` 的 GitHub release time 分别为 8 月 10 日与 8 月 11 日，超出本次 event window；
它们不因今天再次访问而重复计分。SGLang `v0.5.17`（8 月 8 日）和 KServe `v0.20.0`（8 月 6 日）也已由
owner Daily/Weekly 处理。

### Candidate Scoring

本组没有新增评分候选。

## Evidence Level and Claim Boundary

- **官方事实:** arXiv v1 metadata、GitHub signed release/tag 时间与公开实现/实验设置。
- **论文实验结论:** 只在各自 benchmark、model、hardware、seed/rollout 与 evaluator 条件内成立。
- **社区观点:** 未作为候选或评分依据。
- **本项目推断:** 四项分别补足 latent predictive interface、typed compression、authoritative activation 与 Skill
  differential Gate；这些是跨章节联读后的工程归纳，不是作者声称的统一平台规范。

## Knowledge Tree Position

| Candidate | Owner | Current Chapter | Legacy Chapter | Adjacent Chapters Read | Evolution Relationship |
| --- | --- | ---: | ---: | --- | --- |
| ForeWAM | `MULTIMODAL-EMBODIED-VLA` | Ch26 | N/A | Ch25 / Ch26 | Direct Evolution |
| The Sleeping Agent | `AGENT-CONTEXT` | Ch75 | Ch71 | Ch75 / Ch77 | Direct Evolution |
| Beyond Memory | `AGENT-WORKFLOW` | Ch81 | Ch77 | Ch77 / Ch81 / Ch84 | Layering / Dependency |
| Agent Skills Can Be Harmful | `AGENT-PLATFORM` | Ch84 | Ch80 | Ch75 / Ch81 / Ch84 | Direct Evolution |

## Recommended Action

- ForeWAM：`Refine — Existing Argument`，在 Ch26 补 direct-policy latent interface 分支，不改写 Ch25 的 World Model owner。
- The Sleeping Agent：`Refine — Existing Argument`，在 Ch75 将 generic compression loss 提升为 typed preservation contract。
- Beyond Memory：`Refine — Existing Argument`，在 Ch81 区分 stored candidate 与 authoritative activation。
- Agent Skills Can Be Harmful：`Refine — Existing Argument`，在 Ch84 将 paired utility Gate 推进到 trajectory-level attribution。
- 四项均保持 `Status: Experimental`；不把作者 benchmark、比例或 latency 写成普遍收益。

## Ignored Noise

- arXiv 8 月 13 日 recent list 中与本项目知识树无关的 domain application、position paper 和重复 revision。
- 只有标题/摘要、未完成全文核验的高热度候选；不因 Hugging Face、Scholar 或搜索排序提高 Evidence Level。
- vLLM v0.27.0/v0.27.1、SGLang v0.5.17 与 KServe v0.20.0 的窗口外重复发现。
- 缺少 model、hardware、precision、length、batch/concurrency 与 SLO 条件的 performance headline。

## Repository Changes

- 新增 `papers/2026/08/14/README.md`。
- Refine Ch26：补显式 future、joint WAM 与 direct-policy latent interface 的演进及共存边界。
- Refine Ch75：补 per-information-type compression preservation contract 与 temporal-anchor slice。
- Refine Ch81：补 candidate retention → authoritative activation 的事务边界和物理实现限制。
- Refine Ch84：补 Skill paired execution、failure surface 与 marginal cost attribution。
- 同步 `docs/LEARNING_STATE.md`；ROADMAP 与 DECISIONS 不变。
- 未生成 W33 Weekly；未执行 stage、commit、push 或破坏性 Git 操作。

## Open Questions

1. ForeWAM 的 latent registers 是否在 intervention 下携带 control-sufficient dynamics，而非 teacher/policy shortcut？
2. temporal-anchor preservation 能否跨 summarizer、语言、query distribution 与 recursive consolidation 复现？
3. Continuity Kernel 的 activation contract 在真实 storage crash、partition、multi-key contention 与外部 effect 下如何实现？
4. Skill compatibility 与 marginal-cost predictor 如何在不重复运行全部任务的前提下保持可校准？
5. W33 Sunday 汇总时，这四项是否与后续来源形成更稳定的 evolution family，还是保持单篇 Experimental evidence？

## Sources

### Model and Research Institution Surfaces

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Apple Machine Learning Research: https://machinelearning.apple.com/
- Google DeepMind Publications: https://deepmind.google/research/publications/
- Google Research Blog: https://research.google/blog/
- Meta AI Research: https://ai.meta.com/research/
- Microsoft Research Blog: https://www.microsoft.com/en-us/research/blog/
- NVIDIA Research: https://research.nvidia.com/
- Hugging Face Blog: https://huggingface.co/blog

### Academic Primary Sources

- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- Agent Skills Can Be Harmful: https://arxiv.org/abs/2608.11888
- Beyond Memory: https://arxiv.org/abs/2608.11632
- Foresight Without Seeing / ForeWAM: https://arxiv.org/abs/2608.11605
- The Sleeping Agent: https://arxiv.org/abs/2608.11775
- Hugging Face Daily Papers: https://huggingface.co/papers
- Semantic Scholar: https://www.semanticscholar.org/
- Google Scholar: https://scholar.google.com/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### Engineering Primary Sources

- vLLM releases: https://github.com/vllm-project/vllm/releases
- SGLang releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo releases: https://github.com/ai-dynamo/dynamo/releases
- KServe releases: https://github.com/kserve/kserve/releases
- PyTorch releases: https://github.com/pytorch/pytorch/releases
