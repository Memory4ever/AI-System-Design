# 2026-05-08 Independent Fresh-Context Audit

## Auditor Independence and Scope

- Role: non-author reviewer for the 2026-05-08 author packet.
- Scope: all 898 registered identities, the author denominator of 40, all 858
  pre-denominator closures, exact-v1 claim boundaries, Deep Analysis selection,
  and current owner plus adjacent Books comparison.
- Method: full title-and-abstract replay, followed by adversarial exact-v1 review
  for every retained family and for every closure whose title/abstract suggested
  a change to persistent state, control ownership, serving/training runtime,
  security boundary, or evaluation contract.
- Cross-model critique was not used because this autonomous lane had no
  interactive authorization for an external reviewer. Independence comes from
  a different agent/context and a clean replay of the frozen author packet.

## Author-to-Audit Reconciliation

| Metric | Author packet | Independent audit | Delta |
| --- | ---: | ---: | ---: |
| Registered / screened | 898 / 898 | 898 / 898 | 0 |
| Candidate Denominator | 40 | 58 | +18 |
| Pre-denominator closures | 858 | 840 | -18 |
| Exact-v1 complete | 36 | 58 | +22 |
| Blocked | 4 | 0 | -4 |
| Integrate queue | 32 | 47 | +15 |
| No Change — Existing Coverage | 4 | 11 | +7 |

The audit did not promote papers merely because official HTML was available.
The 18 promotions below each alter a stable system contract. Conversely, 11
retained families remain in the denominator but no longer request a Books
write because current chapters already carry the durable proposition or the
exact-v1 result is too workload-specific to change it.

## False-Negative Repairs

| arXiv v1 | Why the author closure was false negative | Exact-v1 locators | Stable owner | Books decision |
| --- | --- | --- | --- | --- |
| 2605.05583 | Memory changes from a point estimate to a versioned set of competing hypotheses; write, merge, retrieval, and action now share explicit uncertainty state. | §3.1–3.3; §4; Appendix D | `AGENT-MEMORY` | Integrate |
| 2605.05687 | Output auditing is tied to the training corpus through a controlled provenance subject, hard negatives, and response-side attribution rather than generic semantic similarity. | §3 FakeWiki; §4 Methods; §5–6; Limitations | `TRAIN-DATA` | Integrate |
| 2605.05701 | Tool and token budgets become runtime control state; the controller decides whether the next unit goes to retrieval, decomposition, or answer commit. | §3–4; §5; §6 | `AGENT-PLANNING` | Integrate |
| 2605.05724 | Search proposals are not the artifact: evaluator-owned outcomes, executable diffs, failure labels, and shared lineage form the persistent research state. | §3; §4; §5–6 | `PLATFORM-EVALUATION-SYSTEM` | Integrate |
| 2605.05868 | Least privilege becomes task-conditioned and action-level; replay checks whether removing an action preserves core flow before the runtime constrains it. | §3 design; §5; §6 | `PLATFORM-SECURITY` | Integrate |
| 2605.06105 | Prefill and decode no longer expose identical layerwise KV visibility; the runtime must own the asymmetric cache contract and its accuracy fallback. | §3–4; §5; §6 | `INFER-PREFILL` | Integrate |
| 2605.06113 | Data-parallel routing must account for live queue/KV work and tail latency, not just round-robin request count. | §3–4; §6; §7 | `INFER-SCHEDULING` | Integrate |
| 2605.06136 | Repository evaluation becomes a two-sided build/find protocol with navigation effort and inspectability, separating artifact correctness from future-agent maintenance cost. | §3–4; §5; §6 | `PLATFORM-EVALUATION-SYSTEM` | Integrate |
| 2605.06161 | A safety judge must remain invariant under policy-preserving rewrites; scalar accuracy cannot hide rubric-framing sensitivity. | §3; §4; §5 Limitations | `PLATFORM-EVALUATION-SYSTEM` | Integrate |
| 2605.06327 | Paired prompts make evaluation-context divergence an explicit measurement subject; familiarity remains only a contamination proxy. | §2–3; §4; Limitations | `PLATFORM-EVALUATION-SYSTEM` | Integrate |
| 2605.06365 | Agent loops are compiled into deterministic execution graphs carrying inputs, outputs, revisions, and lineage, moving reproducibility from transcript convention to workflow state. | §4–5; §8; §9.6–9.7 | `AGENT-WORKFLOW` | Integrate |
| 2605.06455 | Failure detection moves from final outcome checks to prefix-time trace monitors with an intervention horizon and explicit false-warning cost. | §4; §5; §6 | `PLATFORM-MONITORING` | Integrate |
| 2605.06544 | Infrastructure comparisons require a trace subject that freezes model, hardware, framework, parallelism plan, collective overlap, and run scripts. | §3–4; Appendix C; §5 | `PLATFORM-EVALUATION-SYSTEM` | Integrate |
| 2605.06635 | Citation presence and source support become separate claim-level evidence states; parsing, resolution, and support verification cannot be collapsed into one citation score. | §2–3; §4; §5 | `PLATFORM-EVALUATION-SYSTEM` | Integrate |
| 2605.06890 | Exact-v1 exposes a white-box tool-decision sensor, but only for the studied layers/models; this is retained for evidence completeness while current Books already own monitor-versus-authority separation. | §3; §4; Limitations | `AGENT-TOOL-CALLING` | No Change — Existing Coverage |
| 2605.06914 | Parallel branch count becomes a regulated runtime variable rather than a fixed sampling knob; controller error and branch contention enter the serving SLO contract. | §3; §4; §5 | `INFER-SCHEDULING` | Integrate |
| 2605.07068 | A wiki is a compiled, evaluated, revisable knowledge artifact whose freshness and cache identity must be managed at write time, not a static prompt blob. | §3–4; §5; §6 | `AGENT-MEMORY` | Integrate |
| 2606.00050 | Typed bottom-up comprehension and transactional denormalization make write-time knowledge compilation explicit, but current RAG/Context chapters already carry canonical-byte identity, provenance, and invalidation. | §2–3; §4; §5 | `AGENT-RAG` | No Change — Existing Coverage |

## Recovered Exact-v1 Material

The four author blockers were access-route failures, not missing primary
evidence. Official arXiv exact-v1 HTML/PDF was readable, so all four material
requests are removed.

| arXiv v1 | Recovered review boundary | Owner / decision |
| --- | --- | --- |
| 2605.06152 | §3 proves the finite-precision Softmax-collapse/NFI feedback; §4.2 tests mitigations; §4.3 shows visible spikes need not occur in mini-batch/LLM settings; §5 limits the feature-dynamics model. The paper does not prove that every production spike is NFI. | `TRAIN-PRETRAINING` / Integrate |
| 2605.06997 | §3.2 defines constant-size sufficient statistics and spectral retrieval; §6.2 discloses the FP32 Cholesky and small-matrix bottleneck; Appendix G freezes architectures. The result is an alternative recurrent-memory branch, not evidence that KV caches are obsolete. | `MODEL-KV-CACHE` / Integrate |
| 2605.07042 | §3 formulates search as CGDP; §6 evaluates four harnesses on three domains; §7 separates orchestrator-owned operations from model-owned representation. LLM-judge and domain scope remain explicit. | `AGENT-CONTEXT` / Integrate |
| 2605.07073 | §2.1 enforces Planner/Executor/Verifier permissions in separate containers; §3 uses deterministic graders and paired statistics; §3.5 reports verifier false acceptance. It does not establish arbitrary dynamic-team or multi-round scaling. | `AGENT-MULTI-AGENT` / Integrate |

## False-Positive and Books Over-Integration Challenge

The following families remain retained because they are meaningful evidence,
but they do not require a new Books delta after reading the current owner and
both adjacent chapters:

- `2605.05699`: Apple-Silicon INT4 KV is a hardware-specific case already
  covered by per-device quantization/kernel crossover and fallback rules.
- `2605.06068`: agent-generated serving stacks do not change the existing rule
  that generated plans require executable evaluation, bounded search, and
  human/root commit authority.
- `2605.06185`: event segmentation and dual-store retrieval are a domain case
  of the existing RAG provenance/freshness and multimodal state contracts.
- `2605.06221`: dynamic sparse prefill plus continuous batching is already
  covered by prefill sparsity, chunking, and scheduler-aware fallback.
- `2605.06527`: stale-memory adjudication, revision, and propagation are
  already explicit in `AGENT-MEMORY`.
- `2605.06663`: document-level MoE routing is an experimental instance of the
  existing routing/capacity/load-balance branch.
- `2605.06869`: sequential-agent benchmark identity is already captured by
  model × harness × environment × scorer × budget.
- `2605.06890`: white-box probes are sensors, not authorization; current Tool
  and Security chapters already make this boundary explicit.
- `2605.07021`: behavior-cue monitors remain model/workload-specific sensors;
  they do not supersede external policy enforcement.
- `2605.23950`: harness disclosure and harness-induced ranking reversal are
  already explicit in the Evaluation chapter.
- `2606.00050`: write-time compilation adds a concrete architecture but no new
  durable owner beyond existing canonical artifact, provenance, and invalidation.

The remaining 47 `Integrate` decisions represent missing conditional design
judgments, not an instruction to copy paper descriptions. Root writeback must
place each delta inside the existing evolution chain and preserve fallback and
coexistence boundaries.

## Deep Analysis Challenge

All 58 retained families received a Source Review. The three narrative units
remain selected because they are mutually orthogonal and cross layer:

1. heterogeneous HBM/PIM state ownership (`2605.05639`);
2. failure-aware hybrid-parallel control (`2605.06374`);
3. persistent-state writeback security (`2605.06731`).

The newly promoted families are important but owner-local; selecting more would
turn the Daily into 18 additional paper summaries rather than improve its
cross-system explanatory spine.

## Final Audit Result

- Coverage: `Passed` — 898/898 replayed; denominator reconciled to 58.
- Evidence: `Passed` — 58/58 exact-v1 reviews; blocked/material requests 0.
- Books comparison: `Passed` — 47 queued, 11 No Change.
- Books Gate: `Open` — shared Books writeback and a separate post-write
  fresh-context semantic audit are still required.
- Unresolved findings: 1 (Books writeback/post-write audit only).

