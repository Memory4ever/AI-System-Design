# AI Research Daily — 2026-08-05

> Research window: 2026-08-03 09:14 至 2026-08-05 09:14（过去 48 小时，Asia/Shanghai）
>
> Accessed: 2026-08-05（Asia/Shanghai）
>
> Scope: 官方 Research / Blog、arXiv recent、学术 discovery index、官方 GitHub Releases
>
> Organization: 模型与研究机构 → arXiv / 学术来源 → AI Infra 与工程项目

## Executive Summary

本轮没有发现窗口内、同时提供新机制证据的一线模型机构正式发布；有效增量集中在 8 月 4 日
arXiv recent batch。全文审查三项候选：LiveMem 把“上下文仍可访问”与“working context 淘汰后
计算状态仍连续”分开；AtumAI 把 Agent 生成基础设施策略前的自然语言意图编译为 typed、可执行
的任务 contract；AFlex 把 P/D disaggregation 继续细化到 Attention/FFN operator，并联合 GPU
frequency、resource allocation 与 SLO 进行控制。

Books Integration 吸收前两项长期机制。Ch22 新增 bounded KV、external archive 与 lossy recurrent
state 的分层关系，并补齐 Serving state lifetime；Ch77 新增 problem compilation 与 candidate search
的边界。AFlex 仍是单篇 preprint，代码尚未公开，实验集中于 A800、两种模型、指定 traces 与
SLO；它对 control granularity 的启发先保留在 Daily，等待 Weekly 交叉证据，不写成通用 Serving
设计结论。

今天是 Wednesday，不生成 provisional 2026-W32 Weekly。

## 1. 模型与研究机构

### Source Coverage

按 `CODEX_DAILY_RESEARCH_PROMPT.md` 的固定顺序扫描。访问时没有识别到 8 月 3～5 日内、同时
提供 technical report、model/system card 或可核验实现的新模型机构 Research 发布。

| Order | Institution / source | Actual observation | Decision |
| ---: | --- | --- | --- |
| 1 | OpenAI | Research 首页未见窗口内新增研究 | No Material Update |
| 2 | Anthropic | 最新可见 Research 仍早于本窗口 | Deduplicated |
| 3 | Apple ML Research | 未识别到窗口内可核验的一手更新 | No Material Update |
| 4 | Google DeepMind | News 首页未见窗口内新的 technical report | No Material Update |
| 5 | Google Research | 最新可见 Blog 仍为 7 月条目 | Deduplicated |
| 6 | Meta AI / FAIR | Blog 未显示窗口内新增 Research | No Material Update |
| 7 | Microsoft Research | Blog 未显示窗口内新增 Research | No Material Update |
| 8～26 | NVIDIA；xAI；Amazon；Cohere；Ai2；Mistral；国内一线模型与研究机构 | 定向检查未发现窗口内新的 primary technical evidence | No Material Update |
| 27 | Hugging Face Blog | 近期 community / partner 内容没有形成新的可独立核验机制 | Ignored Noise |

### Evidence Level

- **官方事实**：上述公开入口在访问时没有显示符合时间窗与证据门槛的新条目。
- **边界**：网站排序、索引延迟、时区与未公开材料可能造成漏项。
- **不得推断**：公开 Blog 无更新不代表机构内部没有研究，也不能证明没有未索引发布。

## 2. arXiv / 学术来源

### Source Coverage

依次检查 `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR` 与 `stat.ML` recent。三项深读候选均为
2026-08-03 提交、8 月 4 日 Tuesday batch 可见的 arXiv v1。Google Scholar、Semantic Scholar、
OpenAlex 与 DBLP 只用于 discovery、metadata 与重复关系检查；机制、实验和 limitations 均回到
arXiv HTML 正文，未用索引摘要替代全文。

### Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| LiveMem | 5 | 5 | 4 | 4 | 5 | 5 | 28 | Must Read；Refine Ch22 |
| AtumAI | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Must Read；Refine Ch77 |
| AFlex | 5 | 5 | 4 | 4 | 5 | 4 | 27 | Must Read；Status: Experimental |
| PrefixPlace | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Worth Watching；等待 locality family 联读 |
| xPress | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Worth Watching；等待完整 speculative contract |
| Resource-Fair Scheduling | 4 | 4 | 3 | 4 | 4 | 4 | 23 | Worth Watching；理论结果需系统 workload 对齐 |

`SR=4` 表示 primary preprint 正文可核验，但尚无 peer review、独立复现或 production validation。

### Deep Analysis 1 — LiveMem

**Why。** 长期 assistant / Agent stream 最终会超过 active context。RAG 与摘要保留部分历史的
访问能力，但每次都要根据当前问题重建 working set；固定 recurrent state 可以延续计算，却是
有损压缩。论文将缺口定义为 `state continuity under context turnover`：状态生命周期独立于
当前 KV window，而不是把更多 token 永久留在 Attention 中。

**Principle。** 历史证据的可追踪访问与模型内部计算连续性是不同 contract。前者偏向 exact、
addressable 与 governable，后者偏向 fixed-capacity、online update 与 lossy influence。两者应
layering，而不是由后者替代 RAG、archive 或 active KV。

**Mechanism。** 作者在 Qwen3-4B full-Attention backbone 的每层 Attention 旁加入 Gated
DeltaNet-2 recurrent branch。主路径只保存 system-prompt sink 与 bounded FIFO KV window；side
branch 保存固定大小的卷积和矩阵状态。训练和推理主动淘汰旧 KV，使 originating tokens 不再
可见，再用 SFT 与 GRPO-style RL 训练 memory path。Serving 中 ordinary Attention manager 与
paged recurrent-state slot 分开；Prefill slice 受 turnover boundary 约束，状态被 gather、update、
scatter，并在请求结束后释放以避免 leakage。

**Trade-off。** 作者在 Qwen3-4B、32K（部分任务 8K）以及 Wiki QA、conversation、test-time
learning、long QA 上实验；RAG baseline 使用 Qwen3-Embedding-0.6B top-1/top-3。LiveMem 的总体
聚合结果优于所测系统，但部分专门 baseline 在各自 suite 领先，state-only 相对 truncation 的
增益在部分 slice 很小或为零。任意 token needle task 没显示可靠提升，说明 latent state 不是
精确 archive。实验没有披露可迁移的 hardware / throughput / concurrency / SLO contract；RoPE
position horizon、固定状态容量、跨请求 continuity、checkpoint/migration、model upgrade 与
删除语义仍未解决。

**Connection。** Ch22 是 primary owner；Ch73 已明确 model-internal state 不属于 durable Agent
Memory。正文新增 state continuity 与 Serving lifecycle，不在 Ch73 重复。关系是 `Layering /
Dependency`：bounded KV、external retrieval 与 latent state 分别服务不同需求。

**Evolution。** `exact active KV → external reconstructive access → fixed latent continuity state →
hybrid archive + active context + latent state`。短会话、精确引用和强审计任务仍应使用旧分支。

### Deep Analysis 2 — AtumAI

**Why。** Off-the-shelf Agent 可以提出 policy，却常把问题形式化、约束覆盖与 evaluator 设计都
藏在 prompt 中；它既不能保证 hard constraints，也难以把一个控制任务学到的设计原语迁移到
另一个任务。搜索强度不能补救错误或不完整的 feasible region。

**Principle。** 在优化候选前，应先把自然语言 intent 编译为 machine-checkable task IR。模型
可以提出候选，但 decision variables、objectives、hard constraints、evaluation method、execution
budget 与 workload/platform identity 必须由 deterministic control plane 拥有并验证。

**Mechanism。** Datacenter Task Compiler 生成 typed specification；rule-based critic 拒绝
unsupported numbers、undefined variables、unit mismatch 与不可执行 constraints。Transferable
pass library 保存 abstract control idea、applicability 与 evidence，obligation cover 检查目标和
约束是否都有机制覆盖，projection 再绑定当前字段。Evolutionary Design Discovery Loop 组合
LLM masked edits、parametric evolution、surrogate filtering 与 high-fidelity simulation，并维护
measured Pareto frontier。

**Trade-off。** 论文只在 placement、scaling 与 power-management 模拟环境评估。Scaling 使用
Alibaba traces 的 100 services、30 nodes、11 regimes；Power 使用 960-server simulated fleet、
两周 Azure trace、Llama 3 7B/13B/70B，并设置 per-service accuracy floor。作者报告相对 expert
baseline 的改善，但没有 production deployment、独立复现或 sim-to-real 证据。Compiler 仍从
playbook 继承假设，critic 只能检查已编码规则；surrogate、simulator 与反复搜索可能共同过拟合
虚拟环境。论文没有独立 Limitations section，这些缺口是本次 Source Review 的推断边界。

**Connection。** Ch77 已有 evaluator-driven search、lineage、Pareto、held-out verification 与
human deployment authority。AtumAI 补足的不是另一种 Agent loop，而是 search 之前的 problem
compilation boundary，因此采用 `Refine — Existing Argument`，不新增章节。

**Evolution。** `manual policy design → LLM-only candidate generation → typed problem compilation +
constrained search → held-out replay / shadow / canary → human-controlled deployment`。设计空间小、
约束稳定或副作用不可逆时，人工设计与形式化评审仍然合理。

### Deep Analysis 3 — AFlex

**Why。** Prefill/Decode disaggregation 仍把每个 phase 内的 Attention 与 FFN 放在同一 GPU 频率
和资源配置下。二者的 compute/memory balance 与 frequency sensitivity 不同，请求级或 phase-
level DVFS 会留下 operator-level energy slack。

**Principle。** 更细 control granularity 可以暴露新的优化空间，但同时增加数据移动、状态所有权、
重配置时间和 failure semantics。节能结论只有在 energy、TTFT、TPOT、throughput 与 workload
identity 同时绑定时才成立。

**Mechanism。** AFlex 建立 PA/PF/DA/DF 四类 pool。Offline profile 记录 operator latency、energy
与 transfer；global scheduler 周期性解裁剪后的 ILP，选择 GPU allocation、TP 与 baseline
frequency；local controller 再按 operator / microbatch 调整 DVFS。Interleaved A/F pipeline、动态
microbatch depth 与 adaptive request batching 用于减少 bubble。Attention pool 拥有 KV，因此
重配置时 active sequence 留在旧 pool，新 sequence 进入目标 pool；stateless FFN 可在 iteration
boundary 更快切换。

**Trade-off。** 主要实验为 2 台、每台 8×A800-80GB、400 GB/s NVLink、800 Gbps inter-node，
CUDA 12.4；模型为 Qwen3-32B 与 Mixtral-8x7B，使用 Azure Coding/Conversation traces 及受控 QA、
RAG、Chatbot、Summary shapes，P90 TTFT 400 ms、TPOT 120 ms，负载 2/4/8/16 RPS，能耗来自
NVML。作者报告的最高节能数只属于该 contract。DVFS switch、hidden-state transfer 与 TP
reconfiguration 都可能吞噬收益；离线 profile 会漂移，planner 还需处理 stale plan、重配置失败、
多租户 fairness 与 state migration。实现声称基于 SGLang、UCX 与 GPUDirect RDMA，但代码计划
在 final version 发布，当前不可核验。

**Connection。** 机制可连接 Ch52 的 multi-timescale scheduling 与 Ch66 的 cost/energy，但本轮
不改书稿：单一 GPU generation、两模型、有限 trace 与未公开代码不足以把 A/F disaggregation
写成稳定默认设计。Disposition 为 `Emerging / Experimental`。

**Evolution。** `max-frequency colocated serving → request/phase DVFS + P/D disaggregation →
A/F operator disaggregation + local/global control`。旧方案在 transfer cost 高、部署规模小、profile
不稳定或重配置预算不足时仍成立。

### Evidence Level

- **官方事实**：三篇候选均为 arXiv v1，submission date 与 revision history 来自 arXiv metadata。
- **论文实验结论**：架构、实现与 evaluation contract 来自作者正文；结果只适用于披露条件。
- **自己的推断**：Ch22 / Ch77 ownership、AFlex 等待 Weekly、三条 evolution relationship 是本仓库
  integration judgment。
- **不得推断**：不能把作者 aggregate score、simulator 优势或最高节能值外推到其他模型、硬件、
  输入输出长度、batch、concurrency、SLO 或生产环境。

## 3. AI Infra 与工程项目

### Source Coverage

按固定项目顺序检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、
TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Hugging Face、DeepSpeed、Megatron-LM、
Unsloth、MLX、llama.cpp、ONNX Runtime、OpenXLA 与 MCP。

| Project | Latest primary-source state observed | Decision |
| --- | --- | --- |
| PyTorch | 最新正式 Release 仍早于本窗口 | Deduplicated |
| vLLM | Releases 未显示 8 月 3～5 日新的稳定版本 | No Material Update |
| SGLang | Releases 未显示窗口内改变长期 runtime contract 的稳定版本 | No Material Update |
| NVIDIA Dynamo | Releases 未显示窗口内新的稳定版本 | No Material Update |
| TensorRT-LLM | 可见项为早于窗口的 pre-release / existing release family | Deduplicated |
| Ray / KServe | 最新稳定 Release 早于本窗口 | No Material Update |
| MCP | 最新规范 family 仍为 2026-07-28 RC / prior stable lineage | W31 deduplicated |
| 其余项目 | 未识别到窗口内改变 correctness、state ownership、failure semantics 或 SLO 的正式 Release | No Material Update |

普通 dependency bump、nightly build、未合并 PR、缺少设计文档的 patch 与搜索引擎重新收录不进入
候选。Release/tag 只能证明版本事实；没有设计文档、代码路径与 workload contract 时，不推断
生产成熟度或性能收益。

## Knowledge Tree Position

| Candidate | Primary owner | Target and adjacent chapters read | Books decision |
| --- | --- | --- | --- |
| LiveMem | Ch22 Long Context | Ch21～23；核对 Ch51/52 与 Ch73 boundary | Refine — Existing Argument |
| AtumAI | Ch77 Workflow | Ch76～78；核对 Ch62/66/80 boundary | Refine — Existing Argument |
| AFlex | Ch52 Scheduling | Ch51～53；核对 Ch45/66 owner | Emerging / Experimental；Weekly Only |

没有新增 ROADMAP node、Part 或章节；每项技术只有一个主 owner，跨章节只保留边界说明。

## Recommended Action

- 已在 Ch22 写入 state continuity under context turnover，保留 KV、RAG/archive 与 latent state 的
  不同成立条件，并补齐 recurrent state 的 allocation、isolation、reset、migration 与 release。
- 已在 Ch77 写入 problem compilation：先形成 typed task contract，再允许 Agent / evolutionary
  loop 搜索候选；simulation success 不拥有 production deployment authority。
- 2026-W32 结束时重审 AFlex：优先检查公开代码、跨 GPU generation 结果、profile drift、
  reconfiguration failure 与 multi-tenant fairness，再决定是否 refine Ch52。
- 对 PrefixPlace、xPress 与 Resource-Fair Scheduling 完成同 source-family 联读；不能仅凭摘要追加
  locality、speculation 或 fairness 结论。

## Books Integration

### Absorbed

- `books/part-02-model/22-long-context.md`：新增历史访问与计算连续性的区别；把 bounded KV、
  external retrieval/archive 与 lossy recurrent state 写成分层演进，并明确 Serving lifecycle 与
  experimental evidence boundary。
- `books/part-06-agent/77-workflow.md`：在 evaluator-driven search 前新增 problem compilation，
  定义 typed IR、hard constraints、evaluation contract、obligation coverage、sim-to-real 与人工
  deployment authority。
- `docs/LEARNING_STATE.md`：同步上述稳定认知及 AFlex 的等待状态。

### Not Absorbed

- **AFlex**：机制完整度较高，但当前是单篇 v1、代码未发布，实验只覆盖 A800、两模型与有限
  trace；保留为 `Experimental`，不把最高节能值或四池架构外推为通用默认方案。
- **PrefixPlace / xPress / Resource-Fair Scheduling**：本轮没有完成全文 Source Packet，且已有
  owner chapters；等待 Weekly 联读与跨来源确认。

## Ignored Noise

- arXiv recent 中只提供增量 benchmark、缺少机制或与 AI System Design 关联弱的条目。
- Hugging Face community challenge、排行榜、partner marketing 与缺少 technical report 的模型
  headline。
- 缺少模型、硬件、precision、input/output length、batch、concurrency 与 SLO 的性能数字。
- GitHub nightly、dependency bump、未合并 PR 与搜索引擎重收录。

## Repository Changes

- 新增 `papers/2026/08/05/README.md`。
- Refine `books/part-02-model/22-long-context.md`。
- Refine `books/part-06-agent/77-workflow.md`。
- 同步 `docs/LEARNING_STATE.md`。
- 未修改 ROADMAP 或 `docs/DECISIONS.md`；未生成 provisional `2026-W32`。
- 运行前已有 Ch11、Ch16、Ch21、Ch45、ADR、interview 与 8 月 4 日 Daily 修改均保留；未执行
  stage、unstage、commit、push、reset、checkout 或 clean。

## Open Questions

1. LiveMem 的 state slot 怎样在跨 replica failover、checkpoint、model revision 与 session resume
   之间保持兼容，又能提供用户级 reset / delete 与 tenant isolation？
2. Fixed latent state 如何与 exact retrieval 建立 provenance-aware handoff，而不让不可解释的内部
   记忆越过 authorization boundary？
3. AtumAI 的 Task Compiler 如何证明 playbook defaults、unit semantics 与 simulator assumptions 的
   provenance，并在它们变化时使旧 policy 失效？
4. Agentic policy search 怎样使用 held-out trace、shadow/canary 与 failure injection 衡量 sim-to-real
   gap，而不是继续优化同一 simulator？
5. AFlex 在 H100/Blackwell、不同 power-management interface、跨租户负载与 profile drift 下是否
   仍有净收益？Attention-owned KV 的 pool migration 和 planner failure 怎样恢复？

## Sources

访问日期均为 2026-08-05。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Apple Machine Learning Research: https://machinelearning.apple.com/
- Google DeepMind: https://deepmind.google/blog/
- Google Research: https://research.google/blog/
- Meta AI: https://ai.meta.com/blog/
- Microsoft Research: https://www.microsoft.com/en-us/research/blog/
- Hugging Face Blog: https://huggingface.co/blog

### Academic Sources

- LiveMem metadata / abstract: https://arxiv.org/abs/2608.02515
- LiveMem full HTML: https://arxiv.org/html/2608.02515
- AtumAI metadata / abstract: https://arxiv.org/abs/2608.02569
- AtumAI full HTML: https://arxiv.org/html/2608.02569
- AFlex metadata / abstract: https://arxiv.org/abs/2608.01891
- AFlex full HTML: https://arxiv.org/html/2608.01891
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### Engineering Sources

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- NVIDIA Dynamo Releases: https://github.com/ai-dynamo/dynamo/releases
- TensorRT-LLM Releases: https://github.com/NVIDIA/TensorRT-LLM/releases
- Ray Releases: https://github.com/ray-project/ray/releases
- KServe Releases: https://github.com/kserve/kserve/releases
- MCP Releases: https://github.com/modelcontextprotocol/modelcontextprotocol/releases
