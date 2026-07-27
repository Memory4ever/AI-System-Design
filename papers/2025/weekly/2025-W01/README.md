# AI Research Weekly — 2025-W01

> Coverage Window: 2024-12-30～2025-01-05
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Titans。论文 v1 于 2024-12-31 公开，按 ISO week-year 属于 2025-W01；它把长上下文问题从只扩大可访问窗口，推进到推理时更新参数化记忆，但仍属于作者实验结论。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 本组无达到保留门槛的候选。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 保留：Titans: Learning to Memorize at Test Time（arXiv v1：2024-12-31）。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Titans: Learning to Memorize at Test Time | 5 | 5 | 4 | 5 | 5 | 3 | 27/30 | Must Read；与 W16 MIRAS、W49 官方综合说明联合审计 |

## Deep Analysis

### Deep Analysis 1 — Titans: Learning to Memorize at Test Time

- First Public: 2024-12-31（arXiv v1）
- Status: Experimental；作者论文
- Primary Source: https://arxiv.org/abs/2501.00663
- Evolution Relationship: Direct Evolution

#### Why

attention 可以精确访问上下文，却让计算与缓存成本随序列增长；固定状态的 recurrent/linear
路线成本更平稳，却必须把历史压缩进有限状态。Titans 追问的是：能否在两者之间增加一个
会在 test time 学习、容量不被单个固定向量直接限制的长期记忆层。

#### Principle and Mechanism

论文把 memory 设计为可在线更新的神经模块，用与当前输入相关的 surprise signal 决定写入，
并组合短期 attention 与长期 neural memory。这里的“记忆”是模型执行图中的参数化状态，
不是 Agent 的外部 durable store。

#### Trade-off and Evidence Boundary

在线更新扩展了可积累状态，也新增更新稳定性、错误写入、遗忘、并发 session ownership、
checkpoint/rollback 与可解释性问题。论文实验只证明作者披露模型和任务下的结果；不能据此
断言它通用替代 dense attention、retrieval 或外部 Agent Memory。

#### Connection and Evolution

知识树位置：第 14、22、73 章。与 W16 MIRAS 是 `Direct Evolution`：后者把具体架构推广为
统一设计空间；与第 73 章只有 `Principle Reuse`，因为模型内部 test-time state 与
跨运行持久化的 Agent Memory 有不同 owner、identity 和 failure semantics。

## Full Source Review

### Titans: Learning to Memorize at Test Time

- **Candidate / Week / Score:** Titans / 2025-W01 / 27/30。
- **Source Family ID:** `titans-miras-test-time-memory`；后续与 W16 MIRAS、W49 Google Research
  synthesis 联读，但不能用后发材料改变本论文的 first-public date。
- **Source Type:** 作者论文（arXiv，Experimental）。
- **First-public Date / Revision History:** arXiv v1 于 2024-12-31 提交；截至访问日只有 v1。
- **Direct Primary Sources:** arXiv abstract、HTML 全文与公式/appendix，
  https://arxiv.org/abs/2501.00663；https://arxiv.org/html/2501.00663。
- **Related Primary Sources:** W16 MIRAS 论文与 W49 Google Research 官方说明，留待对应
  Source Packet 联读；本 Packet 不预先采用其结论。
- **Access and Verification Status:** Verified；正文、实验、ablation、related work 与相关
  appendix 可访问。作者未提供生产 serving contract 或独立复现证据。
- **Full-read Coverage:** 已读 metadata、Introduction、Preliminaries、Neural Long-term Memory、
  三种 memory integration、parallelization、language/needle/BABILong/time-series/genomics
  experiments、efficiency、ablation、Related Work、Conclusion 与核心 appendices。
- **Original Problem:** dense attention 可以精确按内容访问窗口，却把 pair compute 与显式
  context 限制在二次成本中；linear/recurrent model 以固定状态换取线性执行，却必须持续压缩
  历史，丢失精确依赖。
- **Why the Previous Design Was Reasonable:** attention 的显式 token-to-token access 对短中上下文
  具有高保真；固定 recurrent state 则适合流式、低延迟和有界内存，两者分别优化了不同约束。
- **Changed Constraint:** workload 希望在远超短 attention window 的历史上保留可学习状态，同时
  不让每次访问都重新展开全部 token pairs。
- **Mechanism:** neural memory 是一个在 test time 用 associative loss gradient 更新的 MLP；
  gradient magnitude 被解释为 surprise，更新还组合 past-surprise momentum 与 data-dependent
  decay。Titans 再以 memory-as-context、memory-as-layer、memory-as-gate 三种方式组合短期 attention、
  长期 neural memory 与 persistent task memory。
- **State Ownership:** neural-memory parameters/fast weights 由 sequence model execution 拥有；
  short-term token window 与 persistent task parameters 也是模型内部状态。论文没有定义 tenant、
  user 或 session 级 durable ownership。
- **Control Flow / Data Flow:** token/chunk 进入短期 attention；历史 representation 产生 key/value
  associative objective，surprise 驱动 memory update；当前输入从 memory 读取，再按 variant 与
  attention output 串联或 gated merge。训练通过 chunking/parallel formulation 减少逐 token 串行。
- **Implementation Details:** 论文披露 memory objective、更新规则、parallel scan/chunking 与三种
  integration；未披露 production concurrency isolation、checkpoint/rollback、在线错误写入检测或
  serving replica synchronization。
- **Evaluation Setup:** language modeling、common-sense reasoning、needle-in-haystack、BABILong、
  time-series forecasting 与 DNA modeling；包括 architecture/depth/memory size 等 ablation 和效率比较。
- **Baselines / Ablations / Sensitivity:** 与 Transformer 及 modern linear recurrent models 比较；
  ablation 检查 surprise、momentum/forgetting、memory depth 与 integration variants。结果仍是作者
  同一实验体系内的比较，不是跨实现生产 benchmark。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文展示最长超过 2M context
  的 needle-style 实验；完整生产硬件、precision、batch、并发和 TTFT/TPOT SLO contract 未统一披露，
  因而不在 Books 保留速度或最大长度数字。
- **What the Evidence Actually Proves:** 在作者模型、训练和任务设置中，可在线更新的参数化 memory
  能与局部 attention 组合，并在若干长依赖任务优于所选 baselines；其更新与读取可用公开公式解释。
- **What It Does Not Prove:** 不证明 neural memory 普遍替代 dense attention、RAG、KV cache 或
  Agent durable memory；needle 成功也不等于开放域事实可靠性、并发隔离或可删除性。
- **Limitations / Threats to Validity:** 作者评测与实现同源；长上下文任务以 synthetic retrieval 为
  重要组成；production ownership、污染恢复、持续在线学习 drift 与独立 replication 尚缺失。
- **Trade-offs / New Failure Modes:** 获得可增长的参数化历史状态，却引入错误写入、遗忘策略、
  update instability、跨请求泄漏、replica divergence 与 rollback/checkpoint 问题。
- **Where the Previous Design Still Applies:** 短上下文精确依赖继续适合 dense attention；严格
  provenance、权限、freshness 和删除要求继续适合外部 retrieval/memory；有界流式任务仍可选固定
  recurrent state。
- **Evolution Relationship:** `Direct Evolution`（attention/recurrent memory 的混合架构）；与 Agent
  Memory 仅为 `Principle Reuse`。
- **ROADMAP Node:** Ch22 主 owner；Ch14 提供 attention 成本前提；Ch73 只承接状态边界 handoff。
- **Target and Adjacent Chapters Read:** 已读 Ch14、Ch21、Ch22、Ch23，以及 Ch71～73 的 context/
  RAG/memory 边界。
- **Existing Coverage:** Ch22 已描述 surprise-driven test-time memory、三类 integration 与状态边界；
  Ch73 已明确它不是跨会话 durable Agent Memory。该内容为 provisional，待 W16/W49 联读复核。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch22，Ch73 仅保留模型内部状态与 Agent durable memory 的边界。
  倾向 `Refine — Existing Argument`，不新增独立论文段落。
- **Changed Files or Rejection Reason:** 已复核并保留 `books/part-02-model/22-long-context.md` 与 `books/part-06-agent/73-memory.md` 的演进/边界内容。
- **Open Questions:** multi-tenant serving 的 owner、更新隔离、坏记忆检测、rollback 与跨 replica
  consistency 是否存在可公开验证的实现。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- Titans 按 arXiv v1 回链本周；W16 MIRAS 与 W49 Google Research 官方综合说明保留各自证据角色，不把后发 Blog 当作首次公开。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Titans → 第 14、22、73 章（第 22 章为主 owner）

## Recommended Action

- Titans：Must Read；与 MIRAS 全文联读后 refine 第 22 章，并在第 73 章只保留边界 handoff。

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W01/README.md。
- 更新 books/part-02-model/22-long-context.md。
- 更新 books/part-06-agent/73-memory.md（边界 handoff）。

## Open Questions

- 在线参数化记忆在多租户 serving 中应按 request、session 还是 model replica 拥有，论文尚未给出生产 contract。
- 如何检测错误写入、执行隔离与可回滚更新，仍待实现证据。

## Sources

- Titans — https://arxiv.org/abs/2501.00663（First Public: 2024-12-31；Accessed: 2026-07-31）
