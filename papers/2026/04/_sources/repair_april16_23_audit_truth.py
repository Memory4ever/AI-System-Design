#!/usr/bin/env python3
"""Fail closed the 2026-04-16..23 author packets after evidence audit.

The author renderer recorded abstract-derived prose behind generic section
placeholders as exact-v1 completion.  This repair preserves every author
artifact, but removes the unsupported completion and Books eligibility claims
until a source-specific full-text review is materialized.
"""

from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
MONTH = ROOT / "papers/2026/04"
DAYS = range(16, 24)

# Concrete false-negative challenges found by independently replaying the
# closure titles and abstracts.  They are challenges, not automatic
# admissions: each still needs exact-v1 evidence before denominator promotion.
HIGH_RISK_CLOSURES = {
    16: {
        "2604.15379": "Fleet changes megakernel task/dataflow ownership across multi-die GPUs.",
        "2604.14512": "CBCL proposes a safety boundary for self-extending agent communication.",
        "2604.18614": "HadAgent claims decentralized agent-serving control and proof-of-inference.",
        "2604.14457": "NeuroTrace makes inference provenance an adversarial-detection state owner.",
        "2604.13488": "Multi-role orchestration changes the GUI-agent runtime control path.",
    },
    17: {
        "2604.14661": "AIPC automates model deployment against a concrete device runtime.",
        "2604.18616": "ARGUS uses data-flow invariants to control GPU optimization.",
        "2604.14690": "Switching Efficiency exposes AI-datacenter network efficiency contracts.",
        "2604.14531": "TRACER routes requests using trace-derived cost state.",
        "2604.15522": "EasyRider controls datacenter-scale training power transients.",
        "2604.15499": "SecureRouter changes routing while protecting model-selection state.",
    },
    18: {
        "2604.15750": "DepCap changes block-wise parallel decoding admission.",
        "2604.16145": "The paper models mixed-precision distributed-training completion time.",
        "2604.15728": "Privacy-Preserving LLM Routing changes router visibility and control.",
        "2604.16762": "CapSeal introduces capability-sealed secret mediation for agents.",
        "2604.15751": "PoSME makes sequential memory execution externally verifiable.",
        "2604.16088": "The study measures real HPC communication and congestion state.",
    },
    19: {
        "2604.16802": "The framework jointly controls pricing and scaling in multi-tenant GPU clouds.",
        "2604.16870": "Governed MCP moves tool governance into kernel-level primitives.",
        "2604.17092": "The work defines observability state for AI developer tools.",
        "2604.17172": "UCCL-Zip changes the compression/transport boundary in GPU communication.",
        "2604.17182": "The paper analyzes MoE routing locality under shared-prefix forks.",
    },
    20: {
        "2604.17238": "Breaking Euston demonstrates private-input leakage in secure inference.",
        "2604.17377": "AnchorMem makes fact/context memory write ownership explicit.",
        "2604.17397": "The paper applies speculative commit/verification to autoregressive video.",
        "2604.17550": "Flint changes compiler ownership for distributed-ML design exploration.",
        "2604.17557": "Causal-temporal event graphs model recursive agent execution traces.",
        "2604.17640": "The work controls energy-aware HPC co-scheduling.",
    },
    21: {
        "2604.17861": "GPUOS proposes an OS primitive for transparent GPU operation fusion.",
        "2604.17950": "CADMAS-CTX calibrates capabilities for multi-agent delegation.",
        "2604.18071": "The study identifies durable design decisions in agent harnesses.",
        "2604.18478": "WorldDB owns write-time reconciliation for vector graph memory.",
        "2604.18860": "The paper formalizes TOCTOU state races in computer-use agents.",
        "2604.18909": "ChipLight co-optimizes chiplet interconnects for LLM training.",
    },
    22: {
        "2604.19494": "DPC is a distributed page cache over CXL.",
        "2604.19657": "The execution environment introduces a user-data safety boundary for agents.",
        "2604.19884": "The paper separates signal degradation from computation collapse in quantization.",
        "2604.20032": "LEO traces cross-vendor GPU stall root causes.",
        "2604.20070": "The system audits and controls spreadsheet agent actions.",
    },
    23: {
        "2604.20105": "EnergAIzer estimates GPU power for AI workloads.",
        "2604.20500": "The paper controls deterministic exploration of truncated decoding trees.",
        "2604.20819": "Stream-CQSA schedules attention work to avoid out-of-memory failure.",
        "2604.20833": "AVISE defines a security-evaluation framework for AI systems.",
        "2604.20943": "SCM defines sleep consolidation and algorithmic forgetting for LLM memory.",
    },
}


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def split_row(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def join_row(parts: list[str]) -> str:
    return "| " + " | ".join(parts) + " |"


def patch_table(text: str, marker: str, update) -> str:
    lines = text.splitlines()
    marker_index = next(i for i, line in enumerate(lines) if marker in line)
    header_index = marker_index + 1
    while header_index < len(lines) and not lines[header_index].startswith("|"):
        header_index += 1
    row_index = header_index + 2
    while row_index < len(lines) and lines[row_index].startswith("|"):
        parts = split_row(lines[row_index])
        if parts and parts[0].startswith("SF-"):
            lines[row_index] = join_row(update(parts))
        row_index += 1
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def patch_readme(path: Path, day: int, retained: int, closures: int, old_queue: int, checkpoint_at: str) -> None:
    text = path.read_text()
    text = re.sub(
        r"\*\*Status:\*\*.*",
        "**Status:** In Progress — Evidence Re-review Required；Coverage=Open、Evidence=Open、Books=Open；"
        f"independent audit rejected {retained}/{retained} generic exact-v1 completion claims and {old_queue} provisional Books items.",
        text,
        count=1,
    )
    text = re.sub(
        r"strong-system 反向审计.*?本 lane 未修改共享 Books，不能把 author 自检或 validator 通过表述为 fresh-context 验收。",
        f"全窗 identity 与 title/abstract 仍保留为 author screening input；author denominator={retained}、"
        f"closures={closures}。独立证据审计确认 {retained}/{retained} Review 使用通用占位 locator，"
        "且机制、trade-off 与 claim boundary 主要由摘要句和机制模板拼接，不能证明 exact-v1 已全文阅读。"
        f"原 {old_queue} 项 Books queue 已保存为 author rejected draft；canonical queue 暂时清空，"
        "等待逐 family source-specific exact-v1 re-review 与 current Books comparison。",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(r"\| Denominator ID \|.*", f"| Denominator ID | DEN-202604{day:02d}-UNDER-INDEPENDENT-REVIEW-{retained} |", text)
    # Keep the author's timestamp as a historical checkpoint.  The audit marks
    # its semantic freeze invalid through the Denominator ID and Gate instead.
    text = re.sub(r"\| Denominator Frozen At \|.*", f"| Denominator Frozen At | {checkpoint_at} |", text)

    def candidate(parts: list[str]) -> list[str]:
        if len(parts) >= 22:
            parts[11] = "pending"
            parts[12] = "accessible"
            parts[14] = "—"
            parts[18] = "—"
            parts[19] = "Not Assessed"
            parts[20] = "—"
        return parts

    def receipt(parts: list[str]) -> list[str]:
        if len(parts) >= 11:
            parts[1] = "—"
            parts[5] = "Pending — actual exact-v1 Method section locator not yet captured"
            parts[6] = "Pending — actual exact-v1 Evaluation/table locator not yet captured"
            parts[7] = "Pending — actual exact-v1 Limitations/counterevidence locator not yet captured"
            parts[8] = "Pending — exact-v1 artifact locator not yet verified"
            parts[9] = "Pending — source-specific claim boundary not yet established"
            parts[10] = "pending"
        return parts

    selected_ids = set(re.findall(r"<!-- analysis:DA-(\d+):start -->", text))

    def selection(parts: list[str]) -> list[str]:
        if len(parts) >= 7:
            suffix = parts[0].rsplit("-", 1)[-1]
            parts[0] = parts[0]
            parts[1] = "score_7_9"
            parts[4] = "—"
            if suffix in selected_ids:
                parts[2] = "selected"
                parts[3] = f"DA-{suffix}"
                parts[5] = "author Top-3 draft preserved for traceability; independent evidence audit remains open."
                parts[6] = f"analysis:DA-{suffix}"
            else:
                parts[2] = "not_selected"
                parts[3] = "—"
                parts[5] = "author selection draft preserved; independent evidence audit remains open."
                parts[6] = f"analysis-decision:{parts[0]}"
        return parts

    text = patch_table(text, "validator:candidate-ledger-v2.1", candidate)
    text = patch_table(text, "validator:review-completion-v1", receipt)
    text = patch_table(text, "validator:deep-analysis-selection-v1", selection)
    # A pending candidate has no canonical Books Comparison yet.  Retaining
    # rows with synthetic empty anchors would itself be a false receipt.
    lines = text.splitlines()
    marker_index = next(i for i, line in enumerate(lines) if "validator:books-comparison-v1" in line)
    header_index = marker_index + 1
    while not lines[header_index].startswith("|"):
        header_index += 1
    row_index = header_index + 2
    while row_index < len(lines) and lines[row_index].startswith("|"):
        if split_row(lines[row_index])[0].startswith("SF-"):
            del lines[row_index]
        else:
            row_index += 1
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")

    text = re.sub(
        r"\| SA-202604\d{2}-COVERAGE \|.*",
        f"| SA-202604{day:02d}-COVERAGE | fresh-context:independent-reviewer | coverage | "
        f"coverage:SRC-ARXIV:202604{day:02d} | F-202604{day:02d}-DENOMINATOR | "
        "author retained/closure boundary requires full independent FP/FN replay; high-risk closures were found | open |",
        text,
    )
    text = re.sub(
        r"\| SA-202604\d{2}-EVIDENCE \|.*",
        f"| SA-202604{day:02d}-EVIDENCE | fresh-context:independent-reviewer | evidence | "
        f"validator:review-completion-v1 | F-202604{day:02d}-GENERIC-LOCATORS | "
        f"rejected {retained}/{retained} generic locator / abstract-derived completion claims; source-specific full-text review pending | open |",
        text,
    )
    text = re.sub(
        r"\| SA-202604\d{2}-DEEP \|.*",
        f"| SA-202604{day:02d}-DEEP | fresh-context:independent-reviewer | deep_analysis_selection | "
        f"validator:deep-analysis-selection-v1 | F-202604{day:02d}-PREMATURE-SELECTION | "
        "selection invalidated until evidence routes complete | open |",
        text,
    )
    text = re.sub(
        r"\| SA-202604\d{2}-BOOKS \|.*",
        f"| SA-202604{day:02d}-BOOKS | fresh-context:independent-reviewer | books | "
        f"validator:books-comparison-v1 | F-202604{day:02d}-PREMATURE-BOOKS | "
        "canonical queue cleared; exact-v1 and current owner+adjacent comparison pending | open |",
        text,
    )
    text = re.sub(
        r"## 9\. Recommended Action\n\n.*?\n\n## 10\.",
        "## 9. Recommended Action\n\n逐 family 读取 official exact-v1 正文，记录实际 Method/Evaluation/Limitations/Artifact locator，"
        "完成独立 denominator FP/FN replay 后重新评分、选择 Deep Analysis 并读取 current owner+adjacent。"
        "在此之前 canonical Books queue 为 0，禁止写共享 Books。\n\n## 10.",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"## 11\. Open Questions\n\n.*?\n\n## 12\.",
        f"## 11. Open Questions\n\n- {retained} 项 source-specific exact-v1 Full Source Review 尚未完成。\n"
        f"- {retained + closures}/{retained + closures} identity 的独立 FP/FN replay 尚未签署完成；已发现 high-risk closure。\n"
        f"- author provisional queue={old_queue} 已失效，Books Decision 必须在 Evidence 通过后重做。\n\n## 12.",
        text,
        flags=re.S,
    )
    text = re.sub(r"unresolved findings: \d+", "unresolved findings: 4", text)
    text = re.sub(
        r"Author packet：raw=.*",
        f"Independent audit checkpoint：raw/registered/screened={retained + closures}/{retained + closures}/{retained + closures}；"
        f"author denominator={retained}、closures={closures}；exact-v1 source-specific complete=0、pending={retained}；"
        f"canonical queue=0（author rejected draft={old_queue}）。Coverage/Evidence/Books 均保持 Open。",
        text,
    )
    path.write_text(text)


def main() -> None:
    for day in DAYS:
        src = MONTH / "_sources" / f"daily-202604{day:02d}"
        ledger_path = src / "screening-ledger-final.json"
        ledger = load(ledger_path)
        retained = ledger["candidate_denominator"]
        closures = ledger["pre_denominator_closures"]
        identity_by_id = {row["arxiv_id"]: row for row in ledger["identities"]}
        challenges = []
        for arxiv_id, boundary in HIGH_RISK_CLOSURES[day].items():
            row = identity_by_id.get(arxiv_id)
            if row is None or row["screening_status"] != "pre_denominator_closure":
                raise ValueError(f"high-risk closure {arxiv_id} missing from 2026-04-{day:02d}")
            challenges.append({
                "source_family_id": row["source_family_id"],
                "arxiv_id": arxiv_id,
                "title": row["title"],
                "current_screening_reason": row["screening_reason"],
                "independent_challenge": boundary,
                "status": "false_negative_challenge_pending_exact_v1",
            })
        dump(src / "independent-high-risk-closure-challenges.json", {
            "schema": "independent-high-risk-closure-challenges-v2.1",
            "report_date": f"2026-04-{day:02d}",
            "full_closure_replay_denominator": closures,
            "challenge_count": len(challenges),
            "items": challenges,
            "admission_boundary": "challenge is not promotion; exact-v1 and durable-system-contract review required",
        })

        for row in ledger["identities"]:
            if row["screening_status"] == "candidate_denominator":
                row["review_status"] = "pending"
                row["access_status"] = "accessible"
                row["integration_disposition"] = "Not Assessed"
        dump(ledger_path, ledger)

        packet_path = src / "exact-v1-review-packet.json"
        packet = load(packet_path)
        for item in packet["items"]:
            item["author_draft_rejected_reason"] = (
                "generic section placeholders and abstract-derived prose do not establish exact-v1 full-text review"
            )
            item["review_provenance_id"] = "—"
            item["method_locator"] = "Pending — actual exact-v1 Method section locator not yet captured"
            item["evaluation_locator"] = "Pending — actual exact-v1 Evaluation/table locator not yet captured"
            item["limitations_locator"] = "Pending — actual exact-v1 Limitations/counterevidence locator not yet captured"
            item["artifact_locator"] = "Pending — exact-v1 artifact locator not yet verified"
            item["claim_boundary"] = "Pending — source-specific claim boundary not yet established"
            item["review_status"] = "pending"
            item["access_status"] = "accessible"
            item["result"] = "pending"
            item["stable_node_id"] = "—"
            item["books_disposition"] = "Not Assessed"
        dump(packet_path, packet)

        receipt_path = src / "review-completion-receipt.json"
        receipt = load(receipt_path)
        for item in receipt["items"]:
            item["review_provenance_id"] = "—"
            item["method_locator"] = "Pending — actual exact-v1 Method section locator not yet captured"
            item["evaluation_locator"] = "Pending — actual exact-v1 Evaluation/table locator not yet captured"
            item["limitations_locator"] = "Pending — actual exact-v1 Limitations/counterevidence locator not yet captured"
            item["artifact_locator"] = "Pending — exact-v1 artifact locator not yet verified"
            item["claim_boundary"] = "Pending — source-specific claim boundary not yet established"
            item["review_status"] = "pending"
            item["access_status"] = "accessible"
            item["result"] = "pending"
            item["stable_node_id"] = "—"
            item["books_disposition"] = "Not Assessed"
        dump(receipt_path, receipt)

        provenance_path = src / "exact-v1-provenance.json"
        provenance = load(provenance_path)
        for item in provenance["items"]:
            item["review_provenance_id"] = "—"
            item["review_status"] = "pending"
            item["locators"] = []
            item["independent_finding"] = "author generic locators rejected; exact-v1 source-specific locator capture pending"
        dump(provenance_path, provenance)

        compare_path = src / "books-current-content-comparison.json"
        compare = load(compare_path)
        for item in compare["items"]:
            item["author_provisional_disposition"] = item.get("disposition")
            item["disposition"] = "Not Assessed"
            item["books_review_ref"] = "—"
            item["independent_finding"] = "Evidence Gate open; current owner+adjacent comparison must be repeated after exact-v1 review"
        dump(compare_path, compare)

        queue_path = src / "BOOKS_WRITEBACK_QUEUE.json"
        queue = load(queue_path)
        old_queue = len(queue["items"])
        rejected_path = src / "author-provisional-books-writeback-queue-rejected.json"
        if not rejected_path.exists():
            rejected = deepcopy(queue)
            rejected["status"] = "rejected_by_independent_evidence_audit"
            rejected["rejection_reason"] = "source-specific exact-v1 review and current Books challenge not established"
            dump(rejected_path, rejected)
        queue["items"] = []
        queue["status"] = "open_pending_evidence_and_books_reaudit"
        queue["invalidated_author_item_count"] = old_queue
        queue["canonical_queue_count"] = 0
        dump(queue_path, queue)

        audit = {
            "schema": "independent-semantic-audit-v2.1",
            "report_date": f"2026-04-{day:02d}",
            "status": "open_with_findings",
            "auditor": "fresh-context:independent-reviewer",
            "weekly_semantic_dependency_count": 0,
            "screening_scope": {
                "raw": retained + closures,
                "registered": retained + closures,
                "author_retained": retained,
                "author_closures": closures,
                "independent_replay_status": "open",
            },
            "findings": [
                {
                    "id": f"F-202604{day:02d}-GENERIC-LOCATORS",
                    "scope": "evidence",
                    "affected": retained,
                    "finding": "all author complete reviews use generic section placeholders rather than actual exact-v1 locators",
                    "resolution": "completion claims invalidated; source-specific review returned to pending",
                },
                {
                    "id": f"F-202604{day:02d}-ABSTRACT-TEMPLATES",
                    "scope": "evidence",
                    "affected": retained,
                    "finding": "mechanism/trade-off/claim-boundary prose is substantially abstract-derived and mechanism-template generated",
                    "resolution": "author prose retained as rejected draft only; cannot support RP or Deep Selection",
                },
                {
                    "id": f"F-202604{day:02d}-PREMATURE-BOOKS",
                    "scope": "books",
                    "affected": old_queue,
                    "finding": "Books Integrate decisions were made before valid Evidence completion and use generic owner comparison anchors",
                    "resolution": "canonical queue cleared; original queue preserved as rejected author draft",
                },
                {
                    "id": f"F-202604{day:02d}-DENOMINATOR",
                    "scope": "coverage",
                    "affected": retained + closures,
                    "finding": f"full independent false-positive/false-negative semantic replay is not yet signed; {len(challenges)} concrete high-risk closures recorded",
                    "resolution": "Coverage remains Open; author denominator is provisional; see independent-high-risk-closure-challenges.json",
                },
            ],
            "unresolved_findings": 4,
            "gate": {"coverage": "Open", "evidence": "Open", "books": "Open", "completion": "In Progress"},
        }
        dump(src / "independent-semantic-audit.json", audit)

        coverage = load(src / "coverage-receipt.json")
        checkpoint_at = coverage.get("executed_at") or coverage.get("items", [{}])[0].get("executed_at")
        if not checkpoint_at:
            raise ValueError(f"missing executed_at for 2026-04-{day:02d}")
        patch_readme(MONTH / f"{day:02d}" / "README.md", day, retained, closures, old_queue, checkpoint_at)


if __name__ == "__main__":
    main()
