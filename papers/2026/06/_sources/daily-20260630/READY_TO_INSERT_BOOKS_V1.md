# 2026-06-30 Ready-to-Insert Books Packet V1

> Prewrite packet; do not apply without root's shared Books lock.

## AGENT-MEMORY

- Target: `books/part-07-agent/77-memory.md`
- Adjacent reviewed: `books/part-07-agent/75-context.md`
- Source Families: SF-2026-ARXIV-2606-30788

### 最小正文

把一条文本记忆删除，或直接修改模型权重，在状态单一时曾经可以近似实现遗忘。多模态关联和分阶段学习让事实可从图像、关系边或后续 safety state 中恢复，粗粒度 unlearning 还会误伤公共技能。memory owner 因而要持有跨模态 provenance graph，并把可撤销私有状态隔离到 process sidecar；收益是可验证删除与选择性撤销，代价是额外 lineage、sidecar 生命周期和残留扫描。证据不证明任意架构都能完全遗忘；provenance 不完整时隔离实体并保留人工审计，原始删除和重训作为高成本 fallback 共存。

### exact-v1 Review notes

- **SF-2026-ARXIV-2606-30788 / arXiv:2606.30788v1**：用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。 证据见 arXiv:2606.30788v1 — §3 Method; §Safety post-training.; §Sensitivity through training. 与 arXiv:2606.30788v1 — §2 Setting and evaluation; §5 Experiments; §5.1 Setup；边界见 arXiv:2606.30788v1 — §6 Discussion and limitations; §7 Conclusion; §B.7 Boundary cases for the second-order frontier。未证明未测模型、任务、硬件或生产 SLO；前提失败时回到本节既有保守路径。

## AGENT-PLATFORM

- Target: `books/part-07-agent/84-agent-platform.md`
- Adjacent reviewed: `books/part-07-agent/83-mcp.md`
- Source Families: SF-2026-ARXIV-2606-30616

### 最小正文

靠增加参数获得通用能力，在交互 horizon 短且工具面有限时曾经有效。长程 Agent 的瓶颈转为知识—动作轨迹、领域路由 teacher 与 on-policy distillation，平台需持有 atomic ability graph、horizon budget、teacher route 和失败轨迹。收益是小模型以更长执行链覆盖任务，代价是工具成本、错误累积与训练基础设施复杂度。35B 结果不证明参数规模不再重要；预算或校验不足时缩短 horizon 并转交强模型/人工。

### exact-v1 Review notes

- **SF-2026-ARXIV-2606-30616 / arXiv:2606.30616v1**：以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。 证据见 arXiv:2606.30616v1 — §2 Knowledge-Guided General Agent Training with Specialized Teachers; §4 Three-stage Training Recipe; §4.2 Domain-level Teacher Training 与 arXiv:2606.30616v1 — §5 Experimental Results; §5.1 Evaluation Setting; §5.2 Results and Observations；边界见 arXiv:2606.30616v1 — §6 Limitation and Future Work。未证明未测模型、任务、硬件或生产 SLO；前提失败时回到本节既有保守路径。

