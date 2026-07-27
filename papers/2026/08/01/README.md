# AI Research Daily — 2026-08-01

> Research window: 2026-07-30 至 2026-08-01（重点核验过去 24～48 小时）
>
> Accessed: 2026-08-01（Asia/Shanghai）
>
> Scope: 官方 Research / Blog / model card、primary research papers、官方工程文档、
> RFC、重要 PR 与 GitHub Releases。
>
> Organization: 模型与研究机构 → arXiv / 学术来源 → AI Infra 与工程项目
>
> Archive clock: Saturday Daily；不生成尚未结束的 `2026-W31` Weekly。

## Executive Summary

本轮一线模型机构没有出现足以改变模型训练或 serving 结论的新正式发布；Alibaba Qwen 的
Qwen-UI-Agent technical report 进入 Worth Watching，但其广泛能力与大规模 rollout
数字仍属于作者报告，不能直接转成 Agent Platform 的通用设计结论。

真正形成长期认知增量的是 7 月 30 日提交、7 月 31 日进入 recent list 的三篇预印本：

1. **SemPIC** 说明 position-independent KV cache 的难点不只是 RoPE position：独立
   编译的 KV 没有看到未来组合时的 causal prefix。技术路线由 exact prefix reuse 分叉为
   online state repair 与 offline semantic compilation；该语义边界已融入第 46 章。
2. **OSReward** 与同期 benchmark audit 共同说明 Agent trajectory 的 judge 和 scripted
   verifier 都可能系统性误判。完成声明、action history、environment transition 与
   task-specific outcome 必须分层保存，false success 不能静默成为 RL reward；该原则已
   融入第 62 章。
3. **MANTA** 把 task-topology matching 从部署前选择推进到 trace-triggered、bounded
   runtime repair。长期价值不在“动态增加 Agent”，而在 topology version、mutation
   budget、deterministic validation 与 authority/replay semantics；已融入第 78 章。

这些内容没有推翻旧方案。Exact prefix cache、静态 Multi-Agent topology、deterministic
verifier 仍在各自约束下成立；新机制只是处理了组合变化、长轨迹过程风险与 verifier
可扩展性暴露出的新边界。所有性能与准确率数字仍绑定论文的模型、任务、硬件、输入协议和
作者实现，不写成生产通用结论。

## Candidate Scoring

评分维度均为 `0～5`：Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、
Source Reliability（SR）、Project Relevance（PR）、Longevity（L）。

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Qwen-UI-Agent Technical Report | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching；Daily only |
| SemPIC：semantic position-independent KV | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Must Read；refine Ch46 |
| OSReward：cross-platform trajectory judge audit | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Must Read；refine Ch62 |
| MANTA：bounded runtime topology repair | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Must Read；refine Ch78 |
| WIDE：token-level dynamic width pruning | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching；Daily only |
| How Benchmarks Mis-Score Computer-Use Agents | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Related evidence；Ch62 cross-check |
| Local CUA inference-time scaling | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Worth Watching；Daily only |

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查官方 Research/Publications、技术 Blog、model/system card、官方
GitHub/Hugging Face organization 与 technical report，并与 7 月 27～31 日 Daily 去重。

| Institution | Window result | Decision |
| --- | --- | --- |
| OpenAI | Research index 无窗口内新条目 | No Material Update |
| Anthropic | Research/Newsroom 无窗口内新研究条目 | No Material Update |
| Apple Machine Learning Research | 无达到门槛的新正式条目 | No Material Update |
| Google DeepMind | July news 未提供可确认在本窗口首次发布的新机制 | No Material Update |
| Google Research | 最新 Research Blog 条目早于窗口 | No Material Update |
| Meta AI / FAIR | 最新 Research 条目早于窗口 | No Material Update |
| Microsoft Research | 无达到门槛的一手更新 | No Material Update |
| NVIDIA Research | 无窗口内正式 Research 发布 | No Material Update |
| xAI | 无窗口内 model card / research 更新 | No Material Update |
| Amazon Science / AGI | 无达到门槛的新 publication | No Material Update |
| Cohere Labs | 无窗口内正式 Research 更新 | No Material Update |
| Ai2 | 无窗口内达到门槛的新论文入口 | No Material Update |
| Mistral AI | 无窗口内正式技术发布 | No Material Update |
| Alibaba Qwen | Qwen-UI-Agent technical report 于 7 月 30 日提交 | Worth Watching |
| DeepSeek | 官方入口无窗口内正式 Research 更新 | No Material Update |
| Moonshot AI / Kimi | Kimi K3 已在 7 月 29 日 Daily 处理 | Deduplicated |
| Zhipu AI | 无达到门槛的一手更新 | No Material Update |
| MiniMax | 无窗口内正式技术研究更新 | No Material Update |
| ByteDance Seed / Research | 无达到门槛的一手更新 | No Material Update |
| Baidu ERNIE | 无窗口内正式 Research 更新 | No Material Update |
| Tencent Hunyuan | 无窗口内正式模型/系统更新 | No Material Update |
| Huawei Noah's Ark Lab / Pangu | 无达到门槛的一手更新 | No Material Update |
| Shanghai AI Laboratory / InternLM | 无达到门槛的一手更新 | No Material Update |
| StepFun | 无窗口内正式 Research 更新 | No Material Update |
| Xiaomi MiMo | 无达到门槛的一手更新 | No Material Update |
| InclusionAI / Ant Group | 未找到可稳定核验的新正式发布说明 | 尚未验证 |
| Hugging Face Blog | Blog 首页无 7 月 31 日新高信号一手机制 | No Material Update |

### Alibaba Qwen — Worth Watching：GUI 与 CLI 进入统一 Action Space

- Source: official-team technical report / arXiv
- Submitted: 2026-07-30 13:58:41 UTC
- Accessed: 2026-08-01
- URL: https://arxiv.org/abs/2607.28227
- Score: 24/30
- Status: Experimental

报告将 mobile、desktop、web 与 DeepSearch 放入统一 GUI/CLI action space，并描述
real-device runtime、长于 100 turns 的 online RL、并发环境和 data flywheel。长期信号是
computer-use Agent 的训练对象从单屏点击扩展为跨平台、stateful workflow；但这也把
environment identity、action semantics、side effects、reward verification 与 recovery
一起带进训练 contract。

本轮只核验 metadata、abstract、technical-report structure 与报告的系统边界，没有把作者
benchmark 排名写入 Books。后续若要吸收，必须全文检查 environment construction、action
normalization、RL reward、failure taxonomy、real-device safety 与 ablations，并与
OSReward 的 judge bias 联读。

**Evidence Level**：官方团队 technical report；性能为作者实验，尚无独立复现。

**Knowledge Tree Position**：Ch23 Data、Ch29 Reasoning RL、Ch62 Evaluation、
Ch74 Tool Calling、Ch77 Workflow、Ch80 Agent Platform。

**Recommended Action**：Daily only。当前书稿已经覆盖 action contract、durable workflow、
evaluation environment 与 platform authority；报告尚未形成需要改写这些长期结论的新证据。

## 2. arXiv / 学术来源

### Source Coverage

按顺序检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`stat.ML` recent，并按
主题补充 `cs.SE`、`cs.CR`、`cs.AR`、`cs.PF`。OpenReview / TMLR 未发现窗口内、publication
state 明确且比下列条目更相关的 Accepted 项。

Hugging Face Daily Papers、Semantic Scholar、Google Scholar、OpenAlex 与 DBLP 只用于
discovery、metadata 和去重；标题、作者、v1 日期、正文、公式、实验与限制均回到 arXiv
HTML / primary paper。Crossref 本轮未发现 DOI、venue 或版本冲突，不触发 Daily 交叉核验。

### SemPIC — Must Read：Position Correct 不等于 Context Correct

- Source: primary research paper / arXiv
- First public version: v1, 2026-07-30 11:45:24 UTC
- Accessed: 2026-08-01
- URL: https://arxiv.org/abs/2607.28069
- Full text: https://arxiv.org/html/2607.28069v1
- Score: 27/30
- Status: Experimental

#### Why

Prefix cache 只能复用相同 causal prefix。RAG/Agent workload 会在不同 instruction、history
和 document order 下重复使用同一文档；若独立构建 document KV 再拼接，RoPE re-rotation
虽然修正 position，却无法补回构建时缺失的前序 Context。

#### Principle

KV 是 context-conditioned execution state，不是 document 的无条件 embedding：

```text
same prefix reuse
→ position-independent linking
→ contextual incompleteness
→ online repair or learned offline compilation
```

语义目标不是恢复某个 privileged tensor，而是让未来组合下的 output behavior 接近 full
recompute。这把 cache correctness 从 tensor compatibility 扩展到 behavioral compatibility。

#### Mechanism

SemPIC 用同一 frozen decoder 扮演两个角色：Writer 在 document compilation 时启用 LoRA，
输出 native per-layer K/V；Reader 关闭 LoRA，在新 prompt 中读取这些 caches。Full-context
teacher 与 cached student 的 logits 通过 KL distillation 对齐，gradient 穿过每层 KV 回到
Writer。KV Gradient Checkpointing 保留可微 cache output，却在 backward 重建 Writer
intermediates，以额外计算换训练显存。

#### Trade-off

- online decode path 与 native KV interface 不变，但 offline training、cache construction
  和 rebuild 成为新成本；
- Writer 适配减少 contextual mismatch，却引入 domain transfer 与 model/compiler identity；
- boundary token 与 document-wide adaptation 可互补，但仍残留 block-local attention sink；
- 它不压缩 KV bytes，也不解决多租户隔离、cache invalidation 或远端 transfer。

#### Evidence Boundary

论文在 Llama-3.1-8B-Instruct、Qwen3-4B-Instruct-2507、Qwen3-8B，Synthetic Biographies、
HotpotQA、MuSiQue、NIAH 上以 100 examples/cell、greedy decoding、BF16 比较。质量/TTFT 使用
8×A100 80GB PCIe server 中的单进程单 GPU；TTFT 明确排除 offline construction、training、
model loading、lookup/transfer 与生成首 token 后的计算。作者报告 mean micro-F1 从 KV
Packet `0.53` 提高到 `0.60`，Full Recompute 为 `0.62`；这不证明生产 goodput、并发、P99
或跨域稳定性。

#### Evolution / Connection

`Direct Evolution`：exact prefix reuse → PIC linking → boundary adaptation → document-wide
semantic Writer；online selective recompute 与 offline compiler 长期共存。

主位置为 Ch41、Ch46；连接 Ch39 Prefill、Ch50 GPU Memory、Ch51 KV transfer 与 Ch73
Agent Memory。

#### Recommended Action

已 refine Ch46，加入 position correctness / causal-context correctness 边界，以及 exact
prefix、online repair、offline semantic compilation 的共存条件。不写成 vLLM feature，
不复制论文 benchmark headline。

### OSReward — Must Read：Reward 的首要风险是 False Success

- Source: primary research paper / arXiv
- First public version: v1, 2026-07-30 17:57:41 UTC
- Accessed: 2026-08-01
- URL: https://arxiv.org/abs/2607.28609
- Full text: https://arxiv.org/html/2607.28609v1
- Score: 27/30
- Status: Experimental

#### Why

Computer-use Agent 的 trajectory judge 同时服务评估、data curation 和 RL。人工 annotation
无法覆盖训练规模，scripted verifier 又脆弱，因此系统转向 VLM judge；但若 judge 偏向
相信 Agent 的完成叙述，false success 会直接强化错误行为。

#### Principle

Trajectory evidence 应按 authority 分层：

```text
narrative / thought
→ typed action and tool result
→ environment transition / artifact
→ task-specific completion and side-effect check
```

Judge accuracy 还要拆成 success recall 与 failure recall。总体 accuracy 可能被 class mix
或“几乎总判成功/失败”的 operating point 掩盖。

#### Mechanism

OSReward 自建 web、Windows、Ubuntu、mobile 环境与 human-verified instructions，使用多类
Agent backbones 收集 fresh trajectories，再由多阶段人工 annotation 给出 binary verdict、
failure type，并为成功轨迹标注 alignment / efficiency。OSReward-Hard 聚焦难例；
OS-Shepherd-100K 使用多个强 judges 的高 agreement 样本训练 9B/35B reward models，SFT 后
再针对 false success 做 RL。

#### Trade-off

- full text/action history 对意图重要，却也使 judge 更容易跟随 Agent narrative；
- 多 judge agreement 可筛掉不确定训练样本，但 correlated blindness 不会因投票消失；
- human-gold benchmark 更可靠也更昂贵，synthetic instructions 适合扩大训练集却降低
  evidence level；
- open reward model 降低成本，但 domain、harness、action space 与 base rate 漂移要求持续
  calibration。

#### Evidence Boundary

论文评估 27 个 VLM judges；主协议读取最后 `N=5` 个 states 及逐步 reasoning/action text，
并保持 greedy decoding。作者观察主流 judges 对 incomplete task 存在 leniency bias，hard
set 上显著退化；移除 thought/action text 的消融影响大于改变 screenshot selection。数字
受 2026 模型 roster、trajectory pool、annotation rubric、平台与 class balance 限制。

同期 `How Benchmarks Mis-Score Computer-Use Agents` 审计 5 个公开 benchmarks 的
failure-scored trajectories，进一步证明 scripted evaluator 与 task 本身也会误判。两项
工作共同支持“judge 与 verifier 都必须被评估”，不支持把某一方升级成绝对 ground truth。

#### Evolution / Connection

`Layering / Dependency`：scripted oracle → model judge → human-gold judge audit → specialized
reward model；每一层降低某类成本，也引入新的 bias、correlation 与 maintenance burden。

主位置为 Ch62；连接 Ch74 actions、Ch77 Workflow evidence、Ch80 Agent Platform。

#### Recommended Action

已 refine Ch62，增加 narrative/action/environment/outcome evidence hierarchy、success/failure
recall 与 false-success gate。不保留模型排行榜和 list-price cost。

### MANTA — Must Read：Topology Repair 是受控 State Transition

- Source: primary research paper / arXiv
- First public version: v1, 2026-07-30 17:01:27 UTC
- Accessed: 2026-08-01
- URL: https://arxiv.org/abs/2607.28527
- Full text: https://arxiv.org/html/2607.28527v1
- Score: 26/30
- Status: Experimental

#### Why

静态 topology 容易复现，但 long-horizon task 的 branch overload、missing verifier、duplicate
side effect 与 premature consensus 往往只在运行 trace 中暴露。部署前一次选择不能覆盖
所有过程风险。

#### Principle

Topology 不只是 prompt layout，而是 versioned control state：roles、edges、visibility、
execution order 和 validation path 的改变都必须由 Workflow owner 提交。

#### Mechanism

MANTA 由 Topology Planner、Trace Auditor、Skill Reflector 与 deterministic controller
组成。Planner 根据 task 和 playbook 生成 initial topology；agents 通过 structured relay
packet、evidence ledger 与 visibility policy 执行。Auditor 不读取 benchmark answer，只看
process trace；命中中高风险 flag 后允许一次 bounded mutation、最多三个 operations，并由
确定性代码校验 roles、references、membership、nesting 与 agent limits。

#### Trade-off

- targeted repair 比全局扩容更节省，但 audit miss 会让错误 topology 保持不变；
- clean trace 是 reliability signal，不是 correctness proof；共享语义错误可能没有过程症状；
- cross-run playbook 保存结构经验，却可能把 source-domain policy 带到不匹配的 target；
- runtime mutation 新增 context migration、authority transfer、replay、race 与 rollback。

#### Evidence Boundary

论文使用 Gemma 4 31B、medium reasoning effort，在 BrowseComp、StableToolBench、PlanCraft、
WorkBench、MATH 各 30 questions、3 runs；最大 initial agents 5、repair 后 10，默认每 run
一次 mutation。作者报告五 benchmark mean success `74.0%`，但 workload、model、tool
environment、token accounting 与 auditor prompt 都属于实验 contract，不能当成通用增益。

#### Evolution / Connection

`Direct Evolution`：static topology → task-conditioned topology → trace-triggered bounded
repair；旧的 singleton、chain 与 deterministic Workflow 在短任务和高副作用场景继续成立。

主位置为 Ch78；authoritative transition 与 replay 仍由 Ch77 拥有。

#### Recommended Action

已 refine Ch78，加入 bounded topology repair、mutation budget、deterministic validation 与
authority/replay 边界。不把“self-evolving”写成无监督自治。

### Worth Watching / Related Evidence

#### WIDE：Token-level Dynamic Width Pruning

WIDE 让每个 token 选择 attention-head groups 与 FFN-channel groups，并以 mask reordering、
block skipping 和 architecture-dependent intra-block kernels 尝试把动态 sparsity 变成真实
执行收益。论文训练使用 Llama3.1-8B / Llama3.2-3B、4×A100-SXM4-40G、4096 context，
作者报告的 end-to-end acceleration 绑定其 CuTe kernels 与实验 workload。当前只保留 Daily：
需要独立复现、continuous batching、多并发、长上下文、其他 GPU generations 和质量切片后，
才能判断是否 refine Ch21/45/52。

#### Local Computer-Use Agent Inference-Time Scaling

该论文比较 context、max steps、structural decomposition 与 parallel trials，观察到更多 compute
可能只把 failure 从 stall/repetition 转成 premature false success。它与 OSReward 的
false-success signal 一致，但当前是特定 local models 与 OSWorld 的作者实验；保留 Daily，
不把“inference-time scaling 无效”写成通用结论。

## 3. AI Infra 与工程项目

### Source Coverage

按固定顺序检查官方 Releases、Release Notes、文档与近期重要 PR，并与最近 Daily 去重。

| Project | Window result | Decision |
| --- | --- | --- |
| PyTorch | latest stable `v2.13.0` 为 7 月 8 日 | Outside Window |
| JAX | Releases 页面未显示窗口内新稳定 release | No Material Update |
| CUDA | 无窗口内可核验的正式 release | No Material Update |
| Triton | latest stable `v3.7.1` 为 6 月 18 日 | Outside Window |
| vLLM | `v0.26.0` 已在 7 月 29/31 Daily 处理 | Deduplicated |
| SGLang | latest visible stable release 早于窗口 | No Material Update |
| NVIDIA Dynamo | Kimi K3 pre-release 为 7 月 27 日，已处理 | Deduplicated |
| TensorRT-LLM | 无窗口内新稳定 release | No Material Update |
| Ray | 无窗口内高信号正式 release | No Material Update |
| KServe | latest visible stable release 早于窗口 | No Material Update |
| Kubeflow | 无窗口内高信号正式 release | No Material Update |
| Kubernetes | 无窗口内与 AI System 直接相关的高信号 release/RFC | No Material Update |
| Hugging Face Transformers | latest visible stable release 早于窗口 | No Material Update |
| Hugging Face Accelerate | 无窗口内高信号正式 release | No Material Update |
| DeepSpeed | 无窗口内高信号正式 release | No Material Update |
| Megatron-LM | 无窗口内高信号正式 release | No Material Update |
| Unsloth | 无窗口内高信号正式 release | No Material Update |
| MLX | 无窗口内高信号正式 release | No Material Update |
| llama.cpp | continuous builds / commits 缺少稳定机制边界 | Ignored Noise |
| ONNX Runtime | 无窗口内高信号正式 release | No Material Update |
| OpenXLA | 无窗口内高信号正式 release | No Material Update |

### Evidence Level

- **官方事实**：release 名称、状态与时间来自官方 GitHub Releases。
- **尚未验证**：动态 release 页面可能存在索引延迟；“No Material Update”只表示本轮未发现
  达到阈值的新稳定机制，不证明没有未索引 commit/PR。
- **自己的推断**：连续 commits 只有在形成明确 correctness、compatibility 或长期机制变化
  时才应升级为研究事件。
- **Recommended Action**：不重复吸收 vLLM / Dynamo 版本事实，不修改 Infra 章节。

## Books Integration

| Candidate | ROADMAP owner | Existing coverage | Decision | Changed file |
| --- | --- | --- | --- | --- |
| Qwen-UI-Agent | Ch80，连接 Ch23/29/62/74/77 | 已有 environment、action、workflow、authority contract | Daily only；需全文 source family review | — |
| SemPIC | Ch46，连接 Ch41/50/51 | 已覆盖 cache identity / tiering，缺 semantic composition | Refine — Existing Argument | `books/part-04-inference-system/46-vllm.md` |
| OSReward + benchmark audit | Ch62 | 已覆盖 judge calibration，缺 trajectory evidence authority 与 error direction | Refine — Existing Argument | `books/part-05-ai-infrastructure/62-evaluation-system.md` |
| MANTA | Ch78，handoff Ch77 | 已覆盖 static task-topology matching，缺 runtime bounded repair | Integrate — New Mechanism | `books/part-06-agent/78-multi-agent.md` |
| WIDE | Ch21/45/52 | 已有 conditional compute / kernel / scheduling contract | Daily only；单篇 kernel/system evidence | — |
| Local CUA scaling | Ch62/76/80 | 已有 bounded retry、verification、cost | No Change；实验补强而非新机制 | — |

三个写入都保留旧方案成立条件，没有把新论文写成必然替代。未新增 Part、章节或孤立论文笔记；
没有更新 `docs/DECISIONS.md`，因为知识树 ownership 未改变。

## Recommended Action

- Sunday 生成 W31 时，把 7 月 31 日 InferScale 与 8 月 1 日 SemPIC 联读，重建
  token injection → exact prefix reuse → position-independent linking → online repair / offline
  semantic compilation 的分叉演进。
- Weekly 中联读 OSReward、benchmark mis-score 与 local CUA scaling，区分“Agent 更强”与
  “verifier operating point 改变”。
- 持续观察 SemPIC/WIDE 的公开代码、独立复现和 production-runtime integration；没有新的
  workload contract 前不再扩写 Books。
- 对 Qwen-UI-Agent，后续只在 technical report 全文与 artifact/source family 都可核验后，
  决定是否补充 Ch80；当前 Must Read 不等于修改书稿。

## Ignored Noise

- 模型发布转载、聚合站排名、社交媒体 thread 与没有 technical report/system card 的宣传。
- arXiv recent 的大量 application-specific entries；标题含 Agent/LLM 不自动意味着系统机制。
- 把作者 benchmark、list price 或单模型排名写成跨模型/跨平台的通用结论。
- 缺少模型 revision、hardware、precision、length、batch、concurrency 与 SLO 的 performance
  headline。
- GitHub continuous build、局部 bugfix 与未合并 PR；除非改变 correctness/security contract。
- Discovery index 暂未收录新预印本；metadata lag 不等于独立复现或 rejection。

## Repository Changes

- 新增 `papers/2026/08/01/README.md`，完成当日来源覆盖、候选评分、三项全文分析、
  Evidence Level、Books decisions 与开放问题。
- Refine `books/part-04-inference-system/46-vllm.md`：加入 KV semantic composition contract。
- Refine `books/part-05-ai-infrastructure/62-evaluation-system.md`：加入 trajectory evidence
  hierarchy、false-success / failure-recall 边界。
- Refine `books/part-06-agent/78-multi-agent.md`：加入 trace-triggered bounded topology repair。
- 更新 `docs/LEARNING_STATE.md`，记录三项稳定认知；未改变 2025 primary-source blocker 状态。
- 未生成 `2026-W31`；该周覆盖 2026-07-27～2026-08-02，只在 8 月 2 日完成 Sunday Daily
  与 Books Integration 后生成。
- 保留运行前全部 staged/unstaged 历史重审修改；未 stage、unstage、commit、push 或清理。

## Open Questions

1. SemPIC cache identity 是否必须包含 Writer LoRA、training corpus、distillation target、
   document canonicalization 与 linking policy？Reader/model upgrade 后如何证明 cache rebuild
   完成？
2. Position-independent KV 在 continuous batching、prefix hit、remote transfer 与多租户场景
   下，怎样同时验证 semantic compatibility、P99 TTFT 与 memory pressure？
3. OSReward 的 leniency bias 在不同 judge prompts、tool schemas、platform base rates 与真实
   production outcomes 下是否稳定？如何避免 reward model 学会 harness-specific cues？
4. Scripted verifier 与 model judge 都不可靠时，哪些 tasks 可以用 executable outcome 做
   anchor，哪些必须升级给人？Human-gold 的 disagreement 怎样进入 uncertainty？
5. MANTA 的 topology mutation 在 crash/replay、concurrent external events、delegated
   credentials 与已产生 side effects 时怎样保持 exactly-once-like business semantics？
6. WIDE 的动态 width 在 continuous batching 下是否造成 per-token divergence、kernel
   fragmentation 或 fairness 问题？端到端 goodput 是否仍接近单请求 kernel gain？
7. Qwen-UI-Agent 的 real-device rollout 如何隔离 irreversible actions、保护账号/数据并提供
   reward ground truth？

## Sources

Primary sources，均于 2026-08-01 访问：

### 模型与研究机构

- OpenAI Research: https://openai.com/research/
- Anthropic Research/News: https://www.anthropic.com/news?type=research
- Google DeepMind News: https://deepmind.google/blog/
- Google Research Blog: https://research.google/blog/
- Meta AI Blog: https://ai.meta.com/blog/
- Hugging Face Blog: https://huggingface.co/blog
- Qwen-UI-Agent: https://arxiv.org/abs/2607.28227

### 论文与学术来源

- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- SemPIC: https://arxiv.org/abs/2607.28069
- SemPIC full text: https://arxiv.org/html/2607.28069v1
- OSReward: https://arxiv.org/abs/2607.28609
- OSReward full text: https://arxiv.org/html/2607.28609v1
- MANTA: https://arxiv.org/abs/2607.28527
- MANTA full text: https://arxiv.org/html/2607.28527v1
- WIDE: https://arxiv.org/abs/2607.28418
- WIDE full text: https://arxiv.org/html/2607.28418v1
- How Benchmarks Mis-Score Computer-Use Agents: https://arxiv.org/abs/2607.28367
- Rethinking Inference-Time Scaling in Local CUAs: https://arxiv.org/abs/2607.28573
- OpenReview / TMLR: https://openreview.net/group?id=TMLR
- Hugging Face Daily Papers: https://huggingface.co/papers
- Semantic Scholar: https://www.semanticscholar.org/
- Google Scholar: https://scholar.google.com/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### AI Infra 与工程项目

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- JAX Releases: https://github.com/jax-ml/jax/releases
- Triton Releases: https://github.com/triton-lang/triton/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases
- KServe Releases: https://github.com/kserve/kserve/releases
- Hugging Face Transformers Releases: https://github.com/huggingface/transformers/releases
