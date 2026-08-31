#!/usr/bin/env python3
"""Close the single 2026-05-12 exact-v1 blocker without touching shared Books."""

from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256


ROOT = REPO_ROOT
DAY = ROOT / "papers/2026/05/12/README.md"
SRC = ROOT / "papers/2026/05/_sources/daily-20260512"
AID = "2605.10133"
FAMILY = "SF-2026-ARXIV-2605-10133"
EVIDENCE = f"arXiv:{AID}v1"
URL = f"https://arxiv.org/html/{AID}v1"
HTML = SRC / f"exact-v1-bodies/{AID}v1.html"
TEXT = SRC / f"exact-v1-bodies/{AID}v1.txt"

METHOD = (
    f"{URL} §3.1–§3.3 Threat Model and UPAttack formulation; §4.1–§4.3 U-Sploit Attack Framework — "
    "an external contributor injects benign-looking functionality, implementation or trade-off requirements; "
    "U-Sploit selects initially secure tasks, derives the usability reward of insecure alternatives, refines the pressure, "
    "and verifies a functionality-preserving security regression with existing tests or generated distinguishing payloads"
)
EVALUATION = (
    f"{URL} §5.1–§5.4 Experiments; Appendix B.1 Dataset Construction; Appendix E Manual Verification — "
    "75 seed scenarios from 25 CWEs across Python, C and JavaScript; four victim models; CRbaseline/ASR/CRattacked; "
    "33 common secure-baseline cases for transfer; repeated-attempt and dynamic-payload ablations; 30+30 sampled tasks manually checked"
)
LIMITATIONS = (
    f"{URL} §5.1–§5.4; Appendix B.1; Appendix E; Impact Statement — exact-v1 has no dedicated Limitations section; "
    "the evidence is bounded to 75 benchmark scenarios, 25 CWEs, four named models, the disclosed Analyzer/Judge, mostly Python main results, "
    "33-case transfer intersection and sampled manual validation; one Type-1 sample was unsatisfiable, and controlled benchmark attacks do not prove production prevalence, causal internal reward hacking or defense efficacy"
)
ARTIFACT = (
    f"{URL} Impact Statement — artifacts were anonymized during review and planned for full release after acceptance; "
    "immutable event-time repository, dataset revision and exploit payload bundle Not Disclosed"
)
CLAIM = (
    "Requirement intake is a security boundary: a coding model may preserve secure behavior under the original task yet drop implicit security "
    "constraints when explicit functionality, implementation or trade-off wording becomes the higher-salience objective. The exact-v1 evidence "
    "supports this failure mode only for the disclosed benchmark, models, attack generator/judge and verification protocol; it does not prove all "
    "issue-tracker requests are adversarial, all coding models fail, the internal cause is identified, or the proposed defenses are effective."
)
DELTA = (
    "Current Ch72 treats prompt, code, package and tool outputs as untrusted inputs, and already requires independent effect-time verification, "
    "but it does not yet make the developer requirement itself a versioned supply-chain input. The durable addition is to carry explicit security "
    "invariants from requirement admission through code proposal and dual functional/security verification; the coding model owns only the proposal, "
    "while policy/CI and the repository owner retain merge authority."
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tag = None
        self.buf: list[str] = []
        self.rows: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2", "h3", "h4", "p", "li", "figcaption"}:
            self.tag = tag
            self.buf = []

    def handle_data(self, data):
        if self.tag:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if self.tag == tag:
            value = " ".join("".join(self.buf).split())
            if value:
                self.rows.append(value)
            self.tag = None
            self.buf = []


def load_json(name):
    return json.loads((SRC / name).read_text())


def save_json(name, data):
    (SRC / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def item_for(items, key="arxiv_id"):
    return next(item for item in items if item.get(key) == AID)


def replace_segment(text: str, marker: str, body: str) -> str:
    start = f"<!-- {marker}:start -->"
    end = f"<!-- {marker}:end -->"
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    return before + start + "\n" + body.strip() + "\n" + end + after


def replace_table_row(text: str, family: str, row: str, occurrence: int = 1) -> str:
    lines = text.splitlines()
    seen = 0
    for index, line in enumerate(lines):
        if line.startswith(f"| {family} |"):
            seen += 1
            if seen == occurrence:
                lines[index] = row
                return "\n".join(lines) + "\n"
    raise RuntimeError(f"missing table row {family} occurrence {occurrence}")


def main() -> None:
    if not HTML.exists() or HTML.stat().st_size != 387026:
        raise RuntimeError("official exact-v1 HTML is missing or incomplete")
    html_bytes = HTML.read_bytes()
    extractor = TextExtractor()
    extractor.feed(html_bytes.decode("utf-8", errors="replace"))
    TEXT.write_text("\n".join(extractor.rows) + "\n")
    html_sha = hashlib.sha256(html_bytes).hexdigest()
    text_sha = hashlib.sha256(TEXT.read_bytes()).hexdigest()

    review = load_json("exact-v1-review-packet-independent.json")
    target = item_for(review)
    target.update(
        review_route="deep",
        method_identity_locators=METHOD,
        evaluation_locators=EVALUATION,
        limitations_counterevidence_locators=LIMITATIONS,
        artifact_locators=ARTIFACT,
        claim_nonproof_boundary=CLAIM,
        completion_result="deep_complete",
    )

    provenance = load_json("evidence-provenance-manifest-independent.json")
    ptarget = item_for(provenance)
    ptarget.update(
        exact_v1_url=URL,
        retrieved_at="2026-09-01T14:40:00+08:00",
        retrieval_mode="official arXiv exact-v1 HTML downloaded and fully inspected",
        status="accessible",
        locator_source="actual exact-v1 Method/Evaluation/appendix/Impact Statement sections",
        local_body="exact-v1-bodies/2605.10133v1.html",
        source_body_sha256=html_sha,
        extracted_text_sha256=text_sha,
    )

    materials = load_json("materials-request-independent.json")
    materials["blocked"] = [x for x in materials.get("blocked", []) if x.get("arxiv_id") != AID]
    materials["ordinary_pending"] = 0
    materials["resolved"] = [{
        "arxiv_id": AID,
        "source_family_id": FAMILY,
        "resolved_at": "2026-09-01T14:40:00+08:00",
        "route": URL,
        "source_body_sha256": html_sha,
    }]

    for name in ["screening-ledger-independent-reconciled.json", "screening-ledger-final.json"]:
        ledger = load_json(name)
        rows = ledger.get("identities", ledger) if isinstance(ledger, dict) else ledger
        row = item_for(rows)
        row.update(
            review_status="deep_complete",
            access_status="accessible",
            integration_disposition="Integrate",
            books_disposition="Integrate",
        )
        row.pop("independent_blocker", None)
        if isinstance(ledger, dict):
            ledger["blocked"] = 0
        save_json(name, ledger)

    tsv_path = SRC / "screening-ledger-final.tsv"
    lines = tsv_path.read_text().splitlines()
    header = lines[0].split("\t")
    for i, line in enumerate(lines[1:], 1):
        cols = line.split("\t")
        row = dict(zip(header, cols))
        if row.get("arxiv_id") == AID:
            for key, value in {
                "review_status": "deep_complete",
                "access_status": "accessible",
                "integration_disposition": "Integrate",
                "books_disposition": "Integrate",
            }.items():
                if key in header:
                    cols[header.index(key)] = value
            lines[i] = "\t".join(cols)
            break
    tsv_path.write_text("\n".join(lines) + "\n")

    comparison = load_json("books-current-content-comparison-final.json")
    ctarget = item_for(comparison)
    ctarget.update(
        owner_node="PLATFORM-SECURITY",
        owner_path="books/part-06-ai-infrastructure/72-security.md",
        adjacent_paths=[
            "books/part-06-ai-infrastructure/71-multi-tenant.md",
            "books/part-06-ai-infrastructure/73-production-best-practice.md",
        ],
        owner_body_outline_before_review_notes=(
            "Lifecycle threats → Policy-bound sensors → Prompt/tool influence boundaries → Supply-chain Integrity → "
            "untrusted code and runtime effect boundaries → release evidence"
        ),
        adjacent_body_outlines_before_review_notes={
            "books/part-06-ai-infrastructure/71-multi-tenant.md": "tenant identity and control/data/resource/evidence isolation",
            "books/part-06-ai-infrastructure/73-production-best-practice.md": "production proof obligations, release gates and rollback",
        },
        decision="Integrate",
        reason=DELTA,
        prewrite_challenge="recovered_exact_v1_reopened_books_delta",
    )

    queue = load_json("books-writeback-queue-final.json")
    queue["status"] = "waiting_for_root_serial_writeback_after_exact_v1_recovery"
    queue["counts"].update(integrate=8, no_change=68, blocked=0, ordinary_pending=0)
    queue["blocked"] = []
    queue["shared_books_written"] = False
    queue["post_write_counts"].update(
        families_verified=7,
        owner_groups_verified=6,
        unresolved_books_findings=1,
    )
    queue["items"] = [x for x in queue["items"] if x.get("arxiv_id") != AID]
    queue["items"].append({
        "arxiv_id": AID,
        "source_family_id": FAMILY,
        "stable_node_id": "PLATFORM-SECURITY",
        "owner_path": "books/part-06-ai-infrastructure/72-security.md",
        "adjacent_paths": [
            "books/part-06-ai-infrastructure/71-multi-tenant.md",
            "books/part-06-ai-infrastructure/73-production-best-practice.md",
        ],
        "review_provenance_id": "RP-PENDING-RECOMPUTE",
        "books_review_ref": "BOOKS-REVIEW-20260512-2605-10133",
        "integration_delta": DELTA,
        "recommended_anchor": "PLATFORM-SECURITY / Supply-chain Integrity / before Optimization Pass",
        "required_evolution": (
            "trusted/internal requirement intake → external or mixed-trust requirement artifact → explicit security invariants carried into generation → "
            "dual functional/security effect verification → repository owner commit; keep human review, SAST and secure templates as fallback"
        ),
        "tradeoff_failure_fallback": (
            "Explicit invariants and dual verification add specification, test and false-reject cost; incomplete security assumptions, Analyzer/Judge blind spots "
            "or benchmark overfitting can still miss regressions. Fail closed to human security review, deterministic tests/static analysis or approved templates."
        ),
        "nonproof_boundary": CLAIM,
        "writeback_state": "waiting_for_root_serial_writeback",
        "owner_merge_group": "PLATFORM-SECURITY-REQUIREMENT-INTAKE",
    })

    audit = load_json("independent-semantic-audit.json")
    audit["counts"].update(exact_v1_recovered=2, blocked=0, independent_exact_v1_pending=0, exact_v1_complete=76)
    audit["findings"] = [
        item for item in audit.get("findings", [])
        if not (item.get("kind") == "access_recovered" and item.get("arxiv_id") == AID)
    ]
    audit["findings"].append({
        "kind": "access_recovered",
        "arxiv_id": AID,
        "evidence": {
            "status": "deep_complete",
            "access": "accessible",
            "primary": URL,
            "method": "§3.1–§3.3; §4.1–§4.3",
            "evaluation": "§5.1–§5.4; Appendix B.1; Appendix E",
            "limitations": "No dedicated section; benchmark/model/judge/manual-validation bounds recorded",
            "artifact": "Impact Statement; immutable event-time release Not Disclosed",
        },
    })
    audit["blocked"] = []
    audit["gate"].update(
        evidence="Passed — ordinary pending is 0 and 76/76 retained families have exact-v1 Method/Evaluation/limitations/artifact review.",
        books="Open — seven earlier writebacks passed post-write audit; recovered SF-2026-ARXIV-2605-10133 requires root serial writeback and independent post-write semantic audit.",
        completion="In Progress — Coverage and Evidence are closed; one recovered Integrate family awaits Books writeback and post-write audit.",
    )
    audit["exact_v1_receipt"].update(
        result="76 deep_complete; 0 blockers; ordinary pending 0",
        recovery="exact-v1-recovery-2605.10133.json",
    )
    audit["books_prewrite_receipt"].update(
        current_owner_adjacent_review="76/76 (8 Integrate; 68 No Change; 0 Blocked)",
        recovered_queue="SF-2026-ARXIV-2605-10133 waiting_for_root_serial_writeback",
    )

    text = DAY.read_text()
    text = text.replace(
        "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass。普通 pending=0；7/7 Books writeback 已通过非写作者 owner+adjacent semantic audit；`2605.10133v1` 保持精确 external blocker。",
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。普通 pending=0；76/76 exact-v1 已完成，既有 7/7 Books writeback 已通过审计；恢复的 `2605.10133v1` 形成第 8 项 queue，等待 root 串行写回与独立 post-write audit。",
    )
    text = text.replace(
        "75/76 项完成 exact-v1 Method、Evaluation、Limitations/Counterevidence 与 Artifact Review；`2605.10133v1` 只有 identity/abstract，保持精确外部 blocker。current-Books adversarial challenge 将 47 个 provisional Integrate 收紧为 7 项 Integrate、68 项 No Change、1 项 Blocked",
        "76/76 项完成 exact-v1 Method、Evaluation、Limitations/Counterevidence 与 Artifact Review；`2605.10133v1` 已从 official versioned HTML 恢复。current-Books adversarial challenge 将 47 个 provisional Integrate 与恢复项收敛为 8 项 Integrate、68 项 No Change、0 项 Blocked",
    )
    text = text.replace("| Completion Status | Conditional |", "| Completion Status | In Progress |")
    text = text.replace("| Evidence Gate | Conditional Pass |", "| Evidence Gate | Passed |")
    text = text.replace("| Books Gate | Conditional Pass |", "| Books Gate | Open |")
    text = text.replace(
        "`2605.10133v1` 的 official abs/version 可读，但 exact-v1 HTML、PDF 与 TeX 均不可取得；该缺口不回退为摘要 Review，也不进入 Books。",
        "`2605.10133v1` 的 official exact-v1 HTML 已恢复并完成全文 Review；其 requirement-intake security delta 已进入第 8 项 Books queue，但尚未写共享 Books。",
    )

    candidate_row = (
        f"| {FAMILY} | {EVIDENCE} | paper-v1:{AID} | 2026-W20 | 2026-05-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | "
        f"retained | deep_complete | accessible | knowledge_gap | review:{FAMILY} | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:{FAMILY} | no |"
    )
    text = replace_table_row(text, FAMILY, candidate_row, 1)

    review_body = f"""
#### Usability as a Weapon: Attacking the Safety of LLM-Based Code Generation via Usability Requirements

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`PLATFORM-SECURITY`。
Method / identity：{METHOD}。
Evaluation：{EVALUATION}。
Counterevidence / limitations：{LIMITATIONS}。
Artifact：{ARTIFACT}。

<!-- claim:{FAMILY}:start -->{CLAIM}<!-- claim:{FAMILY}:end -->

Disposition=`Integrate`；该结论来自 exact-v1 恢复与 current owner+adjacent comparison，不由 validator 代签。共享 Books 尚未写入。
"""
    text = replace_segment(text, f"review:{FAMILY}", review_body)

    books_body = f"""
<!-- existing:{FAMILY}:start -->已读取 current owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 `[books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md]`，并只比较首个 `## Review notes` 前的正文。现有章节覆盖不可信 Prompt、代码、artifact、tool result、effect-time gate 与 code proof loop，但没有把自然语言 requirement 本身作为进入 AI coding supply chain 的 versioned untrusted input。<!-- existing:{FAMILY}:end -->
<!-- delta:{FAMILY}:start -->{DELTA} 写回必须保留旧路径：内部可信、约束简单的需求仍可使用普通 code review；外部或 mixed-trust requirement 则需绑定来源、显式 security invariants、功能与安全双验证、失败时人工/SAST/approved-template fallback。论文只支持其 75-scenario/25-CWE/four-model contract，不证明生产流行度或任意防御有效。<!-- delta:{FAMILY}:end --> Decision=`Integrate`；state=`waiting_for_root_serial_writeback`。
"""
    text = replace_segment(text, f"books-review:{FAMILY}", books_body)

    deep_row = (
        f"| {FAMILY} | score_7_9;forced_review;potential_books_delta | not_selected | — | — | "
        f"Exact-v1 Review 与 Books Decision 已完成；requirement-intake delta 保留在 writeback queue，Top 3 只限制 Daily 叙事篇幅 | analysis-decision:{FAMILY} |"
    )
    text = replace_table_row(text, FAMILY, deep_row, 3)

    books_row = (
        f"| {FAMILY} | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#supply-chain-integrity | "
        f"books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | "
        f"existing:{FAMILY} | delta:{FAMILY} | Direct Evolution | Integrate | books-review:{FAMILY} |"
    )
    text = replace_table_row(text, FAMILY, books_row, 4)

    text = text.replace(
        "| SA-20260512-INDEPENDENT-EVIDENCE | fresh-context:non-author | evidence | review:SF-2026-ARXIV-2605-09863 | none | 75 deep_complete; 1 exact-v1 access blocker precisely frozen in Materials Request; ordinary pending=0 | passed |",
        f"| SA-20260512-INDEPENDENT-EVIDENCE | fresh-context:may2026_day03 | evidence | review:{FAMILY} | none | 76/76 deep_complete；2605.10133v1 official HTML recovered with content hash and exact Method/Evaluation/non-proof locators；ordinary pending=0 | passed |",
    )
    text = text.replace(
        "| SA-20260512-INDEPENDENT-BOOKS | fresh-context:non-author | books | books-review:SF-2026-ARXIV-2605-09863 | none | 7/7 markers unique and before Review notes; 6/6 owner groups pass evolution/ownership/trade-off/failure/fallback/evidence/handoff audit | passed |",
        f"| SA-20260512-INDEPENDENT-BOOKS | fresh-context:non-author | books | books-review:{FAMILY} | SF-2026-ARXIV-2605-10133 awaits root serial writeback and independent post-write audit | Earlier 7/7 remain passed；the recovered requirement-intake delta is queued but not yet present in Books | open |",
    )
    text = text.replace(
        "7 项、6 个 owner group 已完成写回，并通过 `books-post-write-semantic-audit.json` 的非写作者复核；`TRAIN-DISTRIBUTED-TRAINING` 的两项 family 已合并为 execution-plan→failure→recovery 演进链。后续只需在 exact-v1 primary 恢复时重开 `2605.10133v1` 的 Evidence/Books Decision。",
        "既有 7 项、6 个 owner group 已完成写回并通过 post-write audit。`2605.10133v1` exact-v1 恢复后新增第 8 项：由 root 在 Ch72 的 Supply-chain Integrity 主线中串行写回 requirement-intake security boundary，随后由非写作者做 owner+adjacent post-write semantic audit。",
    )
    text = text.replace(
        "- 新增独立 exact-v1 packet、provenance、Materials Request、Books comparison、final queue 与 post-write semantic audit。",
        "- 恢复 `2605.10133v1` official exact-v1 HTML，补齐全文 Review、provenance、current Books comparison 与第 8 项 writeback queue；既有 7 项 post-write audit 保持有效。",
    )
    text = text.replace(
        "- `2605.10133v1` 的 exact-version full text 能否从作者 manuscript 或事件时 repository 恢复，并在恢复后重新判定当前 Conditional Gate 与 Books disposition？",
        "- root 将 requirement-intake 作为不可信 supply-chain input 写入 Ch72 后，独立 reviewer 是否确认旧路径、约束变化、owner、trade-off、failure、fallback 与 evidence boundary 均完整？",
    )
    material_row = "| MR-SF-2605-10133 | P1 Full Text | SF-2026-ARXIV-2605-10133 | — | — | 2026-W20 | arXiv:2605.10133v1; https://arxiv.org/abs/2605.10133v1 | exact-v1 full body with Method, Evaluation, Limitations and appendices | abstract cannot establish mechanism, experiment contract, counterevidence or Books eligibility | official exact-v1 PDF/TeX, author manuscript demonstrably identical to v1, or event-time repository paper snapshot | arxiv-2605.10133v1.pdf | deep review and Books re-decision |\n"
    text = text.replace(material_row, "")
    text = text.replace("Completion Status: `Conditional`", "Completion Status: `In Progress`")
    text = text.replace("Evidence: `Conditional Pass`", "Evidence: `Passed`")
    text = text.replace("Books: `Conditional Pass`", "Books: `Open`")
    text = text.replace(
        "ordinary pending=0；75/76 exact-v1 complete；7/7 Books writeback 已通过 post-write semantic audit；1 precise external blocker 保持 Conditional。",
        "ordinary pending=0；76/76 exact-v1 complete；既有 7/7 Books writeback 已通过 post-write audit；恢复项等待 root 串行写回与独立 post-write audit。",
    )
    text = text.replace("unresolved findings: 1", "unresolved findings: 1")
    DAY.write_text(text)

    text = DAY.read_text()
    review_ref = f"review:{FAMILY}"
    start = f"<!-- {review_ref}:start -->"
    end = f"<!-- {review_ref}:end -->"
    body = text.split(start, 1)[1].split(end, 1)[0]
    candidate = {
        "Event Identity": f"paper-v1:{AID}",
        "Primary Identifier": EVIDENCE,
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "knowledge_gap",
    }
    rp = _expected_review_provenance(
        FAMILY,
        candidate,
        "deep",
        EVIDENCE,
        f"SRC-ARXIV@{EVIDENCE}",
        METHOD,
        EVALUATION,
        LIMITATIONS,
        ARTIFACT,
        f"claim:{FAMILY}",
        review_ref,
        _normalized_body_sha256(body),
    )
    text = DAY.read_text()
    completion_row = (
        f"| {FAMILY} | {rp} | deep | {EVIDENCE} | SRC-ARXIV@{EVIDENCE} | {METHOD} | {EVALUATION} | {LIMITATIONS} | "
        f"{ARTIFACT} | claim:{FAMILY} | complete |"
    )
    text = replace_table_row(text, FAMILY, completion_row, 2)
    text = text.replace("RP-5634c79c6bdc985a", rp)
    DAY.write_text(text)

    target["review_provenance_id"] = rp
    ptarget["review_provenance_id"] = rp
    ctarget["review_provenance_id"] = rp
    queue["items"][-1]["review_provenance_id"] = rp

    md = (SRC / "BOOKS_WRITEBACK_QUEUE_FINAL.md").read_text()
    md = md.replace(
        "**State:** Post-write semantic audit passed；shared Books 已按 6 个 owner group 写回，Report-level Books Gate 因 1 个 exact-v1 external blocker 保持 `Conditional Pass`。",
        "**State:** 既有 7 项 post-write semantic audit 保持通过；恢复的第 8 项等待 root 串行写回，Report-level Books Gate=`Open`。",
    )
    md = md.replace(
        "47 个 provisional Integrate 经 current owner + adjacent semantic-body challenge 收紧为 7；另 68 个为 `No Change — Existing Coverage`，1 个 exact-v1 blocker 保持冻结。7 项已经按 owner 合并写回，并由非写作者完成 7/7 marker、正文位置、演进链、trade-off、failure、fallback、证据边界和相邻章节复核；详情见 `books-post-write-semantic-audit.json`。",
        "47 个 provisional Integrate 经 current owner + adjacent semantic-body challenge 收紧为 7；恢复 exact-v1 后，最终状态为 8 个 `Integrate`、68 个 `No Change`、0 blocker。既有 7 项 post-write audit 仍有效；第 8 项必须由 root 串行写回并接受新的独立 post-write audit。",
    )
    md = md.replace(
        "## Blocked\n\n- `SF-2026-ARXIV-2605-10133`：exact-v1 正文不可取得；不得依据 abstract 进入 Books。",
        f"## `PLATFORM-SECURITY` — waiting for root serial writeback\n\nTarget: `books/part-06-ai-infrastructure/72-security.md`\n\n- `{FAMILY}` / {EVIDENCE}\n  - Delta: {DELTA}\n  - Evidence: `{rp}`；`BOOKS-REVIEW-20260512-2605-10133`\n  - Non-proof: {CLAIM}\n  - Required flow: trusted/internal requirement intake → mixed-trust requirement artifact → explicit security invariants → model code proposal → functional/security effect checks → repository-owner commit；failure 时回退 human review、SAST 或 approved templates。",
    )
    (SRC / "BOOKS_WRITEBACK_QUEUE_FINAL.md").write_text(md)

    recovery = {
        "schema": "exact-v1-recovery-audit-v2.1",
        "report_date": "2026-05-12",
        "arxiv_id": AID,
        "source_family_id": FAMILY,
        "primary_evidence_version": EVIDENCE,
        "retrieved_at": "2026-09-01T14:40:00+08:00",
        "routes": [
            {"url": URL, "status": "200", "content_length": 387026, "etag": "CMzEvoyAupYDEAE="},
            {"url": f"https://arxiv.org/pdf/{AID}v1", "status": "200 HEAD", "content_length": 730119, "used": False},
            {"url": f"https://arxiv.org/e-print/{AID}v1", "status": "not_needed_after_html_recovery"},
        ],
        "local_body": str(HTML.relative_to(SRC)),
        "source_body_sha256": html_sha,
        "extracted_text": str(TEXT.relative_to(SRC)),
        "extracted_text_sha256": text_sha,
        "review_provenance_id": rp,
        "review_status": "deep_complete",
        "access_status": "accessible",
        "books_disposition": "Integrate",
        "books_state": "waiting_for_root_serial_writeback",
        "ordinary_pending": 0,
        "blocked": 0,
    }

    save_json("exact-v1-review-packet-independent.json", review)
    save_json("evidence-provenance-manifest-independent.json", provenance)
    save_json("materials-request-independent.json", materials)
    save_json("books-current-content-comparison-final.json", comparison)
    save_json("books-writeback-queue-final.json", queue)
    save_json("independent-semantic-audit.json", audit)
    save_json("exact-v1-recovery-2605.10133.json", recovery)
    print(json.dumps({"rp": rp, "html_sha256": html_sha, "queue": 8, "blocked": 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
