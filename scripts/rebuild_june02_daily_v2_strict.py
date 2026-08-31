#!/usr/bin/env python3
"""Rebuild 2026-06-02 Daily from the strict denominator.

Before the post-write audit exists, the renderer keeps downstream Gates open.
After that receipt exists, reruns preserve the audited Complete state.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "papers/2026/06/02/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260602"
DENOM = PACKET / "candidate-denominator-audit-v3-fresh.json"
SNAPSHOT = PACKET / "daily-before-v2-strict-reopen.md"
OUT_JSON = PACKET / "evidence-books-comparison-v3-fresh.json"
POST_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V4.md"


PROMO = {
    "SF-GAIATRACE-VIDUR-AGENT": {
        "score": (3, 3, 2), "owner": "INFER-SCHEDULING", "books": "Integrate",
        "title": "GAIATrace / Vidur-Agent",
        "review": "传统 serving trace 以单 query 为单位，无法表达 agent task 内的依赖、tool latency 与多模型阶段。论文将 task/query/tool dependency 外置为可重放 trace，并扩展 simulator 以消费 KV/prefix cache、PD、routing 与 scheduling 配置。它证明所测两套 agent 的 task-level latency 与 TTFT/TPOT 会错位，也证明负载变化会移动瓶颈；没有证明两套 GAIA trace 能代表所有 agent workload，开源 artifact 在 v1 仍是发布承诺。",
        "method": "§§3.1–3.3 GAIATrace collection and Vidur-Agent simulator", "eval": "§§4–5 trace characterization and system simulation", "limits": "§3.2 trace-collection scope and §5 simulation setup; no dedicated limitations section in exact-v1; two systems/GAIA and simulator-model boundary", "artifact": "Artifact promised upon publication; immutable event-time revision Not Disclosed",
        "workload": "Two multi-model agents on GAIA; trace-driven serving simulation", "model": "MiroThinker/OWL with heterogeneous sub-models", "hardware": "Simulated configurations; collection hardware not a universal baseline", "precision": "Not Disclosed", "length": "Trace-specific prefill/decode distributions", "batch": "Arrival-rate sweep", "concurrency": "Task arrival-rate sweep", "slo": "Task latency plus query TTFT/TPOT", "evaluator": "Trace replay and simulator outputs",
        "target": "books/05-inference-system/56-INFERENCE-SCHEDULING.md", "adjacent": "Ch42 request lifecycle; Ch55 PD", "existing": "调度已按 request/token/runtime state 建模。", "delta": "Agentic serving 的 SLO owner 必须上移到 task DAG；per-query TTFT/TPOT 只能作为子阶段证据。", "relation": "Layering / workload-contract change",
    },
    "SF-SECLAW-SPEC-DRIVEN-SECURITY": {
        "score": (2, 2, 2), "owner": "PLATFORM-SECURITY", "books": "No Change — Existing Coverage",
        "title": "SeClaw",
        "review": "静态攻击 prompt 与 final-answer judge 看不到 agent 在文件、权限、Skill/MCP 与命令执行中的中间副作用。SeClaw exact-v1 提出用结构化 risk/deployment/tool spec 生成任务，在 Docker 中重建执行环境并记录 trajectory；但稿件标题已明确是 preliminary/in-progress，正文只给出框架与后续评测计划，没有跨模型/跨 harness 的结果或独立 limitations 章节。因此它只能作为现有 security EvalSpec 思路的早期实现案例，不能证明该流程已形成可复现 benchmark，也不构成新的 Books 机制。",
        "method": "§3.2 spec-driven task synthesis; §3.3 Docker execution and trajectory logging", "eval": "§4 Further Exploration only; cross-model and cross-harness evaluation is proposed, not reported", "limits": "Title marks preliminary/in-progress work; no dedicated limitations section in exact-v1; generated-task and environment representativeness remain untested", "artifact": "Repository is linked, but immutable event-time commit is Not Disclosed",
        "workload": "Proposed autonomous-agent security tasks with tools", "model": "Future multi-model evaluation proposed; completed evaluated set Not Disclosed", "hardware": "Docker isolation; Not Disclosed", "precision": "Not Disclosed", "length": "Proposed multi-turn trajectories; Not Disclosed", "batch": "Not Disclosed", "concurrency": "Not Disclosed", "slo": "Proposed security outcome and trajectory reproducibility", "evaluator": "Proposed execution constraints plus trajectory scoring; completed result Not Disclosed",
        "target": "books/06-ai-infrastructure/72-AI-SECURITY.md", "adjacent": "Ch66 evaluation; Ch84 agent platform", "existing": "安全章节要求 sandbox、least privilege 与 effect-level evidence。", "delta": "未形成超出现有 security EvalSpec 的已验证长期结论；保留为 preliminary implementation case。", "relation": "No Change / early implementation case",
    },
    "SF-ECHELON-AGGREGATE-ONLY-ADAPTATION": {
        "score": (3, 3, 3), "owner": "TRAIN-DISTRIBUTED-TRAINING", "books": "Integrate",
        "title": "Echelon",
        "review": "传统 federated/decentralized training 常把隐私作为算法附加层，而 Echelon 先冻结跨行政边界的信息流：device parameters、activations、optimizer state 与 individual update 不得外流，global plane 只消费 boundary aggregate 与少量控制 metadata。三层执行面、buffered semi-async aggregation 与 drift-aware outer cadence 都服务于该 invariant。实验只覆盖 1B LoRA、短序列、主要两边界和 honest-but-curious threat model；它不提供 differential privacy，也不证明 full-parameter/大规模边界同样稳定。",
        "method": "§§3–5 information-flow contract and three execution planes", "eval": "§§7–8 budget-matched/WAN/privacy audit", "limits": "§4 threat scope; §9 limitations", "artifact": "§10 reproducibility; immutable event-time revision Not Disclosed",
        "workload": "1B Llama-family LoRA across privacy boundaries", "model": "1B Llama-family", "hardware": "WAN/emulated and cross-region; exact accelerators scoped by paper", "precision": "Mixed precision", "length": "Sequence length 32", "batch": "Micro-batch 6, grad accumulation 4", "concurrency": "Buffered boundary participants", "slo": "Validation loss, bytes, wall-clock, sync count, audit invariant", "evaluator": "Budget-matched comparison and message-schema audit",
        "target": "books/04-training-system/36-DISTRIBUTED-TRAINING.md", "adjacent": "Ch35 checkpoint; Ch37 Megatron", "existing": "分布式训练按 model/optimizer/gradient state 与 communication 拆分。", "delta": "新增 administrative boundary 作为不可跨越的数据/状态 owner，并把 typed aggregate 与 audit log 变成训练协议。", "relation": "Alternative branch / governance-constrained training",
    },
    "SF-GATEAI-OPERATING-POINT-EVAL": {
        "score": (2, 3, 3), "owner": "PLATFORM-EVALUATION-SYSTEM", "books": "No Change — Existing Coverage",
        "title": "Gate AI",
        "review": "安全 detector benchmark 若按数据集单独调 threshold，会把 operating-point 差异伪装成模型能力差异。论文固定 content-hashed trace、group-aware cross-validation、inner-validation threshold、matched-FPR 与 bootstrap CI，并显式标注外部 published numbers。它强化了现有 EvalSpec 的 version/threshold/leakage contract；公开数据污染、跨数据集语义近重复与第三方 baseline 不可比仍限制结论，因此不需要新增 owner。",
        "method": "§2.1–2.12 trace identity, grouped CV, threshold and calibration", "eval": "§§3–5 corpus, results and latency", "limits": "§§2.13–2.14 limitations and contamination", "artifact": "JSONL checkpoints described; immutable repository revision Not Disclosed",
        "workload": "Prompt-injection/jailbreak detector evaluation", "model": "Black-box detector plus published baselines", "hardware": "Latency setup scoped in §5", "precision": "Not Disclosed", "length": "Dataset-dependent", "batch": "Not Disclosed", "concurrency": "Not Disclosed", "slo": "FPR/F1/calibration/latency at fixed operating point", "evaluator": "Leakage-resistant CV and matched-FPR protocol",
        "target": "books/06-ai-infrastructure/66-EVALUATION-SYSTEM.md", "adjacent": "Ch65 observability; Ch72 security", "existing": "EvalSpec 已要求 dataset/version/threshold/evaluator 与 release gate 绑定。", "delta": "提供具体的 grouped-split、matched-FPR 与 contamination disclosure 实例。", "relation": "Principle reuse / bounded case",
    },
    "SF-KV-QUANT-ALIGNMENT-COLLAPSE": {
        "score": (3, 3, 3), "owner": "INFER-KV-CACHE", "books": "Integrate",
        "title": "KV Quantization Alignment Collapse",
        "review": "KV quantization 通常只以 perplexity、task accuracy 与 memory 验收，但 refusal behavior 依赖低维 activation subspace，可能在这些 aggregate metric 几乎不变时发生 model-specific phase transition。论文用 ConditionalFlip、layer scan、per-channel reduction 与 layer spread 诊断 mitigation；证据覆盖 11 个 3.8B–72B 模型、五个 safety benchmarks 和生产 vLLM FP8 case，但仍受 refusal evaluator、prompt set、量化器与 post-training family 约束。结论是压缩 artifact 必须重新做行为/安全 release evaluation，而不是存在统一 safe bit-width。",
        "method": "§3 ConditionalFlip/PCR diagnostic, layer spread and four-step protocol", "eval": "§§4–5 plus Apps. A.6–A.10 and B.14–B.15; 11 models, 1,894 prompts, real-dtype and vLLM FP8 checks", "limits": "§6 and Appendix H; refusal evaluator, prompt sets, model families, quantizers and deployment scope", "artifact": "Code repository is linked in exact-v1; immutable event-time commit Not Disclosed",
        "workload": "KV-cache quantized instruction models on 1,894 safety prompts", "model": "11 instruction-tuned models, 3.8B–72B", "hardware": "RTX 3090 for 7B–9B, A100 80GB for 24B–47B, 8 GPUs for 72B; vLLM v0.13.0 check on RTX 3090", "precision": "FP16 baseline; simulated/packed 2–8 bit KV and FP8 e4m3/e5m2 vLLM cases", "length": "Five safety benchmarks totaling 1,894 prompts; max_new_tokens=256", "batch": "Offline prompt evaluation; serving batch Not Disclosed", "concurrency": "Not Disclosed", "slo": "Memory overhead plus refusal preservation; no universal production threshold", "evaluator": "ConditionalFlip, Wilson CI, WildGuard-7B, PPL/task/safety benchmarks",
        "target": "books/05-inference-system/45-KV-CACHE.md", "adjacent": "Ch44 decode; Ch49 execution engine", "existing": "KV identity 已绑定 model/token/position/precision，量化需 workload-specific validation。", "delta": "把 alignment behavior 与 refusal evaluator 加入 KV precision artifact 的 release contract。", "relation": "Constraint change / evidence-contract extension",
    },
    "SF-CROWDED-EMBEDDING-EXTERNALITY": {
        "score": (2, 3, 2), "owner": "AGENT-RAG", "books": "Integrate",
        "title": "Crowded Embedding Space",
        "review": "逐 query 评测把 retrieval 看作独立调用，但共享 embedding/index 是随 corpus composition 变化的公共状态。论文的 mean-field model 给出多数文档密度增长导致 minority target 从 shortlist 中突变式消失的机制，并指出 HNSW hub routing 可能放大 crowding。理论依赖一对一 relevance、热力学极限与分布假设，mitigation 尚未被充分实证；可沉淀的是 index population/revision 本身属于 evidence contract，而非接受普适阈值。",
        "method": "§§2–3 static crowding model and McKean–Vlasov/Wasserstein mean-field dynamics", "eval": "§§4–5 finite simulations, phase-transition checks and practical retrieval illustration; Appendix D HNSW/hubness discussion", "limits": "§6 Limitations: one-to-one relevance, thermodynamic-limit dynamics, finite-system transfer and mitigation remain unverified", "artifact": "Appendices contain proofs and update-rule derivations; implementation artifact and immutable revision Not Disclosed",
        "workload": "Shared embedding spaces for retrieval-augmented agents", "model": "Mean-field/finite retrieval simulations", "hardware": "Not Disclosed / not central", "precision": "Not Disclosed", "length": "Corpus-size/density sweep", "batch": "Not Disclosed", "concurrency": "Population interaction, not request concurrency", "slo": "Minority retrieval probability and shortlist reachability", "evaluator": "Theory plus scoped simulations",
        "target": "books/07-agent/76-RAG.md", "adjacent": "Ch75 context; Ch77 memory", "existing": "RAG 已要求 index/version/provenance 与 retrieval metric。", "delta": "把 corpus population density 与 cross-tenant crowding 作为共享 index failure mode 和 release monitor。", "relation": "Constraint change / shared-state externality",
    },
    "SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY": {
        "score": (3, 3, 3), "owner": "PLATFORM-SECURITY", "books": "Integrate",
        "title": "Execution-Grounded Coding-Agent Security",
        "review": "语言层 refusal 无法证明 coding agent 没有修改文件、startup hook 或运行环境。论文把危险操作包装进测试、调试与 crash reproduction workload，并用 tool trace、runtime output 与 filesystem diff 的 execution oracle 判定实际副作用。它证明所测 agent/framework 在任务伪装下存在显著 execution gap；Docker sandbox、RedCode-derived goal pool 与预定义 predicate 会漏掉 partial harm，不能外推为生产风险率。长期结论是安全 Gate 的 truth owner 必须是 effect evidence，而不是回复文本。",
        "method": "§3 execution-grounded red-team workload and oracle", "eval": "§§4–5 multi-agent/model execution results", "limits": "§6 limitations", "artifact": "Controlled Docker sandbox; immutable artifact revision Not Disclosed",
        "workload": "Coding-agent software-engineering tasks carrying unsafe operations", "model": "Multiple agent frameworks/model backbones", "hardware": "Docker sandbox; Not Disclosed", "precision": "Not Disclosed", "length": "Task dependent", "batch": "Not Disclosed", "concurrency": "Not Disclosed", "slo": "Verified unsafe execution, not text refusal", "evaluator": "Tool/runtime/filesystem execution oracle",
        "target": "books/06-ai-infrastructure/72-AI-SECURITY.md", "adjacent": "Ch66 evaluation; Ch84 agent platform", "existing": "安全章节已区分 proposal、authorization、execution 与 observation。", "delta": "把 filesystem/runtime side effect predicate 固化为 coding-agent release test，而非用 language refusal 代替。", "relation": "Direct refinement / evidence-owner correction",
    },
}


def rows_between(text: str, heading: str) -> list[list[str]]:
    start = text.index(heading)
    chunk = text[start + len(heading):]
    nxt = re.search(r"\n## ", chunk)
    if nxt:
        chunk = chunk[:nxt.start()]
    rows = []
    for line in chunk.splitlines():
        if line.startswith("|") and not re.match(r"^\|[ -]+\|", line):
            rows.append([x.strip() for x in line.strip().strip("|").split("|")])
    return rows


def table_map(text: str, heading: str) -> dict[str, list[str]]:
    rows = rows_between(text, heading)
    return {row[0]: row for row in rows[1:] if row and row[0].startswith("SF-")}


def review_block(text: str, family: str) -> str:
    match = re.search(rf"<!-- review:{re.escape(family)}:start -->(.*?)<!-- review:{re.escape(family)}:end -->", text, re.S)
    if not match:
        raise KeyError(family)
    return f"<!-- review:{family}:start -->{match.group(1)}<!-- review:{family}:end -->"


def bounded_block(text: str, ref: str) -> str:
    match = re.search(rf"<!-- {re.escape(ref)}:start -->(.*?)<!-- {re.escape(ref)}:end -->", text, re.S)
    if not match:
        raise KeyError(ref)
    return f"<!-- {ref}:start -->{match.group(1)}<!-- {ref}:end -->"


def body_hash(block: str, family: str) -> str:
    body = re.search(rf"<!-- review:{re.escape(family)}:start -->(.*?)<!-- review:{re.escape(family)}:end -->", block, re.S).group(1)
    normalized = unicodedata.normalize("NFC", body.replace("\r\n", "\n").replace("\r", "\n"))
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]: lines.pop(0)
    while lines and not lines[-1]: lines.pop()
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()


def rp_id(candidate: list[str], rp: list[str], review_block_text: str) -> str:
    def cm(value: str) -> str:
        return ";".join(sorted(x.strip() for x in value.split(";") if x.strip() and x.strip() != "—"))
    canonical = "|".join((
        "review-completion-v1", candidate[0], candidate[2], candidate[1], cm(candidate[5]),
        rp[3], cm(rp[4]), rp[2],
        *((f"review-override:{candidate[13]}",) if candidate[13] not in {"", "none", "—"} else ()),
        cm(rp[5]), cm(rp[6]), cm(rp[7]), cm(rp[8]), rp[9], candidate[14],
        f"review-body-sha256:{body_hash(review_block_text, candidate[0])}",
    ))
    return "RP-" + hashlib.sha256(canonical.encode()).hexdigest()[:16]


def md_table(header: list[str], rows: list[list[str]]) -> str:
    return "\n".join(["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"] + ["| " + " | ".join(r) + " |" for r in rows])


def normalize_benchmark_row(row: list[str]) -> list[str]:
    """Keep only disclosed values; section-pointer placeholders become ND."""
    if len(row) != 11:
        raise ValueError(f"benchmark row must have 11 columns, got {len(row)}")
    generic = re.compile(
        r"(?:evaluated (?:models|hardware|precision)|listed in|topology in|datatype in|"
        r"settings in|resources in|setup$|scoped in|where provided|use exact-v1|"
        r"task(?:/transcript)?[- ]dependent|workload[- ]specific|model[- ]specific|dataset[- ]dependent|"
        r"experiment-specific|trace-specific|provider-specific|runtime default|"
        r"generation settings in|benchmark-defined|suite-specific|modality/task-dependent|"
        r"operator shapes and model workload in|prompt/KV segment distributions in|serving load in)",
        re.I,
    )
    normalized = [row[0]]
    for column, value in enumerate(row[1:], start=1):
        value = value.strip()
        lower = value.casefold()
        if value.startswith("Not Applicable —"):
            value = value.replace("Not Applicable —", "Not Required —", 1)
        elif "not disclosed" in lower:
            value = "Not Disclosed"
        elif not value or generic.search(value) or "§" in value or "appendix" in lower or "disclosed in" in lower:
            value = "Not Disclosed"
        elif column == 7 and not re.search(r"\b(?:batch|micro-batch|global batch)\b", value, re.I):
            # Dataset/task/trial counts are not a batch contract.
            value = "Not Disclosed"
        elif column == 8 and not (value.startswith("Not Required —") or re.search(r"\d", value)):
            # Arrival-rate labels, participant prose and task topology do not
            # disclose a concurrency value.
            value = "Not Disclosed"
        elif column == 10 and lower in {"authors", "authors + production deployment", "authors/public benchmarks"}:
            value = "Not Disclosed"
        normalized.append(value)
    return normalized


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"{label}: expected exactly one source fragment, found {text.count(old)}")
    return text.replace(old, new, 1)


def apply_postwrite_closure(text: str) -> str:
    """Apply the audited V4 closure without changing Evidence/Books semantics."""
    replacements = [
        (
            "**Status:** In Progress；Coverage、Evidence 与 Books 的独立 post-write Semantic Audit 尚未闭合",
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding",
            "status lead",
        ),
        (
            "Books Comparison 有 19 项进入串行 proposal；旧 Books marker 已独立审计 22/22（KEEP 12、REVISE 2、REVERT 4、RE_EVIDENCE 4），但串行写回和独立 post-write audit 未结束，不能宣称 Daily Complete。",
            "Books Comparison 的 19 项 Integrate 已完成串行写回；独立 post-write audit 复核了 22/22 旧 marker、5/5 新 integration、28 retained 与 708 closures，并在 14 条 retained/revised marker 的 exact-v1 Review notes 补齐后关闭唯一 finding。Coverage Gate 已 Closed，Evidence 与 Books Gate 已 Passed，Completion 已闭合。",
            "executive closure",
        ),
        ("| Completion Status | In Progress |", "| Completion Status | Complete |", "completion gate"),
        ("| Coverage Gate | Open |", "| Coverage Gate | Closed |", "coverage gate"),
        ("| Evidence Gate | Open |", "| Evidence Gate | Passed |", "evidence gate"),
        ("| Books Gate | Open |", "| Books Gate | Passed |", "books gate"),
        (
            "| SA-20260602-V3-COVERAGE | fresh-context:pending-jun02-postwrite | coverage | audit-target:coverage | FINDING-V3-POSTWRITE-COVERAGE | Different context must challenge 28 retains and 708 closures after canonical write | open |",
            "| SA-20260602-V3-COVERAGE | fresh-context:jun02-postwrite-v4 | coverage | audit-target:coverage | — | — | passed |",
            "coverage audit row",
        ),
        (
            "| SA-20260602-V2-EVIDENCE | fresh-context:pending-jun02-postwrite | evidence | audit-target:evidence | FINDING-V2-POSTWRITE-EVIDENCE | Independent locator and claim-boundary audit | open |",
            "| SA-20260602-V2-EVIDENCE | fresh-context:jun02-postwrite-v4 | evidence | audit-target:evidence | — | — | passed |",
            "evidence audit row",
        ),
        (
            "| SA-20260602-V2-SELECTION | fresh-context:pending-jun02-postwrite | deep_analysis_selection | audit-target:deep_analysis_selection | FINDING-V2-POSTWRITE-SELECTION | Independent priority and non-overlap audit | open |",
            "| SA-20260602-V2-SELECTION | fresh-context:jun02-postwrite-v4 | deep_analysis_selection | audit-target:deep_analysis_selection | — | — | passed |",
            "selection audit row",
        ),
        (
            "| SA-20260602-V2-BOOKS | fresh-context:pending-jun02-postwrite | books | audit-target:books | FINDING-V2-POSTWRITE-BOOKS | Root marker audit and serial Books reconciliation, then independent audit | open |",
            "| SA-20260602-V2-BOOKS | fresh-context:jun02-postwrite-v4 | books | audit-target:books | — | 14 条 exact-v1 Review notes 已写入 Ch33/36/42/45/48/56/66/72/84，并由 POST_WRITE_FRESH_AUDIT_V4 targeted recheck 逐条验收 | passed |",
            "books audit row",
        ),
        (
            "22 个实际 Books marker 的 fresh audit 已完成，但写回后的文字尚未经过另一上下文审计；本上下文不自证最终 Gate。",
            "独立 post-write audit 已完成 22/22 marker、5/5 新 integration、28 retained 与 708 closures；唯一 traceability finding 在 14 条 exact-v1 Review notes 补齐并复核后关闭。",
            "semantic audit summary",
        ),
        (
            "当前有 19 项 Source Family 形成 Books Integration proposal；本任务不直接修改 Books。root 应按 22/22 marker audit 的 `KEEP / REVISE / REVERT / RE_EVIDENCE` 结果执行最小串行 reconciliation，再由另一 fresh-context reviewer 做 post-write audit。任何旧 06-02 marker 若来自已降级 family，不得因曾经写入而自动保留。",
            "19 项 Source Family 的 Books Decision 已完成写回：12 项既有 marker 按 exact-v1 evidence 保留，两项机制边界已修正，四项来自降级 family 的专属机制已撤回，四项需重新举证的文字已删除或降级为显式设计合同；五项真正新增的长期结论分别进入 `INFER-KV-CACHE`、`PLATFORM-SECURITY`、`INFER-SCHEDULING`、`AGENT-RAG` 与 `TRAIN-DISTRIBUTED-TRAINING`。具体变更与证据边界记录在 `../_sources/daily-20260602/ROOT_BOOKS_RECONCILIATION_V3.md`；独立验收记录在 `../_sources/daily-20260602/POST_WRITE_FRESH_AUDIT_V4.md`。Books Gate 已在 14 条 retained/revised marker 的 exact-v1 Review notes 补齐并 targeted recheck 后通过。",
            "books decision closure",
        ),
        (
            "- 新增 736-row identity provenance、strict denominator audit、strict screening ledger、owner recovery ledger、Evidence/Books Comparison receipt 与 22-marker fresh audit。\n- 通过官方 exact-v1 PDF 恢复两项先前 blocked family；当前材料 blocker 为 0。\n- 重开本 Daily；此前 `Complete/Passed` 不再有效。\n- 未修改 Books；未执行 stage、commit 或 push。",
            "- 新增 736-row identity provenance、strict denominator audit、strict screening ledger、owner recovery ledger、Evidence/Books Comparison receipt、22-marker fresh audit 与 root Books reconciliation receipt。\n- 通过官方 exact-v1 PDF 恢复两项先前 blocked family；当前材料 blocker 为 0。\n- 已按 marker audit 修正/撤回错误吸收，并把五项新长期结论写入 Ch36、Ch45、Ch56、Ch72 与 Ch76；Ch33、Ch48、Ch49、Ch66 的边界同步收紧，Ch26 的无 owner 机制已移除。\n- 新增独立 post-write audit；22/22 marker、5/5 新 integration、28 retained 与 708 closures 均已验收，14 条 Review-note traceability finding 已修复并复核。\n- 本 Daily 为 `Complete`；Coverage Gate 为 `Closed`，Evidence 与 Books Gate 均为 `Passed`。\n- 未执行 stage、commit 或 push。",
            "repository changes",
        ),
        (
            "1. root marker audit 后，哪些旧 06-02 Books 段落来自已降级 family，需回退或改写为保留 family 的机制证据？\n2. agent task-level SLO 如何与 query TTFT/TPOT、tool latency 和 success probability 建立可分解 budget？\n3. KV precision artifact 的 safety evaluator 应按 model/revision/quantizer 如何版本化，才能避免统一 safe bit-width 假设？",
            "1. agent task-level SLO 如何与 query TTFT/TPOT、tool latency 和 success probability 建立可分解 budget？\n2. KV precision artifact 的 safety evaluator 应按 model/revision/quantizer 如何版本化，才能避免统一 safe bit-width 假设？",
            "open questions",
        ),
        (
            "Daily V2.1 的 denominator、exact-v1 Evidence 与 full-frontier Selection 已重建；Books 与 fresh-context post-write audit 未闭合，Completion 保持 In Progress。",
            "Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。",
            "final status",
        ),
    ]
    for old, new, label in replacements:
        text = replace_once(text, old, new, label)

    for family, proposal in PROMO.items():
        old = (
            f"<!-- books-review:{family}:start -->已核对 owner 与相邻章节；"
            "本项只形成串行 Books proposal，不代表已写回。"
            f"<!-- books-review:{family}:end -->"
        )
        if proposal["books"] == "Integrate":
            state = "Root 已完成最小串行写回；当前 owner 与相邻章节、正文机制及 exact-v1 Review note 已通过 post-write audit。"
        else:
            state = "Fresh current-tree comparison 确认现有 owner 已覆盖该长期命题，无 Books mutation；No Change handoff 已通过 post-write audit。"
        new = f"<!-- books-review:{family}:start -->{state}<!-- books-review:{family}:end -->"
        text = replace_once(text, old, new, f"books review {family}")
    return text


def main() -> None:
    current = DAILY.read_text(encoding="utf-8")
    if not SNAPSHOT.exists():
        SNAPSHOT.write_text(current, encoding="utf-8")
    old = SNAPSHOT.read_text(encoding="utf-8")
    den = json.loads(DENOM.read_text())
    candidates = den["candidates"]
    families = [x["source_family_id"] for x in candidates]
    old_families = [x for x in families if x not in PROMO]

    cand_old = table_map(old, "## Candidate Ledger")
    rp_old = table_map(old, "## Review Completion Receipt")
    bench_old = table_map(old, "## Benchmark Contract")
    books_old = table_map(old, "## Books Comparison")

    evidence = []
    candidate_rows = []
    rp_rows = []
    benchmark_rows = []
    books_rows = []
    books_blocks = []
    reviews = []
    selections = []
    selection_decisions = []
    noneligible_closures = []
    for item in candidates:
        fam = item["source_family_id"]
        ident = item["primary_identifier"]
        if fam in PROMO:
            p = PROMO[fam]
            blocked = p.get("blocked", False)
            dd, sr, du = p["score"]
            total = dd + sr + du
            books_disposition = "Blocked / Unverified" if blocked else p["books"]
            candidate_rows.append([fam, ident, f"paper-v1:{ident.removeprefix('arXiv:').removesuffix('v1')}", "2026-W23", "2026-06-01", "SRC-ARXIV", str(dd), str(sr), str(du), str(total), "retained", "blocked" if blocked else ("deep_complete" if total >= 7 else "standard_complete"), "partial" if blocked else "accessible", "knowledge_gap" if p["books"] == "Integrate" else "none", f"review:{fam}", "self", "—", "new_in_window", p["owner"], books_disposition, f"books-review:{fam}", "yes"])
            if blocked:
                boundary = (
                    "仅核实官方 first-submission identity 与摘要；exact-v1 HTML/PDF 在本次恢复链中仍不可取得，"
                    "因此 Method、Evaluation、limitations 与 artifact locator 尚未独立复核，旧 review 结论不得作为 Books 证据。"
                )
                review_text = f"<!-- review:{fam}:start -->\n### {p['title']}\n\n{boundary} <!-- claim:{fam}:start -->当前只保留候选身份与待验证假设；不得支持 Integrate、No Change 或性能/机制结论。<!-- claim:{fam}:end -->\n<!-- review:{fam}:end -->"
                rp_row = [fam, "PENDING", "deep", ident, f"SRC-ARXIV@{ident} abstract-only", "Pending — exact-v1 full text is unavailable for Method review", "Pending — exact-v1 full text is unavailable for Evaluation review", "Pending — exact-v1 full text is unavailable for limitations review", "Pending — exact-v1 artifact linkage is unavailable", f"claim:{fam}", "blocked"]
            else:
                review_text = f"<!-- review:{fam}:start -->\n### {p['title']}\n\n{p['review']} <!-- claim:{fam}:start -->证据边界绑定 exact-v1 与上述 workload；不得把作者结果外推成跨模型/跨部署普遍结论。<!-- claim:{fam}:end -->\n<!-- review:{fam}:end -->"
                rp_row = [fam, "PENDING", "deep" if total >= 7 else "standard", ident, f"SRC-ARXIV@{ident}", f"{ident} {p['method']}", f"{ident} {p['eval']}", f"{ident} {p['limits']}", f"{ident} {p['artifact']}", f"claim:{fam}", "complete"]
            rp_row[1] = rp_id(candidate_rows[-1], rp_row, review_text)
            rp_rows.append(rp_row)
            benchmark_rows.append([fam, p["workload"], p["model"], p["hardware"], p["precision"], p["length"], "Not Disclosed", p["batch"], p["concurrency"], p["slo"], p["evaluator"]])
            target_map = {
                "INFER-SCHEDULING": ("books/part-05-inference-system/56-inference-scheduling.md#L10", "books/part-05-inference-system/42-what-happens-during-inference.md#L10;books/part-05-inference-system/55-pd-disaggregation.md#L10"),
                "PLATFORM-SECURITY": ("books/part-06-ai-infrastructure/72-security.md#L10", "books/part-06-ai-infrastructure/66-evaluation-system.md#L10;books/part-07-agent/84-agent-platform.md#L10"),
                "TRAIN-DISTRIBUTED-TRAINING": ("books/part-04-training-system/36-distributed-training.md#L10", "books/part-04-training-system/35-checkpoint.md#L10;books/part-04-training-system/37-tensor-parallel.md#L10"),
                "PLATFORM-EVALUATION-SYSTEM": ("books/part-06-ai-infrastructure/66-evaluation-system.md#L10", "books/part-06-ai-infrastructure/65-observability.md#L10;books/part-06-ai-infrastructure/72-security.md#L10"),
                "INFER-KV-CACHE": ("books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L10", "books/part-05-inference-system/44-decode.md#L10;books/part-05-inference-system/49-tensorrt-llm.md#L10"),
                "AGENT-RAG": ("books/part-07-agent/76-rag.md#L10", "books/part-07-agent/75-context.md#L10;books/part-07-agent/77-memory.md#L10"),
            }
            target, adjacent = target_map[p["owner"]]
            relation = "Direct Evolution" if p["books"] == "Integrate" else "Principle Reuse"
            books_rows.append([fam, p["owner"], target, adjacent, f"existing:{fam}", f"delta:{fam}", relation, books_disposition, f"books-review:{fam}"])
            books_blocks.extend([
                f"<!-- existing:{fam}:start -->{p['existing']}<!-- existing:{fam}:end -->",
                f"<!-- delta:{fam}:start -->{p['delta']}<!-- delta:{fam}:end -->",
                f"<!-- books-review:{fam}:start -->{'仅定位 provisional owner；exact-v1 全文受阻，禁止形成 Books proposal。' if blocked else '已核对 owner 与相邻章节；本项只形成串行 Books proposal，不代表已写回。'}<!-- books-review:{fam}:end -->",
            ])
            reviews.append(review_text)
            evidence.append({"family": fam, "primary_identifier": ident, "review": "blocked" if blocked else "complete", "books": books_disposition, "new": True})
        else:
            candidate_rows.append(cand_old[fam])
            rp_rows.append(rp_old[fam])
            benchmark_rows.append(bench_old[fam])
            books_rows.append(books_old[fam])
            reviews.append(review_block(old, fam))
            books_blocks.extend([bounded_block(old, f"existing:{fam}"), bounded_block(old, f"delta:{fam}"), bounded_block(old, f"books-review:{fam}")])
            evidence.append({"family": fam, "primary_identifier": ident, "review": "complete", "books": books_old[fam][-2], "new": False})
        total = int(candidate_rows[-1][9])
        eligibility = ["score_7_9"] if total >= 7 else []
        if candidate_rows[-1][13] not in {"none", "—", ""}: eligibility.append("forced_review")
        if candidate_rows[-1][19] == "Integrate": eligibility.append("potential_books_delta")
        # Deep Analysis Selection only routes pre-Books eligible families. A
        # 5–6 point standard review with no override or Books delta is complete
        # in the Evidence ledger but must not be fabricated into this table.
        if not eligibility:
            assert fam == "SF-SECLAW-SPEC-DRIVEN-SECURITY"
            rationale = (
                "`SF-SECLAW-SPEC-DRIVEN-SECURITY`：Score V2=6/9、Review Override=`none`，"
                "且 pre-Books review 不满足 `score_7_9`、`forced_review`、"
                "`potential_books_delta`、`potential_structural_gap` 或 "
                "`cross_cutting_correction`。因此按 REPORT_CONTRACTS §3.5 保留在主 "
                "Selection eligible pool 之外；其 exact-v1 Standard Review、十字段 Benchmark "
                "Contract 与 No Change Books Comparison 仍然完整，不能把 non-eligible closure "
                "误写成 `not_selected`。"
            )
            noneligible_closures.append(
                f"<!-- analysis-noneligible:{fam}:start -->{rationale}"
                f"<!-- analysis-noneligible:{fam}:end -->"
            )
            continue
        route = ";".join(eligibility)
        decision = "selected" if fam in {"SF-GAIATRACE-VIDUR-AGENT", "SF-ECHELON-AGGREGATE-ONLY-ADAPTATION", "SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY"} else "not_selected"
        unit = "DA-20260602-AGENT-SLO" if fam in {"SF-GAIATRACE-VIDUR-AGENT", "SF-SECLAW-SPEC-DRIVEN-SECURITY", "SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY"} else ("DA-20260602-BOUNDARY-STATE" if fam in {"SF-ECHELON-AGGREGATE-ONLY-ADAPTATION", "SF-OPTCC-ASYMMETRIC-ALLREDUCE", "SF-STRAGGLER-AWARE-RL-GROUP"} else "DA-20260602-RUNTIME-EVIDENCE")
        axis = item["retention_axis"]
        if decision == "selected":
            rationale = f"V2={total}/9；{axis} provides this day's clearest cross-cutting owner/evidence delta; selection does not change review depth."
            selections.append([fam, route, decision, unit, "—", rationale, f"analysis:{unit}"])
        else:
            if candidate_rows[-1][11] == "blocked":
                rationale = f"V2 provisional={total}/9；{item['title']} may establish {axis}, but exact-v1 full text remains blocked; it is ineligible for Deep Analysis selection and Books until the Materials Request is resolved."
            else:
                rationale = f"V2={total}/9；{item['title']} establishes {axis}, but its delta is confined to its canonical owner and is less cross-cutting than the three selected units; its exact-v1 review and Books duty remain complete."
            selections.append([fam, route, decision, "—", "—", rationale, f"analysis-decision:{fam}"])
            selection_decisions.append(
                f"<!-- analysis-decision:{fam}:start -->{rationale}<!-- analysis-decision:{fam}:end -->"
            )

    benchmark_rows = [normalize_benchmark_row(row) for row in benchmark_rows]
    review_complete = sum(x["review"] == "complete" for x in evidence)
    blocked_count = sum(x["review"] == "blocked" for x in evidence)
    OUT_JSON.write_text(json.dumps({"schema_version": "evidence-books-comparison-v3-fresh", "candidate_count": len(evidence), "review_complete": review_complete, "ordinary_pending": 0, "blocked": blocked_count, "integrate_proposals": sum(x["books"] == "Integrate" for x in evidence), "records": evidence}, ensure_ascii=False, indent=2) + "\n")

    cand_header = rows_between(old, "## Candidate Ledger")[0]
    rp_header = rows_between(old, "## Review Completion Receipt")[0]
    bench_header = rows_between(old, "## Benchmark Contract")[0]
    books_header = rows_between(old, "## Books Comparison")[0]
    selection_header = rows_between(old, "## Deep Analysis Selection")[0]

    integration_count = sum(row[-2] == "Integrate" for row in books_rows)
    output = f"""# Daily Research — 2026-06-02

**Research Date:** 2026-06-02

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-01 09:00:00 ～ 2026-06-02 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；19 个注册 category Atom snapshot 负责 identity/date recall，机制与 benchmark claim 只绑定 exact arXiv v1 HTML/PDF

**Status:** In Progress；Coverage、Evidence 与 Books 的独立 post-write Semantic Audit 尚未闭合

## Executive Summary

736 条 raw identity 已按官方 arXiv first-submission metadata 全量复核；identifier 前缀与序号不承担日期语义，736 条均由官方 `published` 时间确认属于本窗口。fresh-context denominator audit 将旧 52 项收紧为 {len(candidates)} 项（{len(candidates)/736*100:.2f}%）：31 个旧候选进入具名 pre-denominator closure，7 个原 closure 在全量 false-negative audit 中恢复。相对 V2 Strict，`AsymCache` 是唯一新增 false negative，0 个既有 retain 被撤销。fresh evidence audit 已完成 {review_complete}/{len(candidates)} 项 exact-v1 Review，普通 pending=0、blocked={blocked_count}；其中 `2606.09864v1` 与 `2606.28343v1` 通过官方 exact-v1 PDF 恢复，不再保留 Materials Request。Books Comparison 有 {integration_count} 项进入串行 proposal；旧 Books marker 已独立审计 22/22（KEEP 12、REVISE 2、REVERT 4、RE_EVIDENCE 4），但串行写回和独立 post-write audit 未结束，不能宣称 Daily Complete。

<!-- audit-target:coverage:start -->
## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-02 |
| Window End | 2026-06-02 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260602-V3-FRESH |
| Denominator Frozen At | 2026-08-28T18:30:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-01T09:00:00+08:00 | 2026-06-02T09:00:00+08:00 | 2026-08-28T18:30:00+08:00 | 19 category Atom snapshots; official published metadata; 736/736 fresh full-population title+abstract reconciliation | checked | 736 | {';'.join(families)} | pages=19; final_cursor=end; unique=736; identity=736; semantic_screen=736; retained={len(candidates)}; closure={736-len(candidates)} | 2026-06-02T00:59:39Z | coverage:SRC-ARXIV:20260602-v3-fresh | — |

<!-- coverage:SRC-ARXIV:20260602-v3-fresh:start -->`identity-provenance-v2-strict.json` 保存 736/736 official submission metadata 与 DOI provenance；`screening-ledger-v3-fresh.tsv` 保存 fresh audit 的每一项 retain 或 family-specific closure，并绑定 hash。高序号、`2607` 或 `2608` identifier 均未被用作日期推断。<!-- coverage:SRC-ARXIV:20260602-v3-fresh:end -->

### Coverage Limitations

官方 Atom `published` 字段证明 first submission time；snapshot 的 observed version 可能晚于 v1，因此只承担 identity/recall，不承担候选机制 claim。28 项 retained claim 均已绑定 exact-v1 HTML/PDF；`2606.09864v1` 当前 metadata 已出现后续版本，因此机制与实验只引用官方 v1 PDF。`2606.28343v1` 也以官方 v1 PDF 复核。arXiv 仍是作者稿，不等于 peer review 或生产复现；未披露的 immutable artifact commit、线上并发与生产 SLO 不由作者 benchmark 反推。Required Daily 其他来源的 Effective Date 晚于本历史窗口，不追溯为到期源。
<!-- audit-target:coverage:end -->

<!-- audit-target:evidence:start -->
## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
{md_table(cand_header, candidate_rows)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
{md_table(rp_header, rp_rows)}

### Source Reviews

{chr(10).join(reviews)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
{md_table(bench_header, benchmark_rows)}

## 5. Deep Analysis Selection

<!-- audit-target:deep_analysis_selection:start -->
<!-- validator:deep-analysis-selection-v1 -->
{md_table(selection_header, selections)}

{chr(10).join(selection_decisions)}

### Full-frontier non-eligible closures

{chr(10).join(noneligible_closures)}

<!-- analysis:DA-20260602-AGENT-SLO:start -->
### Agent workload 把 query SLO 推进为 task/effect evidence

Agent 系统不再能用单次 LLM query 的 TTFT、文本 refusal 或 final answer 代表整体正确性。trace-driven serving 把 task dependency 暴露给 scheduler；security evaluation 则把 tool/runtime/filesystem effect 暴露给 release Gate。共同变化是 evidence owner 从 transcript 移到可重放的 task graph 与 environment state，代价是 trace schema、sandbox fidelity 与 predicate coverage 成为新的 failure mode。
<!-- analysis:DA-20260602-AGENT-SLO:end -->

<!-- analysis:DA-20260602-BOUNDARY-STATE:start -->
### 分布式控制从平均拓扑推进到显式 boundary state

对称 collective、固定 group size 与自由交换 update 在原约束下合理；非对称链路、straggler 与行政隐私边界出现后，control plane 必须消费 bandwidth、participation、staleness 与 allowed-message type。收益是故障/治理条件下仍能推进，代价是动态控制误判、额外 buffer 与审计面；旧同步方案在拓扑稳定、边界一致时仍更简单。
<!-- analysis:DA-20260602-BOUNDARY-STATE:end -->

<!-- audit-target:deep_analysis_selection:end -->

## 6. Books Comparison

<!-- audit-target:books:start -->
<!-- validator:books-comparison-v1 -->
{md_table(books_header, books_rows)}

{chr(10).join(books_blocks)}
<!-- audit-target:books:end -->

<!-- audit-target:evidence:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260602-V3-COVERAGE | fresh-context:pending-jun02-postwrite | coverage | audit-target:coverage | FINDING-V3-POSTWRITE-COVERAGE | Different context must challenge {len(candidates)} retains and {736-len(candidates)} closures after canonical write | open |
| SA-20260602-V2-EVIDENCE | fresh-context:pending-jun02-postwrite | evidence | audit-target:evidence | FINDING-V2-POSTWRITE-EVIDENCE | Independent locator and claim-boundary audit | open |
| SA-20260602-V2-SELECTION | fresh-context:pending-jun02-postwrite | deep_analysis_selection | audit-target:deep_analysis_selection | FINDING-V2-POSTWRITE-SELECTION | Independent priority and non-overlap audit | open |
| SA-20260602-V2-BOOKS | fresh-context:pending-jun02-postwrite | books | audit-target:books | FINDING-V2-POSTWRITE-BOOKS | Root marker audit and serial Books reconciliation, then independent audit | open |

Identity/date 736/736、title+abstract denominator FP/FN 736/736、Evidence {review_complete}/{len(candidates)} complete；ordinary pending=0、blocked={blocked_count}。Score V2、RP、Benchmark Contract、Selection 与 Books Comparison 均仅对最终 denominator 重建。22 个实际 Books marker 的 fresh audit 已完成，但写回后的文字尚未经过另一上下文审计；本上下文不自证最终 Gate。

## 8. Ignored Noise

{736-len(candidates)} 项不是静默删除：其 official identity、摘要 digest、closure class 与 family-specific semantic challenge 均保存在 `../_sources/daily-20260602/screening-ledger-v3-fresh.tsv`。ROADMAP 可映射、AI 相关、局部方法改进或单领域 benchmark 本身不足以进入 denominator。

## 9. Recommended Action

当前有 {integration_count} 项 Source Family 形成 Books Integration proposal；本任务不直接修改 Books。root 应按 22/22 marker audit 的 `KEEP / REVISE / REVERT / RE_EVIDENCE` 结果执行最小串行 reconciliation，再由另一 fresh-context reviewer 做 post-write audit。任何旧 06-02 marker 若来自已降级 family，不得因曾经写入而自动保留。

## 10. Repository Changes

- 新增 736-row identity provenance、strict denominator audit、strict screening ledger、owner recovery ledger、Evidence/Books Comparison receipt 与 22-marker fresh audit。
- 通过官方 exact-v1 PDF 恢复两项先前 blocked family；当前材料 blocker 为 0。
- 重开本 Daily；此前 `Complete/Passed` 不再有效。
- 未修改 Books；未执行 stage、commit 或 push。

## 11. Open Questions

1. root marker audit 后，哪些旧 06-02 Books 段落来自已降级 family，需回退或改写为保留 family 的机制证据？
2. agent task-level SLO 如何与 query TTFT/TPOT、tool latency 和 success probability 建立可分解 budget？
3. KV precision artifact 的 safety evaluator 应按 model/revision/quantizer 如何版本化，才能避免统一 safe bit-width 假设？

## 12. Sources

- Strict identity/denominator packet: `../_sources/daily-20260602/`
"""
    pdf_only = {"arXiv:2606.09864v1", "arXiv:2606.28343v1"}
    for item in candidates:
        ident = item['primary_identifier'].removeprefix('arXiv:')
        route = "pdf" if item['primary_identifier'] in pdf_only else "html"
        output += f"- {item['title']}: https://arxiv.org/{route}/{ident}\n"
    output += "\n## 13. Final Status\n\nDaily V2.1 的 denominator、exact-v1 Evidence 与 full-frontier Selection 已重建；Books 与 fresh-context post-write audit 未闭合，Completion 保持 In Progress。\n"
    if POST_AUDIT.exists():
        output = apply_postwrite_closure(output)
    DAILY.write_text(output, encoding="utf-8")
    print(json.dumps({"candidates": len(candidates), "reviews": len(evidence), "integrate_proposals": integration_count}, ensure_ascii=False))


if __name__ == "__main__":
    main()
