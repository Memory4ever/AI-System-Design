# Project Decisions

## ADR-001: Use GitHub as the Single Source of Truth

Decision:

The project will no longer use Word as the primary source.

Reason:

Markdown and Git provide:

- Diff
- History
- Review
- Branching
- Collaboration

Word may be generated as a release artifact.

---

## ADR-002: Organize Around Problems, Not Frameworks

Decision:

Frameworks such as vLLM and KServe will not define the top-level
knowledge architecture.

Reason:

Frameworks change.

Underlying system problems remain.

For example:

Inference Scheduling
    ├── vLLM
    ├── SGLang
    └── future systems

instead of:

vLLM
SGLang
KServe

---

## ADR-003: Store Book Content Under `books/`

Decision:

All generated book content will live under `books/`.

The directory is organized by the six roadmap parts:

- `books/part-01-worldview`
- `books/part-02-model`
- `books/part-03-training-system`
- `books/part-04-inference-system`
- `books/part-05-ai-infrastructure`
- `books/part-06-agent`

Each chapter is stored as an individual Markdown file in its corresponding
part directory.

Reason:

`ROADMAP.md` should remain the single source of truth for the knowledge tree,
chapter ordering, and learning route.

Chapter content needs a separate stable location so the repository can grow
from roadmap to book without mixing planning, state, and long-form writing in
one file.

---

## ADR-004: Make Chapter 62 the Evaluation System Owner

Status:

Accepted

Date:

2026-07-27

Context:

The global knowledge tree already defines Evaluation as both a capability
production signal and an online control-loop signal. Chapters on data,
training, registry, observability, production, and Agents each contain local
evaluation concerns, but no chapter owns the stable end-to-end framework.

This leaves the following questions without a single knowledge-tree owner:

- what object and deployment distribution an evaluation claim applies to;
- how evaluation datasets, scorers, environments, and system versions form
  reproducible evidence;
- how offline, shadow, canary, online, and human evaluation complement one
  another;
- how evaluator error, contamination, uncertainty, slices, and feedback bias
  constrain conclusions;
- how evidence becomes a promotion, rollback, or investigation decision.

Decision:

Chapter 62 becomes the generic `Evaluation System` chapter. It owns the
first-principles evaluation model and the platform contracts that connect
specification, dataset, execution, scoring, aggregation, decision, and
feedback.

MLflow remains in Chapter 62 as one implementation mapping for experiment,
model, dataset, trace, metric, and artifact evidence. It does not define what
quality means and is not treated as the Evaluation System itself.

Chapter 62 has these explicit boundaries:

- domain chapters retain their local metrics and failure modes;
- Model Registry indexes immutable identity, evidence references, and
  promotion state, but does not define evaluation semantics;
- Observability records what happened, while Evaluation judges whether the
  observed behavior satisfied a specified objective;
- release controllers apply policy to evaluation evidence, but do not invent
  the evidence after a release decision;
- Agent chapters retain component and trajectory evaluation mechanisms while
  reusing Chapter 62's evidence and decision contracts.

Alternatives considered:

1. Add a new dedicated chapter and renumber Chapters 63-80. Rejected because
   it creates broad mechanical churn without improving the conceptual
   boundary.
2. Keep Chapter 62 as an MLflow product chapter and scatter Evaluation across
   domain chapters. Rejected because a product cannot own the stable
   cross-system problem, and the feedback loop remains incomplete.
3. Append Evaluation to Monitoring. Rejected because Monitoring describes
   observed state, while Evaluation compares behavior with objectives and
   carries different dataset, scorer, uncertainty, and decision semantics.

Consequences:

- `ROADMAP.md` names Chapter 62 as `Evaluation System`.
- `books/part-05-ai-infrastructure/62-mlflow.md` is replaced by
  `62-evaluation-system.md`.
- Cross-chapter references point to Chapter 62 for the common evaluation
  contract while preserving local evaluation detail.
- The book keeps 80 chapters and avoids unrelated renumbering.

---

## ADR-005: Use a Dual-Axis Knowledge Tree

Status:

Accepted

Date:

2026-07-30

Context:

The six existing Parts organize the book by reading order and primary problem
ownership:

```text
Part I:
  Worldview / coordinate system

Part II-VI lifecycle:
  Model
  -> Training
  -> Inference
  -> Infrastructure
  -> Agent
```

This sequence provides a coherent end-to-end learning route, but it can hide
constraints that recur across several Parts. Compute, memory, communication,
scheduling, and state appear in training, inference, platform, and Agent
systems with different objects and time scales.

An alternative outline organized entirely around those system primitives was
considered. It would make historical connections more visible, but would mix
resource mechanisms, lifecycle stages, runtime layers, and product case
studies at the same hierarchy level. It would also duplicate topics such as KV
Cache, distributed communication, and scheduling across several Parts.

Decision:

Keep the six Parts as the only top-level directory and chapter-order
architecture. Add five cross-cutting system lenses:

- Compute
- Memory
- Communication
- Scheduling
- State

`ROADMAP.md` owns both axes:

- the vertical reading and ownership axis assigns each chapter a primary
  problem owner; Part I is a meta-level coordinate system rather than a
  lifecycle execution stage;
- the horizontal system lenses provide topic-specific reading paths across
  Parts.

The four production, delivery, control, and action-loop views in Chapter 3 are
system-responsibility perspectives. They do not form a third competing chapter
hierarchy.

Horizontal chapter sequences are thematic reading paths, not claims of direct
technical lineage. Each cross-Part handoff should identify whether it is
evolution, layering/dependency, principle reuse, or analogy.

Memory and State remain separate lenses even when they point to the same
chapter:

- Memory asks where bytes reside, how much capacity they consume, and when
  they move, remain, or are evicted.
- State asks what those bytes mean, who owns them, which version is valid, and
  when they commit or recover.

The book also distinguishes four kinds of historical connection:

1. direct evolution;
2. layering or dependency;
3. principle reuse;
4. explanatory analogy.

This prevents similar constraints from being presented as unsupported direct
lineage. For example, KV Cache can reuse cache and paging principles without
being a direct descendant of CPU Cache, and NIXL can coexist with collective
libraries without being their next version.

Framework-focused chapters remain valid implementation studies, but their
titles and central theses should name the stable system problem first and the
framework second.

Alternatives considered:

1. Replace the six Parts with Compute, Memory, Communication, Scheduling,
   Inference, Training, and AI Runtime. Rejected because the categories are not
   at one abstraction level and would fragment the capability lifecycle.
2. Add a seventh foundational Part and renumber Chapters 23-80. Rejected
   because the stable mechanisms can be owned by existing chapters, while
   renumbering would create broad mechanical churn and fragile references.
3. Keep the current outline with no cross-cutting navigation. Rejected because
   it leaves important system evolution paths implicit and encourages
   framework-by-framework reading.

Consequences:

- The repository keeps six Part directories and Chapters 1-80.
- Chapter 3 owns the dual-axis global map.
- Chapter 9 owns the system-evolution method and relationship taxonomy.
- Chapter 32 owns distributed communication foundations for training and
  points forward to inference state transfer.
- The State path starts at Chapter 19's KV-state origin and includes Chapter
  71's per-invocation Context before Chapter 73's persisted Memory.
- Runtime and infrastructure product chapters are named as stable problems
  with the current framework as an implementation case.
- New chapters are not added solely to create a second copy of a cross-cutting
  topic; the horizontal lens points to the existing primary owner.

---

## ADR-006：将面试证据与书稿、研究归档分离

状态：

已接受

日期：

2026-08-03

背景：

仓库六个 Part 的书稿已经形成完整 Draft，`papers/` 负责按时间归档 primary-source
研究证据。面试准备会产生另一类材料，包括岗位矩阵、压缩答案、限时练习、项目故事、
Mock 反馈和投递就绪记录。这些材料的变化速度快于稳定章节，不应重新定义知识树。

决策：

- 稳定的解释性内容继续放在 `books/`，研究证据继续放在 `papers/`。
- 可执行 benchmark、profiling、故障注入和一体化 AI Platform Capstone 放在
  `labs/`。
- 16 周计划、逐周 Checklist、岗位矩阵、问题库、设计练习、项目故事和 Mock 记录
  放在 `interview/`。
- 只有当面试发现暴露了长期有效的知识缺口，并通过仓库正常的来源与写作门禁时，
  才将其沉淀到 `books/`。

影响：

- 面试准备可以针对知识提取速度和可测量的就绪程度优化，同时不会把 Book 变成题库。
- 性能和项目结论必须指向 `labs/` 中的可复现证据，或明确标注的既有生产证据。
- `ROADMAP.md` 继续作为知识树的 single source of truth；`interview/` 不构成
  第七个 Part。

---

## ADR-007：分离 Source-Family Books Gate 与 Archive Completion Gate

状态：

已接受

日期：

2026-08-13

背景：

历史 Weekly 回填同时面对两类不同完成条件。第一类是某个 Source Family 的身份、版本、正文、方法、实验、limitations、artifact 与章节边界已经完成审计，足以判断长期机制。第二类是一个完整年度的 discovery replay、blocked source 恢复、revision 去重和材料清单全部闭合。若把两者绑成一个 Gate，少数不可访问材料会长期冻结已经可靠的知识；若完全取消 Archive Gate，又会把局部完成误写成年度无遗漏。

决策：

- `Source-Family Books Gate` 按 Source Family 独立判断。只有 identity、first-public/revision、full-read coverage、claim/evidence boundary、owner 与相邻章节均完成，且状态不是 `Blocked`、`Disputed` 或仅有 `Version Fact`，才能进入 Books。
- `Archive Completion Gate` 判断一个 Daily/Weekly/年度归档是否已经完成 discovery、去重、缺口恢复和材料账本。它可以保持 Open，而不阻塞已通过前一 Gate 的 Source Family。
- Weekly 摘要和评分本身不构成 Books Gate；正文必须能回溯到 primary source review。
- 进入 Books 后，同步对应研究记录的 owner、current/legacy chapter、integration decision、changed files 与 open questions。
- Archive 仍 Open 时，任何状态汇总必须准确写明剩余 Blocked/Discovery Gap，不得宣称年度审计全部完成。

影响：

- 可靠机制能及时沉淀，而材料缺口继续可见。
- Books 的完成度不再等同 papers archive 的召回完备度。
- 需要维护 Source Family identity，避免同一论文、release 和后续 artifact 被重复吸收。

---

## ADR-008：新增 Part III、扩展至 84 章并引入 Stable Knowledge Node ID

状态：

已接受

日期：

2026-08-13

背景：

2026 研究审计表明，多模态表示、跨模态生成、World Model 与 Embodied/VLA 已形成连续知识链。继续把这些机制分散寄居在 Ch10、Data、Inference execution 或 Agent 章节，会混淆 representation、generation、environment state 与 action authority。另一方面，章节号已被大量 Weekly 引用；直接把编号当永久身份会让未来结构调整产生语义歧义。

决策：

- 在 Model 与 Training 之间新增 Part III：多模态、生成与世界模型。
- 新增 Ch23～26：多模态表示、生成范式、World Models、Embodied AI/VLA。
- 原 Ch23～80 顺延为 Ch27～84，形成七 Part / 84 章结构。
- 为全部章节引入 Stable Knowledge Node ID；ID 按长期问题域与冻结语义 slug 生成，不随阅读顺序变化。
- `ROADMAP.md` 同时维护 Node ID、current chapter、current path 与 legacy chapter。
- 历史 Weekly 的旧章节号不机械重写；年度索引提供 legacy mapping。以后研究记录优先写 Stable Node ID，并附 current/legacy chapter。
- AI for Science 保持 Data → Evaluation → Workflow → Security 的领域路线；compiler/kernel/hardware co-design 保持 Model/Training → inference execution → resource scheduling 路线，不新增独立 Part。

备选方案：

1. 保持 80 章，只在 Ch10 增写 World Model。拒绝：会让趋势章成为机制杂物篮子，无法承载 representation→action 的连续推导。
2. 使用 Ch22A～22D，避免重编号。拒绝：阅读顺序与文件路径会长期保留例外，难以形成清晰 Part 边界。
3. 为 AI for Science 或 hardware 单独建 Part。暂缓：目前证据显示它们是跨章节领域路线和横轴，而不是同一抽象层的纵向知识主干。

影响：

- ADR-005 中“保持六 Part / 80 章”和“拒绝第七 Part”的结构结论被本 ADR 取代；其五条横轴、Memory/State 区分与四种演进关系继续有效。
- Ch10 收缩为未来情景与 handoff；原 Training、Inference、Infrastructure、Agent 章节内容保留并顺延。
- 新研究首先定位 Stable Node ID，只有现有 owner 无法承载时才提出 Structural Candidate。
