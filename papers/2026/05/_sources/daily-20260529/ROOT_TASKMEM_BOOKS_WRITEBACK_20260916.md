# 2026-05-29 TaskMem Books Writeback

Root serialized `SF-2026-SEED-TASKMEM` into `AGENT-MEMORY` after the author-side V3 decision.

The body delta adds a connected evolution:

```text
fixed or general memory-quality policy
-> task-conditioned lightweight adapter
-> recent-task relevance proxy
-> deterministic provenance / authorization / durable commit
```

The prose separates raw evidence, policy proposal, evaluation acceptance and durable commit. It also preserves adapter drift, recent-task bias, cross-task forgetting, evidence limits and fallback to the general policy plus raw evidence. The paired marker is `semantic-body-binding:SF-2026-SEED-TASKMEM:start/end`.

The report remains `Ongoing` until a fresh non-author reviewer validates the source, Ch76/Ch77/Ch78 handoff and writeback.
