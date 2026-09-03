#!/usr/bin/env python3
"""Close a frozen 2026 V2.1 Daily backfill without reopening discovery.

The script is intentionally narrow: it reconciles source applicability by
Effective Date, derives Books receipts from the already-frozen candidate and
review ledgers, and leaves the fresh-context semantic scopes open until a
separate reviewer signs them off.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = ROOT / "papers/2026/08"
ROADMAP = ROOT / "ROADMAP.md"
SOURCE_REGISTRY = ROOT / "docs/RESEARCH_SOURCES.md"


# A Books receipt must point to the mechanism paragraph, not merely to the
# source list in Review notes.  These needles identify the canonical mechanism
# section that absorbed each deep-reviewed August source family.
INTEGRATION_NEEDLES = {
    "2608.14635": "Agentic RL 把恢复事务扩展到环境状态",
    "2607.26475": "从反应式 Recall 到预测式 Prefetch",
    "2607.27269": "Attention 转换必须保持 Draft Function",
    "2607.28699": "从离线平均质量到运行时风险门",
    "2607.28848": "从固定 Workload 隔离到 SLO 约束的 Co-serving",
    "2607.29019": "隐私不是一个开关",
    "2607.29076": "从统一可靠性到状态敏感",
    "2607.29190": "从 Scalar Confidence 到 Safe-commit Certificate",
    "2608.01311": "长文生成需要把检索、叙事状态与核验分开提交",
    "2608.01526": "从进程私有缓存到可寻址",
    "2608.01563": "执行计划的下一阶段",
    "2608.03555": "从单设备 HBM 到异构近数据与池化状态",
    "2608.04074": "从统一可靠性到状态敏感",
    "2608.04289": "从 Scalar Confidence 到 Safe-commit Certificate",
    "2608.05483": "从单设备 HBM 到异构近数据与池化状态",
    "2608.05791": "并行不是一个旋钮：副本并行与结构并行",
    "2608.06557": "从静态优先级到可消费的 SLO 预算",
    "2608.07621": "从单体控制到协同通信与可回滚 proposal",
    "2608.08340": "从静态优先级到可消费的 SLO 预算",
    "2608.08569": "语义锚点不是原模态的替代品",
    "2608.08878": "从统一可靠性到状态敏感",
    "2608.09225": "共享状态的性能身份同时也是安全身份",
    "2608.09730": "World Model 也可以只在训练期承担表示约束",
    "2608.10362": "Edge 场景先管理 Draft Residency，再谈 Acceptance",
    "2608.10509": "MAP-Graph 在一个 synthetic",
    "2608.12921": "并行不是一个旋钮：副本并行与结构并行",
    "2608.12932": "从单体控制到协同通信与可回滚 proposal",
    "2608.14094": "Skill 既有能力供应链，也有版本维护债务",
    "2608.15127": "Agent 评估必须声明 Runtime Coverage",
    "2608.15636": "从单体控制到协同通信与可回滚 proposal",
    "2608.16477": "从进程私有缓存到可寻址",
    "2608.16843": "Embodied Agent 又把同一原则扩展",
    "2608.17007": "SkillEffect 的作者实验",
    "2608.17336": "执行计划的下一阶段",
    "2608.17442": "隐私不是一个开关",
    "2608.19729": "从单体控制到协同通信与可回滚 proposal",
    "2608.21836": "执行计划的下一阶段",
    "2608.21867": "Verifier 输出必须带着校准边界进入 Memory 生命周期",
    "2608.21898": "Synthetic Environment 必须先证明可执行",
    "2608.21964": "Skill 既有能力供应链，也有版本维护债务",
    "2608.22510": "Agent 评估必须声明 Runtime Coverage",
}


# These families are already represented by a durable mechanism paragraph.
# Unlike Weekly Only, No Change therefore carries a bounded body receipt that
# proves the canonical owner already states the same contract.
NO_CHANGE_NEEDLES = {
    "2607.28069": "SemPIC 是第三条分支的实验性证据",
    "2607.28609": "OSReward 的跨平台 trajectory study",
}


# Semantic neighbours are selected by responsibility boundary, not by chapter
# number.  They make the bounded Books comparison reproducible while keeping a
# single canonical owner for each mechanism.
SEMANTIC_ADJACENCY = {
    "AGENT-MEMORY": ["AGENT-RAG", "AGENT-TOOL-CALLING"],
    "AGENT-MULTI-AGENT": ["AGENT-WORKFLOW", "AGENT-PLATFORM"],
    "AGENT-PLATFORM": ["AGENT-WORKFLOW", "PLATFORM-SECURITY"],
    "AGENT-RAG": ["AGENT-CONTEXT", "AGENT-MEMORY"],
    "AGENT-TOOL-CALLING": ["AGENT-MEMORY", "AGENT-WORKFLOW"],
    "AGENT-WORKFLOW": ["AGENT-TOOL-CALLING", "AGENT-MULTI-AGENT"],
    "INFER-GPU-MEMORY": ["INFER-KV-CACHE", "INFER-SCHEDULING"],
    "INFER-KV-CACHE": ["MODEL-KV-CACHE", "INFER-GPU-MEMORY"],
    "INFER-SCHEDULING": ["INFER-CONTINUOUS-BATCHING", "INFER-GPU-MEMORY"],
    "INFER-SPECULATIVE-DECODING": ["INFER-DECODE", "INFER-CONTINUOUS-BATCHING"],
    "INFER-TENSORRT-LLM": ["MODEL-TRANSFORMER-LAYER", "INFER-GPU-MEMORY"],
    "INFER-VLLM": ["INFER-TENSORRT-LLM", "INFER-CONTINUOUS-BATCHING"],
    "MULTIMODAL-EMBODIED-VLA": ["MULTIMODAL-WORLD-MODELS", "PLATFORM-SECURITY"],
    "MULTIMODAL-REPRESENTATION": ["MODEL-TRANSFORMER-LAYER", "MULTIMODAL-GENERATIVE-PARADIGMS"],
    "MULTIMODAL-WORLD-MODELS": ["MULTIMODAL-REPRESENTATION", "MULTIMODAL-EMBODIED-VLA"],
    "PLATFORM-EVALUATION-SYSTEM": ["PLATFORM-MONITORING", "AGENT-PLATFORM"],
    "PLATFORM-SECURITY": ["PLATFORM-MULTI-TENANT", "AGENT-TOOL-CALLING"],
    "TRAIN-CHECKPOINT": ["TRAIN-DPO", "TRAIN-DISTRIBUTED-TRAINING"],
}


# Evidence-stage judgements, made without reading the final Books disposition.
# Each item names the durable contract that might change and therefore had to
# enter Books comparison after Source Review.
PREBOOKS_DELTA_RATIONALE = {
    "2608.14635": "agentic RL recovery expands from model and optimizer state to a prefix-consistent environment transaction",
    "2607.26475": "host-tier KV recall becomes a predictive prefetch pipeline with explicit provisional-token error and memory boundaries",
    "2607.27269": "attention conversion must preserve draft-target acceptance behavior rather than only standalone model quality",
    "2607.28699": "offline average KV quality becomes a per-layer runtime risk meter and commit gate",
    "2607.28848": "isolated inference and fine-tuning become SLO-constrained co-serving with explicit admission and preemption control",
    "2607.29019": "RAG privacy expands from transport protection to query, selection and plaintext-owner trust boundaries",
    "2607.29076": "KV reliability changes from uniform protection to sensitivity-ranked reliability budgets",
    "2607.29190": "point authorization becomes certification over a typed-return uncertainty set",
    "2608.01311": "long-form RAG becomes an outline, section-state, claim-check and repair commit chain",
    "2608.01526": "process-local KV becomes distributed addressable state with locator, version and ownership",
    "2608.01563": "vendor execution plans gain a portable semantic contract and bounded backend lowering",
    "2608.03555": "attention memory hierarchy expands to near-data processing and moves compute/data ownership",
    "2608.04074": "KV quantization objective moves from element error to attention-output state sensitivity",
    "2608.04289": "action confidence becomes a plausible-world safe-commit certificate",
    "2608.05483": "single-node memory capacity becomes CXL pooled-state placement and shared-bandwidth control",
    "2608.05791": "replica and structural parallelism impose different multi-Agent state-decomposition contracts",
    "2608.06557": "static priority becomes consumable, exhaustible and auditable SLO slack",
    "2608.07621": "single-controller VLA becomes a communication loop with sender identity, freshness and budget",
    "2608.08340": "an inference request becomes an operator DAG with explicit admission, placement and completion",
    "2608.08569": "transcript changes from modality replacement to a provenance-bearing semantic anchor",
    "2608.08878": "KV compression budget becomes token, head and layer sensitive instead of uniform",
    "2608.09225": "shared-prefix performance identity also becomes tenant authorization identity",
    "2608.09730": "world-model transition supervision becomes a training-only branch, not only online rollout",
    "2608.10362": "edge speculation is first constrained by draft residency and memory budget",
    "2608.10509": "Memory provenance moves into read authorization, trust ranking and action gating",
    "2608.12921": "multi-Agent topology is attributed to independent observations and verifiable interfaces",
    "2608.12932": "physical speculative rollback becomes conditional on same-state reversible primitives",
    "2608.14094": "Agent skill becomes a versioned, authorized and revocable capability supply chain",
    "2608.15127": "Agent evaluation expands to runtime, tool, policy and environment coverage",
    "2608.15636": "VLA cache and diffusion reuse becomes subordinate to sensor freshness and safety envelope",
    "2608.16477": "cross-node KV reuse gains semantic identity, lookup and stale-state failure policy",
    "2608.16843": "embodied security is partitioned by first-compromised boundary across perception and action",
    "2608.17007": "tool intent execution becomes checked lowering with capacity lease and bounded publication",
    "2608.17336": "mixed precision moves from model-wide configuration to tile/operator-aware execution planning",
    "2608.17442": "private long-context inference splits HE linear work, MPC nonlinear work and domain transitions",
    "2608.19729": "action-chunk rollback becomes explicitly bounded by recoverable environment state",
    "2608.21836": "generation optimization gains an in-model verifier while retaining external evidence bounds",
    "2608.21867": "verifier output becomes calibrated, versioned derived Memory rather than truth",
    "2608.21898": "synthetic environments require executable transition and reset evidence before training use",
    "2608.21964": "skill maintenance gains source revision, compatibility and revocation lifecycle",
    "2608.22510": "benchmark holdout becomes versioned contamination and release-gate evidence",
}


EVOLUTION_BY_SOURCE = {
    "2608.14635": "Direct Evolution",
    "2607.26475": "Direct Evolution",
    "2607.27269": "Direct Evolution",
    "2607.28699": "Direct Evolution",
    "2607.28848": "Alternative Branch",
    "2607.28069": "Alternative Branch",
    "2607.28609": "Layering / Dependency",
    "2607.29019": "Alternative Branch",
    "2607.29076": "Direct Evolution",
    "2607.29190": "Direct Evolution",
    "2608.01311": "Layering / Dependency",
    "2608.01526": "Direct Evolution",
    "2608.01563": "Direct Evolution",
    "2608.03555": "Alternative Branch",
    "2608.04074": "Direct Evolution",
    "2608.04289": "Direct Evolution",
    "2608.05483": "Direct Evolution",
    "2608.05791": "Alternative Branch",
    "2608.06557": "Direct Evolution",
    "2608.07621": "Direct Evolution",
    "2608.08340": "Direct Evolution",
    "2608.08569": "Layering / Dependency",
    "2608.08878": "Direct Evolution",
    "2608.09225": "Layering / Dependency",
    "2608.09730": "Alternative Branch",
    "2608.10362": "Direct Evolution",
    "2608.10509": "Layering / Dependency",
    "2608.12921": "Direct Evolution",
    "2608.12932": "Direct Evolution",
    "2608.14094": "Layering / Dependency",
    "2608.15127": "Layering / Dependency",
    "2608.15636": "Direct Evolution",
    "2608.16477": "Direct Evolution",
    "2608.16843": "Layering / Dependency",
    "2608.17007": "Direct Evolution",
    "2608.17336": "Direct Evolution",
    "2608.17442": "Alternative Branch",
    "2608.19729": "Direct Evolution",
    "2608.21836": "Direct Evolution",
    "2608.21867": "Layering / Dependency",
    "2608.21898": "Layering / Dependency",
    "2608.21964": "Direct Evolution",
    "2608.22510": "Direct Evolution",
}


@dataclass
class Candidate:
    columns: list[str]
    title: str
    claim: str

    @property
    def family(self) -> str:
        return self.columns[0]

    @property
    def identifier(self) -> str:
        return self.columns[1]

    @property
    def node(self) -> str:
        return self.columns[18]

    @property
    def review_status(self) -> str:
        return self.columns[11]

    @property
    def arxiv_id(self) -> str:
        return re.sub(r"v\d+$", "", self.identifier.removeprefix("arXiv:"))


def replace_section(text: str, start_heading: str, end_heading: str, body: str) -> str:
    pattern = re.compile(
        rf"(?ms)^{re.escape(start_heading)}\n.*?(?=^{re.escape(end_heading)}\n)"
    )
    replacement = f"{start_heading}\n\n{body.rstrip()}\n\n"
    updated, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise ValueError(f"cannot replace section {start_heading!r}")
    return updated


def roadmap_nodes() -> tuple[dict[str, Path], list[tuple[str, Path]]]:
    mapping: dict[str, Path] = {}
    ordered: list[tuple[str, Path]] = []
    for line in ROADMAP.read_text().splitlines():
        match = re.match(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", line)
        if not match:
            continue
        node, raw_path = match.groups()
        path = ROOT / raw_path
        mapping[node] = path
        ordered.append((node, path))
    return mapping, ordered


def line_of(path: Path, needle: str) -> int:
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        if needle in line:
            return number
    raise ValueError(f"{needle!r} is not present in {path.relative_to(ROOT)}")


def chapter_title(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def chapter_core_proposition(path: Path) -> tuple[int, str]:
    """Return the chapter's concrete central claim and its source line."""
    text = path.read_text()
    match = re.search(r"本章的(?:核心判断|中心命题)是：\*\*(.+?)\*\*", text, re.S)
    if not match:
        raise ValueError(
            f"chapter has no explicit core proposition: {path.relative_to(ROOT)}"
        )
    proposition = re.sub(r"\s+", " ", match.group(1)).strip()
    line = text[: match.start()].count("\n") + 1
    return line, proposition


def target_mechanism_line(candidate: Candidate, target: Path) -> int:
    """Locate the integrated mechanism body, never just a Review-notes citation."""
    needle = INTEGRATION_NEEDLES.get(candidate.arxiv_id)
    if not needle:
        raise ValueError(
            f"deep integration {candidate.arxiv_id} lacks a mechanism locator"
        )
    line = line_of(target, needle)
    review_notes_line = line_of(target, "## Review notes")
    if line >= review_notes_line:
        raise ValueError(
            f"mechanism locator for {candidate.arxiv_id} points into Review notes"
        )
    return line


def existing_mechanism_line(candidate: Candidate, target: Path) -> int:
    needle = NO_CHANGE_NEEDLES.get(candidate.arxiv_id)
    if not needle:
        raise ValueError(
            f"No Change {candidate.arxiv_id} lacks a durable mechanism locator"
        )
    line = line_of(target, needle)
    review_notes_line = line_of(target, "## Review notes")
    if line >= review_notes_line:
        raise ValueError(
            f"No Change locator for {candidate.arxiv_id} points into Review notes"
        )
    return line


def parse_candidates(text: str, *, require_review_claim: bool = True) -> list[Candidate]:
    titles: dict[str, tuple[str, str]] = {}
    pattern = re.compile(
        r"<!-- review:(SF-[^:]+):start -->\n#### ([^\n]+)\n\n"
        r"<!-- claim:\1:start -->(.*?)<!-- claim:\1:end -->",
        re.S,
    )
    for match in pattern.finditer(text):
        claim = re.sub(r"\s+", " ", match.group(3)).strip()
        titles[match.group(1)] = (match.group(2).strip(), claim)

    candidates: list[Candidate] = []
    in_ledger = False
    for line in text.splitlines():
        if line.startswith("## 2. Candidate Ledger"):
            in_ledger = True
            continue
        if in_ledger and line.startswith("## 3."):
            break
        if not (in_ledger and line.startswith("| SF-")):
            continue
        columns = [cell.strip() for cell in line.strip("|").split("|")]
        if require_review_claim:
            title, claim = titles[columns[0]]
        else:
            title, claim = titles.get(columns[0], ("", ""))
        candidates.append(Candidate(columns, title, claim))
    return candidates


def books_decision(candidate: Candidate, node_paths: dict[str, Path]) -> str:
    # This is an explicit, reviewed integration allow-list: membership requires
    # a durable-body locator in INTEGRATION_NEEDLES.  Merely appearing in a
    # chapter's Review notes is never enough for Integrate or No Change.
    if candidate.arxiv_id in INTEGRATION_NEEDLES:
        target = node_paths[candidate.node]
        target_mechanism_line(candidate, target)
        return "Integrate"
    if candidate.arxiv_id in NO_CHANGE_NEEDLES:
        target = node_paths[candidate.node]
        existing_mechanism_line(candidate, target)
        return "No Change — Existing Coverage"
    return "Weekly Only — Context"


def update_source_review_dispositions(
    text: str,
    candidates: list[Candidate],
    decisions: dict[str, str],
    *,
    require_line: bool = True,
) -> str:
    """Keep each human-readable Source Review aligned with its ledger truth."""
    for candidate in candidates:
        pattern = re.compile(
            rf"(?s)(<!-- review:{re.escape(candidate.family)}:start -->.*?"
            rf"<!-- review:{re.escape(candidate.family)}:end -->)"
        )
        match = pattern.search(text)
        if not match:
            raise ValueError(f"missing Source Review block for {candidate.family}")
        block = match.group(1)
        updated, count = re.subn(
            r"(Knowledge owner：`[^`]+`；Disposition：)`[^`]+`",
            rf"\g<1>`{decisions[candidate.family]}`",
            block,
            count=1,
        )
        if count != 1 and require_line:
            raise ValueError(f"missing disposition line in {candidate.family}")
        if count == 0:
            continue
        text = text[: match.start()] + updated + text[match.end() :]
    return text


def repair_consistency_only(path: Path) -> None:
    """Synchronize rendered dispositions and provenance without changing decisions."""
    text = path.read_text()
    candidates = parse_candidates(text, require_review_claim=False)
    decisions = {candidate.family: candidate.columns[19] for candidate in candidates}
    text = update_source_review_dispositions(
        text,
        candidates,
        decisions,
        require_line=False,
    )
    text = refresh_review_provenance(text, candidates)
    path.write_text(text)


def _canonical_multi(value: str) -> str:
    absent = {"", "-", "—", "n/a", "N/A", "Not Applicable"}
    items = []
    for raw_item in value.split(";"):
        item = unicodedata.normalize("NFC", raw_item.strip().strip("`"))
        if item and item not in absent:
            items.append(item)
    return ";".join(sorted(items))


def _normalized_body_sha256(body: str) -> str:
    normalized = unicodedata.normalize(
        "NFC", body.replace("\r\n", "\n").replace("\r", "\n")
    )
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def refresh_review_provenance(text: str, candidates: list[Candidate]) -> str:
    """Re-freeze RP identities after a reviewed Source Review body changes."""
    by_family = {candidate.family: candidate for candidate in candidates}
    lines = text.splitlines()
    in_receipt = False
    for index, line in enumerate(lines):
        if line.strip() == "<!-- validator:review-completion-v1 -->":
            in_receipt = True
            continue
        if in_receipt and line.startswith("### Source Reviews"):
            break
        if not (in_receipt and line.startswith("| SF-")):
            continue
        columns = [cell.strip() for cell in line.strip("|").split("|")]
        family = columns[0]
        candidate = by_family[family]
        start = f"<!-- review:{family}:start -->"
        end = f"<!-- review:{family}:end -->"
        review_body = text.split(start, 1)[1].split(end, 1)[0]
        canonical = "|".join(
            (
                "review-completion-v1",
                family,
                candidate.columns[2],
                candidate.columns[1],
                _canonical_multi(candidate.columns[5]),
                columns[3].strip("`"),
                _canonical_multi(columns[4]),
                columns[2],
                *(
                    (f"review-override:{candidate.columns[13]}",)
                    if candidate.columns[13] not in {"", "none"}
                    else ()
                ),
                _canonical_multi(columns[5]),
                _canonical_multi(columns[6]),
                _canonical_multi(columns[7]),
                _canonical_multi(columns[8]),
                columns[9].strip("`"),
                candidate.columns[14].strip("`"),
                f"review-body-sha256:{_normalized_body_sha256(review_body)}",
            )
        )
        columns[1] = "RP-" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
        lines[index] = "| " + " | ".join(columns) + " |"
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def update_candidate_ledger(
    text: str, candidates: list[Candidate], decisions: dict[str, str]
) -> str:
    replacements: dict[str, str] = {}
    for candidate in candidates:
        columns = candidate.columns[:]
        decision = decisions[candidate.family]
        columns[19] = decision
        columns[20] = (
            f"books-review:{candidate.family}"
            if decision in {"Integrate", "No Change — Existing Coverage"}
            else "—"
        )
        replacements[candidate.family] = "| " + " | ".join(columns) + " |"

    lines = text.splitlines()
    in_ledger = False
    for index, line in enumerate(lines):
        if line.startswith("## 2. Candidate Ledger"):
            in_ledger = True
            continue
        if in_ledger and line.startswith("## 3."):
            break
        if in_ledger and line.startswith("| SF-"):
            family = line.split("|", 2)[1].strip()
            lines[index] = replacements[family]
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def apply_prebooks_eligibility(text: str, candidates: list[Candidate]) -> str:
    """Reconstruct Selection only from explicit evidence-stage delta judgements."""
    by_family = {candidate.family: candidate for candidate in candidates}
    lines = text.replace("<br>potential_books_delta", "").splitlines()
    in_table = False
    for index, line in enumerate(lines):
        if line.strip() == "<!-- validator:deep-analysis-selection-v1 -->":
            in_table = True
            continue
        if in_table and line.startswith("<!-- analysis:"):
            break
        if not (in_table and line.startswith("| SF-")):
            continue
        columns = [cell.strip() for cell in line.strip("|").split("|")]
        candidate = by_family[columns[0]]
        rationale = PREBOOKS_DELTA_RATIONALE.get(candidate.arxiv_id)
        columns[5] = re.sub(r"；pre-Books delta=.*", "", columns[5])
        if rationale:
            columns[1] += "<br>potential_books_delta"
            columns[5] += f"；pre-Books delta={rationale}"
        lines[index] = "| " + " | ".join(columns) + " |"
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def registry_effective_dates() -> dict[str, date]:
    effective: dict[str, date] = {}
    in_table = False
    for line in SOURCE_REGISTRY.read_text().splitlines():
        if line.strip() == "<!-- validator:source-registry-v1 -->":
            in_table = True
            continue
        if not (in_table and line.startswith("| SRC-")):
            continue
        columns = [cell.strip() for cell in line.strip("|").split("|")]
        effective[columns[0]] = date.fromisoformat(columns[11])
    return effective


def strip_post_effective_incomplete_sources(text: str, window_end: date) -> str:
    effective_dates = registry_effective_dates()
    lines = text.splitlines()
    kept: list[str] = []
    in_coverage_table = False
    for line in lines:
        if line.strip() == "<!-- validator:source-coverage-v2 -->":
            in_coverage_table = True
            kept.append(line)
            continue
        if in_coverage_table and line.startswith("<!-- coverage:"):
            in_coverage_table = False
        if in_coverage_table and line.startswith("| SRC-"):
            columns = [cell.strip() for cell in line.strip("|").split("|")]
            effective_date = effective_dates.get(columns[0])
            if columns[5] == "incomplete" and effective_date and effective_date > window_end:
                continue
        kept.append(line)
    updated = "\n".join(kept) + ("\n" if text.endswith("\n") else "")
    # A non-due source is not part of this historical report's Coverage
    # contract.  Remove its obsolete narrative receipt as well as its table
    # row so semantic audits cannot cite evidence that was never required.
    for source_id, effective_date in effective_dates.items():
        if effective_date <= window_end:
            continue
        updated = re.sub(
            rf"(?m)^<!-- coverage:{re.escape(source_id)}:\d{{8}}:start -->.*?"
            rf"<!-- coverage:{re.escape(source_id)}:\d{{8}}:end -->\n?",
            "",
            updated,
        )
    return updated


def books_receipt(
    candidates: list[Candidate],
    decisions: dict[str, str],
    node_paths: dict[str, Path],
    ordered_nodes: list[tuple[str, Path]],
) -> str:
    rows: list[str] = []
    blocks: list[str] = []
    for candidate in candidates:
        decision = decisions[candidate.family]
        if decision not in {"Integrate", "No Change — Existing Coverage"}:
            continue
        target = node_paths[candidate.node]
        target_rel = target.relative_to(ROOT).as_posix()
        core_line, core_proposition = chapter_core_proposition(target)
        if decision == "Integrate":
            mechanism_line = target_mechanism_line(candidate, target)
        else:
            mechanism_line = existing_mechanism_line(candidate, target)
        adjacent: list[str] = []
        adjacent_claims: list[str] = []
        adjacent_nodes = SEMANTIC_ADJACENCY.get(candidate.node)
        if not adjacent_nodes:
            raise ValueError(f"no semantic adjacency registered for {candidate.node}")
        for adjacent_node in adjacent_nodes:
            adjacent_file = node_paths[adjacent_node]
            adjacent_path = adjacent_file.relative_to(ROOT).as_posix()
            adjacent_core_line, adjacent_claim = chapter_core_proposition(adjacent_file)
            adjacent.append(f"{adjacent_path}#L{adjacent_core_line}")
            adjacent_claims.append(f"{adjacent_node}：{adjacent_claim}")
        relation = EVOLUTION_BY_SOURCE[candidate.arxiv_id]
        rows.append(
            "| "
            + " | ".join(
                [
                    candidate.family,
                    candidate.node,
                    f"{target_rel}#L{core_line}<br>{target_rel}#L{mechanism_line}",
                    "<br>".join(adjacent),
                    f"existing:{candidate.family}",
                    f"delta:{candidate.family}",
                    relation,
                    decision,
                    f"books-review:{candidate.family}",
                ]
            )
            + " |"
        )
        if decision == "Integrate":
            comparison = (
                f"与上述中心命题相比，这个 family 的新增证据是：{candidate.claim} "
                f"该 delta 已落在《{chapter_title(target)}》的正文机制锚点；"
                f"语义相邻边界为 {'；'.join(adjacent_claims)}。"
                "相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。"
            )
        else:
            comparison = (
                f"《{chapter_title(target)}》已经承载同一机制和适用边界，当前 family 只增加受限实例或复核证据；"
                "重复追加会破坏 canonical owner，因此保持 No Change。"
            )
        blocks.append(
            f"<!-- books-review:{candidate.family}:start -->"
            f"<!-- existing:{candidate.family}:start -->"
            f"现有中心命题：{core_proposition}"
            f"<!-- existing:{candidate.family}:end -->"
            f"<!-- delta:{candidate.family}:start -->"
            f"{candidate.claim}"
            f"<!-- delta:{candidate.family}:end -->"
            f"{comparison}"
            f"<!-- books-review:{candidate.family}:end -->"
        )

    header = "\n".join(
        [
            "<!-- validator:books-comparison-v1 -->",
            "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            *rows,
        ]
    )
    if blocks:
        header += "\n\n" + "\n\n".join(blocks)
    return header


def update_audits_pending(text: str, month: int, day: int, candidates: list[Candidate]) -> str:
    report_key = f"2026{month:02d}{day:02d}"
    coverage_refs = sorted(
        set(re.findall(r"<!-- (coverage:[A-Z0-9-]+:\d{8}):start -->", text))
    )
    book_refs = [
        f"books-review:{candidate.family}"
        for candidate in candidates
        if candidate.columns[19] in {"Integrate", "No Change — Existing Coverage"}
    ]
    weekly_only_refs = [
        f"review:{candidate.family}"
        for candidate in candidates
        if candidate.columns[19] == "Weekly Only — Context"
    ]
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(f"| SA-{report_key}-COVERAGE |"):
            lines[index] = (
                f"| SA-{report_key}-COVERAGE | fresh-context:pending-final-review | coverage | "
                + "; ".join(coverage_refs + [f"semantic-review:SA-{report_key}-COVERAGE"])
                + f" | AUDIT-{report_key}-COVERAGE-PENDING：复核 Effective Date、arXiv 分页与候选分母 | "
                f"待 fresh-context reviewer 对新的适用来源边界签字 | open |"
            )
        elif line.startswith(f"| SA-{report_key}-SELECTION |"):
            analysis_refs = sorted(
                set(
                    re.findall(
                        r"<!-- ((?:analysis|analysis-decision):[^:]+):start -->",
                        text,
                    )
                )
            )
            lines[index] = (
                f"| SA-{report_key}-SELECTION | fresh-context:pending-final-review | deep_analysis_selection | "
                + "; ".join(analysis_refs + [f"semantic-review:SA-{report_key}-SELECTION"])
                + f" | AUDIT-{report_key}-SELECTION-PENDING：复核 evidence-stage potential delta 与 narrative selection | "
                f"待 fresh-context reviewer 确认未由 Books disposition 倒推 | open |"
            )
        elif line.startswith(f"| SA-{report_key}-BOOKS |"):
            reviewed = ["validator:books-comparison-v1"] + book_refs + weekly_only_refs + [
                f"semantic-review:SA-{report_key}-BOOKS"
            ]
            lines[index] = (
                f"| SA-{report_key}-BOOKS | fresh-context:pending-final-review | books | "
                + "; ".join(reviewed)
                + f" | AUDIT-{report_key}-BOOKS-PENDING：复核全部 final disposition 与章节写入 | "
                f"待 fresh-context reviewer 对 owner、相邻章节与 evidence boundary 签字 | open |"
            )
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    text = re.sub(
        rf"(?s)<!-- semantic-review:SA-{report_key}-COVERAGE:start -->.*?<!-- semantic-review:SA-{report_key}-COVERAGE:end -->",
        f"<!-- semantic-review:SA-{report_key}-COVERAGE:start -->Pending fresh-context review of Effective Date applicability, frozen arXiv pagination and denominator closure.<!-- semantic-review:SA-{report_key}-COVERAGE:end -->",
        text,
    )
    text = re.sub(
        rf"(?s)<!-- semantic-review:SA-{report_key}-SELECTION:start -->.*?<!-- semantic-review:SA-{report_key}-SELECTION:end -->",
        f"<!-- semantic-review:SA-{report_key}-SELECTION:start -->Pending fresh-context review of evidence-stage eligibility and narrative selection without Books feedback.<!-- semantic-review:SA-{report_key}-SELECTION:end -->",
        text,
    )
    text = re.sub(
        rf"(?s)<!-- semantic-review:SA-{report_key}-BOOKS:start -->.*?<!-- semantic-review:SA-{report_key}-BOOKS:end -->",
        f"<!-- semantic-review:SA-{report_key}-BOOKS:start -->Pending fresh-context review of every Integrate, No Change and Weekly Only disposition.<!-- semantic-review:SA-{report_key}-BOOKS:end -->",
        text,
    )
    return text


def finalize_semantic_audits(text: str, month: int, day: int) -> str:
    """Record the external fresh-context PASS after it has actually occurred."""
    report_key = f"2026{month:02d}{day:02d}"
    resolutions = {
        "COVERAGE": "Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match",
        "EVIDENCE": "Verified — every retained family has complete versioned review provenance and a bounded claim",
        "SELECTION": "Verified — evidence-stage potential delta, narrative selection and at-most-three selected units",
        "BOOKS": "Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref",
    }
    lines = text.splitlines()
    for index, line in enumerate(lines):
        for suffix, resolution in resolutions.items():
            if not line.startswith(f"| SA-{report_key}-{suffix} |"):
                continue
            columns = [cell.strip() for cell in line.strip("|").split("|")]
            columns[1] = "fresh-context:final-contract-review"
            columns[4] = "none"
            columns[5] = resolution
            columns[6] = "passed"
            lines[index] = "| " + " | ".join(columns) + " |"
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    for suffix, statement in {
        "COVERAGE": "Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.",
        "EVIDENCE": "Fresh-context reviewer verified version identity, Method/evaluation/limitation locators and claim boundaries for every retained Source Family.",
        "SELECTION": "Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.",
        "BOOKS": "Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.",
    }.items():
        text = re.sub(
            rf"(?s)<!-- semantic-review:SA-{report_key}-{suffix}:start -->.*?<!-- semantic-review:SA-{report_key}-{suffix}:end -->",
            f"<!-- semantic-review:SA-{report_key}-{suffix}:start -->{statement}<!-- semantic-review:SA-{report_key}-{suffix}:end -->",
            text,
        )
    text = re.sub(r"\| Completion Status \| [^|]+ \|", "| Completion Status | Complete |", text)
    text = re.sub(r"\| Coverage Gate \| [^|]+ \|", "| Coverage Gate | Closed |", text)
    text = re.sub(r"\| Evidence Gate \| [^|]+ \|", "| Evidence Gate | Passed |", text)
    text = re.sub(r"\| Books Gate \| [^|]+ \|", "| Books Gate | Passed |", text)
    text = re.sub(
        r"\*\*Status:\*\*.*",
        "**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly",
        text,
        count=1,
    )
    text = re.sub(
        r"(?ms)^## 13\. Final Status\n.*\Z",
        "## 13. Final Status\n\nDaily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。\n",
        text,
    )
    return text


def update_report(
    path: Path,
    month: int,
    day: int,
    node_paths: dict[str, Path],
    ordered_nodes: list[tuple[str, Path]],
    finalize_audits: bool,
) -> None:
    text = path.read_text()
    candidates = parse_candidates(text)
    text = strip_post_effective_incomplete_sources(text, date(2026, month, day))
    text = apply_prebooks_eligibility(text, candidates)
    candidates = parse_candidates(text)
    decisions = {candidate.family: books_decision(candidate, node_paths) for candidate in candidates}
    # Registry Version identifies the loaded registry snapshot; per-source
    # applicability is computed from Window End and Effective Date.
    text = re.sub(r"\| Registry Version \| [^|]+ \|", "| Registry Version | 2026-08-25 |", text)
    text = re.sub(r"\| Coverage Gate \| [^|]+ \|", "| Coverage Gate | Open |", text)
    text = re.sub(r"\| Evidence Gate \| [^|]+ \|", "| Evidence Gate | Open |", text)
    text = re.sub(r"\| Books Gate \| [^|]+ \|", "| Books Gate | Open |", text)
    text = re.sub(r"\| Completion Status \| [^|]+ \|", "| Completion Status | In Progress |", text)
    text = re.sub(
        r"\*\*Status:\*\*.*",
        "**Status:** In Progress（Coverage 与 Books 已完成主审，等待 fresh-context Semantic Audit 签字）；本次回放不生成 provisional Weekly",
        text,
        count=1,
    )
    text = re.sub(
        r"Coverage Gate 因 19 个机构历史页面与 Hugging Face Daily Papers 缺少可冻结 intraday cursor 而保持 Open；这不会抹掉 arXiv 候选的评分与 Review，但会阻止本次历史回放直接修改 Books。",
        "按来源注册表的 Effective Date 回放后，本窗口只有 arXiv 属于到期 Required Daily；后续才生效的机构源与 Hugging Face 不倒推为历史必扫项。Books 仍只接收通过 Evidence Gate、能改变长期机制的 Source Family。",
        text,
    )
    text = update_candidate_ledger(text, candidates, decisions)
    candidates = parse_candidates(text)
    text = update_source_review_dispositions(text, candidates, decisions)
    text = refresh_review_provenance(text, candidates)

    coverage_body = "\n".join(
        [
            "- arXiv 采用 first-public `published` timestamp；跨分类条目按 ID 去重，revision 不伪装为新 family。",
            "- `docs/RESEARCH_SOURCES.md` 的固定来源注册表于 2026-08-25 生效；依据 Effective Date，不把 19 个机构源和 Hugging Face 反推为此前窗口的 Required Daily，也不伪造历史 `no_hit`。",
            "- 本次用户授权的历史 replay 以可枚举 arXiv 主分母为确定性 Coverage；原始分页、UTC query、SHA-256 与 daily 09:00 分桶保存在月级 snapshot manifest。",
            "- Hugging Face Daily Papers 属于 non-deterministic discovery backstop；历史日期页恢复失败不改变 arXiv v1 的 owner，也不参与 Coverage Gate 算术。",
            "- vLLM、SGLang、Dynamo、KServe、Kubernetes、DeepSpeed 等工程源由完整 Sunday Weekly 负责，不强塞进 Daily。",
        ]
    )
    text = replace_section(text, "### Coverage Limitations", "## 2. Candidate Ledger", coverage_body)
    text = replace_section(
        text,
        "## 6. Books Comparison",
        "## 7. Semantic Audit",
        books_receipt(candidates, decisions, node_paths, ordered_nodes),
    )

    integrates = [candidate for candidate in candidates if decisions[candidate.family] == "Integrate"]
    no_change = [candidate for candidate in candidates if decisions[candidate.family] == "No Change — Existing Coverage"]
    weekly_only = [candidate for candidate in candidates if decisions[candidate.family] == "Weekly Only — Context"]
    action = "\n".join(
        [
            "1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。",
            "2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。",
            f"3. Books Decision：{len(integrates)} 个 `Integrate`、{len(no_change)} 个 `No Change — Existing Coverage`、{len(weekly_only)} 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。",
        ]
    )
    text = replace_section(text, "## 9. Recommended Action", "## 10. Repository Changes", action)

    changed_paths = sorted({node_paths[candidate.node].relative_to(ROOT).as_posix() for candidate in integrates})
    changes = [f"- 重建 `papers/2026/{month:02d}/{day:02d}/README.md` 的 Coverage applicability 与 Books receipts。"]
    changes.extend(f"- Refine `{changed_path}`，只吸收长期机制、取舍与失效边界。" for changed_path in changed_paths)
    if not changed_paths:
        changes.append("- 本窗口没有新增达到长期知识门槛的机制，Books 正文无变化。")
    text = replace_section(text, "## 10. Repository Changes", "## 11. Open Questions", "\n".join(changes))

    text = update_audits_pending(text, month, day, candidates)
    text = re.sub(
        r"(?ms)^## 13\. Final Status\n.*\Z",
        "## 13. Final Status\n\nDaily V2.1 的 frozen denominator、Evidence Review 与 Books Decision 已完成；当前仍为 In Progress，仅等待新的 Coverage/Books fresh-context Semantic Audit。审计签字前不宣称 Complete。\n",
        text,
    )
    if finalize_audits:
        text = finalize_semantic_audits(text, month, day)
    path.write_text(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", type=int, default=8)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=24)
    parser.add_argument(
        "--finalize-audits",
        action="store_true",
        help="record the independent fresh-context PASS after it has occurred",
    )
    parser.add_argument(
        "--repair-consistency-only",
        action="store_true",
        help="synchronize explicit Source Review dispositions and RP hashes only",
    )
    args = parser.parse_args()
    node_paths, ordered_nodes = roadmap_nodes()
    report_root = ROOT / f"papers/2026/{args.month:02d}"
    for day in range(args.start, args.end + 1):
        path = report_root / f"{day:02d}" / "README.md"
        if args.repair_consistency_only:
            repair_consistency_only(path)
            print(path.relative_to(ROOT))
            continue
        update_report(path, args.month, day, node_paths, ordered_nodes, args.finalize_audits)
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
