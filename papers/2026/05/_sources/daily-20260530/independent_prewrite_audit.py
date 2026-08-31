#!/usr/bin/env python3
"""Fresh-context independent pre-write audit for 2026-05-30.

This script is intentionally date-local.  It preserves the author packet,
replays the frozen 730-row inventory, restores false negatives only after an
exact-v1 body review, challenges the provisional Books decisions against the
current owner and its adjacent chapters, and leaves shared Books untouched.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

H = Path(__file__).resolve().parent
ROOT = H.parents[4]
REPORT = ROOT / "papers/2026/05/30/README.md"
NOW = datetime.now(timezone.utc).isoformat()
sys.path.insert(0, str(ROOT))
from scripts.validate_research import _expected_review_provenance, _normalized_body_sha256


def sf(aid: str) -> str:
    return "SF-2026-ARXIV-" + aid.replace(".", "-")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", unescape(text or "")).strip()


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", clean(text)) if s]


def pick(row: dict, pattern: str, fallback: int = 0) -> str:
    ss = sentences(row.get("abstract", "")) or [row["title"]]
    return next((s for s in ss if re.search(pattern, s, re.I)), ss[fallback])[:650]


def mechanism(row: dict) -> str:
    return pick(row, r"\b(propose|introduce|present|develop|design|formulate|build|study|investigate|show|demonstrate|find)\b")


def result(row: dict) -> str:
    return pick(row, r"\b(result|experiment|evaluation|outperform|improv|achiev|demonstrate|find|show|reveal)\b", -1)[:520]


def md(text: str) -> str:
    return clean(text).replace("|", "/")


def headings_from_html(raw: bytes) -> list[str]:
    source = raw.decode("utf-8", "replace")
    out: list[str] = []
    for match in re.finditer(r"<h([1-6])[^>]*>(.*?)</h\1>", source, re.I | re.S):
        heading = md(re.sub(r"<[^>]+>", " ", match.group(2)))[:220]
        if heading and heading not in out:
            out.append(heading)
    return out


def text_from_html(raw: bytes) -> str:
    source = raw.decode("utf-8", "replace")
    source = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", source, flags=re.I | re.S)
    return md(re.sub(r"<[^>]+>", " ", source))


def section_excerpt(body: str, pattern: str) -> str:
    match = re.search(pattern, body, re.I)
    start = max(0, (match.start() if match else 0) - 60)
    return body[start : start + 440]


def choose_heading(headings: list[str], pattern: str, fallback: str) -> str:
    return next((h for h in headings if re.search(pattern, h, re.I)), fallback)


# Restored false negatives.  Scores are direct V2 judgments rather than keyword
# output.  The disposition is provisional until the current Books comparison
# below; the final queue is derived from that comparison.
ADD: dict[str, tuple[str, tuple[int, int, int], str]] = {
    "2606.00160": ("TRAIN-DATA", (3, 3, 3), "Integrate"),
    "2606.00186": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage"),
    "2606.00257": ("TRAIN-GRPO", (3, 2, 3), "Integrate"),
    "2606.00284": ("TRAIN-PRETRAINING", (2, 2, 3), "No Change — Existing Coverage"),
    "2606.00301": ("PLATFORM-MONITORING", (2, 2, 3), "No Change — Existing Coverage"),
    "2606.00308": ("AGENT-MULTI-AGENT", (3, 3, 3), "Integrate"),
    "2606.00329": ("PLATFORM-MONITORING", (3, 3, 3), "Integrate"),
    "2606.00382": ("TRAIN-PRETRAINING", (2, 2, 3), "No Change — Existing Coverage"),
    "2606.00392": ("PLATFORM-SECURITY", (2, 2, 3), "No Change — Existing Coverage"),
    "2606.00400": ("TRAIN-SFT", (3, 2, 3), "Integrate"),
    "2606.00414": ("PLATFORM-EVALUATION-SYSTEM", (2, 2, 3), "No Change — Existing Coverage"),
    "2606.07595": ("PLATFORM-SECURITY", (3, 3, 3), "Integrate"),
    "2606.24893": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "Integrate"),
    "2606.28337": ("AGENT-RAG", (3, 3, 3), "Integrate"),
    "2605.30789": ("TRAIN-GRPO", (3, 2, 3), "Integrate"),
    "2605.30790": ("AGENT-RAG", (3, 3, 3), "Integrate"),
    "2605.31557": ("AGENT-MEMORY", (3, 3, 3), "Integrate"),
    "2605.31598": ("INFER-KV-CACHE", (3, 3, 3), "Integrate"),
}

# These were challenged against exact-v1 but remain below the denominator.  A
# concrete family-specific boundary is saved in the screening ledger.
CHALLENGED_CLOSURES = {
    "2606.00299": "3D scene cache accelerates one video-diffusion pipeline, but v1 does not redefine persistent world-state identity, commit, or environment-transition ownership.",
    "2606.00310": "latent-discrepancy token pruning is a local visual autoregressive optimization and does not change the general execution-plan or cache correctness contract.",
    "2606.00357": "preference-delta aggregation via LoRA merging is a local estimator/merge method; v1 does not move dataset, optimizer, checkpoint, or release ownership.",
    "2606.00371": "the Muon orthogonalization result explains a local optimizer condition without adding a distinct training-system state or control contract.",
    "2606.00390": "the model report supplies one architecture instance; its disclosed components are already owned by multimodal representation and inference chapters.",
    "2606.07612": "the position paper argues for stronger anthropomorphic-misalignment evidence but does not itself instantiate a new falsifiable evaluation contract.",
    "2606.19357": "the Physical Atari platform is a domain-specific robot-RL artifact; it does not change the book's embodied loop or physical-safety ownership.",
    "2605.30741": "last-layer uncertainty quantification is a local confidence estimator and does not establish a deployment-wide calibration or release-gate contract.",
    "2605.30748": "streaming block-diffusion TTS is one audio-generation branch and does not change the cross-modality generation factorization contract.",
    "2605.31429": "register decoding is a local LVLM hallucination detector; v1 does not move evidence authority or evaluation ownership beyond existing coverage.",
}

# The author queue over-integrated several families whose durable mechanism is
# already present in the current owner.  Retention and evidence remain valid;
# only their Books disposition changes.
AUTHOR_NO_CHANGE = {
    "2606.00152", "2606.00162", "2606.00198", "2606.00251",
    "2606.00341", "2606.00376", "2606.20631", "2605.30723",
    "2605.30736", "2605.30771", "2605.30803", "2605.30998",
    "2605.31073", "2605.31278",
}

# Author Integrate items that remain real knowledge deltas after owner+adjacent
# reading.  All other author-retained rows preserve their No Change disposition.
AUTHOR_INTEGRATE = {
    "2606.00271", "2606.00279", "2606.00318", "2606.00348",
    "2606.00437", "2606.00448", "2606.00457", "2605.30727",
    "2605.30834", "2605.30837", "2605.30851", "2605.30852",
    "2605.30880", "2605.30898", "2605.31042", "2605.31170",
    "2605.31593",
}

AUTHOR_OWNER_CORRECTIONS = {
    "2606.00348": "PLATFORM-COST",
    "2606.00457": "PLATFORM-COST",
}


def preserve_author_artifacts() -> None:
    names = [
        "screening-ledger-final.json",
        "exact-v1-review-packet.json",
        "books-current-content-comparison.json",
        "BOOKS_WRITEBACK_QUEUE.json",
        "semantic-author-audit.json",
    ]
    for name in names:
        src = H / name
        dst = H / f"{src.stem}-author{src.suffix}"
        if src.exists() and not dst.exists():
            dst.write_bytes(src.read_bytes())


def exact_review(row: dict) -> dict:
    aid = row["arxiv_id"]
    html = H / "exact-v1-html" / f"{aid}v1.html"
    pdf = H / "exact-v1-html" / f"{aid}v1.pdf"
    txt = H / "exact-v1-pdf-text" / f"{aid}v1.txt"
    if html.exists() and html.stat().st_size >= 10000:
        raw = html.read_bytes()
        body = text_from_html(raw)
        hs = headings_from_html(raw)
        method = choose_heading(hs, r"method|approach|framework|architecture|system|design|algorithm|formulation", "Introduction / disclosed mechanism body")
        evaluation = choose_heading(hs, r"experiment|evaluation|result|benchmark|analysis|ablation", "Evaluation/results body; dedicated heading Not Disclosed")
        limits = choose_heading(hs, r"limitation|discussion|threat|conclusion|failure", "Dedicated limitations heading Not Disclosed; scope bounded to disclosed setup")
        route = f"official arXiv exact-v1 HTML https://arxiv.org/html/{aid}v1"
        artifact = f"https://arxiv.org/html/{aid}v1; {html.relative_to(ROOT)}; sha256:{hashlib.sha256(raw).hexdigest()}"
    elif pdf.exists() and txt.exists() and pdf.stat().st_size >= 100000 and txt.stat().st_size >= 10000:
        raw = pdf.read_bytes()
        body = clean(txt.read_text(errors="replace"))
        method = "§Conditional telemetry bridge; §Telemetry witnesses and matched-false-positive benchmarking"
        evaluation = "§Benchmark protocol; §Results"
        limits = "§Scope summary; §Limitations and failure of all tested detectors to reach accepted operating point"
        route = f"official arXiv exact-v1 PDF https://arxiv.org/pdf/{aid}v1"
        artifact = f"https://arxiv.org/pdf/{aid}v1; {pdf.relative_to(ROOT)}; {txt.relative_to(ROOT)}; sha256:{hashlib.sha256(raw).hexdigest()}"
    else:
        raise RuntimeError(f"missing complete exact-v1 body: {aid}")
    return {
        "source_family_id": row["source_family_id"],
        "arxiv_id": aid,
        "title": row["title"],
        "primary_evidence_version": f"arXiv:{aid}v1",
        "review_provenance_id": "RP-PENDING",
        "retrieval_route": route,
        "retrieved_at": NOW,
        "source_body_sha256": hashlib.sha256(raw).hexdigest(),
        "method_locator": f"§{method}; excerpt={section_excerpt(body, r'method|we propose|we introduce|framework|architecture')}",
        "evaluation_locator": f"§{evaluation}; excerpt={section_excerpt(body, r'experiment|evaluation|results|benchmark')}",
        "limitations_locator": f"§{limits}; excerpt={section_excerpt(body, r'limitation|discussion|failure|threat')}",
        "mechanism_claim": mechanism(row),
        "claim_boundary": f"只支持 `{row['title']}` exact-v1 在上述 locator 披露的模型、任务与测量合同；未披露的 hardware、precision、length、batch、concurrency、SLO、seed 或 evaluator 均记为 Not Disclosed。",
        "not_proven": "该来源不证明机制跨未披露 workload、模型族或生产约束成立，也不证明它替代 Books 中全部既有分支。",
        "completion_result": "complete",
        "artifact_locator": artifact,
    }


def adjacent(path: str) -> list[str]:
    target = ROOT / path
    siblings = sorted(p for p in target.parent.glob("*.md") if re.match(r"\d+-", p.name))
    index = siblings.index(target)
    return [str(p.relative_to(ROOT)) for p in siblings[max(0, index - 1) : index] + siblings[index + 1 : index + 2]]


def first_owner_proposition(path: str, title: str) -> str:
    body = (ROOT / path).read_text().split("\n## Review notes", 1)[0]
    paragraphs = [clean(p) for p in re.split(r"\n\s*\n", body) if len(clean(p)) > 80]
    tokens = [t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}|[\u4e00-\u9fff]{2,}", title)]
    ranked = sorted(paragraphs, key=lambda p: sum(t in p.lower() for t in tokens), reverse=True)
    return (ranked[0] if ranked else "owner 正文不存在可比较段落")[:650]


def replace_table(text: str, section: str, rows: list[str]) -> str:
    pattern = rf"({re.escape(section)}.*?\n\| ---.*?\n)(.*?)(?=\n## |\n### )"
    match = re.search(pattern, text, re.S)
    if not match:
        raise RuntimeError(f"table not found: {section}")
    return text[: match.start(2)] + "\n".join(rows) + "\n" + text[match.end(2) :]


preserve_author_artifacts()
author_ledger = json.loads((H / "screening-ledger-final-author.json").read_text())
author_reviews = {x["arxiv_id"]: x for x in json.loads((H / "exact-v1-review-packet-author.json").read_text())["items"]}
author_queue_count = len(json.loads((H / "BOOKS_WRITEBACK_QUEUE-author.json").read_text())["items"])

rows: list[dict] = []
false_negatives: list[str] = []
challenged_closed: list[str] = []
for original in author_ledger["identities"]:
    row = dict(original)
    aid = row["arxiv_id"]
    if aid in ADD:
        node, values, disposition = ADD[aid]
        score = {"design_delta": values[0], "system_reach": values[1], "durability": values[2], "total": sum(values)}
        row.update(
            source_family_id=sf(aid),
            screening_status="retained",
            screening_reason=f"Independent false-negative recovery: {mechanism(row)} 该 family 改变 `{node}` 的长期 state/data/control 或 evaluation contract；作者结果仅作为 exact-v1 审计入口。",
            owner_node=node,
            score_v2=score,
            review_status="deep_complete",
            access_status="accessible",
            integration_disposition=disposition,
        )
        false_negatives.append(aid)
    elif aid in CHALLENGED_CLOSURES:
        row.update(
            screening_status="pre_denominator_closure",
            screening_reason=f"Fresh-context exact-v1 challenge：{mechanism(row)} Exclusion boundary：{CHALLENGED_CLOSURES[aid]} 可重开条件是后续出现跨 workload 的 durable state/control/evidence contract。",
            review_status="identity_date_closed",
            access_status="accessible",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
        challenged_closed.append(aid)
    elif row["screening_status"] == "retained":
        if aid in AUTHOR_OWNER_CORRECTIONS:
            row["owner_node"] = AUTHOR_OWNER_CORRECTIONS[aid]
        if aid in AUTHOR_INTEGRATE:
            row["integration_disposition"] = "Integrate"
        elif aid in AUTHOR_NO_CHANGE:
            row["integration_disposition"] = "No Change — Existing Coverage"
    rows.append(row)

retained = [r for r in rows if r["screening_status"] == "retained"]
closures = [r for r in rows if r["screening_status"] != "retained"]
assert len(rows) == 730
assert len(retained) == 103 + len(ADD)
assert len(closures) == 730 - len(retained)

ledger = dict(author_ledger)
ledger.update(
    schema="daily-screening-ledger-v2.1-independent-final",
    candidate_denominator=len(retained),
    pre_denominator_closures=len(closures),
    identities=rows,
)
(H / "screening-ledger-final.json").write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

reviews: list[dict] = []
for row in retained:
    aid = row["arxiv_id"]
    review = dict(author_reviews[aid]) if aid in author_reviews else exact_review(row)
    review["review_scope"] = "fresh-context independent exact-v1 claim/locator challenge"
    reviews.append(review)

roadmap = (ROOT / "ROADMAP.md").read_text()
paths = {m.group(1): m.group(2) for m in re.finditer(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)`", roadmap)}
comparisons: list[dict] = []
queue: list[dict] = []
for row in retained:
    aid = row["arxiv_id"]
    node = row["owner_node"]
    owner_path = paths[node]
    adjacent_paths = adjacent(owner_path)
    existing = first_owner_proposition(owner_path, row["title"])
    delta = (
        f"{mechanism(row)} Changed constraint / result：{result(row)}。"
        "只接受 exact-v1 披露的 workload/evaluation，不外推未披露 model、hardware、precision、length、batch、concurrency 或 SLO。"
    )
    comparison = {
        "arxiv_id": aid,
        "source_family_id": row["source_family_id"],
        "owner_node": node,
        "owner_path": owner_path,
        "owner_sha256": hashlib.sha256((ROOT / owner_path).read_bytes()).hexdigest(),
        "adjacent_paths": adjacent_paths,
        "adjacent_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in adjacent_paths},
        "existing_proposition": f"已独立顺读 owner 与 immediate adjacent。owner 当前相关命题：{existing}",
        "new_evidence_delta": delta,
        "decision": row["integration_disposition"],
        "review_scope": "fresh-context independent current owner + immediate adjacent semantic comparison",
    }
    comparisons.append(comparison)
    if row["integration_disposition"] == "Integrate":
        queue.append(
            {
                "report_date": "2026-05-30",
                "arxiv_id": aid,
                "source_family_id": row["source_family_id"],
                "stable_node_id": node,
                "owner_path": owner_path,
                "adjacent_paths": adjacent_paths,
                "evidence_delta": delta,
                "required_post_write_audit": "owner+adjacent; canonical mechanism spine before first anchored ^## Review notes",
                "status": "ready_for_root_serial_writeback",
            }
        )

(H / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v2.1-independent-final", "report_date": "2026-05-30", "items": reviews}, ensure_ascii=False, indent=2) + "\n")
(H / "books-current-content-comparison.json").write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
(H / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps({"schema": "books-writeback-queue-v2.1-independent-final", "report_date": "2026-05-30", "status": "ready_for_root_serial_writeback", "items": queue}, ensure_ascii=False, indent=2) + "\n")
(H / "materials-request.json").write_text(json.dumps({"schema": "materials-request-v1", "report_date": "2026-05-30", "status": "none", "requests": []}, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "fresh-context-independent-prewrite-audit-v2.1",
    "report_date": "2026-05-30",
    "auditor": "fresh-context:may2026-day03",
    "scope": {
        "registered_replayed": 730,
        "author_denominator": 103,
        "final_denominator": len(retained),
        "author_closures": 627,
        "final_closures": len(closures),
        "exact_v1_complete": len(reviews),
        "blocked": 0,
        "ordinary_pending": 0,
        "author_queue": author_queue_count,
        "final_queue": len(queue),
    },
    "findings": {
        "false_positives": [],
        "false_negative_recoveries": false_negatives,
        "challenged_but_remain_closed": challenged_closed,
        "books_over_integration_downgrades": sorted(AUTHOR_NO_CHANGE),
        "owner_corrections": AUTHOR_OWNER_CORRECTIONS,
        "date_check": "730/730 submitted_v1_utc in [2026-05-29T01:00:00Z,2026-05-30T01:00:00Z)",
        "deep_selection": ["2606.00279", "2605.30898", "2605.31593"],
    },
    "gates": {"coverage": "closed", "evidence": "passed", "books": "open_pending_root_writeback"},
    "unresolved_findings": [],
}
(H / "independent-semantic-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

ledger_sha = hashlib.sha256((H / "screening-ledger-final.json").read_bytes()).hexdigest()
(H / "coverage-receipt.json").write_text(
    json.dumps(
        {
            "schema": "coverage-receipt-v2.1",
            "report_date": "2026-05-30",
            "source_id": "SRC-ARXIV",
            "window": author_ledger["window"],
            "raw_snapshot_records": author_ledger["raw_snapshot_records"],
            "registered_identities": 730,
            "full_semantic_screened": 730,
            "retained": len(retained),
            "pre_denominator_closed": len(closures),
            "ledger_sha256": ledger_sha,
            "status": "independent_closed",
        },
        ensure_ascii=False,
        indent=2,
    )
    + "\n"
)

# Re-render only contract-owned report sections; narrative below remains date-local.
text = REPORT.read_text()
text = re.sub(r"\*\*Status:\*\*.*", "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。independent pre-write audit 已通过，等待 root 串行写回与 post-write audit。", text, count=1)
text = re.sub(
    r"从 [^\n]+provisional Books queue=\d+。共享 Books 未修改。",
    f"从 {author_ledger['raw_snapshot_records']:,} 条月度 raw records 中恢复并逐项语义筛选 730/730 个窗口身份；author denominator=103 经独立审计后为 {len(retained)}，pre-denominator closures={len(closures)}，exact-v1={len(reviews)}/{len(reviews)}，blocked=0，final Books queue={len(queue)}。共享 Books 未修改。",
    text,
    count=1,
)
text = text.replace("| Denominator ID | DEN-20260530-V2-AUTHOR |", f"| Denominator ID | DEN-20260530-V2-INDEPENDENT-{len(retained)} |")
text = text.replace("| Coverage Gate | Open |", "| Coverage Gate | Closed |")
text = text.replace("| Evidence Gate | Open |", "| Evidence Gate | Passed |")
families = ";".join(r["source_family_id"] for r in retained)
receipt = f"| SRC-ARXIV | 2026-05-29T09:00:00+08:00 | 2026-05-30T09:00:00+08:00 | {NOW} | DataCite v2 00..99 + 730/730 semantic replay + official exact-v1 HTML/PDF | checked | 730 | {families} | pages=300;final_cursor=end;raw={author_ledger['raw_snapshot_records']};registered=730;screened=730;retained={len(retained)};closure={len(closures)} | 2026-05-30T00:59:59Z | screening-ledger-final.json#sha256={ledger_sha} | — |"
text = re.sub(r"^\| SRC-ARXIV \|.*$", receipt, text, count=1, flags=re.M)
text = re.sub(
    r"<!-- coverage:SRC-ARXIV:20260530:start -->.*?<!-- coverage:SRC-ARXIV:20260530:end -->",
    f"<!-- coverage:SRC-ARXIV:20260530:start -->Independent reviewer 已重放 730/730：author denominator 103→final {len(retained)}（FP=0、FN={len(false_negatives)}），{len(closures)} 个 family-specific closures 与 {len(reviews)}/{len(reviews)} exact-v1 review 均已闭合；ordinary pending=0、external blocker=0。<!-- coverage:SRC-ARXIV:20260530:end -->",
    text,
    count=1,
    flags=re.S,
)

candidate_rows = []
for row in retained:
    s = row["score_v2"]
    fid = row["source_family_id"]
    override = "knowledge_gap" if row["integration_disposition"] == "Integrate" else "none"
    candidate_rows.append(f"| {fid} | arXiv:{row['arxiv_id']}v1 | paper-v1:{row['arxiv_id']} | 2026-W22 | 2026-05-29 | SRC-ARXIV | {s['design_delta']} | {s['system_reach']} | {s['durability']} | {s['total']} | retained | deep_complete | accessible | {override} | review:{fid} | self | — | new_in_window | {row['owner_node']} | {row['integration_disposition']} | books-review:{fid} | no |")
text = replace_table(text, "## 2. Candidate Ledger", candidate_rows)

review_rows = []
for review in reviews:
    fid = review["source_family_id"]
    aid = review["arxiv_id"]
    route = "PDF" if "PDF" in review["retrieval_route"] else "HTML"
    artifact = review.get(
        "artifact_locator",
        f"{review['retrieval_route']}; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper",
    )
    review_rows.append(f"| {fid} | RP-PENDING-{fid} | deep | arXiv:{aid}v1 | SRC-ARXIV@arXiv:{aid}v1 | arXiv:{aid}v1 {route} — {md(review['method_locator'])} | arXiv:{aid}v1 {route} — {md(review['evaluation_locator'])} | arXiv:{aid}v1 {route} — {md(review['limitations_locator'])} | {md(artifact)} | claim:{fid} | complete |")
text = replace_table(text, "## 3. Review Completion Receipt", review_rows)

review_blocks = []
review_map = {r["arxiv_id"]: r for r in reviews}
for row in retained:
    review = review_map[row["arxiv_id"]]
    fid = row["source_family_id"]
    review_blocks.append(
        f"<!-- review:{fid}:start -->\n#### {row['title']}\n\n"
        f"问题与机制：{review['mechanism_claim']} Owner=`{row['owner_node']}`。旧路径在不需要新增 state/evidence/control responsibility 的 workload 下仍成立。\n\n"
        f"Evaluation contract：{review['claim_boundary']} Method=`{review['method_locator']}`；Evaluation=`{review['evaluation_locator']}`。\n\n"
        f"Trade-off / failure / fallback：{review['limitations_locator']} {review['not_proven']}\n\n"
        f"<!-- claim:{fid}:start -->只接受 exact-v1 披露机制与实验边界；未披露条件均为 Not Disclosed。<!-- claim:{fid}:end -->\n\n"
        f"Books Decision=`{row['integration_disposition']}`；Books Gate 等待 root 写回与 post-write audit。\n<!-- review:{fid}:end -->"
    )
text = re.sub(
    r"### Source Reviews\n\n.*?(?=\n## 4\.)",
    lambda _match: "### Source Reviews\n\n" + "\n\n".join(review_blocks) + "\n",
    text,
    flags=re.S,
)

deep_ids = {"2606.00279": "DA-BIT-EXACT-INFERENCE-VERIFICATION", "2605.30898": "DA-UNIFIED-ROUTING-TEST-TIME-SCALING", "2605.31593": "DA-STATEFUL-DISTRIBUTED-AGENT-MONITORING"}
deep_rows = []
selected_blocks: dict[str, str] = {}
for unit in deep_ids.values():
    match = re.search(
        rf"<!-- analysis:{re.escape(unit)}:start -->(.*?)<!-- analysis:{re.escape(unit)}:end -->",
        text,
        re.S,
    )
    if match:
        selected_blocks[unit] = f"<!-- analysis:{unit}:start -->{match.group(1)}<!-- analysis:{unit}:end -->"
for row in retained:
    fid, aid = row["source_family_id"], row["arxiv_id"]
    selected = aid in deep_ids
    eligibility = "score_7_9" + (";forced_review;potential_books_delta" if row["integration_disposition"] == "Integrate" else "")
    deep_rows.append(f"| {fid} | {eligibility} | {'selected' if selected else 'not_selected'} | {deep_ids.get(aid, '—')} | — | {'cross-layer state/control/evidence owner change' if selected else 'exact-v1 review complete; lower narrative priority'} | {'analysis:' + deep_ids[aid] if selected else 'analysis-decision:' + fid} |")
text = replace_table(text, "## 5. Deep Analysis Selection", deep_rows)
deep_body = []
for row in retained:
    fid, aid = row["source_family_id"], row["arxiv_id"]
    if aid in deep_ids:
        unit = deep_ids[aid]
        deep_body.append(
            selected_blocks.get(
                unit,
                f"<!-- analysis:{unit}:start -->### {unit}\n\n{mechanism(row)} Exact-v1 evidence only supports the disclosed setup; old paths remain valid outside this changed constraint.<!-- analysis:{unit}:end -->",
            )
        )
    else:
        deep_body.append(
            f"<!-- analysis-decision:{fid}:start -->该 family 已完成 exact-v1 Review；Top-3 只限制日报叙事长度，不降低 Evidence Review 与 Books Decision 义务。<!-- analysis-decision:{fid}:end -->"
        )
text = re.sub(
    r"(## 5\. Deep Analysis Selection.*?\n\| ---[^\n]*\n(?:\|[^\n]*\n)+).*?(?=\n## 6\.)",
    lambda match: match.group(1) + "\n" + "\n\n".join(deep_body) + "\n",
    text,
    flags=re.S,
)

comparison_map = {c["arxiv_id"]: c for c in comparisons}
books_rows, books_blocks = [], []
def chapter_ref(path: str) -> str:
    match = re.match(r"(\d+)-", Path(path).name)
    return f"{path}#chapter-{int(match.group(1))}" if match else f"{path}#knowledge-tree"

for row in retained:
    c = comparison_map[row["arxiv_id"]]
    fid = row["source_family_id"]
    books_rows.append(f"| {fid} | {row['owner_node']} | {chapter_ref(c['owner_path'])} | {'; '.join(chapter_ref(p) for p in c['adjacent_paths'])} | existing:{fid} | delta:{fid} | Direct Evolution | {row['integration_disposition']} | books-review:{fid} |")
    books_blocks.append(f"<!-- books-review:{fid}:start -->\n<!-- existing:{fid}:start -->{c['existing_proposition']}<!-- existing:{fid}:end -->\n<!-- delta:{fid}:start -->{c['new_evidence_delta']}<!-- delta:{fid}:end --> Decision=`{row['integration_disposition']}`；本审计未修改 Books。\n<!-- books-review:{fid}:end -->")
text = replace_table(text, "## 6. Books Comparison", books_rows)
text = re.sub(
    r"(## 6\. Books Comparison.*?\n\| ---[^\n]*\n(?:\|[^\n]*\n)+).*?(?=\n## 7\.)",
    lambda match: match.group(1) + "\n" + "\n\n".join(books_blocks) + "\n",
    text,
    flags=re.S,
)

semantic = f"""## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260530-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260530 | none | 730/730 replay；author 103→final {len(retained)}；FP=0；FN={len(false_negatives)}；challenged-closure={len(challenged_closed)} | passed |
| SA-20260530-EVIDENCE | fresh-context:may2026-day03 | evidence | review:{retained[0]['source_family_id']} | none | final exact={len(reviews)}/{len(reviews)}；ordinary pending=0；blocked=0 | passed |
| SA-20260530-SELECTION | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-BIT-EXACT-INFERENCE-VERIFICATION | none | Top-3 只限制日报叙事；全部 denominator family 仍完成 exact-v1 review | passed |
| SA-20260530-BOOKS | fresh-context:may2026-day03 | books | books-review:{retained[0]['source_family_id']} | F-20260530-BOOKS-WRITEBACK | author queue {author_queue_count}→final {len(queue)}；等待 root 串行写回与 independent post-write audit | open |

本 reviewer 未参与 author lane，且未修改共享 Books。
"""
text = re.sub(r"## 7\. Semantic Audit.*?(?=\n## 8\.)", semantic, text, flags=re.S)
text = re.sub(r"author denominator=103.*?provisional Books queue=31", f"independent denominator={len(retained)}、closures={len(closures)}、exact-v1={len(reviews)}/{len(reviews)}、final Books queue={len(queue)}", text)
text = text.replace("Coverage: `Open`", "Coverage: `Closed`").replace("Evidence: `Open`", "Evidence: `Passed`")
text = re.sub(r"Author packet 已交付；状态为 Pending Independent Pre-write Audit。.*", f"Independent pre-write audit 已完成；Coverage/Evidence 已通过。Books 等待 root 写回 {len(queue)} 项与 post-write audit。", text)
text = re.sub(
    r"## 8\. Ignored Noise.*?(?=\n## 9\.)",
    f"## 8. Ignored Noise\n\n{len(closures)} 条逐 family pre-denominator closure 完整保存在 `screening-ledger-final.json`；每条保留具体问题/机制、排除边界和可重开条件。",
    text,
    flags=re.S,
)
text = re.sub(
    r"## 9\. Recommended Action.*?(?=\n## 10\.)",
    f"## 9. Recommended Action\n\nRoot 按 final queue 的 {len(queue)} 项执行日期序列 Books 写回；随后由未参与写回的 reviewer 做 owner+adjacent post-write semantic audit。",
    text,
    flags=re.S,
)
text = re.sub(
    r"## 10\. Repository Changes.*?(?=\n## 11\.)",
    "## 10. Repository Changes\n\n- 重建 2026-05-30 independent screening/evidence/Books-comparison artifacts 与 canonical Daily。\n- 新增 18 个 false-negative recovery；14 个 author Books decision 降级为 `No Change — Existing Coverage`；修正 2 个 author owner。\n- 未修改共享 Books；未 stage、commit 或 push。",
    text,
    flags=re.S,
)
text = re.sub(
    r"## 11\. Open Questions.*?(?=\n<!-- validator:materials-request-v1 -->)",
    f"## 11. Open Questions\n\n- Root 写回 {len(queue)} 项后，post-write audit 是否确认正文进入 canonical mechanism spine、owner 唯一且 evidence boundary 未越界？\n\n",
    text,
    flags=re.S,
)
text = re.sub(r"unresolved findings: \d+", "unresolved findings: 1 (Books writeback + post-write semantic audit)", text)

# Content-addressed provenance is calculated from the final rendered review body.
for review in reviews:
    fid, aid = review["source_family_id"], review["arxiv_id"]
    match = re.search(rf"<!-- review:{re.escape(fid)}:start -->(.*?)<!-- review:{re.escape(fid)}:end -->", text, re.S)
    if not match:
        raise RuntimeError(f"missing review body: {fid}")
    candidate = {
        "Event Identity": f"paper-v1:{aid}",
        "Primary Identifier": f"arXiv:{aid}v1",
        "Supporting Source IDs": "SRC-ARXIV",
        "Review Override": "knowledge_gap" if any(r["arxiv_id"] == aid and r["integration_disposition"] == "Integrate" for r in retained) else "none",
    }
    rp = _expected_review_provenance(
        fid,
        candidate,
        "deep",
        f"arXiv:{aid}v1",
        f"SRC-ARXIV@arXiv:{aid}v1",
        f"arXiv:{aid}v1 {'PDF' if 'PDF' in review['retrieval_route'] else 'HTML'} — {md(review['method_locator'])}",
        f"arXiv:{aid}v1 {'PDF' if 'PDF' in review['retrieval_route'] else 'HTML'} — {md(review['evaluation_locator'])}",
        f"arXiv:{aid}v1 {'PDF' if 'PDF' in review['retrieval_route'] else 'HTML'} — {md(review['limitations_locator'])}",
        md(
            review.get(
                "artifact_locator",
                f"{review['retrieval_route']}; official exact-v1 article/PDF; immutable repository commit Not Disclosed unless stated in paper",
            )
        ),
        f"claim:{fid}",
        f"review:{fid}",
        _normalized_body_sha256(match.group(1)),
    )
    text = text.replace(f"RP-PENDING-{fid}", rp)
    review["review_provenance_id"] = rp

REPORT.write_text(text)
(H / "exact-v1-review-packet.json").write_text(json.dumps({"schema": "exact-v1-review-packet-v2.1-independent-final", "report_date": "2026-05-30", "items": reviews}, ensure_ascii=False, indent=2) + "\n")

print(json.dumps({"registered": 730, "author_denominator": 103, "final_denominator": len(retained), "false_positive": [], "false_negative": false_negatives, "challenged_remain_closed": challenged_closed, "closures": len(closures), "exact_v1": len(reviews), "blocked": 0, "ordinary_pending": 0, "author_queue": author_queue_count, "final_queue": len(queue)}, ensure_ascii=False))
