# V3 Round 7 Bounded Author Repair — 2026-05-13

- Audit time: 2026-09-15T16:51:28+08:00
- Scope: exactly six false negatives; no window/source/838-identity replay
- Books mutation: none
- Denominator: 157 retained + 490 closure + 191 isolation = 838

## Decisions

## 2605.11136 — EVOCHAMBER: Test-Time Co-evolution of Multi-Agent System at Individual, Team, and Population Scales

Multi-Agent 的 test-time learning 不能简化为 N 个单 Agent memory 更新：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同状态 owner。

- V3: 8 (3+2+3)
- Owner: `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`
- Decision: Integrate — Root write required
- Evidence: https://arxiv.org/html/2605.11136v1
- Withdrawal: no official banner observed

## 2605.11167 — The Bicameral Model: Bidirectional Hidden-State Coupling Between Parallel Language Models

两个 frozen LM 可在每个 generation step 通过 trainable hidden-state interface 双向通信；这改变的不是消息格式，而是并发 agent 的同步、causal schedule 与 tool-state ownership。

- V3: 7 (3+2+2)
- Owner: `AGENT-MULTI-AGENT` → `books/part-07-agent/82-multi-agent.md`
- Decision: Integrate — Root write required
- Evidence: https://arxiv.org/html/2605.11167v1
- Withdrawal: no official banner observed

## 2605.11169 — OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents

在 frozen ReAct reasoner 与 tool execution 之间加入 deployment-time contextual bandit，使 action selection 能由 action-level feedback 在线更新，而不重训 reasoning model。

- V3: 8 (3+2+3)
- Owner: `AGENT-TOOL-CALLING` → `books/part-07-agent/78-tool-calling.md`
- Decision: Integrate — Root write required
- Evidence: https://arxiv.org/html/2605.11169v1
- Withdrawal: no official banner observed

## 2605.11225 — PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement

把完整 trajectory 视为可版本化、可验证的优化状态：执行产生 discrepancy，再用 structured textual gradient 定位并替换 suffix，只有验证后不退化才提交。

- V3: 7 (3+2+2)
- Owner: `AGENT-PLANNING` → `books/part-07-agent/79-planning.md`
- Decision: Integrate — Root write required
- Evidence: https://arxiv.org/html/2605.11225v1
- Withdrawal: no official banner observed

## 2605.11996 — BadSKP: Backdoor Attacks on Knowledge Graph-Enhanced LLMs with Soft Prompts

KG-derived soft prompt 是独立于可见文本的 graph-conditioned channel；攻击上游 KG representation 可在不改用户文本时改变模型行为，因此 graph→projector→prompt 必须成为供应链信任边界。

- V3: 9 (3+3+3)
- Owner: `PLATFORM-SECURITY` → `books/part-06-ai-infrastructure/72-security.md`
- Decision: Integrate — Root write required
- Evidence: https://arxiv.org/html/2605.11996v1
- Withdrawal: no official banner observed

## 2605.12477 — MEME: Multi-entity &amp; Evolving Memory Evaluation

长期 memory 不能只测静态 recall；多实体状态随时间变化时，Deletion、Cascade 与 Absence 分别测试过期事实、依赖传播和无证据拒答。

- V3: 9 (3+3+3)
- Owner: `PLATFORM-EVALUATION-SYSTEM` → `books/part-06-ai-infrastructure/66-evaluation-system.md`
- Decision: Integrate — Root write required
- Evidence: https://arxiv.org/html/2605.12477v1
- Withdrawal: no official banner observed

## Gate

Author repair is complete but not a completion signature. Root later applied all six queued writes. Daily remains Ongoing pending a different fresh non-author reviewer.
