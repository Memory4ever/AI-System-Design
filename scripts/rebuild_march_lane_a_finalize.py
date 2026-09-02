#!/usr/bin/env python3
"""Render March 1--8 independent Historical Daily author packets.

This adapter deliberately does not edit shared Books or claim fresh-context
acceptance.  It binds each retained family to exact-v1 evidence, current Books
text, and a date-local serial writeback proposal.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import re
import subprocess
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from extract_april_2026_review_text import PaperParser, normalize
from rebuild_march_lane_a_review_notes import NOTES


ROOT = Path(__file__).resolve().parents[1]
EXECUTED = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def md(value: str, limit: int | None = None) -> str:
    value = " ".join(str(value).split()).replace("|", "/")
    return value if limit is None else value[:limit].rstrip()


def canonical(value: str) -> str:
    parts = sorted(unicodedata.normalize("NFC", x.strip()) for x in value.split(";") if x.strip())
    return ";".join(parts)


def norm_body(value: str) -> str:
    lines = unicodedata.normalize("NFC", value.replace("\r\n", "\n").replace("\r", "\n")).splitlines()
    return "\n".join(x.rstrip() for x in lines).strip("\n")


def roadmap() -> tuple[dict[str, str], list[str]]:
    rows = re.findall(r"\| `([^`]+)` \| Ch\d+ \| `([^`]+)` \|", (ROOT / "ROADMAP.md").read_text())
    return dict(rows), [node for node, _ in rows]


PATHS, ORDER = roadmap()


def locate_html(body_path: Path, patterns: tuple[str, ...]) -> tuple[str, str]:
    parser = PaperParser()
    source = body_path.read_text(errors="replace")
    try:
        parser.feed(source)
    except NotImplementedError:
        parser = PaperParser()
        parser.feed(re.sub(r"<!\[[\s\S]*?\]>", "", source))
    # Pattern order encodes facet specificity.  Within one pattern prefer the
    # shallowest section, then the most substantive text.  The previous global
    # longest-section rule could turn an Appendix case study into a Method
    # locator merely because it contained more words.
    for pattern in patterns:
        matches: list[tuple[str, str, str]] = []
        for sid, heading in parser.headings.items():
            if re.search(pattern, heading, re.I):
                text = normalize("".join(parser.section_text.get(sid, [])))
                if text:
                    matches.append((sid, heading, text))
        if matches:
            sid, heading, text = min(
                matches,
                key=lambda value: (value[0].count("."), -len(value[2]), value[0]),
            )
            return f"{sid} — {heading}", md(text, 900)
    whole = normalize(" ".join(parser.section_text.get("__root__", [])))
    return "Not Disclosed — exact-v1 has no dedicated matching section", md(whole, 700) or "Not Disclosed"


def pdf_text(path: Path) -> str:
    converter = Path("/Users/apple/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/pdftotext")
    if not converter.exists():
        raise RuntimeError("bundled pdftotext unavailable; cannot claim exact-v1 PDF review")
    result = subprocess.run(
        [str(converter), "-layout", str(path), "-"], check=True, capture_output=True, text=True
    )
    # Keep form-feed page boundaries so PDF facet locators can name an exact page.
    return result.stdout


def locate_pdf(body_path: Path, patterns: tuple[str, ...]) -> tuple[str, str]:
    text = pdf_text(body_path)
    pages = text.split("\f")
    heading_prefix = re.compile(r"^(?:\d+(?:\.\d+)*\.?|[IVXLC]+(?:-[A-Z])?\.?|Appendix\s+[A-Z])\s+", re.I)
    for pattern in patterns:
        for page_number, page in enumerate(pages, 1):
            lines = page.splitlines()
            for index, line in enumerate(lines):
                stripped = line.strip()
                # A prose mention is not a stable locator.  Accept only a
                # numbered/Appendix heading recovered from the exact-v1 PDF.
                # ``pdftotext -layout`` may place the second column's numbered
                # heading after the first column on the same physical line.
                # Accept that layout only when the caller's paper-specific
                # expression still matches the heading text; generic patterns
                # cannot turn arbitrary two-column prose into a locator.
                second_column_heading = re.search(
                    r"\s{3,}\d+(?:\.\d+)*\.?\s+[A-Z]", line
                )
                paper_specific_column_pattern = pattern.startswith("(?:^")
                if (
                    heading_prefix.search(stripped)
                    or (second_column_heading and paper_specific_column_pattern)
                ) and re.search(pattern, stripped, re.I):
                    excerpt = " ".join(lines[index:index + 45])
                    return f"PDF page {page_number}; exact heading {md(stripped, 160)}", md(excerpt, 900)
    return "Not Disclosed — exact-v1 has no dedicated matching section", md(text, 700) or "Not Disclosed"


def locate(path: Path, patterns: tuple[str, ...]) -> tuple[str, str]:
    if path.suffix.lower() == ".pdf":
        return locate_pdf(path, patterns)
    return locate_html(path, patterns)


def chapter_binding(node: str, query: str) -> dict:
    if node not in PATHS:
        raise RuntimeError(f"Stable Node not in ROADMAP: {node}")
    path = ROOT / PATHS[node]
    lines = path.read_text().splitlines()
    review_index = next((i for i, line in enumerate(lines) if line.strip() == "## Review notes"), len(lines))
    query_words = {x.lower() for x in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}", query)}
    heading = ""
    best = (-1, 1, "", "")
    for line_number, line in enumerate(lines[:review_index], 1):
        if line.startswith("## "):
            heading = line[3:].strip()
            continue
        if not line or line.startswith("#") or len(line) < 40:
            continue
        words = {x.lower() for x in re.findall(r"[A-Za-z][A-Za-z0-9_-]{4,}", line)}
        score = len(words & query_words)
        if score > best[0]:
            best = (score, line_number, heading, md(line, 520))
    _, line_number, heading, proposition = best
    if not heading:
        heading = next((x[3:].strip() for x in lines if x.startswith("## ")), lines[0].lstrip("# "))
    target = f"{PATHS[node]}#{heading} (line {line_number})"
    index = ORDER.index(node)
    adjacent = []
    for position in (index - 1, index + 1):
        if 0 <= position < len(ORDER):
            adjacent_node = ORDER[position]
            adjacent_path = ROOT / PATHS[adjacent_node]
            adjacent_lines = adjacent_path.read_text().splitlines()
            adjacent_heading = next(
                (x[3:].strip() for x in adjacent_lines if x.startswith("## ")),
                adjacent_lines[0].lstrip("# "),
            )
            adjacent_line = next((n for n, x in enumerate(adjacent_lines, 1) if x.startswith("## ")), 1)
            adjacent.append(f"{PATHS[adjacent_node]}#{adjacent_heading} (line {adjacent_line})")
    return {
        "target": target,
        "adjacent": "; ".join(adjacent),
        "existing": proposition or "当前章节已经定义该 owner 的基础责任与边界。",
    }


def archive_index() -> dict[str, dict]:
    index: dict[str, dict] = {}
    for path in sorted(Path("/tmp").glob("arxiv-cs-2026-03-*.html")):
        body = path.read_bytes()
        digest = hashlib.sha256(body).hexdigest()
        skip_match = re.search(r"-(\d+)\.html$", path.name)
        skip = int(skip_match.group(1)) if skip_match else 0
        for aid in set(re.findall(rb"2603\.\d{5}", body)):
            identity = aid.decode()
            index.setdefault(identity, {
                "archive_url": f"https://arxiv.org/list/cs/2026-03?show=500&skip={skip}",
                "snapshot_path": path,
                "snapshot_sha256": digest,
                "skip": skip,
            })
    return index


ARCHIVE = archive_index()


def extract_review(row: dict, access: dict) -> dict:
    aid = row["arxiv_id"]
    family = row["source_family_id"]
    node = row["stable_node_id"]
    body_path = ROOT / access["body_path"]
    # These additions are deliberately paper-specific.  A broad keyword such as
    # ``system`` or ``benchmark`` is not enough to prove that a section owns a
    # facet; each override below was checked against the exact-v1 heading tree.
    method_overrides = {
        "2603.01966": (r"^3\s+AMemGym$",),
        "2603.03116": (r"^3\s+Procedure-Aware Evaluation",),
        "2603.04902": (r"^2\s+Privacy Flow Graph$",),
        "2603.04417": (r"^3\.?\s+Experiment$",),
        "2603.04443": (r"(?:^|\s{3,})4\.?\s+AMV-L Overview$",),
    }
    evaluation_overrides = {
        "2603.03394": (r"\btesting\b",),
        "2603.01548": (r"^3\.?\s+Multi-Domain Evaluation$",),
        "2603.04417": (r"^3\.?\s+Experiment$",),
        "2603.04443": (r"^9\.1\s+Experimental protocol$",),
    }
    artifact_overrides = {
        "2603.00349": (r"cooperation analysis: algorithmic details", r"step-level feedback and logging"),
        "2603.00381": (r"experimental details",),
        "2603.01499": (r"experiment details",),
        "2603.02271": (r"real hardware characterization",),
        "2603.02376": (r"static analysis example", r"meta-summarizer"),
        "2603.02482": (r"system interface",),
        "2603.03589": (r"system architecture",),
        "2603.04028": (r"reproducibility",),
        "2603.04257": (r"details of the used prompts", r"experiments setup"),
        "2603.04402": (r"config-driven system synthesis",),
        "2603.04444": (r"\bdeployment\b",),
        "2603.04797": (r"Helios system design",),
        "2603.04902": (r"contextual integrity-focused benchmark",),
        "2603.05438": (r"details of CompACT tokenizer", r"world model details"),
        "2603.04427": (r"deployment via factored keys",),
        "2603.05147": (r"\btraining\b", r"real robot"),
        "2603.04443": (r"reproducibility",),
        "2603.04417": (r"\bexperiment\b",),
        "2603.05399": (r"^4\s+Experiments$",),
        "2603.05451": (r"system and libraries",),
    }
    method_loc, method_text = locate(body_path, method_overrides.get(aid, ()) + (
        r"\bmethod", r"approach", r"architecture", r"design", r"framework", r"overview",
        r"protocol", r"proof of concept", r"sophisticated watermark", r"cross-layer solutions",
        r"formalism", r"algebra", r"operator", r"infrastructure",
        r"system (?:overview|architecture|design|model)",
    ))
    eval_loc, eval_text = locate(body_path, evaluation_overrides.get(aid, ()) + (
        r"experiment", r"evaluation", r"results", r"benchmark", r"performance", r"analysis",
        r"characterization", r"case stud", r"worst-case failures",
    ))
    limit_loc, limit_text = locate(body_path, (
        r"limitation", r"discussion", r"conclusion", r"future work", r"threat model",
        r"failure", r"ablation", r"attack",
    ))
    artifact_loc, artifact_text = locate(body_path, artifact_overrides.get(aid, ()) + (
        r"implementation", r"system setup", r"open resources",
        r"experimental setup", r"reproducibility",
    ))
    for facet, value in (
        ("Method / state-control mechanism", method_loc),
        ("Evaluation contract", eval_loc),
        ("Limitations / counterevidence", limit_loc),
        ("Artifact / implementation", artifact_loc),
    ):
        if value.startswith("Not Disclosed —"):
            replacement = f"Not Disclosed — arXiv:{aid}v1 exposes no dedicated {facet} section in the recovered exact-v1 body"
            if facet.startswith("Method"):
                method_loc, method_text = replacement, "Not Disclosed"
            elif facet.startswith("Evaluation"):
                eval_loc, eval_text = replacement, "Not Disclosed"
            elif facet.startswith("Limitations"):
                limit_loc, limit_text = replacement, "Not Disclosed"
            else:
                artifact_loc, artifact_text = replacement, "Not Disclosed"
    binding = chapter_binding(node, row["title"] + " " + row["abstract"])
    score = row["score_v2"]
    disposition = row["proposed_books_disposition"]
    archive = ARCHIVE.get(aid)
    if archive is None:
        raise RuntimeError(f"retained exact ID absent from official March cs archive snapshot: {aid}")
    event_timestamp = row["announcement_beijing"]
    event_date = event_timestamp[:10]
    note = NOTES.get(aid)
    if note is None:
        raise RuntimeError(f"retained family has no paper-specific synthesis: {aid}")
    boundary = (
        f"只接受 arXiv:{aid}v1 在 exact-v1 公开 workload 下的作者机制与实验主张；"
        "未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO "
        "均为 Not Disclosed，不外推为通用结论。"
    )
    body = (
        f"#### {md(row['title'])}\n\n"
        f"问题与 changed constraint：{note['constraint']}\n\n"
        f"旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、"
        "更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。\n\n"
        f"机制、state/data/control owner：{note['mechanism']} 对应 exact-v1 `{method_loc}`；"
        f"该机制由 `{node}` 承载。原文定位摘录仅作核对：{md(method_text, 520)}\n\n"
        f"Evaluation contract：{note['evidence']} exact-v1 定位为 `{eval_loc}`；"
        f"用于核对的原文摘录：{md(eval_text, 520)}\n\n"
        f"证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为"
        "其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。\n\n"
        f"Trade-off、failure 与共存边界：{note['tradeoff']} 反证/限制定位为 `{limit_loc}`；"
        f"用于核对的原文摘录：{md(limit_text, 420)}\n\n"
        f"Artifact / implementation：exact-v1 `{artifact_loc}`；公开范围摘录：{md(artifact_text, 360)}。"
        "未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。\n\n"
        f"<!-- claim:{family}:start -->{boundary}<!-- claim:{family}:end -->\n\n"
        f"Books Comparison：已读 `{node}` 的 `{binding['target']}` 及相邻 `{binding['adjacent']}`；"
        f"现有命题为“{binding['existing']}”。Decision=`{disposition}`；该 author-side 判断仍待"
        "fresh-context Books reviewer，Integrate 项只进入日期队列。"
    )
    def evidence_locator(kind: str, locator: str) -> str:
        if locator.startswith("Not Disclosed —"):
            return locator
        if access["body_route"] == "official_pdf_v1":
            page = re.search(r"PDF page (\d+)", locator)
            suffix = f"#page={page.group(1)}" if page else ""
            return md(f"{access['body_url']}{suffix} — {locator} ({kind})")
        fragment = locator.split(" — ", 1)[0]
        return md(f"{access['body_url']}#{fragment} — exact-v1 {locator} ({kind})")
    fields = [
        "review-completion-v1", family, f"paper-v1:{aid}", f"arXiv:{aid}v1", "SRC-ARXIV",
        f"arXiv:{aid}v1", f"SRC-ARXIV@arXiv:{aid}v1", "deep",
        canonical(evidence_locator("Method", method_loc)),
        canonical(evidence_locator("Evaluation", eval_loc)),
        canonical(evidence_locator("Limitations", limit_loc)),
        canonical(evidence_locator("Artifact", artifact_loc)),
        f"claim:{family}", f"review:{family}",
        f"review-body-sha256:{hashlib.sha256(norm_body(body).encode()).hexdigest()}",
    ]
    if disposition == "Integrate":
        fields.insert(8, "review-override:knowledge_gap")
    return {
        "aid": aid, "family": family, "title": row["title"], "event_date": event_date,
        "event_timestamp": event_timestamp,
        "node": node, "disposition": disposition, "score": score, "body": body,
        "method": evidence_locator("Method", method_loc),
        "evaluation": evidence_locator("Evaluation", eval_loc),
        "limits": evidence_locator("Limitations", limit_loc),
        "artifact": evidence_locator("Artifact", artifact_loc),
        "delta": method_text, "boundary": boundary, **binding,
        "archive": {k: (v.as_posix() if isinstance(v, Path) else v) for k, v in archive.items()},
        "rp": "RP-" + hashlib.sha256("|".join(fields).encode()).hexdigest()[:16],
    }


def save_archive_receipt(packet: Path, reviews: list[dict]) -> None:
    snapshot_dir = packet / "official-archive-pages"
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    copied: dict[str, str] = {}
    rows = []
    for review in reviews:
        source_path = Path(review["archive"]["snapshot_path"])
        name = source_path.name + ".gz"
        target = snapshot_dir / name
        if name not in copied:
            target.write_bytes(gzip.compress(source_path.read_bytes()))
            copied[name] = target.relative_to(ROOT).as_posix()
        rows.append({
            "arxiv_id": review["aid"], "membership": True,
            "archive_url": review["archive"]["archive_url"],
            "snapshot_path": copied[name],
            "snapshot_sha256_uncompressed": review["archive"]["snapshot_sha256"],
        })
    payload = {
        "schema": "official-arxiv-month-archive-membership-v1",
        "archive": "cs/2026-03", "status": "exact_id_membership_checked",
        "rows": rows,
    }
    (packet / "official-archive-membership-receipt.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    )


def render(day: int) -> None:
    date = f"2026-03-{day:02d}"
    compact = date.replace("-", "")
    packet = ROOT / f"papers/2026/03/_sources/daily-{compact}"
    ledger = json.loads((packet / "screening-ledger-author.json").read_text())
    non_arxiv_path = packet / "non-arxiv-historical-replay-receipt.json"
    if not non_arxiv_path.exists():
        raise RuntimeError(f"missing requested non-arXiv archival replay receipt: {non_arxiv_path}")
    non_arxiv = json.loads(non_arxiv_path.read_text())
    non_arxiv_statuses: dict[str, int] = {}
    non_arxiv_leads = []
    for source in non_arxiv["rows"]:
        non_arxiv_statuses[source["assessment"]] = non_arxiv_statuses.get(source["assessment"], 0) + 1
        for lead in source["date_overlapping_leads"]:
            non_arxiv_leads.append((source["source_id"], lead))
    access_receipt = json.loads((packet / "exact-v1-access-receipt.json").read_text())
    access = {row["arxiv_id"]: row for row in access_receipt["rows"]}
    retained = [row for row in ledger["identities"] if row["screening_decision"] == "retained"]
    if {row["arxiv_id"] for row in retained} != set(access):
        raise RuntimeError(f"03-{day:02d} denominator/access identity mismatch")
    reviews = [extract_review(row, access[row["arxiv_id"]]) for row in retained]
    reviews.sort(key=lambda value: (-value["score"]["total"], value["aid"]))
    selected: list[dict] = []
    selected_nodes: set[str] = set()
    for review in reviews:
        if review["node"] not in selected_nodes and len(selected) < 3:
            selected.append(review)
            selected_nodes.add(review["node"])
    for review in reviews:
        if len(selected) < 3 and review not in selected:
            selected.append(review)
    selected_ids = {review["aid"]: f"DA-{compact}-{index + 1}" for index, review in enumerate(selected)}
    raw = ledger["registered_identities"]
    closures = ledger["pre_denominator_closed"]
    denominator = ledger["denominator_id"]
    start_date = f"2026-02-28" if day == 1 else f"2026-03-{day - 1:02d}"
    start = f"{start_date}T09:00:00+08:00"
    end = f"{date}T09:00:00+08:00"
    families = "; ".join(review["family"] for review in reviews) or "—"
    queue_items = [review for review in reviews if review["disposition"] == "Integrate"]
    status_summary = (
        f"窗口内 raw identities={raw}，完成 title+abstract semantic screening={raw}/{raw}；"
        f"冻结 Candidate Denominator={len(reviews)}，pre-denominator closures={closures}。"
        f"exact-v1 Review={len(reviews)}/{len(reviews)}，withdrawn=0，blocked=0；"
        f"Books Integrate proposal={len(queue_items)}。"
    )
    lines = [
        f"# Daily Research — {date}", "", f"**Research Date:** {date}", "",
        "**Timezone:** Asia/Shanghai", "",
        f"**Strict Window:** {start_date} 09:00:00 ～ {date} 09:00:00（Asia/Shanghai，左闭右开）", "",
        "**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。", "",
        "**Status:** In Progress；Coverage=Open；Evidence=Open；Books=Open；作者侧 inventory、screening、exact-v1 Review 与 Books Comparison 已完成；等待独立 fresh-context audit 和日期串行 Books writeback。", "",
        "## Executive Summary", "", status_summary,
        "", "3 月 arXiv 的 `Submitted:v1` 与 `Updated:v1` 只作为版本 provenance，不承担事件归属。日报以 DataCite DOI `created/registered` 恢复 identity，再按官方 Sun–Thu 20:00 Eastern 公告时刻映射到北京时间半开窗口。公告落在 09:00 右边界时不归结束于该时刻的窗口，而归下一份日报。", "",
        "## 1. Coverage", "", "<!-- validator:report-metadata-v2 -->",
        "| Field | Value |", "| --- | --- |", "| Contract Version | V2.1 |", "| Score Schema | V2 |",
        "| Report Type | Daily |", f"| Window Start | {date} |", f"| Window End | {date} |",
        "| Registry Version | 2026-08-25 |", "| Coverage Mode | Full Replay |", "| Baseline Report | — |",
        "| Changed Source IDs | — |", "| Previous Denominator ID | — |", f"| Denominator ID | {denominator} |",
        f"| Denominator Frozen At | {EXECUTED} |", "| Completion Status | In Progress |", "| Coverage Gate | Open |",
        "| Evidence Gate | Open |", "| Books Gate | Open |", "",
        "### Source Coverage Receipt", "", "<!-- validator:source-coverage-v2 -->",
        "| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |",
        "| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
        f"| SRC-ARXIV | {start} | {end} | {EXECUTED} | official arXiv March archive + scheduled announcement recovery + exact-v1 abs/HTML/PDF; registered categories; {raw}/{raw} semantic replay | {'checked' if reviews else 'no_hit'} | {len(reviews)} | {families} | Not Applicable — frozen shared archive receipt enumerates the complete owner batch | {end} | papers/2026/03/_sources/daily-{compact}/official-archive-membership-receipt.json; papers/2026/03/_sources/daily-{compact}/screening-ledger-author.json; coverage:SRC-ARXIV:{compact} | GAP-{compact}-FRESH-AUDIT |", "",
        f"<!-- coverage:SRC-ARXIV:{compact}:start -->本次独立重放以官方公告日程恢复 strict-window inventory；保留 exact-ID archive membership 与 exact-v1 identity/access。当前注册表在 2026-08-25 生效，不反推 2026-03 的机构来源为当日 Required；fresh-context false-positive/false-negative audit 尚未执行，Coverage Gate 保持 Open。<!-- coverage:SRC-ARXIV:{compact}:end -->", "",
        "### Later-effective non-arXiv archival replay", "",
        f"虽然 20 个机构/发现来源的 registry Effective Date 为 2026-08-25、按合同不反推为本日 Required，父任务仍要求本次执行 bounded archival replay。独立收据为 `papers/2026/03/_sources/daily-{compact}/non-arxiv-historical-replay-receipt.json`；状态计数为 `{json.dumps(non_arxiv_statuses, ensure_ascii=False, sort_keys=True)}`。没有任何线索同时取得 strict-window first-public instant 与长期机制证据，因此新增 Candidate Source Family=0。", "",
        "## 2. Candidate Ledger", "", "<!-- validator:candidate-ledger-v2.1 -->",
        "| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |",
        "| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    if non_arxiv_leads:
        insertion = ["日期-only 边界线索（不归属、不评分、不进入分母）：", ""]
        for source_id, lead in non_arxiv_leads:
            insertion.append(f"- `{source_id}` — `{lead['date']}` — [{lead['title']}]({lead['url']})；官方页面没有精确发布时间/时区。")
        insertion.append("")
        marker = lines.index("## 2. Candidate Ledger")
        lines[marker:marker] = insertion
    for review in reviews:
        score = review["score"]
        iso = datetime.fromisoformat(review["event_date"]).isocalendar()
        override = "knowledge_gap" if review["disposition"] == "Integrate" else "none"
        lines.append(
            f"| {review['family']} | arXiv:{review['aid']}v1 | paper-v1:{review['aid']} | {iso.year}-W{iso.week:02d} | {review['event_date']} | SRC-ARXIV | {score['design_delta']} | {score['system_reach']} | {score['durability']} | {score['total']} | retained | deep_complete | accessible | {override} | review:{review['family']} | self | — | new_in_window | {review['node']} | {review['disposition']} | books-review:{review['family']} | no |"
        )
    if not reviews:
        lines += ["", "No retained candidate in this strict window; all raw identities, if any, are closed before denominator admission."]
    lines += [
        "", "## 3. Review Completion Receipt", "", "<!-- validator:review-completion-v1 -->",
        "| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for review in reviews:
        lines.append(
            f"| {review['family']} | {review['rp']} | deep | arXiv:{review['aid']}v1 | SRC-ARXIV@arXiv:{review['aid']}v1 | {md(review['method'])} | {md(review['evaluation'])} | {md(review['limits'])} | {md(review['artifact'])} | claim:{review['family']} | complete |"
        )
    lines += ["", "### Source Reviews", ""]
    for review in reviews:
        lines += [f"<!-- review:{review['family']}:start -->", review["body"], f"<!-- review:{review['family']}:end -->", ""]
    if not reviews:
        lines += ["None — denominator is empty.", ""]
    lines += [
        "## 4. Benchmark Contracts", "", "None — 本日报不把作者结果或摘要数字重标为可跨 workload 外推的 benchmark claim。", "",
        "## 5. Deep Analysis Selection", "", "<!-- validator:deep-analysis-selection-v1 -->",
        "| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for review in reviews:
        eligibility = "score_7_9; forced_review; potential_books_delta" if review["disposition"] == "Integrate" else "score_7_9"
        if review["aid"] in selected_ids:
            unit = selected_ids[review["aid"]]
            lines.append(f"| {review['family']} | {eligibility} | selected | {unit} | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:{unit} |")
        else:
            lines.append(f"| {review['family']} | {eligibility} | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:{review['family']} |")
    for review in reviews:
        if review["aid"] in selected_ids:
            unit = selected_ids[review["aid"]]
            lines += ["", f"<!-- analysis:{unit}:start -->", f"### {unit} — {review['title']}", "", f"旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `{review['node']}`。exact-v1 机制为：{review['delta']} 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：{review['boundary']}", f"<!-- analysis:{unit}:end -->"]
        else:
            lines += ["", f"<!-- analysis-decision:{review['family']}:start -->", f"`{review['title']}` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。", f"<!-- analysis-decision:{review['family']}:end -->"]
    if not reviews:
        lines += ["", "No eligible analysis unit in this strict window."]
    lines += [
        "", "## 6. Books Comparison", "", "<!-- validator:books-comparison-v1 -->",
        "| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for review in reviews:
        relation = "Direct Evolution" if review["disposition"] == "Integrate" else "Principle Reuse"
        lines.append(f"| {review['family']} | {review['node']} | {md(review['target'])} | {md(review['adjacent'])} | existing:{review['family']} | delta:{review['family']} | {relation} | {review['disposition']} | books-review:{review['family']} |")
    for review in reviews:
        lines += [
            "", f"<!-- existing:{review['family']}:start -->", f"author-side 已读 current owner `{review['node']}` 的具体命题：{review['existing']}", f"<!-- existing:{review['family']}:end -->",
            "", f"<!-- delta:{review['family']}:start -->", review["delta"], f"<!-- delta:{review['family']}:end -->",
            "", f"<!-- books-review:{review['family']}:start -->", f"Decision=`{review['disposition']}`；owner=`{review['node']}`；target=`{review['target']}`；adjacent=`{review['adjacent']}`。证据边界：{review['boundary']} 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。", f"<!-- books-review:{review['family']}:end -->",
        ]
    if not reviews:
        lines += ["", "None — no candidate passed denominator admission."]
    all_reviews = "; ".join(f"review:{review['family']}" for review in reviews) or "coverage:SRC-ARXIV:" + compact
    all_books = "; ".join(f"books-review:{review['family']}" for review in reviews) or "coverage:SRC-ARXIV:" + compact
    auditor = f"fresh-context:pending-march-lane-a-{compact}"
    lines += [
        "", "## 7. Semantic Audit", "", "<!-- validator:semantic-audit-v1 -->",
        "| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        f"| SA-{compact}-COVERAGE-PENDING | {auditor} | coverage | coverage:SRC-ARXIV:{compact} | FRESH-{compact}-FP-FN-DATE | 独立审查全部 retained/closures、公告窗口与 anomaly adjudication | open |",
        f"| SA-{compact}-EVIDENCE-PENDING | {auditor} | evidence | {all_reviews} | FRESH-{compact}-EVIDENCE | 独立对读 exact-v1 locators、claim boundary 与 RP | open |",
        f"| SA-{compact}-SELECTION-PENDING | {auditor} | deep_analysis_selection | validator:deep-analysis-selection-v1 | FRESH-{compact}-SELECTION | 独立比较完整 eligibility frontier 与最多三个叙事单元 | open |",
        f"| SA-{compact}-BOOKS-PENDING | {auditor} | books | {all_books} | FRESH-{compact}-BOOKS-WRITEBACK | 验收 owner/adjacent comparison；Integrate 按日期写回后再做 post-write audit | open |",
        "", "## 8. Ignored Noise", "",
        f"{closures} 个 pre-denominator closure 保存在 `papers/2026/03/_sources/daily-{compact}/screening-ledger-author.json`；每个 family 保存 identity、title、abstract 与具体排除理由。withdrawn=0。", "",
        "## 9. Recommended Action", "",
        f"- 由独立 reviewer 完成四个 fresh-context scope。\n- 按日期顺序处理 {len(queue_items)} 项 Books writeback queue；完成共享章节写回与 post-write audit 后才能关闭 Books Gate。", "",
        "## 10. Repository Changes", "",
        f"- 新增/更新本日报与 `papers/2026/03/_sources/daily-{compact}/` 独立证据包。\n- 未修改 Books、Weekly、月级共享索引或 `docs/LEARNING_STATE.md`。", "",
        "## 11. Open Questions", "",
        "- Fresh-context denominator/date/evidence/selection/Books findings 尚未闭合。\n- Integrate queue 尚未取得共享 Books 写锁与 post-write semantic audit。", "",
        "## 12. Sources", "",
    ]
    for review in reviews:
        lines.append(f"- [arXiv:{review['aid']}v1](https://arxiv.org/abs/{review['aid']}v1) — official announcement instant `{review['event_timestamp']}`；按半开窗口 owner report=`{date}`；访问日期 2026-09-02。")
    if not reviews:
        lines.append("- [arXiv March 2026 cs archive](https://arxiv.org/list/cs/2026-03) — strict-window inventory recovery；访问日期 2026-09-02。")
    lines += [
        "", "## 13. Final Status", "",
        f"Completion Status=`In Progress`；Coverage=`Open`；Evidence=`Open`；Books=`Open`；Unresolved Findings=4。作者侧 raw={raw}、retained={len(reviews)}、closures={closures}、exact-v1 reviews={len(reviews)}、blocked=0、Integrate queue={len(queue_items)}。", "",
    ]
    report = ROOT / f"papers/2026/03/{day:02d}/README.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines))

    save_archive_receipt(packet, reviews)
    queue = {
        "schema": "books-writeback-queue-v2.1-author-proposal", "report_date": date,
        "status": "pending_root_serial_writeback",
        "items": [{
            "source_family_id": review["family"], "primary_identifier": f"arXiv:{review['aid']}v1",
            "exact_source": access[review["aid"]]["body_url"], "review_ref": f"review:{review['family']}",
            "stable_node_id": review["node"], "target_chapter_ref": review["target"],
            "adjacent_chapter_refs": review["adjacent"], "existing_proposition": review["existing"],
            "proposed_long_term_mechanism": review["delta"], "evidence_boundary": review["boundary"],
        } for review in queue_items],
    }
    (packet / "BOOKS_WRITEBACK_QUEUE.json").write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
    queue_md = [f"# Books Writeback Queue — {date}", "", "Status: pending root serial writeback and fresh-context Books audit.", ""]
    for item in queue["items"]:
        queue_md += [
            f"## {item['source_family_id']}", "", f"- Primary: `{item['primary_identifier']}`",
            f"- Exact source: {item['exact_source']}", f"- Stable Node: `{item['stable_node_id']}`",
            f"- Target: `{item['target_chapter_ref']}`", f"- Adjacent: `{item['adjacent_chapter_refs']}`",
            f"- Existing proposition: {item['existing_proposition']}",
            f"- Proposed mechanism: {item['proposed_long_term_mechanism']}",
            f"- Evidence boundary: {item['evidence_boundary']}", "",
        ]
    if not queue["items"]:
        queue_md += ["No Integrate proposal for this strict window.", ""]
    (packet / "BOOKS_WRITEBACK_QUEUE.md").write_text("\n".join(queue_md))
    (packet / "review-extract.json").write_text(json.dumps({
        "schema": "source-specific-review-extract-v2.1-author", "report_date": date, "items": reviews,
    }, ensure_ascii=False, indent=2) + "\n")
    # Export the canonical artifact names consumed by the month-level
    # reconciliation.  The author ledger remains available as provenance, but
    # downstream audits must not need a lane-specific filename or schema.
    final_identities = []
    for identity in ledger["identities"]:
        exported = dict(identity)
        retained_identity = identity["screening_decision"] == "retained"
        exported["candidate_state"] = "retained" if retained_identity else "pre_denominator_closed"
        exported["screening_status"] = (
            "candidate_denominator" if retained_identity else "pre_denominator_closure"
        )
        final_identities.append(exported)
    (packet / "screening-ledger-final.json").write_text(json.dumps({
        "schema": "screening-ledger-v2.1",
        "report_date": date,
        "window": {"start": start, "end": end, "semantics": "left_closed_right_open"},
        "raw_snapshot_records": 15767,
        "registered_window_identities": raw,
        "screened_identities": raw,
        "candidate_denominator": len(reviews),
        "pre_denominator_closures": closures,
        "withdrawn_primary_sources": [],
        "weekly_dependency_count": 0,
        "fresh_context_false_positive_false_negative_audit": "pending_independent_reviewer",
        "identities": final_identities,
    }, ensure_ascii=False, indent=2) + "\n")
    standard_reviews = []
    for review in reviews:
        exported = dict(review)
        exported["result"] = "complete"
        exported["review_provenance_id"] = review["rp"]
        exported["books_disposition"] = review["disposition"]
        exported["stable_node_id"] = review["node"]
        exported["source_family_id"] = review["family"]
        standard_reviews.append(exported)
    (packet / "exact-v1-review-packet.json").write_text(json.dumps({
        "schema": "exact-v1-review-packet-v2.1-author",
        "report_date": date,
        "status": "author_complete_fresh_context_audit_pending",
        "items": standard_reviews,
    }, ensure_ascii=False, indent=2) + "\n")
    (packet / "coverage-receipt.json").write_text(json.dumps({
        "schema": "coverage-receipt-v2.1-author", "report_date": date, "source_id": "SRC-ARXIV",
        "window_start": start, "window_end": end, "registered_identities": raw,
        "full_semantic_screened": raw, "retained": len(reviews), "pre_denominator_closed": closures,
        "withdrawn": 0, "blocked": 0, "status": "author_complete_fresh_audit_pending", "executed_at": EXECUTED,
    }, ensure_ascii=False, indent=2) + "\n")
    (packet / "PROVENANCE_BOUNDARY.md").write_text(
        "# Provenance Boundary\n\n"
        "Canonical Daily ownership uses `inventory.json`, whose event time comes from the "
        "current shared DOI-created + official arXiv announcement-schedule recovery receipt.\n\n"
        "Any `arxiv-api-enumeration.json` or `arxiv-atom-*.xml` in this packet was collected "
        "during an earlier Submitted-time recovery attempt. It is preserved only as raw "
        "identity provenance and is not an input to date ownership, denominator screening, "
        "scoring, Source Review, or Books Comparison.\n"
    )
    print(json.dumps({
        "date": date, "raw": raw, "retained": len(reviews), "closures": closures,
        "reviews": len(reviews), "integrate_queue": len(queue_items), "blocked": 0,
    }))


def main() -> None:
    for day in range(1, 9):
        render(day)


if __name__ == "__main__":
    main()
